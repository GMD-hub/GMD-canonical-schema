"""Keep the human-written variable reference in step with model field names."""

import re
from collections import Counter
from pathlib import Path
from typing import get_args

from pydantic import BaseModel

from schema.variable import VariableDefinition


REFERENCE = Path(__file__).resolve().parents[1] / "wiki/CVS-Variable-YAML-Reference.md"
START = "<!-- variable-field-paths:start -->"
END = "<!-- variable-field-paths:end -->"
FIELD_ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|", re.MULTILINE)


def model_field_paths(model: type[BaseModel], prefix: str = "") -> set[str]:
    paths = set()
    for name, field in model.model_fields.items():
        path = f"{prefix}.{name}" if prefix else name
        paths.add(path)
        pending = [field.annotation]
        while pending:
            annotation = pending.pop()
            if isinstance(annotation, type) and issubclass(annotation, BaseModel):
                paths.update(model_field_paths(annotation, path))
            else:
                pending.extend(get_args(annotation))
    return paths


def declared_field_paths(text: str) -> list[str]:
    assert text.count(START) == text.count(END) == 1, "field-path markers missing or repeated"
    declaration = text.split(START, 1)[1].split(END, 1)[0]
    return FIELD_ROW.findall(declaration)


def coverage_errors(model: type[BaseModel], text: str) -> list[str]:
    declared = declared_field_paths(text)
    actual = model_field_paths(model)
    duplicates = sorted(path for path, count in Counter(declared).items() if count > 1)
    errors = []
    if missing := sorted(actual - set(declared)):
        errors.append(f"Missing field paths: {', '.join(missing)}")
    if obsolete := sorted(set(declared) - actual):
        errors.append(f"Obsolete field paths: {', '.join(obsolete)}")
    if duplicates:
        errors.append(f"Duplicate field paths: {', '.join(duplicates)}")
    return errors


def test_variable_reference_covers_current_schema() -> None:
    errors = coverage_errors(VariableDefinition, REFERENCE.read_text(encoding="utf-8"))
    assert not errors, "\n".join(errors)


def test_model_field_paths_include_nullable_and_list_children() -> None:
    class Child(BaseModel):
        name: str

    class Parent(BaseModel):
        optional: Child | None
        entries: list[Child]

    assert model_field_paths(Parent) == {
        "optional", "optional.name", "entries", "entries.name"
    }


def test_coverage_reports_missing_and_obsolete_paths() -> None:
    class Child(BaseModel):
        name: str

    class Parent(BaseModel):
        entries: list[Child]

    text = f"{START}\n| `entries` | described |\n| `old_name` | obsolete |\n{END}"
    assert coverage_errors(Parent, text) == [
        "Missing field paths: entries.name",
        "Obsolete field paths: old_name",
    ]


def test_coverage_reports_duplicate_paths() -> None:
    class Parent(BaseModel):
        name: str

    text = f"{START}\n| `name` | first |\n| `name` | second |\n{END}"
    assert coverage_errors(Parent, text) == ["Duplicate field paths: name"]
