---
type: GlossaryTerm
id: https://w3id.org/lmodel/cis-controls/knowledge/glossary/security-function
genre: reference
title: Security function
description: "In the CIS Controls, the function of the NIST Cybersecurity Framework (CSF) 2.0 a Safeguard serves: Govern, Identify, Protect, Detect, Respond or Recover. The schema renders the functions as `CisSecurityFunction`, related to lmodel/nist-csf-v2's function class."
definition: The function of the NIST Cybersecurity Framework 2.0 that a Safeguard of the CIS Controls serves.
resource: src/cis_controls/schema/cis_controls.yaml
definedBy:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: cis-v8-1
    resource: https://www.cisecurity.org/controls/v8-1
    title: the guide this page offers, v8.1.2 of March 2025, read on 2026-10-30
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the enum CisSecurityFunction and the slot safeguard_security_function
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# Security function

CIS's page for Version 8.1 says that the version realigned the security functions to the NIST Cybersecurity Framework (CSF) 2.0 and added the Govern function that CSF 2.0 introduced. The guide gives each Safeguard one of the six functions.[^cis-v8-1] The schema renders the functions as `CisSecurityFunction`, with the values `GOVERN`, `IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND` and `RECOVER`, each annotated with the function's two letters in CSF 2.0, such as `GV`. The enum names `nist_csf_v2:Function` in `related_mappings`, and a Safeguard names its function in `safeguard_security_function`.[^cis_controls.yaml]

[^cis-v8-1]: <https://www.cisecurity.org/controls/v8-1>, the page's list of what is new, and the guide it offers
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the enum CisSecurityFunction
