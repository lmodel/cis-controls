"""Checks on the edition file, src/cis_controls/data/cis-controls-8.1.2.yaml.

The file is the whole edition as one CisControls document: the Controls, the
Safeguards of each, and each Safeguard's asset class, security function and
Implementation Groups, as CIS's guide sets them out, with a title and a
description for each Control and Safeguard in this project's own words. The
validator holds it to the schema; the tests here hold it to the guide's counts,
to the rules no validator checks, and to carrying a title and a description
for every element.
"""

from collections import Counter
from pathlib import Path

import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

from cis_controls.datamodel.cis_controls import CisControls

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "cis_controls" / "schema" / "cis_controls.yaml"
EDITION = ROOT / "src" / "cis_controls" / "data" / "cis-controls-8.1.2.yaml"

# The counts CIS's pages state for the edition: the Safeguards of each
# Control, and the Safeguards each Implementation Group holds.
SAFEGUARDS_PER_CONTROL = {
    "1": 5,
    "2": 7,
    "3": 14,
    "4": 12,
    "5": 6,
    "6": 8,
    "7": 7,
    "8": 12,
    "9": 7,
    "10": 7,
    "11": 5,
    "12": 8,
    "13": 11,
    "14": 9,
    "15": 7,
    "16": 14,
    "17": 9,
    "18": 5,
}
SAFEGUARDS_PER_GROUP = {"IG1": 56, "IG2": 130, "IG3": 153}
CUMULATIVE = ({"IG3"}, {"IG2", "IG3"}, {"IG1", "IG2", "IG3"})


def _edition():
    return yaml.safe_load(EDITION.read_text())


def _safeguards(edition):
    for control in edition["cis_controls"]:
        for safeguard in control["control_safeguards"]:
            yield control, safeguard


def test_edition_validates_and_loads():
    """The edition passes the validator and loads into the dataclasses."""
    report = validate(_edition(), str(SCHEMA), "CisControls")
    assert not report.results, [r.message for r in report.results]
    assert yaml_loader.load(str(EDITION), target_class=CisControls)


def test_edition_holds_the_guides_counts():
    """The edition is 8.1.2, holds the 18 Controls in order, gives each its
    Safeguards numbered from 1 without a gap, and fills each Implementation
    Group to the count CIS states."""
    edition = _edition()
    assert edition["cis_version"] == "8.1.2"
    controls = [c["cis_control_id"] for c in edition["cis_controls"]]
    assert controls == [str(n) for n in range(1, 19)]
    for control in edition["cis_controls"]:
        numbers = [s["cis_safeguard_id"] for s in control["control_safeguards"]]
        expected = SAFEGUARDS_PER_CONTROL[control["cis_control_id"]]
        assert numbers == [
            f"{control['cis_control_id']}.{n}" for n in range(1, expected + 1)
        ], control["cis_control_id"]
    groups = Counter()
    for _, safeguard in _safeguards(edition):
        groups.update(safeguard["safeguard_implementation_groups"])
    assert dict(groups) == SAFEGUARDS_PER_GROUP


def test_edition_keeps_the_rules_no_validator_checks():
    """Implementation Groups are cumulative and never repeated, and no
    Safeguard is listed under a Control other than its own."""
    for control, safeguard in _safeguards(_edition()):
        groups = safeguard["safeguard_implementation_groups"]
        assert len(groups) == len(set(groups)), safeguard["cis_safeguard_id"]
        assert set(groups) in CUMULATIVE, safeguard["cis_safeguard_id"]
        assert safeguard["cis_safeguard_id"].startswith(f"{control['cis_control_id']}.")


def test_edition_describes_every_element_in_its_own_words():
    """Every Control and Safeguard has a title and a description, the title
    is short, and no two elements share a title."""
    edition = _edition()
    elements = list(edition["cis_controls"])
    elements += [s for _, s in _safeguards(edition)]
    titles = []
    for element in elements:
        assert element["title"].strip(), element
        assert len(element["title"].split()) <= 9, element["title"]
        assert len(element["description"].split()) >= 4, element
        titles.append(element["title"])
    repeated = [t for t, n in Counter(titles).items() if n > 1]
    assert not repeated, repeated
