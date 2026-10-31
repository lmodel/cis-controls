"""Checks that the schema header and the upstream watch name the same edition.

The Center for Internet Security (CIS) publishes no openly licensed,
machine-readable form of the CIS Controls, so nothing here is copied or
matched by hash. What can drift is the pins: the schema header's `version`
and `source`, and the edition scripts/check_upstream_release.py watches for.
"""

import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "cis_controls" / "schema" / "cis_controls.yaml"


def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_header_and_watch_pin_the_same_edition():
    """The header's version and source are the watch's pinned edition and
    page, and its annotations repeat the watch's other pins."""
    header = yaml.safe_load(SCHEMA.read_text())
    watch = _watch()
    assert str(header["version"]) == watch.PINNED_EDITION
    assert header["source"] == watch.PINNED_SOURCE
    assert watch.PINNED_SOURCE in watch.PAGES
    annotations = header["annotations"]
    assert annotations["cis_site_version"] == watch.PINNED_VERSION
    assert annotations["pages_read_on"] == watch.PINNED_ON


def test_pinned_edition_is_a_revision_of_the_site_version():
    """The guide's label for the revision starts with the version CIS's site
    shows, and the watch counts both as the pinned one."""
    watch = _watch()
    assert watch.PINNED_EDITION.startswith(watch.PINNED_VERSION + ".")
    page = f"CIS Controls v{watch.PINNED_VERSION}, CIS Controls v{watch.PINNED_EDITION}"
    assert watch.versions(page) == {watch.PINNED_VERSION, watch.PINNED_EDITION}
