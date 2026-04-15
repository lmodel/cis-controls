"""Data test."""
import os
import glob
import pytest
from pathlib import Path

import cis_controls.datamodel.cis_controls
from linkml_runtime.loaders import yaml_loader
from linkml.validator import validate_file as linkml_validate_file

SCHEMA_PATH = Path(__file__).parent.parent / "src" / "cis_controls" / "schema" / "cis_controls.yaml"

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test that valid data files load without error."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        cis_controls.datamodel.cis_controls,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test that invalid data files fail JSON schema validation."""
    target_class_name = Path(filepath).stem.split("-")[0]
    report = linkml_validate_file(filepath, str(SCHEMA_PATH), target_class=target_class_name)
    assert report.results, (
        f"Expected validation errors in {filepath} but none were raised. "
        "Check that this file genuinely violates the schema."
    )
