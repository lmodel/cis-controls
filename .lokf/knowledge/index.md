---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/cis-controls/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: cis-controls Knowledge Bundle
description: CIS Critical Security Controls v8.1 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/cis-controls/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# cis-controls Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for cis-controls. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/cis-controls>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website.

# Datasets

* [cis-controls LinkML schema](datasets/cis-controls-linkml-schema.md) - The LinkML schema of the structure of the CIS Critical Security Controls, `src/cis_controls/schema/cis_controls.yaml` (schema id `https://w3id.org/lmodel/cis-controls`, version 8.1.2): three classes, three enums and two identifier types, with no CIS text. Its `lokf adapt` copy `.lokf/cis-controls.yaml`, rooted on the Control and the Safeguard, is the bundle's domain schema.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/cis_controls/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/cis-controls.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: seven valid examples and 20 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator and checks the rules it cannot, `tests/test_edition.py`, which holds the edition file to the schema and the guide's counts, `tests/test_upstream.py`, which holds the schema header and the upstream watch to the same edition, `tests/test_watch.py`, which runs the watch against stubbed pages, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and nine released lmodel copies in `tests/neighbours/`.
* [The edition file](datasets/edition-file.md) - The edition file, `src/cis_controls/data/cis-controls-8.1.2.yaml`: CIS Controls v8.1 at its v8.1.2 revision as one `CisControls` document, with the 18 Controls, the 153 Safeguards, each Safeguard's asset class, security function and Implementation Groups, and a title and description for each element in the project's own words.

# Controls

* [Control 1](controls/control-1.md) - Control 1 of the CIS Controls, Version 8.1, which the edition file titles Knowing every device in the project's own words: it holds 5 Safeguards, 1.1 to 1.5, of which 2 are in Implementation Group 1, 4 in Implementation Group 2 and all 5 in Implementation Group 3.
* [Control 2](controls/control-2.md) - Control 2 of the CIS Controls, Version 8.1, which the edition file titles Knowing every program in the project's own words: it holds 7 Safeguards, 2.1 to 2.7, of which 3 are in Implementation Group 1, 6 in Implementation Group 2 and all 7 in Implementation Group 3.
* [Control 3](controls/control-3.md) - Control 3 of the CIS Controls, Version 8.1, which the edition file titles Looking after data in the project's own words: it holds 14 Safeguards, 3.1 to 3.14, of which 6 are in Implementation Group 1, 12 in Implementation Group 2 and all 14 in Implementation Group 3.
* [Control 4](controls/control-4.md) - Control 4 of the CIS Controls, Version 8.1, which the edition file titles Secure settings for devices and software in the project's own words: it holds 12 Safeguards, 4.1 to 4.12, of which 7 are in Implementation Group 1, 11 in Implementation Group 2 and all 12 in Implementation Group 3.
* [Control 5](controls/control-5.md) - Control 5 of the CIS Controls, Version 8.1, which the edition file titles Managing accounts in the project's own words: it holds 6 Safeguards, 5.1 to 5.6, of which 4 are in Implementation Group 1, all 6 in Implementation Group 2 and all 6 in Implementation Group 3.
* [Control 6](controls/control-6.md) - Control 6 of the CIS Controls, Version 8.1, which the edition file titles Managing access rights in the project's own words: it holds 8 Safeguards, 6.1 to 6.8, of which 5 are in Implementation Group 1, 7 in Implementation Group 2 and all 8 in Implementation Group 3.
* [Control 7](controls/control-7.md) - Control 7 of the CIS Controls, Version 8.1, which the edition file titles Finding and fixing vulnerabilities in the project's own words: it holds 7 Safeguards, 7.1 to 7.7, of which 4 are in Implementation Group 1, all 7 in Implementation Group 2 and all 7 in Implementation Group 3.
* [Control 8](controls/control-8.md) - Control 8 of the CIS Controls, Version 8.1, which the edition file titles Keeping and reviewing logs in the project's own words: it holds 12 Safeguards, 8.1 to 8.12, of which 3 are in Implementation Group 1, 11 in Implementation Group 2 and all 12 in Implementation Group 3.
* [Control 9](controls/control-9.md) - Control 9 of the CIS Controls, Version 8.1, which the edition file titles Email and browser protections in the project's own words: it holds 7 Safeguards, 9.1 to 9.7, of which 2 are in Implementation Group 1, 6 in Implementation Group 2 and all 7 in Implementation Group 3.
* [Control 10](controls/control-10.md) - Control 10 of the CIS Controls, Version 8.1, which the edition file titles Defending against malware in the project's own words: it holds 7 Safeguards, 10.1 to 10.7, of which 3 are in Implementation Group 1, all 7 in Implementation Group 2 and all 7 in Implementation Group 3.
* [Control 11](controls/control-11.md) - Control 11 of the CIS Controls, Version 8.1, which the edition file titles Recovering data in the project's own words: it holds 5 Safeguards, 11.1 to 11.5, of which 4 are in Implementation Group 1, all 5 in Implementation Group 2 and all 5 in Implementation Group 3.
* [Control 12](controls/control-12.md) - Control 12 of the CIS Controls, Version 8.1, which the edition file titles Managing network equipment in the project's own words: it holds 8 Safeguards, 12.1 to 12.8, of which 1 is in Implementation Group 1, 7 in Implementation Group 2 and all 8 in Implementation Group 3.
* [Control 13](controls/control-13.md) - Control 13 of the CIS Controls, Version 8.1, which the edition file titles Watching and defending the network in the project's own words: it holds 11 Safeguards, 13.1 to 13.11, of which none is in Implementation Group 1, 6 in Implementation Group 2 and all 11 in Implementation Group 3.
* [Control 14](controls/control-14.md) - Control 14 of the CIS Controls, Version 8.1, which the edition file titles Training the workforce in the project's own words: it holds 9 Safeguards, 14.1 to 14.9, of which 8 are in Implementation Group 1, all 9 in Implementation Group 2 and all 9 in Implementation Group 3.
* [Control 15](controls/control-15.md) - Control 15 of the CIS Controls, Version 8.1, which the edition file titles Managing service providers in the project's own words: it holds 7 Safeguards, 15.1 to 15.7, of which 1 is in Implementation Group 1, 4 in Implementation Group 2 and all 7 in Implementation Group 3.
* [Control 16](controls/control-16.md) - Control 16 of the CIS Controls, Version 8.1, which the edition file titles Secure applications in the project's own words: it holds 14 Safeguards, 16.1 to 16.14, of which none is in Implementation Group 1, 11 in Implementation Group 2 and all 14 in Implementation Group 3.
* [Control 17](controls/control-17.md) - Control 17 of the CIS Controls, Version 8.1, which the edition file titles Responding to incidents in the project's own words: it holds 9 Safeguards, 17.1 to 17.9, of which 3 are in Implementation Group 1, 8 in Implementation Group 2 and all 9 in Implementation Group 3.
* [Control 18](controls/control-18.md) - Control 18 of the CIS Controls, Version 8.1, which the edition file titles Testing the defences as an attacker would in the project's own words: it holds 5 Safeguards, 18.1 to 18.5, of which none is in Implementation Group 1, 3 in Implementation Group 2 and all 5 in Implementation Group 3.

# Glossary

* [Control](glossary/control.md) - In the CIS Controls, one of 18 numbered groups of Safeguards, each on one subject. The schema renders a Control as `CisControl`, with its number, 1 to 18, in `cis_control_id`.
* [Safeguard](glossary/safeguard.md) - In the CIS Controls, one action an enterprise takes under a Control, named by the Control's number and its own, such as Safeguard 4.1; Version 8.1 has 153. The schema renders a Safeguard as `CisSafeguard`, with its number in `cis_safeguard_id`.
* [Implementation Group](glossary/implementation-group.md) - In the CIS Controls, one of three tiers, IG1, IG2 and IG3, that say which Safeguards an enterprise takes up first; each includes the one before it, so IG1 holds 56 Safeguards, IG2 130 and IG3 all 153. The schema renders the tiers as `CisImplementationGroup`.
* [Asset class](glossary/asset-class.md) - In the CIS Controls, the kind of enterprise asset a Safeguard is about: Devices, Software, Data, Users, Network or Documentation in Version 8.1. The schema renders the classes as `CisAssetClass`.
* [Security function](glossary/security-function.md) - In the CIS Controls, the function of the NIST Cybersecurity Framework (CSF) 2.0 a Safeguard serves: Govern, Identify, Protect, Detect, Respond or Recover. The schema renders the functions as `CisSecurityFunction`, related to lmodel/nist-csf-v2's function class.

# References

* [CIS Critical Security Controls, Version 8.1](references/cis-controls-guide.md) - The guide the schema renders: the CIS Critical Security Controls, Version 8.1, from the Center for Internet Security (CIS), at its v8.1.2 revision of March 2025, licensed CC BY-NC-ND 4.0, and offered for download from <https://www.cisecurity.org/controls/v8-1>.
* [CIS's pages on the CIS Controls](references/cis-controls-site.md) - The public pages of the Center for Internet Security (CIS) that the schema and this bundle cite: the list of the 18 Controls, the Implementation Groups pages with their counts of Safeguards (56, 130 and 153), and the page on the guide to the asset classes.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - Why the schema models only the structure of the CIS Controls and none of CIS's text, what shaped it (only the CIS Controls, with lmodel/slsa's release pattern), what it crosses to (lmodel/oscal and lmodel/nist-csf-v2) and what it leaves out.
* [Element names and the shared namespace](explanations/element-names.md) - Why the schema's classes and enums carry the `Cis` prefix, why its identifiers are CIS's own numbers written as strings, why the enum values are upper case, and why no class, enum, type or key of the adapt copy is shared with LOKF or the nine released lmodel copies.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, edit `src/cis_controls/schema/cis_controls.yaml` with no CIS text in it, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-cis-controls.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the weekly upstream watch reports that CIS's pages name a version of the CIS Controls newer than the pinned 8.1.2, no longer name 8.1, have gone or redirected, or could not be read: read CIS's notes, decide whether the schema moves, and move the pins in `scripts/check_upstream_release.py` and the schema header together.
* [Validate data against the schema](playbooks/validate-data.md) - How to validate CIS Controls data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No validator checks that a Safeguard carries its Control's number, a repeated identifier or group, or that IG1 brings IG2.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders the CIS Controls in the project's own words and cites CIS's guide, no CIS text is added however it was produced, and the scheduled librarian proposes changes only through reviewed pull requests.
* [License and attribution](policies/license-and-attribution.md) - The repository's licences: Apache 2.0 for the schema and the code; CIS's CC BY-NC-ND 4.0 for the CIS Controls, which is why the repository carries no CIS text and the text slots are for text their user may use; MIT for the copier template's scaffolding; Apache 2.0 for the KTL sidecar and website templates; and CC BY 4.0 for this bundle.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.

# Workflows

* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-cis-controls.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/cis-controls.yaml` is current.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its cis-pages job runs `scripts/check_upstream_release.py` against CIS's pages for the CIS Controls, and on a finding opens or updates the issue titled Upstream watch: the CIS Controls have changed.
