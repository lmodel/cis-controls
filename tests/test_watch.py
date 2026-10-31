"""Checks the upstream watch's decisions against stubbed answers from CIS's site.

scripts/check_upstream_release.py reads two pages of CIS's site. These tests
replace its one network call, `_get`, with a table of answers, so they run
offline. They show what the report says when CIS names a newer version,
drops the pinned one, moves a page, or blocks the reader.
"""

import http.client
import importlib.util
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"

# Pages cut down to the strings the watch reads: the version after the word
# Controls and the version in the address of a version's page. The words
# around them are this test's own.
PINNED_PAGE = """<html><body>
<h1>CIS Critical Security Controls Version 8.1</h1>
<p>Get <a href="/controls/v8-1">CIS Controls&reg; v8.1</a> here.</p>
<p>Older: <a href="/controls/v8">CIS Controls v8</a>,
<a href="/controls/v7-1">CIS Controls v7.1</a>.</p>
</body></html>"""
NEWER_PAGE = PINNED_PAGE.replace(
    "</body>", '<p>New: <a href="/controls/v8-2">CIS Controls v8.2</a></p></body>'
)


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, a pair is
    the address that answered and its page, and a string is the page at the
    address asked."""

    def get(url):
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, tuple):
            return answer
        return url, answer

    watch._get = get


def _answers(watch, page=PINNED_PAGE):
    return dict.fromkeys(watch.PAGES, page)


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def _http_error(url, code):
    return urllib.error.HTTPError(url, code, "stubbed", None, None)


def test_nothing_changed(watch, tmp_path):
    """With every page naming the pinned version and nothing newer, the watch
    reports both pages current and exits 0."""
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    for url in watch.PAGES:
        assert f"- {url} names v8.1 and the older v7.1, v8, and no newer" in text


def test_versions_read_from_text_and_addresses(watch):
    """The watch reads a version beside the word Controls, past the
    trademark sign, and in a version page's address."""
    assert watch.versions(PINNED_PAGE) == {"8", "7.1", "8.1"}
    assert watch.versions("CIS Controls® v9") == {"9"}
    assert watch.versions('<a href="/controls/v10-0-guide">') == {"10.0"}
    assert watch.versions("access control v2, NIST CSF 2.0") == set()


def test_a_newer_version(watch, tmp_path):
    """A page that names v8.2 needs attention."""
    answers = _answers(watch)
    answers[watch.PAGES[1]] = NEWER_PAGE
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{watch.PAGES[1]} names a newer version: v8.2.**" in text
    assert f"- {watch.PAGES[0]} names v8.1" in text


def test_a_revision_of_the_pinned_version(watch, tmp_path):
    """A label after the pinned edition, such as v8.1.3, is newer; the pinned
    edition's own label is not."""
    page = PINNED_PAGE + "<p>CIS Controls v8.1.2</p>"
    _stub(watch, _answers(watch, page))
    assert _run(watch, tmp_path)[0] == 0
    _stub(watch, _answers(watch, page.replace("v8.1.2", "v8.1.3")))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "names a newer version: v8.1.3." in text


def test_the_pinned_version_gone(watch, tmp_path):
    """A page that names only other versions needs attention."""
    page = PINNED_PAGE.replace("v8-1", "v9").replace("8.1", "9")
    _stub(watch, _answers(watch, page))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{watch.PAGES[0]} no longer names v8.1.**" in text
    assert "names a newer version: v9." in text


def test_a_page_that_is_gone(watch, tmp_path):
    """A 404 says the page is gone, and the other page is still checked."""
    answers = _answers(watch)
    answers[watch.PAGES[0]] = _http_error(watch.PAGES[0], 404)
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{watch.PAGES[0]} is gone (HTTP 404).**" in text
    assert f"- {watch.PAGES[1]} names v8.1" in text


def test_a_blocked_reader_could_not_finish(watch, tmp_path):
    """A refusal, a network failure and a challenge page with no version are
    each a check that could not finish, and still give a report."""
    answers = _answers(watch)
    answers[watch.PAGES[0]] = _http_error(watch.PAGES[0], 403)
    answers[watch.PAGES[1]] = urllib.error.URLError("Connection refused")
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The check of {watch.PAGES[0]} could not finish: `HTTP Error 403" in text
    assert f"**The check of {watch.PAGES[1]} could not finish: `<urlopen error" in text

    _stub(watch, _answers(watch, "<html><title>Just a moment...</title></html>"))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "the page names no version of the CIS Controls.**" in text


def test_a_cut_connection_or_unknown_charset_could_not_finish(watch, tmp_path):
    """A page cut off mid-read and a charset Python does not know are checks
    that could not finish, and the other page is still checked."""
    answers = _answers(watch)
    answers[watch.PAGES[0]] = http.client.IncompleteRead(b"<html>")
    answers[watch.PAGES[1]] = LookupError("unknown encoding: x-bogus")
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The check of {watch.PAGES[0]} could not finish: `IncompleteRead" in text
    assert (
        f"**The check of {watch.PAGES[1]} could not finish: `unknown encoding" in text
    )


def test_a_redirect_is_reported(watch, tmp_path):
    """The report names the address that answered when it is not the one
    asked."""
    answers = _answers(watch)
    moved = "https://www.cisecurity.org/controls/v8-1-1"
    answers[watch.PAGES[0]] = (moved, PINNED_PAGE)
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert f"- {watch.PAGES[0]} redirected to `{moved}`." in text


def test_text_the_site_chose_is_quoted(watch, tmp_path):
    """A redirect target is quoted as code, so it cannot mention a person in
    the issue, and a backtick in it cannot end the quotation."""
    answers = _answers(watch)
    answers[watch.PAGES[0]] = ("https://example.org/@someone`x", PINNED_PAGE)
    _stub(watch, answers)
    text = _run(watch, tmp_path)[1]
    assert "redirected to `https://example.org/@someone'x`." in text


def test_no_credentials_are_sent(watch, monkeypatch):
    """The request carries only a User-Agent, even when a token is set in the
    environment."""
    monkeypatch.setenv("GITHUB_TOKEN", "not-to-be-sent")
    sent = {}

    class Answer:
        headers = type("H", (), {"get_content_charset": lambda self: "utf-8"})()

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def geturl(self):
            return sent["url"]

        def read(self, size):
            return PINNED_PAGE.encode()

    def urlopen(req, timeout):
        sent["url"] = req.full_url
        sent["headers"] = dict(req.header_items())
        return Answer()

    monkeypatch.setattr(watch.urllib.request, "urlopen", urlopen)
    watch._get(watch.PAGES[0])
    assert set(sent["headers"]) == {"User-agent"}
