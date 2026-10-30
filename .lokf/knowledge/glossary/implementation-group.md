---
type: GlossaryTerm
id: https://w3id.org/lmodel/cis-controls/knowledge/glossary/implementation-group
genre: reference
title: Implementation Group
description: In the CIS Controls, one of three tiers, IG1, IG2 and IG3, that say which Safeguards an enterprise takes up first; each includes the one before it, so IG1 holds 56 Safeguards, IG2 130 and IG3 all 153. The schema renders the tiers as `CisImplementationGroup`.
definition: One of three cumulative tiers of the CIS Controls that say which Safeguards an enterprise takes up first.
resource: src/cis_controls/schema/cis_controls.yaml
definedBy:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: cis-implementation-groups
    resource: https://www.cisecurity.org/controls/implementation-groups
    title: the total of Safeguards, read on 2026-10-30
  - id: cis-ig1
    resource: https://www.cisecurity.org/controls/implementation-groups/ig1
    title: the count of IG1, read on 2026-10-30
  - id: cis-ig2
    resource: https://www.cisecurity.org/controls/implementation-groups/ig2
    title: the count of IG2, read on 2026-10-30
  - id: cis-ig3
    resource: https://www.cisecurity.org/controls/implementation-groups/ig3
    title: the count of IG3, read on 2026-10-30
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the enum CisImplementationGroup and the slot safeguard_implementation_groups
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# Implementation Group

CIS's pages on the Implementation Groups say that each group is a set of Safeguards, and that an enterprise begins with IG1.[^cis-implementation-groups] IG1 holds 56 Safeguards.[^cis-ig1] IG2 adds 74 to those of IG1.[^cis-ig2] IG3 adds 23 more, which makes the 153 Safeguards of Versions 8 and 8.1.[^cis-ig3] So the groups are cumulative: a Safeguard in IG1 is in all three, and one in IG2 is in IG3 too. The schema renders the groups as `CisImplementationGroup`, with the values `IG1`, `IG2` and `IG3`, and a Safeguard lists its groups in `safeguard_implementation_groups`, which must hold `IG3`.[^cis_controls.yaml]

[^cis-implementation-groups]: <https://www.cisecurity.org/controls/implementation-groups>, the total of Safeguards
[^cis-ig1]: <https://www.cisecurity.org/controls/implementation-groups/ig1>, the count of IG1
[^cis-ig2]: <https://www.cisecurity.org/controls/implementation-groups/ig2>, the count of IG2
[^cis-ig3]: <https://www.cisecurity.org/controls/implementation-groups/ig3>, the count of IG3
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the enum CisImplementationGroup
