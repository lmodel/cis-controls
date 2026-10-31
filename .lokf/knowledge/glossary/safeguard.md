---
type: GlossaryTerm
id: https://w3id.org/lmodel/cis-controls/knowledge/glossary/safeguard
genre: reference
title: Safeguard
description: In the CIS Controls, one action an enterprise takes under a Control, named by the Control's number and its own, such as Safeguard 4.1; Version 8.1 has 153. The schema renders a Safeguard as `CisSafeguard`, with its number in `cis_safeguard_id`.
definition: One action an enterprise takes under a Control of the CIS Controls, named by the Control's number and its own.
resource: src/cis_controls/schema/cis_controls.yaml
definedBy:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: cis-implementation-groups
    resource: https://www.cisecurity.org/controls/implementation-groups
    title: the total of Safeguards, read on 2026-10-30
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the class CisSafeguard
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:10:19Z"
status: draft
---

# Safeguard

CIS's page on the Implementation Groups says that Versions 8 and 8.1 of the CIS Controls hold 153 Safeguards in total, and that the Safeguards were earlier called Sub-Controls.[^cis-implementation-groups] A Safeguard is one action under a Control, named by the Control's number, a dot and its own number. The schema renders a Safeguard as `CisSafeguard`, with its number in `cis_safeguard_id`, such as `"4.1"`, and requires its asset class, its security function and its Implementation Groups.[^cis_controls.yaml]

[^cis-implementation-groups]: <https://www.cisecurity.org/controls/implementation-groups>, the total of Safeguards
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the class CisSafeguard
