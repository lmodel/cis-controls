---
type: Service
id: https://w3id.org/lmodel/cis-controls/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/cis-controls>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website."
resource: website
endpoint: https://lmodel.github.io/cis-controls
documentation: website/README.md
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-11-15T02:33:31Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site. `website/site.toml` names the repository `lmodel/cis-controls`, the site `https://lmodel.github.io` with the base path `/cis-controls`, and the title `cis-controls`.[^site.toml] It shows the pages of `docs/` except `docs/templates-linkml/`. It redirects the addresses the retired mkdocs site gave its pages:

- `/elements` to `/schema/`;
- each class, enum, type and slot page of the retired schema to its successor's page, such as `/elements/Safeguard` to `/schema/CisSafeguard/`, or to `/schema/` where it has none;
- any other page under `/elements` whose name the schema still has to that page under `/schema/`;
- `/about` to `/docs/about/`.

The other options take the site's defaults: the Knowledge Trust Ladder logo, the README as the home page, the changelog once it holds a release, and the schema's pages that `just gen-doc` writes.

`website/README.md` says what each page is built from. It also says that `npm run build` syncs the bundle, the README, the docs and the schema's pages before it builds and checks every link.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the build and its sources
