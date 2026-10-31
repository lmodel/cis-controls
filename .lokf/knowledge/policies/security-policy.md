---
type: Policy
id: https://w3id.org/lmodel/cis-controls/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the five update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-31T01:04:53Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. It says that one person maintains the repository, so a first reply takes days and there is no bounty. It also says that only the latest release receives fixes.[^security.md]

The repository releases the schema and the Python models generated from it. Nothing is published to PyPI. When the bundle or the schema has changed, the knowledge release attaches the adapt copy, the bundle as a zip and a Microsoft 365 Copilot skill zip, each with its `.sha256` and a build-provenance attestation. The upstream watch reads two public pages of CIS, sends no credentials and writes nothing but its report.

The policy's table of surfaces names each workflow and what holds it. The pull request checks run read-only. The release job runs only on a push to `main`, in the `release` Environment. The website's deploy job alone holds the Pages scopes. The upstream watch writes only issues. The librarian's agent runs without a write token, and its `publish` job runs no agent.

Every workflow declares `permissions: {}` at the top, pins its actions to commit hashes and runs harden-runner in audit mode. Dependabot keeps the pins, the package's lock, the sidecar's lock, the website's npm packages and the release tools' npm lock current, each monthly.[^dependabot.yml] The policy says that a ruleset on `main` blocks deletion and force-pushes and keeps the history linear. It names two settings not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection.

The policy leaves out the CIS Controls themselves, LinkML, a compromised runner or harness, and whether the knowledge bundle is true.

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the five entries
