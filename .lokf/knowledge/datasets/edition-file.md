---
type: Dataset
id: https://w3id.org/lmodel/cis-controls/knowledge/datasets/edition-file
genre: reference
title: The edition file
description: "The edition file, `src/cis_controls/data/cis-controls-8.1.2.yaml`: CIS Controls v8.1 at its v8.1.2 revision as one `CisControls` document, with the 18 Controls, the 153 Safeguards, each Safeguard's asset class, security function and Implementation Groups, and a title and description for each element in the project's own words."
resource: src/cis_controls/data/cis-controls-8.1.2.yaml
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-guide
relatedTo:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/test-data
sources:
  - id: edition
    resource: src/cis_controls/data/cis-controls-8.1.2.yaml
    title: the header comment and the document
  - id: readme.md
    resource: README.md
    title: the What it models section
  - id: notice
    resource: NOTICE
    title: The CIS Critical Security Controls
  - id: test_edition.py
    resource: tests/test_edition.py
    title: SAFEGUARDS_PER_GROUP and the four tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:14:49Z"
status: draft
---

# The edition file

`src/cis_controls/data/cis-controls-8.1.2.yaml` holds CIS Controls v8.1 at its v8.1.2 revision of March 2025 as one `CisControls` document. It lists the 18 Controls and their 153 Safeguards, and gives each Safeguard its asset class, security function and Implementation Groups, as CIS's guide sets them out.[^edition] Implementation Group 1 holds 56 Safeguards, Implementation Group 2 holds 130 and Implementation Group 3 holds all 153.[^test_edition.py]

The file gives each Control and Safeguard a title and a one- or two-sentence description in the project's own words, written from what each requires.[^readme.md] NOTICE says why: CIS licenses the CIS Controls under CC BY-NC-ND 4.0, so the repository holds no title, description, overview, explanation or procedure from the guide, copied or paraphrased. Each title is the project's own name for the element, never CIS's.[^notice]

`tests/test_edition.py` holds the file to the schema, to the guide's counts and to the rules no validator checks, as [Test data and tests](test-data.md) lists. The 18 [Control concepts](../controls/index.md) give each Control's title and description from it.

[^edition]: src/cis_controls/data/cis-controls-8.1.2.yaml, the header comment and the document
[^readme.md]: README.md, the What it models section
[^notice]: NOTICE, The CIS Critical Security Controls
[^test_edition.py]: tests/test_edition.py, SAFEGUARDS_PER_GROUP and the four tests
