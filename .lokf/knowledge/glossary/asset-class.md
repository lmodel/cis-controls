---
type: GlossaryTerm
id: https://w3id.org/lmodel/cis-controls/knowledge/glossary/asset-class
genre: reference
title: Asset class
description: "In the CIS Controls, the kind of enterprise asset a Safeguard is about: Devices, Software, Data, Users, Network or Documentation in Version 8.1. The schema renders the classes as `CisAssetClass`."
definition: The kind of enterprise asset a Safeguard of the CIS Controls is about.
resource: src/cis_controls/schema/cis_controls.yaml
definedBy:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: cis-asset-classes
    resource: https://www.cisecurity.org/insights/white-papers/guide-to-asset-classes-cis-critical-security-controls-v8-1
    title: the page on CIS's guide to the asset classes, read on 2026-10-30
  - id: cis-v8-1
    resource: https://www.cisecurity.org/controls/v8-1
    title: the guide this page offers, v8.1.2 of March 2025, read on 2026-10-30
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the enum CisAssetClass and the slot safeguard_asset_class
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# Asset class

CIS's page on its guide to the asset classes says that CIS restructured the asset classes and their definitions in Version 8.1.[^cis-asset-classes] The guide names six classes: Devices, Software, Data, Users, Network and Documentation. It divides each into subclasses and gives each Safeguard one class.[^cis-v8-1] The schema renders the classes as `CisAssetClass`, with upper-case values such as `DEVICES` and CIS's spelling as each value's title. A Safeguard names its class in `safeguard_asset_class`. The schema leaves the subclasses out.[^cis_controls.yaml]

[^cis-asset-classes]: <https://www.cisecurity.org/insights/white-papers/guide-to-asset-classes-cis-critical-security-controls-v8-1>, the page's summary
[^cis-v8-1]: <https://www.cisecurity.org/controls/v8-1>, the guide this page offers, the section on asset classes
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the enum CisAssetClass
