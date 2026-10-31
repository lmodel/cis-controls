---
type: Dataset
id: https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
genre: reference
title: cis-controls LinkML schema
description: "The LinkML schema of the structure of the CIS Critical Security Controls, `src/cis_controls/schema/cis_controls.yaml` (schema id `https://w3id.org/lmodel/cis-controls`, version 8.1.2): three classes, three enums and two identifier types, with no CIS text. Its `lokf adapt` copy `.lokf/cis-controls.yaml`, rooted on the Control and the Safeguard, is the bundle's domain schema."
resource: src/cis_controls/schema/cis_controls.yaml
version: 8.1.2
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-site
sources:
  - id: cis_controls.yaml
    resource: src/cis_controls/schema/cis_controls.yaml
    title: the header, the slots, the classes, the enums and the types
  - id: readme.md
    resource: README.md
    title: the What it models, Mappings and Knowledge Trust Ladder (KTL) sections
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: cis-controls.yaml
    resource: .lokf/cis-controls.yaml
    title: the notes lokf adapt wrote
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:10:19Z"
status: draft
---

# cis-controls LinkML schema

`src/cis_controls/schema/cis_controls.yaml` is the schema, titled "CIS Critical Security Controls". Its header gives `version: 8.1.2`, the label that the pages of CIS's guide carry for its revision of March 2025. It also gives `source: https://www.cisecurity.org/controls/v8-1`, CIS's page for Version 8.1.[^cis_controls.yaml] Its annotations give the version that CIS's site shows, `8.1`, the revision's month, `2025-03`, and the day the pages were read, `2026-10-30`.

The schema's comments say that CIS licenses the CIS Controls under CC BY-NC-ND 4.0, so the schema carries no CIS text. They also say that the edition holds 18 Controls and 153 Safeguards: Implementation Group 1 holds 56, Implementation Group 2 holds 130 and Implementation Group 3 holds all 153. The schema declares the prefix `cis_controls:` as `https://w3id.org/lmodel/cis-controls/` and the license Apache-2.0, and it imports only `linkml:types`.

## Classes

- **`CisControls`** is the tree root: one edition of the CIS Controls as a whole. It requires `cis_version`, such as `8.1` or `8.1.2`, and `cis_controls`, which holds at least one Control.
- **`CisControl`** is one Control. It requires `cis_control_id`, such as `"4"`, and it may hold `title`, `description` and its Safeguards in `control_safeguards`.
- **`CisSafeguard`** is one Safeguard. It requires `cis_safeguard_id`, such as `"4.1"`, `safeguard_asset_class`, `safeguard_security_function` and `safeguard_implementation_groups`, and it may hold `title` and `description`.

The list of Implementation Groups holds one to three values and must hold `IG3`, because Implementation Group 3 includes every Safeguard. The schema's comment says that the groups are cumulative, that the validator cannot check the rest of that rule, and that `tests/test_data.py` checks it over the examples.

## Enums and types

- `CisImplementationGroup` has the values `IG1`, `IG2` and `IG3`.
- `CisAssetClass` has `DEVICES`, `SOFTWARE`, `DATA`, `USERS`, `NETWORK` and `DOCUMENTATION`.
- `CisSecurityFunction` has `GOVERN`, `IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND` and `RECOVER`, each with a `csf_function_id` annotation such as `GV`.

Each value has a title in CIS's spelling, such as `Devices`. Two types hold the forms of the identifiers:

- `cis_control_identifier` is a number from 1 to 18, as CIS writes it.
- `cis_safeguard_identifier` is the Control's number, a dot and the Safeguard's number, as CIS writes it.

`title` and `description` carry the IRIs `schema:name` and `schema:description`, and their descriptions say that they hold text their user has the right to use.

## Mappings

Each class names a class of lmodel/oscal in `broad_mappings`: `oscal:Catalog` for the edition, `oscal:Group` for the Control and `oscal:Control` for the Safeguard. `CisSecurityFunction` names `nist_csf_v2:Function`, the class of lmodel/nist-csf-v2 for a function of the NIST Cybersecurity Framework (CSF) 2.0, in `related_mappings`.[^readme.md] [Scope, influences and mappings](../explanations/scope-and-influences.md) says more.

## As the bundle's domain schema

A domain schema of the Linked Open Knowledge Format (LOKF) is a LinkML schema that imports LOKF's `lokf.yaml` and adds a host's classes and keys, so that `lokf validate` checks the concepts typed with them. The README says that this bundle's domain schema is `.lokf/cis-controls.yaml`, which `lokf adapt` writes from the schema. Edit the source, never the copy. The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name the copy.

`project.justfile` passes two roots to `lokf adapt`: `CisControl` and `CisSafeguard`. Its comment says that these are the two elements that CIS numbers and other documents cite. It also says that `CisControls` is the document that holds an edition's Controls.[^project.justfile] The copy's notes say that `lokf adapt` re-rooted the two classes on `lokf:Concept` and folded `title` and `description` into LOKF's slots.[^cis-controls.yaml] The copy renames nothing, and `CisControls` is no longer a tree root in it. The concepts under `controls/` in this bundle are typed `CisControl`.

The generated models, `project/` and the adapt copy come from this file: see [Generated artefacts](generated-artefacts.md). [Element names and the shared namespace](../explanations/element-names.md) says why no class, enum or type shares a name with LOKF's or a neighbour's.

[^cis_controls.yaml]: src/cis_controls/schema/cis_controls.yaml, the header and the classes
[^readme.md]: README.md, the Mappings section
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^cis-controls.yaml]: .lokf/cis-controls.yaml, the notes
