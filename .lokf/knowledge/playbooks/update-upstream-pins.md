---
type: Playbook
id: https://w3id.org/lmodel/cis-controls/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the weekly upstream watch reports that CIS's pages name a version of the CIS Controls newer than the pinned 8.1.2, no longer name 8.1, have gone or redirected, or could not be read: read CIS's notes, decide whether the schema moves, and move the pins in `scripts/check_upstream_release.py` and the schema header together."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins, check_page and main
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the two tests
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# Update the upstream pins

`scripts/check_upstream_release.py` runs every Monday in [Upstream watch](../workflows/upstream-watch.md) with the standard library alone. CIS publishes no openly licensed, machine-readable form of the Controls, so nothing is copied or matched by hash. The script reads two public pages instead, CIS's page for Version 8.1 and the list of the Controls, and finds the version strings CIS writes after the word Controls and in the address of a version's page. It matches those strings and not the markup, and it sends no token. It always writes a report, and it exits 1, so that the workflow opens or updates an issue, on each of these findings:[^check_upstream_release.py]

- **A page names a newer version** than the pinned edition, 8.1.2, such as v8.2 or v9. Read what CIS changed, decide whether the schema moves to it, and move the pins.
- **A page no longer names v8.1.** Find out whether CIS has replaced or withdrawn it.
- **A page is gone**, with HTTP 404 or 410. Find where CIS now publishes the Controls, and move the pins.
- **A check could not finish**: CIS's site refused the reader, the network failed, or the page named no version at all, as a page that blocks automated readers does. Read the page in a browser.

The report also says when a page redirected to another address. The script cannot see a revision that keeps the version CIS's site shows, such as a v8.1.3 the site still calls 8.1, and it cannot check the licence, because no page that can be read without registering states it.

To move to another edition, read the guide, then change together: `PINNED_VERSION`, `PINNED_EDITION`, `PINNED_SOURCE` and `PINNED_ON` in the script; `version`, `source` and the `cis_site_version`, `revision_date` and `pages_read_on` annotations in the schema header; and NOTICE. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, since the header reaches the generated files and the adapt copy. Then run `just test`: `tests/test_upstream.py` checks that the header and the script name the same edition and page.[^test_upstream.py] A new edition may also renumber the Controls or change their count, which the identifier types' patterns state.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring, check_page and main
[^test_upstream.py]: tests/test_upstream.py, the two tests
