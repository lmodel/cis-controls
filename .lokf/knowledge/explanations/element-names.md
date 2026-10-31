---
type: Explanation
id: https://w3id.org/lmodel/cis-controls/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: Why the schema's classes and enums carry the `Cis` prefix, why its identifiers are CIS's own numbers written as strings, why the enum values are upper case, and why no class, enum, type or key of the adapt copy is shared with LOKF or the nine released lmodel copies.
resource: docs/about.md
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: docs-about.md
    resource: docs/about.md
    title: the paragraph on names
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the comment on cis_control_id
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:10:19Z"
status: draft
---

# Element names and the shared namespace

`docs/about.md` says that the element names are the schema's own. Classes and enums carry the `Cis` prefix, such as `CisControl` and `CisAssetClass`, so that they can be imported beside other vocabularies. Slots are snake_case, the identifiers sit in `cis_control_id` and `cis_safeguard_id`, and a Safeguard's other fields start with `safeguard_`. Every element is in the `cis_controls:` namespace.[^docs-about.md]

An identifier is CIS's own number as a string, such as `"4"` for Control 4 and `"4.1"` for Safeguard 4.1. The schema's comment says why: data then joins with CIS's guide and with the crosswalks that cite it without a translation. It also says to quote the number in YAML, which reads an unquoted `4` as a number and an unquoted `1.10` as the number 1.1. The validator rejects either as not a string, but a file loaded into the generated dataclasses without validation would turn 1.10 into 1.1.[^cis_controls.yaml]

The enum values are upper case, such as `IG1`, `DEVICES` and `GOVERN`, each with CIS's spelling as its title. `.linkmllint.yaml` relaxes the linter's naming rule for upper-case values. Its comment says why: the Implementation Groups are `IG1`, `IG2` and `IG3` in CIS's guide, so a value can be compared with CIS's label directly. The other enums follow the same form.[^linkmllint.yaml]

A host imports the adapt copy beside other copies and `lokf.yaml`, the schema of the Linked Open Knowledge Format (LOKF), and LinkML merges them into one namespace, where the last definition of a name wins silently. The README says that no class, enum or type shares a name with LOKF's or with the released copies of slsa, github-actions, oscal, spdx, nist-sp-800-218, nist-sp-800-53, nist-sp-800-171, nist-csf-v2 and in-toto. `title` and `description` carry LOKF's IRIs, so `lokf adapt` folds them into LOKF's slots and renames nothing. The copy shares no other key with the nine neighbours.[^readme.md] [Test data and tests](../datasets/test-data.md) names the test that checks it.

[^docs-about.md]: docs/about.md, the paragraph on names
[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the comment on cis_control_id
[^linkmllint.yaml]: .linkmllint.yaml, the comment
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
