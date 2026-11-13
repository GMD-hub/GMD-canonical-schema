from copy import deepcopy
from pathlib import Path

import pytest
from pydantic import ValidationError

from schema.frontmatter import load_markdown
from schema.variable import VariableDefinition


ROOT = Path(__file__).resolve().parents[1]


def variable_data() -> dict:
    data, _ = load_markdown(ROOT / "knowledge/variables/dem/VAR-male.md")
    result = deepcopy(data)
    result["status"] = "draft"
    result["provenance"]["human_reviewed"] = False
    result["provenance"]["reviewer"] = None
    return result


def validate_variable(data: dict) -> VariableDefinition:
    return VariableDefinition.model_validate(
        data,
        context={
            "allow_unresolved_draft": True,
            "parameter_ids": set(data["country_parameters"]),
            "rule_ids": set(data["rules"]),
        },
    )


def test_approved_variable_requires_reviewed_provenance() -> None:
    data = variable_data()
    data["status"] = "approved"

    with pytest.raises(
        ValidationError, match="approved status requires human_reviewed provenance"
    ):
        validate_variable(data)


def test_approved_variable_accepts_recorded_reviewer() -> None:
    data = variable_data()
    data["status"] = "approved"
    data["provenance"]["human_reviewed"] = True
    data["provenance"]["reviewer"] = "reviewer@example.invalid"

    variable = validate_variable(data)

    assert variable.status == "approved"
    assert variable.provenance.human_reviewed is True


def test_unchanged_draft_variable_remains_valid() -> None:
    variable = validate_variable(variable_data())

    assert variable.status == "draft"
    assert variable.provenance.human_reviewed is False
    assert variable.provenance.reviewer is None


def test_reviewed_provenance_requires_reviewer() -> None:
    data = variable_data()
    data["status"] = "approved"
    data["provenance"]["human_reviewed"] = True

    with pytest.raises(
        ValidationError, match="reviewer is required when human_reviewed is true"
    ):
        validate_variable(data)


@pytest.mark.parametrize("reviewer", ["", "   "])
def test_reviewed_provenance_rejects_blank_reviewer(reviewer: str) -> None:
    data = variable_data()
    data["status"] = "approved"
    data["provenance"]["human_reviewed"] = True
    data["provenance"]["reviewer"] = reviewer

    with pytest.raises(
        ValidationError, match="reviewer is required when human_reviewed is true"
    ):
        validate_variable(data)


def test_reviewed_provenance_rejects_coerced_boolean() -> None:
    data = variable_data()
    data["status"] = "approved"
    data["provenance"]["human_reviewed"] = "yes"
    data["provenance"]["reviewer"] = "reviewer@example.invalid"

    with pytest.raises(ValidationError, match="valid boolean"):
        validate_variable(data)


def test_draft_variable_rejects_reviewed_provenance() -> None:
    data = variable_data()
    data["provenance"]["human_reviewed"] = True
    data["provenance"]["reviewer"] = "reviewer@example.invalid"

    with pytest.raises(
        ValidationError, match="draft status requires unreviewed provenance"
    ):
        validate_variable(data)


def test_unreviewed_provenance_rejects_reviewer() -> None:
    data = variable_data()
    data["provenance"]["reviewer"] = "reviewer@example.invalid"

    with pytest.raises(
        ValidationError, match="reviewer must be null when human_reviewed is false"
    ):
        validate_variable(data)


def test_approved_variable_rejects_unresolved_reference() -> None:
    data = variable_data()
    data["status"] = "approved"
    data["derived_from"] = ["VAR-missing"]
    data["provenance"]["human_reviewed"] = True
    data["provenance"]["reviewer"] = "reviewer@example.invalid"

    with pytest.raises(ValidationError, match="unknown variable IDs"):
        validate_variable(data)


def test_label_longer_than_a_stata_variable_label_is_refused() -> None:
    data = variable_data()
    data["canonical_label"] = "x" * 81

    with pytest.raises(ValidationError, match="a Stata variable label holds 80"):
        validate_variable(data)


def test_label_of_exactly_the_limit_is_accepted() -> None:
    data = variable_data()
    data["canonical_label"] = "x" * 80

    assert validate_variable(data).canonical_label == "x" * 80


def test_every_draft_variable_label_fits_a_stata_variable_label() -> None:
    too_long = {}
    for path in sorted((ROOT / "extraction/20_drafts").rglob("VAR-*.md")):
        data, _ = load_markdown(path)
        if len(data["canonical_label"]) > 80:
            too_long[path.name] = len(data["canonical_label"])

    assert too_long == {}
