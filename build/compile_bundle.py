#!/usr/bin/env python3
"""Compile the universal CVS and one country layer into validated JSON."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import RootModel, ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from schema.country_exceptions import CountryExceptionFile, CountryExceptionRecord
from schema.country_parameters import CountryParameterFile, CountryParameterRecord
from schema.frontmatter import load_markdown
from schema.parameter import ParameterDefinition


class UniversalArtifact(RootModel[dict[str, Any]]):
    pass


def in_window(record: CountryParameterRecord | CountryExceptionRecord, year: int) -> bool:
    return (
        (record.effective_from is None or record.effective_from <= year)
        and (record.effective_to is None or year <= record.effective_to)
    )


def load_universal_artifacts(
    folder: Path,
    registry: dict[str, ParameterDefinition],
) -> list[dict[str, Any]]:
    artifacts: list[dict[str, Any]] = []
    for path in sorted(folder.rglob("*.md")):
        data, body = load_markdown(path)
        if folder.name == "parameters":
            parameter = ParameterDefinition.model_validate(data)
            registry[parameter.parameter_id] = parameter
            structured = parameter.model_dump(mode="json")
        else:
            structured = UniversalArtifact.model_validate(data).root
        artifacts.append({**structured, "body": body})
    return artifacts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso3", help="ISO 3166-1 alpha-3 country code")
    parser.add_argument("survey_id_year", nargs="?", type=int)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Z]{3}", args.iso3):
        parser.error("iso3 must contain exactly three uppercase letters")
    return args


def main() -> int:
    args = parse_args()
    registry: dict[str, ParameterDefinition] = {}

    try:
        parameters = load_universal_artifacts(
            ROOT / "knowledge" / "parameters", registry
        )
        variables = load_universal_artifacts(
            ROOT / "knowledge" / "variables", registry
        )
        rules = load_universal_artifacts(ROOT / "knowledge" / "rules", registry)
        modules = load_universal_artifacts(ROOT / "knowledge" / "modules", registry)

        variable_ids = {item["variable_id"] for item in variables}
        for variable in variables:
            for parameter_id in variable.get("country_parameters", []):
                if parameter_id not in registry:
                    raise ValueError(
                        f"{variable['variable_id']} declares unknown parameter {parameter_id}"
                    )

        country_folder = ROOT / "country-parameters" / "countries" / args.iso3
        parameter_data, parameter_body = load_markdown(country_folder / "parameters.md")
        exception_data, exception_body = load_markdown(country_folder / "exceptions.md")
        country_parameters = CountryParameterFile.model_validate(
            parameter_data, context={"registry": registry}
        )
        country_exceptions = CountryExceptionFile.model_validate(
            exception_data, context={"variable_ids": variable_ids}
        )
        if country_parameters.iso3 != args.iso3 or country_exceptions.iso3 != args.iso3:
            raise ValueError("country file iso3 does not match requested folder")
    except (FileNotFoundError, KeyError, ValueError, ValidationError) as exc:
        print(f"Bundle compilation failed: {exc}", file=sys.stderr)
        return 1

    selected_parameters = [
        record
        for record in country_parameters.parameters
        if args.survey_id_year is None or in_window(record, args.survey_id_year)
    ]
    selected_exceptions = [
        record
        for record in country_exceptions.exceptions
        if args.survey_id_year is None or in_window(record, args.survey_id_year)
    ]

    commit_hash = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    bundle = {
        "bundle_version": "0.1",
        "generated_on": datetime.now(timezone.utc).isoformat(),
        "commit_hash": commit_hash,
        "country_code": args.iso3,
        "survey_id_year": args.survey_id_year,
        "universal": {
            "modules": modules,
            "variables": variables,
            "rules": rules,
            "parameters": parameters,
        },
        "country": {
            "iso3": args.iso3,
            "parameters": [
                {**record.model_dump(mode="json"), "body": parameter_body}
                for record in selected_parameters
            ],
            "exceptions": [
                {**record.model_dump(mode="json"), "body": exception_body}
                for record in selected_exceptions
            ],
        },
    }

    year_label = str(args.survey_id_year) if args.survey_id_year is not None else "all"
    output_dir = ROOT / "build" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"bundle_{args.iso3}_{year_label}.json"
    output_path.write_text(
        json.dumps(bundle, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    print(output_path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
