# cis-controls

This project is a LinkML model of the structure of the CIS Critical Security
Controls, Version 8.1, which the Center for Internet Security (CIS)
publishes, at the guide's v8.1.2 revision of March 2025. It covers the
Controls, the Safeguards of each Control, and each Safeguard's asset class,
security function and Implementation Groups. It names every element by its
number and carries none of CIS's text.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`cis_controls.yaml`](schema/cis_controls.yaml): the schema

## Validating data

`linkml-validate -s src/cis_controls/schema/cis_controls.yaml -C CisSafeguard safeguard.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

Validate a file before loading it into either model in
`src/cis_controls/datamodel/`. LinkML 1.12.1 generates models that check
less:

- The dataclasses check required fields and enum values, but no pattern.
- The Pydantic models also check the patterns a field carries itself, such
  as the form of `cis_version`. They do not check the patterns of the two
  identifier types, so a Control or Safeguard identifier goes unchecked.

No validator checks these rules:

- that a Safeguard's identifier starts with the number of the Control it is
  listed under;
- that a list never repeats an identifier or an Implementation Group;
- that the Implementation Groups are cumulative. The validator checks that
  every Safeguard is in IG3, but not that a Safeguard in IG1 is in IG2 too.

`tests/test_data.py` checks the first and the last over every valid
example, and that no Safeguard repeats a group.
