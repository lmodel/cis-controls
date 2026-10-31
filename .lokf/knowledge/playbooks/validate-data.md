---
type: Playbook
id: https://w3id.org/lmodel/cis-controls/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: "How to validate CIS Controls data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No validator checks that a Safeguard carries its Control's number, a repeated identifier or group, or that IG1 brings IG2."
resource: docs/index.md
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: Validating data
generated:
  by: process:ktl-librarian
  at: "2026-10-31T01:04:53Z"
status: draft
---

# Validate data against the schema

Run `linkml-validate -s src/cis_controls/schema/cis_controls.yaml -C CisSafeguard safeguard.yaml`, naming the class the file holds. It checks the file against the JSON Schema the validator generates from the schema, and `tests/test_data.py` holds every example to the same check.[^docs-index.md]

Validate a file before loading it into either model in `src/cis_controls/datamodel/`. The page says that the models LinkML 1.12.1 generates check less:

- the dataclasses check required fields and enum values, but no pattern;
- the Pydantic models also check the patterns a field carries itself, such as the form of `cis_version`, but not the patterns of the two identifier types.

No validator checks three rules:

- a Safeguard's identifier starts with the number of the Control it is listed under;
- a list never repeats an identifier or an Implementation Group;
- the Implementation Groups are cumulative: the validator checks that every Safeguard is in IG3, but not that a Safeguard in IG1 is in IG2 too.

`tests/test_data.py` checks all three over every valid example.

[^docs-index.md]: docs/index.md, Validating data
