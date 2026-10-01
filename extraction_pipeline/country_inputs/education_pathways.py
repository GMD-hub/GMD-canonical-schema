"""Infer draft education pathways from country education crosswalks."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from schema.frontmatter import load_markdown


ROOT = Path(__file__).resolve().parents[2]
COUNTRY_ROOT = ROOT / "country-parameters" / "countries"
DRAFT_ROOT = ROOT / "extraction" / "20_drafts" / "runs" / "country-parameters" / "education-pathways"
CLI_DRAFT_ROOT = ROOT / "extraction" / "20_drafts" / "runs" / "country-parameters"
SUMMARY_PATH = ROOT / "extraction" / "25_agent_review" / "education-pathways-summary.yaml"


def _normalise(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def _is_adult(row: dict[str, Any]) -> bool:
    return "adult" in _normalise(row.get("national_label_en"))


def _is_general_upper(row: dict[str, Any]) -> bool:
    text = _normalise(row.get("national_label_en"))
    return row.get("isced_level") == "3" and "vocational" not in text and "technical" not in text


def _select_one(rows: list[dict[str, Any]], predicate) -> dict[str, Any] | None:
    matches = [row for row in rows if predicate(row)]
    return matches[0] if len(matches) == 1 else None


def _candidate_parents(row: dict[str, Any], rows: list[dict[str, Any]]) -> list[str]:
    isced = str(row.get("isced_level") or "")
    adult = _is_adult(row)
    same_track = [item for item in rows if _is_adult(item) == adult]
    if isced in {"0", "1"}:
        return []
    if isced == "2":
        return [item["country_entry_id"] for item in same_track if item.get("isced_level") == "1"]
    if isced == "3":
        return [item["country_entry_id"] for item in same_track if item.get("isced_level") == "2"]

    label = _normalise(row.get("national_label_en"))
    if "master" in label:
        return [item["country_entry_id"] for item in rows if item.get("isced_level") == "6"]
    if isced == "8":
        return [item["country_entry_id"] for item in rows if item.get("isced_level") == "7"]
    return [item["country_entry_id"] for item in same_track if _is_general_upper(item)]


def _compute_row(
    row_id: str,
    rows_by_id: dict[str, dict[str, Any]],
    parents: dict[str, list[str]],
    memo: dict[str, tuple[int | None, list[str], list[str]]],
    visiting: list[str],
) -> tuple[int | None, list[str], list[str]]:
    if row_id in memo:
        return memo[row_id]
    if row_id in visiting:
        cycle = visiting[visiting.index(row_id) :] + [row_id]
        return None, [], [f"cycle detected: {' -> '.join(cycle)}"]

    row = rows_by_id[row_id]
    if str(row.get("isced_level")) == "0":
        result = (0, [], ["ISCED 0 excluded from school-year total"])
        memo[row_id] = result
        return result

    parent_ids = parents[row_id]
    if not parent_ids:
        result = (int(row.get("duration_years") or 0), [row_id], [])
        memo[row_id] = result
        return result

    if len(parent_ids) > 1:
        candidates = [
            _compute_row(parent_id, rows_by_id, parents, memo, visiting + [row_id])
            for parent_id in parent_ids
        ]
        valid = [candidate for candidate in candidates if candidate[0] is not None]
        if not valid:
            result = (None, [], [f"no valid parent path among: {', '.join(parent_ids)}"])
            memo[row_id] = result
            return result
        parent_total, path, flags = min(valid, key=lambda candidate: candidate[0] or 0)
        result = (
            parent_total + int(row.get("duration_years") or 0),
            path + [row_id],
            flags + [f"minimum parent path selected from: {', '.join(parent_ids)}"],
        )
        memo[row_id] = result
        return result

    parent_total, path, flags = _compute_row(
        parent_ids[0], rows_by_id, parents, memo, visiting + [row_id]
    )
    if parent_total is None:
        result = (None, [], flags)
    else:
        result = (parent_total + int(row.get("duration_years") or 0), path + [row_id], flags)
    memo[row_id] = result
    return result


def enrich_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Add parent_country_entry_ids/cum_years_schooling/cum_years_computation_path/
    cum_years_status/review_flags to a flat list of education crosswalk rows
    (each row must already have a country_entry_id)."""
    rows_by_id = {str(row["country_entry_id"]): row for row in rows if isinstance(row, dict)}
    parents = {row_id: _candidate_parents(row, rows) for row_id, row in rows_by_id.items()}
    memo: dict[str, tuple[int | None, list[str], list[str]]] = {}
    output_rows: list[dict[str, Any]] = []

    for row_id, row in rows_by_id.items():
        total, path, flags = _compute_row(row_id, rows_by_id, parents, memo, [])
        output = dict(row)
        output["parent_country_entry_ids"] = parents[row_id]
        output["cum_years_schooling"] = total
        output["cum_years_computation_path"] = path
        output["cum_years_status"] = "computed" if total is not None else "review_required"
        output["review_flags"] = flags
        output_rows.append(output)

    return output_rows


def infer_period(period: dict[str, Any], iso3: str) -> dict[str, Any]:
    rows = [row for row in period.get("value", []) if isinstance(row, dict)]
    return {
        "effective_from": period.get("effective_from"),
        "effective_to": period.get("effective_to"),
        "rows": enrich_rows(rows),
    }


def infer_country(iso3: str) -> dict[str, Any]:
    source_path = COUNTRY_ROOT / iso3 / "parameters.md"
    data, _ = load_markdown(source_path)
    periods = [
        record
        for record in data.get("parameters", [])
        if record.get("parameter_id") == "PARAM-EDU-LEVEL-CROSSWALK"
    ]
    return {
        "country_id": data["country_id"],
        "country_name": data.get("country_name", iso3),
        "iso3": iso3,
        "parameter_id": "PARAM-EDU-LEVEL-CROSSWALK",
        "status": "draft",
        "source": str(source_path.relative_to(ROOT)),
        "periods": [infer_period(period, iso3) for period in periods],
    }


def write_country_draft(iso3: str) -> Path:
    return _write_draft_data(iso3, infer_country(iso3))


def _write_draft_data(iso3: str, data: dict[str, Any]) -> Path:
    DRAFT_ROOT.mkdir(parents=True, exist_ok=True)
    output_path = DRAFT_ROOT / f"{iso3}.yaml"
    output_path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=False),
        encoding="utf-8",
    )
    return output_path


def discover_all_iso3() -> list[str]:
    return sorted(p.parent.name for p in COUNTRY_ROOT.glob("*/parameters.md"))


def _summarize_country(data: dict[str, Any]) -> dict[str, Any]:
    rows = [row for period in data.get("periods", []) for row in period.get("rows", [])]
    review_required = sum(1 for row in rows if row.get("cum_years_status") == "review_required")
    ambiguous = sum(
        1
        for row in rows
        if any("minimum parent path selected" in flag for flag in row.get("review_flags") or [])
    )
    if not rows:
        status = "no_crosswalk"
    elif review_required:
        status = "review_required"
    elif ambiguous:
        status = "ambiguous"
    else:
        status = "clean"
    return {
        "total_rows": len(rows),
        "review_required_rows": review_required,
        "ambiguous_rows": ambiguous,
        "status": status,
    }


def run_sweep(iso3_list: list[str]) -> dict[str, Any]:
    countries: dict[str, Any] = {}
    failed: dict[str, str] = {}
    for iso3 in iso3_list:
        try:
            data = infer_country(iso3)
            _write_draft_data(iso3, data)
        except Exception as exc:  # noqa: BLE001 - collect all failures for the summary report
            failed[iso3] = str(exc)
            continue
        countries[iso3] = _summarize_country(data)

    totals = {"clean": 0, "ambiguous": 0, "review_required": 0, "no_crosswalk": 0, "failed": len(failed)}
    for summary in countries.values():
        totals[summary["status"]] += 1

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_countries": len(iso3_list),
        "failed_countries": failed,
        "totals": totals,
        "countries": countries,
    }


def write_summary_report(summary: dict[str, Any]) -> Path:
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(
        yaml.safe_dump(summary, sort_keys=False, allow_unicode=False),
        encoding="utf-8",
    )
    return SUMMARY_PATH


def _write_country_file(path: Path, data: dict[str, Any], body: str) -> None:
    front_matter = yaml.safe_dump(data, sort_keys=False, allow_unicode=False).rstrip()
    path.write_text(f"---\n{front_matter}\n---\n\n{body}", encoding="utf-8")


def _load_periods_for_promotion(iso3: str) -> list[dict[str, Any]] | None:
    """Prefer the real extraction pipeline's draft (cli.py `extract`, already
    enriched via enrich_rows). Fall back to the standalone `--all` sweep draft
    (derived straight from committed data, used for ad-hoc review)."""
    cli_draft_path = CLI_DRAFT_ROOT / iso3 / "PARAM-EDU-LEVEL-CROSSWALK.yaml"
    if cli_draft_path.exists():
        data = yaml.safe_load(cli_draft_path.read_text(encoding="utf-8"))
        return [
            {
                "effective_from": record.get("effective_from"),
                "effective_to": record.get("effective_to"),
                "rows": record.get("value", []),
            }
            for record in data.get("parameters", [])
            if record.get("parameter_id") == "PARAM-EDU-LEVEL-CROSSWALK"
        ]
    sweep_draft_path = DRAFT_ROOT / f"{iso3}.yaml"
    if sweep_draft_path.exists():
        data = yaml.safe_load(sweep_draft_path.read_text(encoding="utf-8"))
        return data.get("periods", [])
    return None


def promote_country(iso3: str) -> str:
    """Replace this country's committed PARAM-EDU-LEVEL-CROSSWALK rows with the
    enriched (derived-field) rows from its generated draft. Returns a status
    string: 'promoted', 'no_draft', or 'no_crosswalk'."""
    draft_periods = _load_periods_for_promotion(iso3)
    if draft_periods is None:
        return "no_draft"

    country_path = COUNTRY_ROOT / iso3 / "parameters.md"
    data, body = load_markdown(country_path)
    crosswalk_records = [
        record for record in data["parameters"] if record.get("parameter_id") == "PARAM-EDU-LEVEL-CROSSWALK"
    ]
    if not crosswalk_records:
        return "no_crosswalk"
    if len(crosswalk_records) != len(draft_periods):
        raise ValueError(
            f"{iso3}: {len(crosswalk_records)} committed periods vs {len(draft_periods)} draft periods"
        )

    for record, period in zip(crosswalk_records, draft_periods):
        if record.get("effective_from") != period.get("effective_from") or record.get(
            "effective_to"
        ) != period.get("effective_to"):
            raise ValueError(
                f"{iso3}: period mismatch, committed "
                f"({record.get('effective_from')}, {record.get('effective_to')}) vs draft "
                f"({period.get('effective_from')}, {period.get('effective_to')})"
            )
        record["value"] = period["rows"]

    _write_country_file(country_path, data, body)
    return "promoted"


def promote_all(iso3_list: list[str]) -> dict[str, Any]:
    results: dict[str, str] = {}
    failed: dict[str, str] = {}
    for iso3 in iso3_list:
        try:
            results[iso3] = promote_country(iso3)
        except Exception as exc:  # noqa: BLE001 - collect all failures for the report
            failed[iso3] = str(exc)
    totals = {"promoted": 0, "no_draft": 0, "no_crosswalk": 0, "failed": len(failed)}
    for status in results.values():
        totals[status] += 1
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_countries": len(iso3_list),
        "totals": totals,
        "failed_countries": failed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso3", nargs="*", help="Country ISO3 code(s)")
    parser.add_argument(
        "--all", action="store_true", help="Sweep every country under country-parameters/countries"
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="Replace committed PARAM-EDU-LEVEL-CROSSWALK rows with enriched draft rows "
        "(country-parameters/, requires prior --all draft generation)",
    )
    args = parser.parse_args()

    if args.promote:
        iso3_list = args.iso3 or discover_all_iso3()
        result = promote_all(iso3_list)
        print(result["totals"])
        if result["failed_countries"]:
            print(f"failed: {result['failed_countries']}")
        return 0

    if args.all:
        iso3_list = discover_all_iso3()
        summary = run_sweep(iso3_list)
        report_path = write_summary_report(summary)
        print(f"processed {len(iso3_list)} countries -> {report_path}")
        print(summary["totals"])
        if summary["failed_countries"]:
            print(f"failed: {sorted(summary['failed_countries'])}")
        return 0

    if not args.iso3:
        parser.error("provide at least one ISO3 code, or use --all")
    for iso3 in args.iso3:
        print(write_country_draft(iso3.upper()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())