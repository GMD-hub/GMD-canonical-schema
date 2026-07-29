#!/usr/bin/env python3
"""Validate the Country Parameter Layer and print governance reports."""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from pydantic import ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from schema.country_exceptions import CountryExceptionFile, CountryExceptionRecord
from schema.country_parameters import CountryParameterFile, CountryParameterRecord
from schema.frontmatter import load_markdown
from schema.parameter import ParameterDefinition
from schema.rule import RuleDefinition
from schema.variable import (
    VariableDefinition,
    unresolved_variable_references,
    validate_acyclic_derivation_graph,
)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> None:
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join("---" for _ in headers) + "|")
    if not rows:
        print("| " + " | ".join(["None"] + [""] * (len(headers) - 1)) + " |")
        return
    for row in rows:
        values = [str(value).replace("|", "\\|").replace("\n", " ") for value in row]
        print("| " + " | ".join(values) + " |")


def scalar_strings(value: Any):
    if isinstance(value, dict):
        for item in value.values():
            yield from scalar_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from scalar_strings(item)
    elif isinstance(value, str):
        yield value


EffectiveDatedRecord = CountryParameterRecord | CountryExceptionRecord


def windows_overlap(left: EffectiveDatedRecord, right: EffectiveDatedRecord) -> bool:
    left_start = float("-inf") if left.effective_from is None else left.effective_from
    left_end = float("inf") if left.effective_to is None else left.effective_to
    right_start = float("-inf") if right.effective_from is None else right.effective_from
    right_end = float("inf") if right.effective_to is None else right.effective_to
    return left_start <= right_end and right_start <= left_end


def validate_repository(root: Path = ROOT) -> int:
    errors: list[tuple[str, str]] = []
    registry: dict[str, ParameterDefinition] = {}
    variable_ids: set[str] = set()
    rule_ids: set[str] = set()
    country_files: dict[str, CountryParameterFile] = {}
    exception_files: dict[str, CountryExceptionFile] = {}
    exception_locations: dict[str, str] = {}
    exception_overlap_rows: list[list[str]] = []
    unresolved_reference_rows: list[list[str]] = []

    for path in sorted((root / "knowledge" / "parameters").glob("*.md")):
        try:
            definition = ParameterDefinition.model_validate(load_markdown(path)[0])
            if definition.parameter_id in registry:
                errors.append((str(path.relative_to(root)), "duplicate parameter_id"))
            registry[definition.parameter_id] = definition
        except (ValueError, ValidationError) as exc:
            errors.append((str(path.relative_to(root)), str(exc)))

    raw_rules: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / "knowledge" / "rules").rglob("*.md")):
        try:
            data, _ = load_markdown(path)
            rule_ids.add(data["rule_id"])
            raw_rules.append((path, data))
        except (KeyError, ValueError) as exc:
            errors.append((str(path.relative_to(root)), str(exc)))

    for path, data in raw_rules:
        try:
            RuleDefinition.model_validate(data)
        except ValidationError as exc:
            errors.append((str(path.relative_to(root)), str(exc)))

    raw_variables: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / "knowledge" / "variables").rglob("*.md")):
        try:
            data, _ = load_markdown(path)
            variable_ids.add(data["variable_id"])
            raw_variables.append((path, data))
        except (KeyError, ValueError) as exc:
            errors.append((str(path.relative_to(root)), str(exc)))

    variables: list[VariableDefinition] = []
    reference_context = {
        "variable_ids": variable_ids,
        "parameter_ids": set(registry),
        "rule_ids": rule_ids,
        "allow_unresolved_draft": True,
    }
    for path, data in raw_variables:
        try:
            variable = VariableDefinition.model_validate(data, context=reference_context)
            variables.append(variable)
            unresolved = unresolved_variable_references(variable, variable_ids)
            if unresolved:
                unresolved_reference_rows.append(
                    [variable.variable_id, ", ".join(sorted(unresolved))]
                )
        except ValidationError as exc:
            errors.append((str(path.relative_to(root)), str(exc)))

    try:
        validate_acyclic_derivation_graph(variables)
    except ValueError as exc:
        errors.append(("knowledge/variables", str(exc)))

    countries_root = root / "country-parameters" / "countries"
    folders = sorted(path for path in countries_root.iterdir() if path.is_dir())
    country_codes = {path.name for path in folders}

    for folder in folders:
        parameter_path = folder / "parameters.md"
        exception_path = folder / "exceptions.md"
        try:
            parameters = CountryParameterFile.model_validate(
                load_markdown(parameter_path)[0], context={"registry": registry}
            )
            if parameters.iso3 != folder.name:
                errors.append((str(parameter_path.relative_to(root)), "iso3 differs from folder name"))
            country_files[folder.name] = parameters
        except (ValueError, ValidationError) as exc:
            errors.append((str(parameter_path.relative_to(root)), str(exc)))

        try:
            exception_data, _ = load_markdown(exception_path)
            seen_in_file: set[str] = set()
            for raw_exception in exception_data.get("exceptions", []):
                if not isinstance(raw_exception, dict):
                    continue
                exception_id = raw_exception.get("exception_id")
                if not isinstance(exception_id, str):
                    continue
                if exception_id in seen_in_file:
                    errors.append(
                        (str(exception_path.relative_to(root)), f"duplicate exception_id {exception_id}")
                    )
                seen_in_file.add(exception_id)
                previous_location = exception_locations.get(exception_id)
                if previous_location is not None:
                    errors.append(
                        (
                            str(exception_path.relative_to(root)),
                            f"duplicate exception_id {exception_id}; first found in {previous_location}",
                        )
                    )
                else:
                    exception_locations[exception_id] = str(exception_path.relative_to(root))

            exceptions = CountryExceptionFile.model_validate(
                exception_data, context={"variable_ids": variable_ids}
            )
            if exceptions.iso3 != folder.name:
                errors.append((str(exception_path.relative_to(root)), "iso3 differs from folder name"))
            exception_files[folder.name] = exceptions
        except (ValueError, ValidationError) as exc:
            errors.append((str(exception_path.relative_to(root)), str(exc)))

    for iso3, country_file in country_files.items():
        grouped: dict[str, list[CountryParameterRecord]] = defaultdict(list)
        for record in country_file.parameters:
            grouped[record.parameter_id].append(record)
        for parameter_id, records in grouped.items():
            for index, left in enumerate(records):
                for right in records[index + 1 :]:
                    if windows_overlap(left, right):
                        errors.append(
                            (
                                iso3,
                                f"overlapping validity windows for {parameter_id}",
                            )
                        )

    for iso3, exception_file in exception_files.items():
        for index, left in enumerate(exception_file.exceptions):
            for right in exception_file.exceptions[index + 1 :]:
                shared_variables = sorted(
                    set(left.applies_to_variables).intersection(right.applies_to_variables)
                )
                if not shared_variables or not windows_overlap(left, right):
                    continue
                # Ordering is a governance decision, so overlap is informational until
                # the GPID Team defines exception precedence.
                for variable_id in shared_variables:
                    exception_overlap_rows.append(
                        [iso3, variable_id, left.exception_id, right.exception_id]
                    )

    for path in sorted((root / "knowledge").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        try:
            data, _ = load_markdown(path)
        except ValueError as exc:
            errors.append((str(path.relative_to(root)), str(exc)))
            continue
        leaked = sorted(country_codes.intersection(scalar_strings(data)))
        if leaked:
            errors.append(
                (
                    str(path.relative_to(root)),
                    f"country ISO3 value found under knowledge: {', '.join(leaked)}",
                )
            )

    print("## Undecided fallback report")
    markdown_table(
        ["Parameter", "Kind", "Global default"],
        [
            [item.parameter_id, item.kind, item.global_default]
            for item in registry.values()
            if item.fallback_policy == "undecided"
        ],
    )
    if unresolved_reference_rows:
        print()
        print("Draft variable reference warnings:")
        markdown_table(["Variable", "Unresolved variable IDs"], unresolved_reference_rows)
    print()

    print("## Coverage gap report")
    coverage_rows: list[list[str]] = []
    for parameter_id in sorted(registry):
        missing = [
            iso3
            for iso3 in sorted(country_codes)
            if not any(
                record.parameter_id == parameter_id
                for record in country_files.get(iso3, CountryParameterFile.model_construct(parameters=[])).parameters
            )
        ]
        focal_points = [
            f"{iso3}: {country_files.get(iso3).focal_point or 'None'}"
            for iso3 in missing
            if country_files.get(iso3) is not None
        ]
        coverage_rows.append(
            [parameter_id, ", ".join(missing) or "None", ", ".join(focal_points) or "None"]
        )
    markdown_table(["Parameter", "Countries with no record", "Focal points"], coverage_rows)
    print()

    print("## Unverified values report")
    unverified_rows: list[list[Any]] = []
    for iso3, country_file in sorted(country_files.items()):
        for record in country_file.parameters:
            if not record.provenance.human_reviewed:
                unverified_rows.append(
                    [iso3, record.parameter_id, record.effective_from, record.effective_to]
                )
    markdown_table(
        ["Country", "Parameter", "Effective from", "Effective to"],
        unverified_rows,
    )

    print()
    print("## Overlapping exception report")
    markdown_table(
        ["Country", "Variable", "First exception", "Second exception"],
        exception_overlap_rows,
    )

    if errors:
        print("\n## Structural failures")
        markdown_table(["Location", "Failure"], [[location, message] for location, message in errors])
        return 1
    return 0


def main() -> int:
    return validate_repository()


if __name__ == "__main__":
    raise SystemExit(main())
