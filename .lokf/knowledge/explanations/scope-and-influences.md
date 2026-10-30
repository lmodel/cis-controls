---
type: Explanation
id: https://w3id.org/lmodel/cis-controls/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: Why the schema models only the structure of the CIS Controls and none of CIS's text, what shaped it (only the CIS Controls, with lmodel/slsa's release pattern), what it crosses to (lmodel/oscal and lmodel/nist-csf-v2) and what it leaves out.
resource: README.md
about:
  - https://w3id.org/lmodel/cis-controls/knowledge/datasets/cis-controls-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Removed entries
  - id: docs-about.md
    resource: docs/about.md
    title: What is left out
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# Scope, influences and mappings

The README says that the schema models the structure of the CIS Controls, Version 8.1, at its v8.1.2 revision: the Controls, the Safeguards, and each Safeguard's asset class, security function and Implementation Groups. It carries none of CIS's text, because CIS licenses the Controls under CC BY-NC-ND 4.0 and the repository is Apache-2.0.[^readme.md]

Its influences are the CIS Controls alone: the schema renders one publication, and its release asset and governance files follow lmodel/slsa. It crosses to two vocabularies and borrows from neither:

- **OSCAL**: each class names its lmodel/oscal counterpart in `broad_mappings`, a Control as `oscal:Group` and a Safeguard as `oscal:Control`, because the OSCAL class is the more general one;
- **NIST CSF 2.0**: `CisSecurityFunction` names `nist_csf_v2:Function` in `related_mappings`, and each value carries the CSF function's two letters in an annotation. lmodel/nist-csf-v2 gives no single function an IRI, so the values carry no `meaning`.

The README leaves out CIS's text, CIS's own mappings to other frameworks, its companion guides, the subclasses of each asset class, earlier versions of the Controls, and the rules no validator can check.

The changelog says what the rewrite removed: CIS's text in the examples and descriptions, the slots that held it, the three subsets, the mappings file to lmodel/nist-csf-v2, whose rows all named elements that nist-csf-v2 v0.1.0 no longer has, and the mappings to lmodel/iso27001, which is being rewritten.[^changelog.md] `docs/about.md` repeats what is left out for readers of the schema's pages.[^docs-about.md]

[^readme.md]: README.md, What it models, Influences, Mappings and Not modelled here
[^changelog.md]: CHANGELOG.md, the Removed entries
[^docs-about.md]: docs/about.md, What is left out
