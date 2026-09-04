from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
DRAFT_ROOT = ROOT / "extraction" / "20_drafts" / "runs" / "country-parameters"
BENCHMARK_ROOT = ROOT / "governance" / "benchmarks"


def _provenance(source: str) -> dict[str, Any]:
    return {
        "source": source,
        "verified_on": None,
        "human_reviewed": False,
        "reviewer": None,
    }


def emit_parameter_draft(
    *,
    iso3: str,
    country_name: str,
    parameter_id: str,
    rows: list[dict[str, Any]],
    source: str,
    effective_from: int | None,
    effective_to: int | None,
    selectors: dict[str, str | int | bool] | None = None,
) -> Path:
    out_dir = DRAFT_ROOT / iso3
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{parameter_id}.yaml"

    payload = {
        "country_id": f"CTY-{iso3}",
        "country_name": country_name,
        "iso3": iso3,
        "schema_version": "0.2",
        "status": "draft",
        "parameters": [
            {
                "parameter_id": parameter_id,
                "effective_from": effective_from,
                "effective_to": effective_to,
                "selectors": selectors,
                "value": rows,
                "provenance": _provenance(source),
            }
        ],
    }

    text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=False)
    out_path.write_text(text, encoding="utf-8")
    return out_path


def emit_benchmark(iso3: str, domain: str, payload: dict[str, Any], source: str) -> Path:
    BENCHMARK_ROOT.mkdir(parents=True, exist_ok=True)
    out_path = BENCHMARK_ROOT / f"{iso3}_{domain}_benchmark_draft.yaml"
    envelope = {
        "iso3": iso3,
        "domain": domain,
        "source": source,
        "status": "draft",
        "benchmark": payload,
    }
    text = yaml.safe_dump(envelope, sort_keys=False, allow_unicode=False)
    out_path.write_text(text, encoding="utf-8")
    return out_path
