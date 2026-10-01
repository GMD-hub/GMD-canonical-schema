from copy import deepcopy
from pathlib import Path

from schema.frontmatter import load_markdown
from validation.validate_country_layer import validate_repository

from conftest import write_markdown


def test_overlapping_parameter_windows_fail(
    temp_repository: Path, capsys
) -> None:
    path = (
        temp_repository
        / "country-parameters"
        / "countries"
        / "PER"
        / "parameters.md"
    )
    data, body = load_markdown(path)
    base = next(
        record
        for record in data["parameters"]
        if record["parameter_id"] == "PARAM-DEM-MIN-MARRIAGE-AGE"
    )
    overlapping = deepcopy(base)
    overlapping["effective_from"] = 1999
    overlapping["effective_to"] = 2005
    data["parameters"].append(overlapping)
    write_markdown(path, data, body)

    assert validate_repository(temp_repository) == 1
    assert "overlapping validity windows for PARAM-DEM-MIN-MARRIAGE-AGE" in capsys.readouterr().out


def test_selector_disjoint_parameter_windows_pass(
    temp_repository: Path, capsys
) -> None:
    path = (
        temp_repository
        / "country-parameters"
        / "countries"
        / "PER"
        / "parameters.md"
    )
    data, body = load_markdown(path)
    base_index = next(
        index
        for index, record in enumerate(data["parameters"])
        if record["parameter_id"] == "PARAM-DEM-MIN-MARRIAGE-AGE"
    )
    data["parameters"][base_index]["selectors"] = {"survey_type": "consumption"}

    overlapping = deepcopy(data["parameters"][base_index])
    overlapping["effective_from"] = 1990
    overlapping["effective_to"] = 2010
    overlapping["selectors"] = {"survey_type": "income"}
    data["parameters"].append(overlapping)
    write_markdown(path, data, body)

    assert validate_repository(temp_repository) == 0
    output = capsys.readouterr().out
    assert "Structural failures" not in output