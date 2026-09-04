"""Tests for float parameter value_schema."""


from schema.parameter import ParameterDefinition

def _parameter(**overrides):
    data = {
        "parameter_id": "PARAM-WLF-TEST",
        "parameter_name": "Test",
        "module_id": "MOD-WLF",
        "schema_version": "0.1",
        "status": "draft",
        "authority": "GPID Team",
        "kind": "construction",
        "value_type": "mapping",
        "value_schema": {"alpha": "number", "theta": "number"},
        "applies_to_variables": [],
        "fallback_policy": "undecided",
        "global_default": None,
        "provenance": {
            "source_document": "x",
            "extraction_method": "manual",
            "extracted_on": "2026-09-01",
            "human_reviewed": False,
            "reviewer": None,
            "notes": "x",
        },
    }
    data.update(overrides)
    return data


def test_parameter_float_value_schema_validates():
    param = ParameterDefinition.model_validate(_parameter())
    assert param.value_schema["alpha"] == "number"
