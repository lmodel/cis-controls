"""Data test."""

import glob
import os
from pathlib import Path

import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

import cis_controls.datamodel.cis_controls

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))

SCHEMA = (
    Path(__file__).parent.parent
    / "src"
    / "cis_controls"
    / "schema"
    / "cis_controls.yaml"
)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        cis_controls.datamodel.cis_controls,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint (docs/index.md says what the generated models leave out), so each
# example is held to it: a valid one must pass, and a counter-example must fail.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    report = validate(
        yaml.safe_load(Path(filepath).read_text()),
        str(SCHEMA),
        Path(filepath).stem.split("-")[0],
    )
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, so a file that starts failing for
    another reason fails this test."""
    text = Path(filepath).read_text()
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    pointer = first.removeprefix("# Fails at: ").strip()
    report = validate(
        yaml.safe_load(text), str(SCHEMA), Path(filepath).stem.split("-")[0]
    )
    messages = [r.message for r in report.results]
    assert any(m.endswith(f" in {pointer}") for m in messages), messages


def test_every_concept_class_has_an_example():
    """Each class a knowledge-bundle concept may name as its type, and each
    class those hold, has a valid example."""
    classes = set(yaml.safe_load(SCHEMA.read_text())["classes"])
    examples = {Path(f).stem.split("-")[0] for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)


# The rules the validator cannot check, held over every valid example. The
# schema's comments say why each is out of the validator's reach.
CUMULATIVE = ({"IG3"}, {"IG2", "IG3"}, {"IG1", "IG2", "IG3"})


def _safeguards(node, control=None):
    """Every Safeguard an example holds, with the identifier of the Control
    it is listed under, or None for a Safeguard on its own."""
    if isinstance(node, list):
        for item in node:
            yield from _safeguards(item, control)
    elif isinstance(node, dict):
        if "cis_safeguard_id" in node:
            yield node, control
        control = node.get("cis_control_id", control)
        for value in node.values():
            yield from _safeguards(value, control)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_examples_keep_the_rules_no_validator_checks(filepath):
    """A Safeguard's Implementation Groups are cumulative, and a Safeguard
    listed under a Control carries that Control's number."""
    data = yaml.safe_load(Path(filepath).read_text())
    for safeguard, control in _safeguards(data):
        groups = safeguard["safeguard_implementation_groups"]
        assert len(groups) == len(set(groups)), safeguard
        assert set(groups) in CUMULATIVE, safeguard
        if control:
            assert safeguard["cis_safeguard_id"].startswith(f"{control}."), safeguard
