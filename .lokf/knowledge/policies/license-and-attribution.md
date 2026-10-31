---
type: Policy
id: https://w3id.org/lmodel/cis-controls/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "The repository's licences: Apache 2.0 for the schema and the code; CIS's CC BY-NC-ND 4.0 for the CIS Controls, which is why the repository carries no CIS text and the text slots are for text their user may use; MIT for the copier template's scaffolding; Apache 2.0 for the KTL sidecar and website templates; and CC BY 4.0 for this bundle."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: license
    resource: LICENSE
    title: the Apache License 2.0
  - id: readme.md
    resource: README.md
    title: the License section
  - resource: website/NOTICE
    title: the part adapted from the LOKF toolkit's site
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# License and attribution

The schema and the code are under the Apache License, Version 2.0.[^license] NOTICE describes the third-party work the repository models or derives from.[^notice]

- The schema, the generated models and `project/` model the structure of the CIS Critical Security Controls, Version 8.1, as CIS revised it in March 2025, in the project's own words. They are not CIS's, and their use implies no endorsement by CIS.
- CIS licenses the CIS Controls under CC BY-NC-ND 4.0. NOTICE says that the licence lets anyone share the guide unchanged, for non-commercial purposes and with credit to CIS. It also says that the licence lets no one share a changed version, and that CIS requires its prior approval for commercial use. So the repository carries no CIS text, names each Control and Safeguard by its number, and records only the structure the guide sets out.
- The schema's `title` and `description` slots are for text their user has the right to use: the user's own words, or CIS's under CIS's terms. The Apache License does not cover CIS's text.
- The justfile, configuration and documentation scaffolding derive from linkml-project-copier, under the MIT License, whose text NOTICE carries.
- The sidecar's scripts and workflows are copies of the ktl-sidecar templates, and the site under `website/` derives from the ktl-website templates, all under the Apache License 2.0. `website/NOTICE` lists the part adapted from the site of the Linked Open Knowledge Format (LOKF) toolkit.

The README says that the knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares. It adds that this is not an official CIS project, and that its use implies no endorsement by CIS.[^readme.md]

[^license]: LICENSE, the Apache License 2.0
[^notice]: NOTICE, every section
[^readme.md]: README.md, the License section
