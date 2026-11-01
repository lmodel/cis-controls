<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# cis-controls

CIS Critical Security Controls v8.1 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/cis-controls](https://lmodel.github.io/cis-controls)

## What it models

The schema models the structure of the [CIS Critical Security Controls, Version 8.1](https://www.cisecurity.org/controls/v8-1), which the Center for Internet Security (CIS) publishes, as CIS revised it in March 2025 (v8.1.2). It holds the 18 Controls (`CisControl`), their 153 Safeguards (`CisSafeguard`) with each one's asset class, security function and Implementation Groups, and the edition that holds them all (`CisControls`).

The schema carries none of CIS's text. The edition file, [src/cis_controls/data/cis-controls-8.1.2.yaml](src/cis_controls/data/cis-controls-8.1.2.yaml), gives each Control and Safeguard a title and a short description in this project's own words, and `tests/test_edition.py` holds it to the schema and to CIS's counts. A weekly workflow reads CIS's pages and opens an issue when they name a newer version or no longer name the pinned one.

## Mappings

* **OSCAL**: each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`: a Control is a group, and a Safeguard a control.
* **NIST CSF 2.0**: `CisSecurityFunction` names the function class of [lmodel/nist-csf-v2](https://github.com/lmodel/nist-csf-v2) in `related_mappings`, and each value carries the function's two letters, such as `GV`, in a `csf_function_id` annotation.

The schema maps no Safeguard to another framework's elements. CIS publishes those mappings itself.

## Not modelled here

* CIS's text: its titles and descriptions of the Controls and Safeguards, and the guide's overviews, explanations, procedures and glossary. The edition file describes each Control and Safeguard in this project's words instead.
* CIS's mappings from the Safeguards to other frameworks, and its companion guides.
* The subclasses into which CIS's guide divides each asset class. A Safeguard names only the class.
* Earlier versions of the CIS Controls.
* The rules no validator can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/cis_controls/schema/](src/cis_controls/schema): the LinkML schema, `cis_controls.yaml` (edit this)
* [src/cis_controls/data/](src/cis_controls/data): the edition file, `cis-controls-8.1.2.yaml`
* [src/cis_controls/datamodel/](src/cis_controls/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/cis-controls.yaml`, is the copy `just lokf-adapt` writes from `src/cis_controls/schema/cis_controls.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-cis-controls.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots two classes on `Concept`, so a concept may name either as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
CisControl, CisSafeguard
```

A concept writes the CIS number in `cis_control_id` or `cis_safeguard_id`, and a Safeguard's concept names its Control's concept in `isPartOf`. A name and a description are the concept's own `title` and `description`, in words the bundle has the right to use.

No class, enum or type of the copy shares a name with LOKF's schema or with another lmodel copy, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

CIS licenses the CIS Controls under CC BY-NC-ND 4.0, which allows no changed version. So this repository carries no CIS text, copied or paraphrased, and the Apache License does not extend to CIS's text. [NOTICE](NOTICE) states the position. This is not an official CIS project, and its use implies no endorsement by CIS.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
