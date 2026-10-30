#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check CIS's pages for a version of the CIS Controls other than the pinned one.

The schema renders the CIS Critical Security Controls at one edition. The
Center for Internet Security (CIS) publishes no openly licensed,
machine-readable form of them: its spreadsheet sits behind a registration,
under the same licence as the guide. So nothing here is copied or matched by
hash.

Instead, this script reads two public pages of CIS's site: the page of the
pinned version and the list of the Controls. On each it looks for two kinds
of version string:

- the version CIS writes after the word Controls, such as "CIS Controls v8.1"
  or "Controls Version 8.1";
- the version in the address of a version's page, such as /controls/v8-1.

It matches those strings and never the markup around them, so a change of
layout does not break it. It prints a Markdown report, and exits 1 when:

- a page names a version newer than the pinned edition, such as v8.2 or v9;
- a page no longer names the pinned version, or is gone;
- a page could not be read because it was blocked, failed or timed out.

The script has two limits:

- It cannot see a revision that keeps the version CIS's site shows. CIS
  labels the March 2025 revision of the guide v8.1.2 on its pages, while the
  site still calls it Version 8.1.
- It cannot check the licence. No page that can be read without registering
  states it, so NOTICE records the licence as the guide states it, with the
  date it was read.

It sends no token or other credentials. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# The version CIS's site gives the pinned edition, and the label the guide's
# pages carry for its latest revision, which is the schema header's
# `version`. Move them together, with PINNED_SOURCE and PINNED_ON and the
# schema header, when the schema moves to another edition.
PINNED_VERSION = "8.1"
PINNED_EDITION = "8.1.2"

# The page of the pinned version, which is the schema header's `source`.
# tests/test_upstream.py holds the header and these pins equal.
PINNED_SOURCE = "https://www.cisecurity.org/controls/v8-1"

# The day the pages were last read by a person, who found the pins above.
PINNED_ON = "2026-10-30"

PAGES = (
    PINNED_SOURCE,
    "https://www.cisecurity.org/controls/cis-controls-list",
)
USER_AGENT = "lmodel-cis-controls-upstream-check"

# A version after the word Controls, with CIS's registered-trademark sign
# allowed between them, as in "CIS Controls v8.1" and "Controls Version 8.1".
TEXT_VERSION = re.compile(r"\bControls(?:\s*®)?\s+(?:v|Version\s+)(\d+(?:\.\d+)*)\b")
# A version in the address of a version's page, such as /controls/v8-1.
ADDRESS_VERSION = re.compile(r"/controls/v(\d+(?:-\d+)*)\b")
# A page larger than this is read only this far.
MAX_BYTES = 5_000_000


def _get(url: str) -> tuple[str, str]:
    """The address that answered, after any redirect, and the page's text."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.geturl(), resp.read(MAX_BYTES).decode(charset, "replace")


def _key(version: str) -> tuple[int, ...]:
    """The numeric parts of a version, padded so that 8.1 and 8.1.0 order
    alike."""
    parts = [int(x) for x in version.split(".")]
    return tuple(parts + [0] * (4 - len(parts)))


def versions(page: str) -> set[str]:
    """Every version of the CIS Controls a page names, in its text or in the
    address of a version's page, written with dots."""
    found = {m.replace("-", ".") for m in ADDRESS_VERSION.findall(page)}
    text = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", page, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    found |= set(TEXT_VERSION.findall(re.sub(r"\s+", " ", text)))
    return found


def _shown(names: set[str]) -> str:
    """The versions in order, each once: v8 and v8.0 are the same version."""
    by_key = {}
    for name in sorted(names, key=len):
        by_key[_key(name)] = name
    return ", ".join(f"v{by_key[k]}" for k in sorted(by_key))


def check_page(url: str) -> tuple[list[str], bool]:
    """Report the versions one page names, and whether one needs attention."""
    try:
        answered, page = _get(url)
    except urllib.error.HTTPError as err:
        if err.code in (404, 410):
            return [
                f"- **{url} is gone (HTTP {err.code}).** Find where CIS now "
                "publishes the CIS Controls, and move the pins."
            ], True
        raise
    report = []
    if answered.rstrip("/") != url.rstrip("/"):
        report.append(f"- {url} redirected to {answered}.")
    found = versions(page)
    if not found:
        return report + [
            f"- **The check of {url} could not finish: the page names no "
            "version of the CIS Controls.** It may be a page that blocks "
            "automated readers; read it in a browser."
        ], True
    pinned = {
        v for v in found if _key(v) in (_key(PINNED_VERSION), _key(PINNED_EDITION))
    }
    newer = {v for v in found if _key(v) > _key(PINNED_EDITION)}
    older = found - pinned - newer
    attention = False
    if newer:
        attention = True
        report.append(
            f"- **{url} names a newer version: {_shown(newer)}.** Read what CIS "
            "changed, decide whether the schema moves to it, and move the pins "
            "here and in the schema header."
        )
    if not pinned:
        attention = True
        report.append(
            f"- **{url} no longer names v{PINNED_VERSION}.** Find out whether CIS "
            "has replaced or withdrawn it."
        )
    if not attention:
        line = f"- {url} names v{PINNED_VERSION}"
        if older:
            line += f" and the older {_shown(older)}"
        report.append(line + ", and no newer version.")
    return report, attention


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned edition: CIS Controls Version {PINNED_VERSION}, revised as "
        f"v{PINNED_EDITION}, {PINNED_SOURCE}, last read by a person on {PINNED_ON}."
    ]
    attention = False
    for url in PAGES:
        try:
            found, needs = check_page(url)
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as err:
            found, needs = [f"- **The check of {url} could not finish: {err}.**"], True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
