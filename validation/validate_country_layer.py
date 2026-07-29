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

from schema.country_exceptions import CountryExceptionFile
from schema.country_parameters import CountryParameterFile, CountryParameterRecord
from schema.frontmatter import load_markdown
from schema.parameter import ParameterDefinition


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


def windows_overlap(left: CountryParameterRecord, right: CountryParameterRecord) -> bool:
    left_start = float("-inf") if left.effective_from is None else left.effective_from
    left_end = float("inf") if left.effective_to is None else left.effective_to
    right_start = float("-inf") if right.effective_from is None else right.effective_from
    right_end = float("inf") if right.effective_to is None else right.effective_to
    return left_start <= right_end and right_start <= left_end


def main() -> int:
    errors: list[tuple[str, str]] = []
    registry: dict[str, ParameterDefinition] = {}
    variable_ids: set[str] = set()
    declarations: list[tuple[str, str]] = []
    country_files: dict[str, CountryParameterFile] = {}

    for path in sorted((ROOT / "knowledge" / "parameters").glob("*.md")):
        try:
            definition = ParameterDefinition.model_validate(load_markdown(path)[0])
            if definition.parameter_id in registry:
                errors.append((str(path.relative_to(ROOT)), "duplicate parameter_id"))
            registry[definition.parameter_id] = definition
        except (ValueError, ValidationError) as exc:
            errors.append((str(path.relative_to(ROOT)), str(exc)))

    for path in sorted((ROOT / "knowledge" / "variables").rglob("*.md")):
        try:
            data, _ = load_markdown(path)
            variable_id = data["variable_id"]
            variable_ids.add(variable_id)
            for parameter_id in data.get("country_parameters", []):
                declarations.append((variable_id, parameter_id))
        except (KeyError, ValueError) as exc:
            errors.append((str(path.relative_to(ROOT)), str(exc)))

    for variable_id, parameter_id in declarations:
        if parameter_id not in registry:
            errors.append((variable_id, f"unknown country parameter {parameter_id}"))

    countries_root = ROOT / "country-parameters" / "countries"
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
                errors.append((str(parameter_path.relative_to(ROOT)), "iso3 differs from folder name"))
            country_files[folder.name] = parameters
        except (ValueError, ValidationError) as exc:
            errors.append((str(parameter_path.relative_to(ROOT)), str(exc)))

        try:
            exceptions = CountryExceptionFile.model_validate(
                load_markdown(exception_path)[0], context={"variable_ids": variable_ids}
            )
            if exceptions.iso3 != folder.name:
                errors.append((str(exception_path.relative_to(ROOT)), "iso3 differs from folder name"))
        except (ValueError, ValidationError) as exc:
            errors.append((str(exception_path.relative_to(ROOT)), str(exc)))

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

    for path in sorted((ROOT / "knowledge").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        try:
            data, _ = load_markdown(path)
        except ValueError as exc:
            errors.append((str(path.relative_to(ROOT)), str(exc)))
            continue
        leaked = sorted(country_codes.intersection(scalar_strings(data)))
        if leaked:
            errors.append(
                (
                    str(path.relative_to(ROOT)),
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
        coverage_rows.append([parameter_id, ", ".join(missing) or "None"])
    markdown_table(["Parameter", "Countries with no record"], coverage_rows)
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

    if errors:
        print("\n## Structural failures")
        markdown_table(["Location", "Failure"], [[location, message] for location, message in errors])
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
