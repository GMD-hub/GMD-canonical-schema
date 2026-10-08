from __future__ import annotations

from dataclasses import asdict
from typing import Any


def _educat4_target(gmd: str) -> str:
    mapping = {
        "none": "no_education",
        "pre_primary": "no_education",
        "primary": "primary",
        "lower_secondary": "secondary",
        "upper_secondary": "secondary",
        "post_secondary": "tertiary",
        "tertiary": "tertiary",
        "other": "other",
    }
    return mapping.get(gmd, "unknown")


def _educat5_target(gmd: str, completion: str) -> str:
    if gmd in {"none", "pre_primary"}:
        return "no_education"
    if gmd == "primary":
        return "primary_complete" if completion == "full" else "primary_incomplete"
    if gmd == "lower_secondary":
        return "lower_secondary"
    if gmd == "upper_secondary":
        return "upper_secondary"
    if gmd in {"post_secondary", "tertiary"}:
        return "tertiary"
    return "other"


def _educat7_target(gmd: str, completion: str) -> str:
    if gmd in {"none", "pre_primary"}:
        return "none"
    if gmd == "primary":
        return "primary_complete" if completion == "full" else "primary_incomplete"
    if gmd == "lower_secondary":
        return "lower_secondary_complete" if completion == "full" else "lower_secondary_incomplete"
    if gmd == "upper_secondary":
        return "upper_secondary_complete" if completion == "full" else "upper_secondary_incomplete"
    if gmd in {"post_secondary", "tertiary"}:
        return "tertiary"
    return "other"


def _value_of(maybe_inferred: Any) -> Any:
    if isinstance(maybe_inferred, dict) and "value" in maybe_inferred:
        return maybe_inferred["value"]
    return maybe_inferred


def transform_education_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    instruction = result["instruction"]
    rows = []
    for item in instruction.rows:
        rows.append(
            {
                "national_label_en": item.programme or "",
                "national_label_local": item.programme_national or "",
                "entry_age": int(float(_value_of(item.entrance_age).get("min", 0)))
                if isinstance(_value_of(item.entrance_age), dict)
                and _value_of(item.entrance_age).get("min") is not None
                else 0,
                "duration_years": int(float(_value_of(item.duration_years).get("min", 0)))
                if isinstance(_value_of(item.duration_years), dict)
                and _value_of(item.duration_years).get("min") is not None
                else 0,
                "isced_level": item.isced or "",
                "isced_label": item.isced_label or "",
                "gmd_educat4_target": _educat4_target(item.gmd or ""),
                "gmd_educat5_target": _educat5_target(item.gmd or "", item.completion or ""),
                "gmd_educat7_target": _educat7_target(item.gmd or "", item.completion or ""),
                "source_row": item.source_row or 0,
            }
        )
    return rows


def transform_wash_rows(result: dict[str, Any], domain: str) -> list[dict[str, Any]]:
    instruction = result["domains"][domain]["instruction"]
    rows = []
    for item in instruction.rows:
        rows.append(
            {
                "source_category_code": item.code or "",
                "national_label_en": item.label or "",
                "national_label_local": item.jmp_label_local or "",
                "jmp_classification": item.jmp or "",
                "jmp_id": item.jmp_id or "",
                "gmd_target": item.gmd or "",
                "gmd_spans": "|".join(item.spans or []),
                "improved_flag": bool(item.improved) if item.improved is not None else False,
                "shared_flag": bool(item.shared) if item.shared is not None else False,
                "source_row": item.source_row or 0,
            }
        )
    return rows


def to_benchmark_payload(result: dict[str, Any], domain: str) -> dict[str, Any]:
    instruction = result["domains"][domain]["instruction"]
    payload = asdict(instruction)
    return payload.get("benchmark") or {}
