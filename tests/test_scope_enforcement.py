from pathlib import Path

from schema.frontmatter import load_markdown
from validation.validate_country_layer import validate_repository

from conftest import write_markdown


def test_disallowed_country_file_key_is_rejected(
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
    data["value_codes"] = []
    write_markdown(path, data, body)

    assert validate_repository(temp_repository) == 1
    output = capsys.readouterr().out
    assert "value_codes" in output
    assert "Extra inputs are not permitted" in output