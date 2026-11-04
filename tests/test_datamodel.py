"""Checks what the generated Python models do with the examples and the catalogue."""

from pathlib import Path

import pytest
import yaml
from linkml_runtime.loaders import yaml_loader

from capec.datamodel import capec as dataclasses_module
from capec.datamodel import capec_pydantic
from tests.capec_xml import converter

DATA = Path(__file__).parent / "data"
SMALL = DATA / "valid" / "CapecAttackPatternCatalog-small.yaml"
PATTERN = DATA / "valid" / "CapecAttackPattern-every-key.yaml"


def test_a_small_catalogue_loads_into_the_dataclasses():
    catalogue = yaml_loader.load(
        str(SMALL), target_class=dataclasses_module.CapecAttackPatternCatalog
    )
    assert catalogue.Version == "3.9"
    assert catalogue.Attack_Patterns[0].ID == "1"


def test_a_small_catalogue_loads_into_the_pydantic_model():
    catalogue = capec_pydantic.CapecAttackPatternCatalog(
        **yaml.safe_load(SMALL.read_text(encoding="utf-8"))
    )
    assert catalogue.Attack_Patterns[0].Abstraction == "Standard"


def test_the_fullest_pattern_loads_into_both():
    data = yaml.safe_load(PATTERN.read_text(encoding="utf-8"))
    assert capec_pydantic.CapecAttackPattern(**data).ID == "1"
    loaded = yaml_loader.load(
        str(PATTERN), target_class=dataclasses_module.CapecAttackPattern
    )
    assert loaded.Execution_Flow[0].Step == 1


def test_the_pydantic_model_refuses_a_key_the_xsd_lacks():
    data = yaml.safe_load(SMALL.read_text(encoding="utf-8"))
    data["Not_In_The_XSD"] = "x"
    with pytest.raises(ValueError, match="Not_In_The_XSD"):
        capec_pydantic.CapecAttackPatternCatalog(**data)


def test_the_whole_catalogue_loads_into_the_pydantic_model():
    catalogue = capec_pydantic.CapecAttackPatternCatalog(**converter.catalogue_data())
    assert len(catalogue.Attack_Patterns) == 615


def test_the_whole_catalogue_loads_into_the_dataclasses():
    catalogue = dataclasses_module.CapecAttackPatternCatalog(
        **converter.catalogue_data()
    )
    assert len(catalogue.Attack_Patterns) == 615
    assert catalogue.Attack_Patterns[0].ID == "1"
