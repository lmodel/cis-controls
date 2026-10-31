# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A LinkML schema of the structure of the CIS Critical Security Controls, Version 8.1, at its v8.1.2 revision.** It holds the Controls, the Safeguards of each, and each Safeguard's asset class, security function and Implementation Groups, names each element by its number, and carries no text of the Center for Internet Security (CIS).
- **A weekly upstream watch**, which reads CIS's pages for the pinned version and reports a newer version, a missing pinned one, a moved page or a check that could not finish.
- **`.lokf/cis-controls.yaml`, the schema's `lokf adapt` copy, rooted on the Control and the Safeguard.** The knowledge release attaches it as `schema-<tag>-cis-controls.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of nine released lmodel copies.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **Classes, enums and keys carry the schema's own prefix**: `CisControls`, `CisControl`, `CisSafeguard`, `CisImplementationGroup`, `CisAssetClass` and `CisSecurityFunction`, with the identifiers in `cis_control_id` and `cis_safeguard_id`, so none shares a name with LOKF or another lmodel schema.
- **The schema's name is `cis_controls`, as its file and package are, and the Python project's name is `cis-controls-linkml`.** PyPI publishing stays off.

### Removed

- **CIS's text, from the examples and the descriptions.** The CIS Controls are licensed CC BY-NC-ND 4.0, and this repository is Apache-2.0.
- **The `overview`, `why_critical` and `procedures_and_tools` slots and the three subsets.** The slots held CIS's text, and a subset marks schema elements, not a Safeguard's Implementation Group.
- **The SSSOM mappings to lmodel/nist-csf-v2 and the `iso27001:` mappings.** Every SSSOM row named an element that nist-csf-v2 v0.1.0 no longer has, and lmodel/iso27001 is being rewritten.
- **The PyPI publishing workflow and the mkdocs site and its preview.** The knowledge website replaces the site.
- **The unused `yamllint` runtime dependency.** No code imports it, and the pre-commit hook installs its own copy.
