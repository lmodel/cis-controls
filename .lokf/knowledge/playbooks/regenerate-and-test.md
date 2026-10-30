---
type: Playbook
id: https://w3id.org/lmodel/cis-controls/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the schema and check it: `uv sync --group dev`, edit `src/cis_controls/schema/cis_controls.yaml` with no CIS text in it, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint recipe
  - id: project.justfile
    resource: project.justfile
    title: lokf-adapt and lokf-adapt-check
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# Regenerate and test after a schema change

1. Install the toolchain once: Python 3.10 or later, `uv` and `just`, then `uv sync --group dev` in the clone.[^contributing.md]
2. Edit `src/cis_controls/schema/cis_controls.yaml`. It is the one file to write by hand. `project/`, `src/cis_controls/datamodel/`, `docs/schema/` and `.lokf/cis-controls.yaml` are generated from it. Put no CIS text in it, name elements by number, and say in the pull request which part of CIS's guide a new or changed element renders.
3. Run `just lint`, which runs `linkml-lint --ignore-warnings` under `.linkmllint.yaml`.[^justfile]
4. Run `just gen-project` and `just gen-doc`, then `just lokf-adapt`, which rewrites the adapt copy with the two roots.[^project.justfile] Commit the output.
5. Add an example under `tests/data/valid/` for a new class and a counter-example under `tests/data/invalid/` for a new constraint, named `ClassName-suffix.yaml`, with a first line `# Fails at: <pointer>`, then run `just test`.
6. Run the pre-commit hooks on what you staged (`uvx pre-commit run`), and write a changelog entry under `## [Unreleased]` when the change alters behaviour.

CI runs the same: `main.yaml` runs `just lint`, `just test` and `just lokf-adapt-check`, and fails when the adapt copy is stale.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint recipe
[^project.justfile]: project.justfile, lokf-adapt and lokf-adapt-check
