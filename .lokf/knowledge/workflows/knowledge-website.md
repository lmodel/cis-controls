---
type: Service
id: https://w3id.org/lmodel/cis-controls/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:03:26Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website", which the ktl-website skill installed. It runs on a push or a pull request that touches the site's sources, every Monday at 05:23 UTC, and by hand. Those sources are `website/`, `ktl-website/`, `.lokf/`, `knowledge_bundle/`, the README, `docs/`, `.assets/`, the changelog, `.linkml/`, a schema under `src/*/schema/`, this workflow and `knowledge-federation.yaml`. The weekly run catches what no push brings, such as the changelog's promotion, whose commit skips CI.[^knowledge-website.yaml]

Its `build` job runs under a read-only token. A push builds on the default branch only, and every other event builds. The job:

- runs harden-runner in audit mode;
- checks the repository out with its full history, because the health page's "a source moved" lines come from git;
- sets up uv;
- finds the site's folder: `ktl-website/` when it holds a `site.toml`, else `website/`;
- installs `just` when `site.toml` builds the site's data with it;
- runs the site's `scripts/build.sh`, which runs `lokf export` and, for a LinkML schema, gen-doc, then builds the site with Hugo and Pagefind from the site's own `uv.lock`, cleans its raw HTML and checks its links;
- uploads the site's `dist/` as the Pages artifact.

Its `deploy` job runs harden-runner and GitHub's own deploy-pages action, and nothing else. It holds `pages: write` and `id-token: write` in the `github-pages` Environment. It runs from the default branch only, once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. Until then the workflow builds the site but deploys nothing. In a private repository the job warns when the Pages site is public or of unknown visibility. [Documentation site](../services/documentation-site.md) describes what it publishes.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
