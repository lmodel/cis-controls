---
type: Reference
id: https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
genre: reference
title: CIS Critical Security Controls, Version 8.1
description: "The guide the schema renders: the CIS Critical Security Controls, Version 8.1, from the Center for Internet Security (CIS), at its v8.1.2 revision of March 2025, licensed CC BY-NC-ND 4.0, and offered for download from <https://www.cisecurity.org/controls/v8-1>."
resource: https://www.cisecurity.org/controls/v8-1
sources:
  - id: cis-v8-1
    resource: https://www.cisecurity.org/controls/v8-1
    title: the page and the guide it offers, v8.1.2 of March 2025, read on 2026-10-30
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the header's version, source and comments
  - id: notice
    resource: NOTICE
    title: the section on the CIS Critical Security Controls
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# CIS Critical Security Controls, Version 8.1

The Center for Internet Security (CIS) publishes the CIS Critical Security Controls as a guide, which its page for Version 8.1 offers for download with a spreadsheet, a change log and a page on the Implementation Groups. The page describes Version 8.1 as a small update of Version 8: it realigned the security functions to the NIST Cybersecurity Framework 2.0, added the Govern function, and revised the asset classes.[^cis-v8-1] The guide's pages carry the label v8.1.2, and its change log names two minor revisions, v8.1.1 in August 2024 and v8.1.2 in March 2025.

The schema header names this page in `source` and the label of the revision, 8.1.2, in `version`.[^cis_controls.yaml] The guide is licensed under CC BY-NC-ND 4.0, and CIS requires its prior approval for commercial use. NOTICE says what that licence allows, and why the repository and this bundle carry none of the guide's text.[^notice] The download asks for a registration, so `scripts/check_upstream_release.py` watches CIS's public pages instead: see [Update the upstream pins](../playbooks/update-upstream-pins.md).

[^cis-v8-1]: <https://www.cisecurity.org/controls/v8-1>, the page, and the guide's licence page and change log
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the header
[^notice]: NOTICE, The CIS Critical Security Controls
