# About cis-controls

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

The CIS Critical Security Controls sort an enterprise's security work into
Controls, each a group of Safeguards on one subject. Each Safeguard is about
one class of enterprise asset and serves one security function. CIS places
it in one or more of three Implementation Groups, which say how soon an
enterprise should take it up. The schema gives the Control and the
Safeguard a class each, and holds them in one document for an edition.

Element names are the schema's own. Classes and enums carry the `Cis` prefix
(`CisControl`, `CisSafeguard`, `CisAssetClass`) so they can be imported
beside other vocabularies. Slots are snake_case, and the fields of a
Safeguard start with `safeguard_`. The enum values are upper case, such as
`IG1`, `DEVICES` and `GOVERN`, each with CIS's spelling as its title. Every
element is in the `cis_controls:` namespace
(`https://w3id.org/lmodel/cis-controls/`).

The identifiers sit in `cis_control_id` and `cis_safeguard_id`. An identifier
is CIS's own number as a string, such as `"4"` for Control 4 and `"4.1"` for
Safeguard 4.1, so data joins with CIS's guide and the crosswalks that cite it.
Quote it in YAML, which reads an unquoted `1.10` as the number 1.1.

The descriptions are this project's own words. CIS licenses the CIS Controls
under CC BY-NC-ND 4.0, so the schema, its examples, the edition file and
these pages carry no CIS text, copied or paraphrased. The edition file,
`src/cis_controls/data/cis-controls-8.1.2.yaml`, gives each Control and
Safeguard a title and a short description in the project's words, written
from what each requires. The `title` and `description` slots are for text
their user has the right to use. NOTICE states the position.

## What is left out

The schema models the structure of the Controls and nothing of CIS's text:
no title, description, overview or procedure of a Control or Safeguard as
CIS wrote it, and none of the guide's glossary. It leaves out the subclasses into which CIS's
guide divides each asset class, CIS's mappings from the Safeguards to other
frameworks, its companion guides, and earlier versions of the Controls.

## Reference

- [CIS Critical Security Controls, Version 8.1](https://www.cisecurity.org/controls/v8-1)
- [The CIS Controls list](https://www.cisecurity.org/controls/cis-controls-list)
- [The Implementation Groups](https://www.cisecurity.org/controls/implementation-groups)
- [CIS's guide to the asset classes of Version 8.1](https://www.cisecurity.org/insights/white-papers/guide-to-asset-classes-cis-critical-security-controls-v8-1)
