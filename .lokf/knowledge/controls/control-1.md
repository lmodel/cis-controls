---
type: CisControl
id: https://w3id.org/lmodel/cis-controls/knowledge/controls/control-1
title: Control 1
description: "Control 1 of the CIS Controls, Version 8.1, which the edition file titles Knowing every device in the project's own words: it holds 5 Safeguards, 1.1 to 1.5, of which 2 are in Implementation Group 1, 4 in Implementation Group 2 and all 5 in Implementation Group 3."
cis_control_id: "1"
resource: https://www.cisecurity.org/controls/v8-1
definedBy:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/glossary/control
sources:
  - id: cis-v8-1
    resource: https://www.cisecurity.org/controls/v8-1
    title: the guide this page offers, v8.1.2 of March 2025, read on 2026-10-30
  - id: edition
    resource: src/cis_controls/data/cis-controls-8.1.2.yaml
    title: Control 1 and its Safeguards
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:14:49Z"
status: draft
---

# Control 1

Control 1 is one of the 18 Controls of the CIS Controls, Version 8.1. CIS's guide, at its v8.1.2 revision, lists 5 Safeguards under it, numbered 1.1 to 1.5.[^cis-v8-1] The schema uses those numbers as their identifiers. Of the Safeguards, 2 are in Implementation Group 1, 4 in Implementation Group 2 and all 5 in Implementation Group 3. All its Safeguards are about the asset class Devices.

This bundle leaves out CIS's name and description for the Control and CIS's text for its Safeguards, because CIS licenses that text under CC BY-NC-ND 4.0; CIS's guide gives them, and [the guide's reference](../references/cis-controls-guide.md) says where to find it. The edition file gives the Control and each of its Safeguards a title and a description in the project's own words, written from what each requires.[^edition] For Control 1 they are:

- **Title:** Knowing every device
- **Description:** Keeping track of every device that can hold or handle the enterprise's data, so that only known and approved devices are on its network and unknown ones are found and dealt with.

[^cis-v8-1]: <https://www.cisecurity.org/controls/v8-1>, the guide this page offers, the Safeguards of Control 1
[^edition]: src/cis_controls/data/cis-controls-8.1.2.yaml, Control 1 and its Safeguards
