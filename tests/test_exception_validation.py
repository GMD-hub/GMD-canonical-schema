from copy import deepcopy
from pathlib import Path

from schema.frontmatter import load_markdown
from validation.validate_country_layer import validate_repository

from conftest import write_markdown


def exception_path(repository: Path, iso3: str) -> Path:
    return repository / "country-parameters" / "countries" / iso3 / "exceptions.md"


def test_reversed_exception_window_fails(temp_repository: Path, capsys) -> None:
    path = exception_path(temp_repository, "PER")
    data, body = load_markdown(path)
    data["exceptions"][0]["effective_from"] = 2000
    data["exceptions"][0]["effective_to"] = 1999
    write_markdown(path, data, body)

    assert validate_repository(temp_repository) == 1
    assert "effective_from must be less than or equal to effective_to" in capsys.readouterr().out


def test_duplicate_exception_id_within_file_fails(
    temp_repository: Path, capsys
) -> None:
    path = exception_path(temp_repository, "PER")
    data, body = load_markdown(path)
    data["exceptions"].append(deepcopy(data["exceptions"][0]))
    write_markdown(path, data, body)

    assert validate_repository(temp_repository) == 1
    assert "duplicate exception_id EXC-PER-001" in capsys.readouterr().out


def test_duplicate_exception_id_across_repository_fails(
    temp_repository: Path, capsys
) -> None:
    per_data, _ = load_markdown(exception_path(temp_repository, "PER"))
    alb_path = exception_path(temp_repository, "ALB")
    alb_data, alb_body = load_markdown(alb_path)
    alb_data["exceptions"].append(deepcopy(per_data["exceptions"][0]))
    write_markdown(alb_path, alb_data, alb_body)

    assert validate_repository(temp_repository) == 1
    output = capsys.readouterr().out
    assert "duplicate exception_id EXC-PER-001; first found in" in output


def test_overlapping_exceptions_are_informational(
    temp_repository: Path, capsys
) -> None:
    path = exception_path(temp_repository, "PER")
    data, body = load_markdown(path)
    overlap = deepcopy(data["exceptions"][0])
    overlap["exception_id"] = "EXC-PER-002"
    overlap["effective_from"] = 1995
    overlap["effective_to"] = 2005
    data["exceptions"].append(overlap)
    write_markdown(path, data, body)

    assert validate_repository(temp_repository) == 0
    output = capsys.readouterr().out
    assert "## Overlapping exception report" in output
    assert "PER | VAR-educy | EXC-PER-001 | EXC-PER-002" in output
