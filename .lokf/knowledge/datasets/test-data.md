---
type: Dataset
id: https://w3id.org/lmodel/cis-controls/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: seven valid examples and 20 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator and checks the rules it cannot, `tests/test_upstream.py`, which holds the schema header and the upstream watch to the same edition, `tests/test_watch.py`, which runs the watch against stubbed pages, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and nine released lmodel copies in `tests/neighbours/`."
resource: tests
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid folders
  - id: test_data.py
    resource: tests/test_data.py
    title: the four tests
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the two tests
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the stubbed pages and the tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS, ROOTS and the tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:10:19Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds seven examples: one edition with two Controls, two Controls and four Safeguards. `tests/data/invalid/` holds 20 counter-examples, each invalid for one reason.[^data] A file's class is the part of its name before the first hyphen, such as `CisSafeguard-without-ig3.yaml`. A counter-example's first line names where it fails, as `# Fails at:` and a JSON pointer such as `/safeguard_implementation_groups`. The examples name each Control and Safeguard by its number and carry no CIS text. One Safeguard example shows the text slots holding a user's own note.

`tests/test_data.py` loads each valid example into the generated dataclasses and validates it, checks that each counter-example fails at the place its first line names, and checks that each class has a valid example. It also checks the rules the validator cannot: that a Safeguard's Implementation Groups are one of the three cumulative sets, never repeating a group, and that a Safeguard listed under a Control carries that Control's number.[^test_data.py]

`tests/test_upstream.py` checks that the schema header's `version` and `source` and its annotations name the edition and the page that `scripts/check_upstream_release.py` pins.[^test_upstream.py] `tests/test_watch.py` runs the watch against stubbed pages: nothing changed, a newer version, a revision past the pinned one, the pinned version gone, a page gone, a blocked reader, a redirect, and no credentials sent.[^test_watch.py]

`tests/test_schema_rules.py` checks the adapt copy. It holds each neighbour copy in `tests/neighbours/` to its release's checksum: slsa v0.7.0, github-actions v0.3.0, oscal v0.1.2, spdx v0.1.0, nist-sp-800-218 v0.1.1, nist-sp-800-53 v0.1.0, nist-sp-800-171 v0.1.0, nist-csf-v2 v0.1.0 and in-toto v0.1.0. It checks that:

- the copy shares no class, enum, type or subset name with LOKF or a neighbour, and no key with a neighbour;
- it roots exactly `CisControl` and `CisSafeguard` on `Concept`;
- every mapping uses a prefix the copy binds;
- each mapping into oscal or nist-csf-v2 names a term that neighbour's copy declares.[^test_schema_rules.py]

[^data]: tests/data, valid and invalid
[^test_data.py]: tests/test_data.py, the four tests
[^test_upstream.py]: tests/test_upstream.py, the two tests
[^test_watch.py]: tests/test_watch.py, the tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS, ROOTS and the tests
