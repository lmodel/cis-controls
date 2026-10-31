---
type: GlossaryTerm
id: https://w3id.org/lmodel/cis-controls/knowledge/glossary/control
genre: reference
title: Control
description: In the CIS Controls, one of 18 numbered groups of Safeguards, each on one subject. The schema renders a Control as `CisControl`, with its number, 1 to 18, in `cis_control_id`.
definition: One of the numbered groups of Safeguards that make up the CIS Controls, each on one subject.
resource: src/cis_controls/schema/cis_controls.yaml
definedBy:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: cis-controls-list
    resource: https://www.cisecurity.org/controls/cis-controls-list
    title: the page's title, read on 2026-10-30
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the class CisControl
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:10:19Z"
status: draft
---

# Control

CIS's list of the Controls names 18 of them.[^cis-controls-list] Each Control groups the Safeguards on one subject, and CIS names it by its number. The schema renders a Control as `CisControl`, with its number in `cis_control_id`, such as `"4"`, and its Safeguards in `control_safeguards`.[^cis_controls.yaml] In a knowledge bundle a Safeguard names its Control with `isPartOf` instead. The bundle describes each Control under [controls](../controls/index.md), by its number alone.

[^cis-controls-list]: <https://www.cisecurity.org/controls/cis-controls-list>, the page's title
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the class CisControl
