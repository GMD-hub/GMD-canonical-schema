from copy import deepcopy
import json
import subprocess
import sys
from pathlib import Path

from schema.country_parameters import CountryParameterFile
from schema.frontmatter import load_markdown
from schema.parameter import ParameterDefinition

from conftest import write_markdown


PARAMETER_ID = "PARAM-DEM-MIN-MARRIAGE-AGE"


def applies_in_year(record, year: int) -> bool:
    return (
        (record.effective_from is None or record.effective_from <= year)
        and (record.effective_to is None or year <= record.effective_to)
    )


def test_effective_dating_boundaries(temp_repository: Path) -> None:
    path = (
        temp_repository / "country-parameters" / "countries" / "PER" / "parameters.md"
    )
    data, body = load_markdown(path)
    base = next(
        record for record in data["parameters"] if record["parameter_id"] == PARAMETER_ID
    )
    data["parameters"] = [
        record for record in data["parameters"] if record["parameter_id"] != PARAMETER_ID
    ]
    early = deepcopy(base)
    early["effective_from"] = 1980
    early["effective_to"] = 1999
    early["value"] = 16
    late = deepcopy(base)
    late["effective_from"] = 2000
    late["effective_to"] = None
    late["value"] = 18
    data["parameters"].extend([early, late])
    write_markdown(path, data, body)

    registry = {}
    for definition_path in (temp_repository / "knowledge" / "parameters").glob("*.md"):
        definition = ParameterDefinition.model_validate(load_markdown(definition_path)[0])
        registry[definition.parameter_id] = definition

    country_file = CountryParameterFile.model_validate(
        load_markdown(path)[0],
        context={"registry": registry},
    )

    def selected(year: int):
        return [
            record
            for record in country_file.parameters
            if record.parameter_id == PARAMETER_ID and applies_in_year(record, year)
        ]

    assert [record.effective_to for record in selected(1999)] == [1999]
    assert [record.effective_from for record in selected(2000)] == [2000]
    assert selected(1979) == []


def test_2019_bundle_excludes_expired_exception(temp_repository: Path) -> None:
    result = subprocess.run(
        [sys.executable, "build/compile_bundle.py", "PER", "2019"],
        cwd=temp_repository,
        check=True,
        capture_output=True,
        text=True,
    )
    bundle_path = temp_repository / result.stdout.strip()
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    assert bundle["country"]["exceptions"] == []