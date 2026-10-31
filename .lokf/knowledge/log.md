# Change Log

## 2026-10-31

* **Changed**: the 18 Control concepts and the licence policy now point to the edition file, `src/cis_controls/data/cis-controls-8.1.2.yaml`, which describes each Control and Safeguard in the project's own words; no Control's counts changed.
* **Prose**: reworded 9 concept bodies in plain English, splitting long sentences and blocks. No fact, link, number or frontmatter changed.
* **Changed**: `tests/test_data.py` now checks that no example repeats a Control or Safeguard identifier, so the validate-data playbook and the test-data concept say it checks all three rules.
* **Changed**: the security policy now names the three assets a release carries, as SECURITY.md does.
* **Changed**: the Controls and Safeguards are named by CIS's own numbers, such as "4" and "4.1", as the schema now names them.

## 2026-10-30

* **Prose**: reworded 35 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Added**: cis-controls LinkML schema, from `src/cis_controls/schema/cis_controls.yaml`.
* **Added**: Generated artefacts, from the justfile, `.linkml/generators.yaml` and `project/`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: Control 1, from CIS's guide at v8.1.2.
* **Added**: Control 2, from CIS's guide at v8.1.2.
* **Added**: Control 3, from CIS's guide at v8.1.2.
* **Added**: Control 4, from CIS's guide at v8.1.2.
* **Added**: Control 5, from CIS's guide at v8.1.2.
* **Added**: Control 6, from CIS's guide at v8.1.2.
* **Added**: Control 7, from CIS's guide at v8.1.2.
* **Added**: Control 8, from CIS's guide at v8.1.2.
* **Added**: Control 9, from CIS's guide at v8.1.2.
* **Added**: Control 10, from CIS's guide at v8.1.2.
* **Added**: Control 11, from CIS's guide at v8.1.2.
* **Added**: Control 12, from CIS's guide at v8.1.2.
* **Added**: Control 13, from CIS's guide at v8.1.2.
* **Added**: Control 14, from CIS's guide at v8.1.2.
* **Added**: Control 15, from CIS's guide at v8.1.2.
* **Added**: Control 16, from CIS's guide at v8.1.2.
* **Added**: Control 17, from CIS's guide at v8.1.2.
* **Added**: Control 18, from CIS's guide at v8.1.2.
* **Added**: Control, a glossary term, from CIS's pages and the schema.
* **Added**: Safeguard, a glossary term, from CIS's pages and the schema.
* **Added**: Implementation Group, a glossary term, from CIS's pages and the schema.
* **Added**: Asset class, a glossary term, from CIS's pages and the schema.
* **Added**: Security function, a glossary term, from CIS's pages and the schema.
* **Added**: CIS Critical Security Controls, Version 8.1, the guide the schema renders.
* **Added**: CIS's pages on the CIS Controls, which the schema cites.
* **Added**: Scope, influences and mappings, from the README, the changelog and `docs/about.md`.
* **Added**: Element names and the shared namespace, from `docs/about.md`, `.linkmllint.yaml` and the README.
* **Added**: Regenerate and test after a schema change, from CONTRIBUTING.md and the justfiles.
* **Added**: Cut a release, from `.releaserc.json`, the changelog and CONTRIBUTING.md.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from NOTICE, LICENSE and the README.
* **Added**: Security policy, from SECURITY.md and the Dependabot settings.
* **Added**: Documentation site, from `website/`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Knowledge sources map, the first scrape map of this repository.
* **Removal**: Example Service A, the sidecar's placeholder, now that real concepts stand in its place.
* **Removal**: Example Service B, the sidecar's placeholder, now that real concepts stand in its place.
* **Initialization**: Scaffolded the LOKF bundle for cis-controls with placeholder
  services. Real concepts to follow.
