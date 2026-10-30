---
type: Policy
id: https://w3id.org/lmodel/cis-controls/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders the CIS Controls in the project's own words and cites CIS's guide, no CIS text is added however it was produced, and the scheduled librarian proposes changes only through reviewed pull requests."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the project note and the section on agent automation
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that everything a contributor submits is theirs, whatever tools helped make it, and that they must understand, verify and defend it.[^ai_covenant.md] Its note for this project says that the repository models someone else's framework, the CIS Controls. It names two failure modes that are worse here than elsewhere:

- a rule or element a model produced, presented as what the CIS Controls say;
- CIS's own text, which the repository may not carry.

Three rules follow:

- an element under `src/cis_controls/schema/` says what the CIS Controls say, in the project's own words, with the part of CIS's guide cited in the pull request;
- no CIS text goes into the schema, the examples, the docs or the bundle, copied or closely paraphrased, and a model's text is checked for CIS's wording before it is submitted;
- everything the schema defines is in the `cis_controls:` namespace, with CIS's numbers appearing only as values.

The covenant forbids posting AI output as an independent voice in issues or discussions. It sets four rules for the scheduled librarian:

- a bot identity or the maintainer's, never both;
- every change as a pull request a person approves;
- a read-only job that hands a patch to a separate job that runs no agent;
- a recorded verdict only where a person said it.

AI co-authorship trailers in commits are discouraged.

[^ai_covenant.md]: AI_COVENANT.md, A note specific to this project and Repository-Owned Agent Automation
