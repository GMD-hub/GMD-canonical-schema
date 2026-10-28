from __future__ import annotations

from dataclasses import asdict
from typing import Any


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
