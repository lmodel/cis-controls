<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# cis-controls

CIS Critical Security Controls v8.1 (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/cis-controls](https://lmodel.github.io/cis-controls)

## What it models

The structure of the [CIS Critical Security Controls, Version 8.1](https://www.cisecurity.org/controls/v8-1), which the Center for Internet Security (CIS) publishes, as CIS revised it in March 2025, when the guide's pages were labelled v8.1.2:

* **Controls** (`CisControl`): the 18 Controls, each named by its number, as `CIS-1` to `CIS-18`, and holding its Safeguards.
* **Safeguards** (`CisSafeguard`): the 153 Safeguards, each named by its Control's number and its own, such as `CIS-1.1`. Each Safeguard has:
  * one asset class (`CisAssetClass`): Devices, Software, Data, Users, Network or Documentation;
  * one security function (`CisSecurityFunction`): one of the six functions of the NIST Cybersecurity Framework (CSF) 2.0, Govern, Identify, Protect, Detect, Respond or Recover;
  * the Implementation Groups that include it (`CisImplementationGroup`): IG1 holds 56 Safeguards, IG2 130 and IG3 all 153, since each group includes the one before it.
* **The edition** (`CisControls`): one edition of the CIS Controls as a single document that holds all of these.

The schema carries none of CIS's text: no Control or Safeguard title or description. It names each element by its number, and records which Safeguards belong to which Control and the three properties above. The schema header's `version` is 8.1.2, and its `source` is CIS's page for Version 8.1. CIS publishes no openly licensed, machine-readable form of the Controls, so the repository holds no copy of them. A weekly workflow reads CIS's pages and opens an issue when they name a newer version or no longer name the pinned one.

The counts come from CIS's pages on [the Controls list](https://www.cisecurity.org/controls/cis-controls-list) and [the Implementation Groups](https://www.cisecurity.org/controls/implementation-groups). Release tags number the schema's versions.

## Influences

None beyond the CIS Controls: the schema renders one publication, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema crosses to two vocabularies and borrows from none.

* **OSCAL**: a CIS Control is a group of Safeguards, and a Safeguard a single control, in the sense of the Open Security Controls Assessment Language (OSCAL). Each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`, because the OSCAL class is the more general one.
* **NIST CSF 2.0**: the security functions are the six functions of CSF 2.0. `CisSecurityFunction` names the function class of [lmodel/nist-csf-v2](https://github.com/lmodel/nist-csf-v2) in `related_mappings`, and each value carries the function's two letters, such as `GV`, in a `csf_function_id` annotation. nist-csf-v2 gives no single function an IRI of its own, so the values carry no `meaning`.

The schema names no mapping from a Safeguard to any other framework's elements. CIS publishes those mappings itself.

## Not modelled here

* CIS's text: the titles and descriptions of the Controls and Safeguards, and the guide's overviews, explanations, procedures and glossary.
* CIS's mappings from the Safeguards to other frameworks, and its companion guides.
* The subclasses into which CIS's guide divides each asset class; a Safeguard names only the class.
* Earlier versions of the CIS Controls.
* The rules no validator can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/cis_controls/schema/](src/cis_controls/schema): the LinkML schema, `cis_controls.yaml` (edit this)
* [src/cis_controls/datamodel/](src/cis_controls/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/cis-controls.yaml`, which `lokf adapt` writes from `src/cis_controls/schema/cis_controls.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-cis-controls.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name either of them as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
CisControl, CisSafeguard
```

A concept writes the CIS number in `cis_control_id` or `cis_safeguard_id`, and a Safeguard's concept also writes its `safeguard_asset_class`, `safeguard_security_function` and `safeguard_implementation_groups`. A Safeguard's concept names its Control's concept in `isPartOf`. A name and a description are the concept's own `title` and `description`, in words the bundle has the right to use.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the released copies of slsa, github-actions, oscal, spdx, nist-sp-800-218, nist-sp-800-53, nist-sp-800-171, nist-csf-v2 and in-toto. A slot shares a name only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing. The copy shares no other key with the nine neighbours, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

CIS licenses the CIS Controls under CC BY-NC-ND 4.0. That licence lets anyone share CIS's guide unchanged, for non-commercial purposes and with credit to CIS. It lets no one share a changed version, and CIS requires its prior approval for commercial use. So this repository carries no CIS text, and the schema's `title` and `description` slots are for text you have the right to use: your own words, or CIS's under CIS's terms. The Apache License does not extend to CIS's text. [NOTICE](NOTICE) says more.

This is not an official CIS project, and its use implies no endorsement by CIS.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
