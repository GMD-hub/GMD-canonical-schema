from pathlib import Path

from schema.frontmatter import load_markdown
from validation.validate_country_layer import validate_repository

from conftest import write_markdown


def parameter_path(repository: Path, parameter_id: str) -> Path:
    return repository / "knowledge" / "parameters" / f"{parameter_id}.md"


def country_parameter_path(repository: Path, iso3: str) -> Path:
    return repository / "country-parameters" / "countries" / iso3 / "parameters.md"


def _set_table_parameter_contract(temp_repository: Path) -> None:
    definition_path = parameter_path(temp_repository, "PARAM-EDU-YEARS-BY-LEVEL")
    definition, body = load_markdown(definition_path)
    definition["value_type"] = "table"
    definition["value_schema"] = None
    definition["row_schema"] = {
        "national_label_en": "string",
        "national_label_local": "string",
        "entry_age": "integer",
        "duration_years": "integer",
        "isced_level": "string",
        "gmd_educat4": "integer",
        "gmd_educat5": "integer",
        "gmd_educat7": "integer",
    }
    write_markdown(definition_path, definition, body)


def _set_table_values(temp_repository: Path) -> None:
    values_path = country_parameter_path(temp_repository, "PER")
    values, body = load_markdown(values_path)
    table_rows = [
        {
            "national_label_en": "Primary complete",
            "national_label_local": "Primaria completa",
            "entry_age": 6,
            "duration_years": 6,
            "isced_level": "ISCED 1",
            "gmd_educat4": 2,
            "gmd_educat5": 2,
            "gmd_educat7": 3,
        },
        {
            "national_label_en": "Lower secondary complete",
            "national_label_local": "Secundaria basica completa",
            "entry_age": 12,
            "duration_years": 3,
            "isced_level": "ISCED 2",
            "gmd_educat4": 3,
            "gmd_educat5": 3,
            "gmd_educat7": 5,
        },
    ]
    for record in values["parameters"]:
        if record["parameter_id"] == "PARAM-EDU-YEARS-BY-LEVEL":
            record["value"] = table_rows
    write_markdown(values_path, values, body)


def test_table_parameter_rows_validate(temp_repository: Path) -> None:
    _set_table_parameter_contract(temp_repository)
    _set_table_values(temp_repository)

    assert validate_repository(temp_repository) == 0


def test_table_parameter_missing_row_key_fails(
    temp_repository: Path, capsys
) -> None:
    _set_table_parameter_contract(temp_repository)
    _set_table_values(temp_repository)

    values_path = country_parameter_path(temp_repository, "PER")
    values, body = load_markdown(values_path)
    for record in values["parameters"]:
        if record["parameter_id"] == "PARAM-EDU-YEARS-BY-LEVEL":
            record["value"][0].pop("isced_level")
            break
    write_markdown(values_path, values, body)

    assert validate_repository(temp_repository) == 1
    output = capsys.readouterr().out
    assert "row 0 keys must be" in output
