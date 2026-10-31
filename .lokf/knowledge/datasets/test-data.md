---
type: Dataset
id: https://w3id.org/lmodel/cis-controls/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: seven valid examples and 20 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator and checks the rules it cannot, `tests/test_edition.py`, which holds the edition file to the schema and the guide's counts, `tests/test_upstream.py`, which holds the schema header and the upstream watch to the same edition, `tests/test_watch.py`, which runs the watch against stubbed pages, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and nine released lmodel copies in `tests/neighbours/`."
resource: tests
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid folders
  - id: test_data.py
    resource: tests/test_data.py
    title: the six tests
  - id: test_edition.py
    resource: tests/test_edition.py
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
  at: "2026-10-31T12:14:49Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds seven examples: one edition with two Controls, two Controls and four Safeguards. `tests/data/invalid/` holds 20 counter-examples, each invalid for one reason.[^data] A file's class is the part of its name before the first hyphen, such as `CisSafeguard-without-ig3.yaml`. A counter-example's first line names where it fails, as `# Fails at:` and a JSON pointer such as `/safeguard_implementation_groups`. The examples name each Control and Safeguard by its number and carry no CIS text. One Safeguard example shows the text slots holding a user's own note.

`tests/test_data.py` loads each valid example into the generated dataclasses and validates it, checks that each counter-example fails at the place its first line names, and checks that each class has a valid example. It also checks the rules the validator cannot:[^test_data.py]

- a Safeguard's Implementation Groups are one of the three cumulative sets, and never repeat a group;
- a Safeguard listed under a Control carries that Control's number;
- no example repeats a Control or Safeguard identifier.

`tests/test_edition.py` holds the edition file, `src/cis_controls/data/cis-controls-8.1.2.yaml`, to the schema and to the guide. It checks that:[^test_edition.py]

- the file passes the validator and loads into the generated dataclasses;
- it is edition 8.1.2, holds the 18 Controls in order, numbers each Control's Safeguards from 1 without a gap, and fills each Implementation Group to the count CIS states;
- its Implementation Groups are cumulative and never repeat a group, and no Safeguard is listed under a Control other than its own;
- every Control and Safeguard has a title and a description, each title is short, and no two elements share a title.

`tests/test_upstream.py` checks that the schema header's `version` and `source` and its annotations name the edition and the page that `scripts/check_upstream_release.py` pins.[^test_upstream.py]

`tests/test_watch.py` runs the watch against stubbed pages, in these cases:[^test_watch.py]

- nothing changed;
- a newer version, or a revision past the pinned one;
- the pinned version gone, or a page gone;
- a blocked reader, a connection cut off, or a charset Python does not know;
- a redirect, and the site's text quoted as code;
- no credentials sent.

`tests/test_schema_rules.py` checks the adapt copy. It holds each neighbour copy in `tests/neighbours/` to its release's checksum: slsa v0.7.0, github-actions v0.3.0, oscal v0.1.2, spdx v0.1.0, nist-sp-800-218 v0.1.1, nist-sp-800-53 v0.1.0, nist-sp-800-171 v0.1.0, nist-csf-v2 v0.1.0 and in-toto v0.1.0. It checks that:

- the copy shares no class, enum, type or subset name with LOKF or a neighbour, and no key with a neighbour;
- it roots exactly `CisControl` and `CisSafeguard` on `Concept`;
- every mapping uses a prefix the copy binds;
- each mapping into oscal or nist-csf-v2 names a term that neighbour's copy declares.[^test_schema_rules.py]

[^data]: tests/data, valid and invalid
[^test_data.py]: tests/test_data.py, the six tests
[^test_edition.py]: tests/test_edition.py, the four tests
[^test_upstream.py]: tests/test_upstream.py, the two tests
[^test_watch.py]: tests/test_watch.py, the tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS, ROOTS and the tests
