---
type: Reference
id: https://w3id.org/lmodel/cis-controls/knowledge/references/cis-controls-site
genre: reference
title: CIS's pages on the CIS Controls
description: "The public pages of the Center for Internet Security (CIS) that the schema and this bundle cite: the list of the 18 Controls, the Implementation Groups pages with their counts of Safeguards (56, 130 and 153), and the page on the guide to the asset classes."
resource: https://www.cisecurity.org/controls/cis-controls-list
sources:
  - id: cis-controls-list
    resource: https://www.cisecurity.org/controls/cis-controls-list
    title: the page's title and links, read on 2026-10-30
  - id: cis-implementation-groups
    resource: https://www.cisecurity.org/controls/implementation-groups
    title: the total of Safeguards, read on 2026-10-30
  - id: cis-asset-classes
    resource: https://www.cisecurity.org/insights/white-papers/guide-to-asset-classes-cis-critical-security-controls-v8-1
    title: the page on CIS's guide to the asset classes, read on 2026-10-30
generated:
  by: process:ktl-librarian
  at: "2026-10-30T23:47:49Z"
status: draft
---

# CIS's pages on the CIS Controls

CIS's list of the Controls is titled with their number, 18, and links the resources for Version 8.1 and the earlier Versions 8 and 7.1.[^cis-controls-list] CIS's page on the Implementation Groups says that Versions 8 and 8.1 hold 153 Safeguards, and links a page for each group, which gives its count: 56 in IG1, 74 more in IG2 and 23 more in IG3.[^cis-implementation-groups] CIS's page on its guide to the asset classes, published on May 12, 2025, says that Version 8.1 restructured the asset classes and their definitions; the guide itself asks for a registration.[^cis-asset-classes]

The schema's `see_also` names these pages, and its comments take the counts from them. The upstream watch reads the list page and the page for Version 8.1 every week.

[^cis-controls-list]: <https://www.cisecurity.org/controls/cis-controls-list>, the page's title and links
[^cis-implementation-groups]: <https://www.cisecurity.org/controls/implementation-groups>, the total, and the pages for each group
[^cis-asset-classes]: <https://www.cisecurity.org/insights/white-papers/guide-to-asset-classes-cis-critical-security-controls-v8-1>, the page's summary
