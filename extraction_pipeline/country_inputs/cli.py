from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from .emit import emit_benchmark, emit_parameter_draft
from .legacy import ROOT, load_edu_module, load_wash_module
from .transform import (
    to_benchmark_payload,
    transform_education_rows,
    transform_wash_rows,
)
from schema.country_parameters import CountryParameterFile
from schema.frontmatter import load_markdown
from schema.parameter import ParameterDefinition

SOURCE_ROOT = ROOT / "extraction" / "10_source" / "country-parameters-inputs"
DRAFT_ROOT = ROOT / "extraction" / "20_drafts" / "runs" / "country-parameters"
CONTRACT_ROOT = DRAFT_ROOT / "contracts"


def _find_xlsx(folder: Path) -> list[Path]:
    return sorted(path for path in folder.glob("*.xlsx") if not path.name.startswith("~$"))


def inspect_inputs() -> dict[str, list[str]]:
    isced = _find_xlsx(SOURCE_ROOT / "ISCED")
    jmp = _find_xlsx(SOURCE_ROOT / "JMP")
    return {
        "ISCED": [str(path.relative_to(ROOT)) for path in isced],
        "JMP": [str(path.relative_to(ROOT)) for path in jmp],
    }


def load_parameter_registry() -> dict[str, ParameterDefinition]:
    registry: dict[str, ParameterDefinition] = {}

    for path in sorted((ROOT / "knowledge" / "parameters").glob("*.md")):
        data, _ = load_markdown(path)
        parameter = ParameterDefinition.model_validate(data)
        if parameter.parameter_id in registry:
            raise ValueError(f"duplicate parameter_id in registry: {parameter.parameter_id}")
        registry[parameter.parameter_id] = parameter

    for path in sorted(CONTRACT_ROOT.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"contract is not a mapping: {path}")
        parameter = ParameterDefinition.model_validate(data)
        if parameter.parameter_id in registry:
            raise ValueError(f"duplicate parameter_id in registry: {parameter.parameter_id}")
        registry[parameter.parameter_id] = parameter

    return registry


def _extract_education(path: Path) -> tuple[str, str, list[dict[str, Any]], int | None]:
    module = load_edu_module()
    result = module.extract(str(path), out=None)
    instruction = result["instruction"]
    rows = transform_education_rows(result)
    return instruction.iso3, instruction.country, rows, instruction.source.reference_year


def _extract_wash(path: Path) -> tuple[str, str, list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    module = load_wash_module()
    result = module.extract(str(path), out=None)
    water_rows = transform_wash_rows(result, "water")
    sanitation_rows = transform_wash_rows(result, "sanitation")

    water_instruction = result["domains"]["water"]["instruction"]
    bench_water = to_benchmark_payload(result, "water")
    bench_san = to_benchmark_payload(result, "sanitation")
    return (
        water_instruction.iso3,
        water_instruction.country,
        water_rows,
        sanitation_rows,
        bench_water,
        bench_san,
    )


def run_extract() -> dict[str, Any]:
    inputs = inspect_inputs()
    if not inputs["ISCED"] and not inputs["JMP"]:
        return {
            "ok": False,
            "errors": ["no input workbooks found under extraction/10_source/country-parameters-inputs"],
            "inputs": inputs,
            "written": [],
        }

    written: list[str] = []

    for relative in inputs["ISCED"]:
        source = ROOT / relative
        iso3, country_name, rows, reference_year = _extract_education(source)
        out_path = emit_parameter_draft(
            iso3=iso3,
            country_name=country_name,
            parameter_id="PARAM-EDU-LEVEL-CROSSWALK",
            rows=rows,
            source=str(source.relative_to(ROOT)),
            effective_from=reference_year,
            effective_to=None,
        )
        written.append(str(out_path.relative_to(ROOT)))

    for relative in inputs["JMP"]:
        source = ROOT / relative
        (
            iso3,
            country_name,
            water_rows,
            sanitation_rows,
            bench_water,
            bench_san,
        ) = _extract_wash(source)

        water_path = emit_parameter_draft(
            iso3=iso3,
            country_name=country_name,
            parameter_id="PARAM-WASH-WATER-CROSSWALK",
            rows=water_rows,
            source=str(source.relative_to(ROOT)),
            effective_from=None,
            effective_to=None,
        )
        san_path = emit_parameter_draft(
            iso3=iso3,
            country_name=country_name,
            parameter_id="PARAM-WASH-SANITATION-CROSSWALK",
            rows=sanitation_rows,
            source=str(source.relative_to(ROOT)),
            effective_from=None,
            effective_to=None,
        )
        written.extend(
            [
                str(water_path.relative_to(ROOT)),
                str(san_path.relative_to(ROOT)),
            ]
        )

        b1 = emit_benchmark(
            iso3,
            "water",
            bench_water,
            str(source.relative_to(ROOT)),
        )
        b2 = emit_benchmark(
            iso3,
            "sanitation",
            bench_san,
            str(source.relative_to(ROOT)),
        )
        written.extend([str(b1.relative_to(ROOT)), str(b2.relative_to(ROOT))])

    return {"ok": True, "inputs": inputs, "written": written}


def run_check() -> dict[str, Any]:
    base = DRAFT_ROOT
    errors: list[dict[str, str]] = []
    try:
        registry = load_parameter_registry()
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "count": 0,
            "files": [],
            "errors": [{"file": "registry", "error": str(exc)}],
        }

    findings: list[dict[str, Any]] = []
    paths = [path for path in sorted(base.rglob("*.yaml")) if CONTRACT_ROOT not in path.parents]
    if not paths:
        return {
            "ok": False,
            "count": 0,
            "files": [],
            "errors": [
                {
                    "file": str(base.relative_to(ROOT)),
                    "error": "no draft country-parameter files found",
                }
            ],
        }

    for path in paths:
        text = path.read_text(encoding="utf-8")
        file_ok = True
        detail_error = ""
        try:
            payload = yaml.safe_load(text)
            if not isinstance(payload, dict):
                raise ValueError("draft file must contain a mapping")
            parsed = CountryParameterFile.model_validate(payload, context={"registry": registry})

            for record in parsed.parameters:
                definition = registry[record.parameter_id]
                if definition.value_type == "table" and len(record.value) == 0:
                    raise ValueError(f"{record.parameter_id} table value must contain at least one row")
        except Exception as exc:  # noqa: BLE001
            file_ok = False
            detail_error = str(exc)
            errors.append(
                {
                    "file": str(path.relative_to(ROOT)),
                    "error": detail_error,
                }
            )

        findings.append(
            {
                "file": str(path.relative_to(ROOT)),
                "size": len(text),
                "has_parameters": "parameters:" in text,
                "has_value": "value:" in text,
                "valid": file_ok,
                "error": detail_error,
            }
        )
    return {
        "ok": len(errors) == 0,
        "count": len(findings),
        "files": findings,
        "errors": errors,
    }


def run_bulk() -> dict[str, Any]:
    return run_extract()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Country parameter input extraction")
    parser.add_argument("command", choices=["inspect", "extract", "check", "bulk"])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "inspect":
        print(json.dumps(inspect_inputs(), indent=2, ensure_ascii=False))
        return 0
    if args.command == "extract":
        result = run_extract()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result.get("ok", False) else 1
    if args.command == "check":
        result = run_check()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result.get("ok", False) else 1
    if args.command == "bulk":
        result = run_bulk()
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result.get("ok", False) else 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
