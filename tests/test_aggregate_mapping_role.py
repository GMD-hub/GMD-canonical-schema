"""Tests for the aggregate variable role"""

import pytest
from pydantic import ValidationError

from schema.variable import VariableDefinition

_CTX = {"allow_unresolved_draft": True}


def _variable(**overrides):
    data = {
        "variable_id": "VAR-agg",
        "canonical_label": "Test aggregate",
        "variable_name": "agg",
        "module_id": "MOD-WLF",
        "gmd_version": "3.0",
        "schema_version": "0.1",
        "status": "draft",
        "tier": 1,
        "unit_of_analysis": "household",
        "mapping_role": "aggregate",
        "data_type": "numeric_continuous",
        "value_codes": None,
        "allowed_range": {"min": 0, "max": None},
        "missing_codes": [],
        "derived_from": [],
        "derives_to": [],
        "country_parameters": [],
        "prerequisites": [],
        "rules": [],
        "exceptions": [],
        "external_standards": [],
        "source_hints": {"question_keywords": [], "typical_section_names": []},
        "provenance": {
            "source_document": "x",
            "source_section": "x",
            "extraction_method": "manual",
            "extracted_on": "2026-09-01",
            "human_reviewed": False,
            "reviewer": None,
            "notes": "x",
        },
    }
    data.update(overrides)
    return data


def test_aggregate_role_with_blocks_and_open_range_validates():
    var = VariableDefinition.model_validate(
        _variable(component_structure={"operation": "sum"}), context=_CTX
    )
    assert var.mapping_role == "aggregate"
    assert var.allowed_range.max is None


def test_aggregate_requires_component_structure():
    with pytest.raises(ValidationError):
        VariableDefinition.model_validate(_variable(), context=_CTX)


def test_aggregate_blocks_forbidden_on_non_aggregate():
    data = _variable(
        mapping_role="atomic",
        component_structure={"operation": "sum"},
        allowed_range={"min": 0, "max": 10},
    )
    with pytest.raises(ValidationError):
        VariableDefinition.model_validate(data, context=_CTX)

