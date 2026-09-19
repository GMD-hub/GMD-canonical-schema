import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from extraction_pipeline.country_inputs.cli import run_extract


def main() -> None:
    result = run_extract(force=True)

    result_path = ROOT / "extraction/20_drafts/runs/extract_result_jmp_redo.json"
    result_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    statuses = result.get("jmp_file_statuses", [])
    summary = {
        "ok": result.get("ok", False),
        "jmp_files_total": len(statuses),
        "water": {
            "written": sum(1 for s in statuses if s.get("water") == "written"),
            "unchanged": sum(1 for s in statuses if s.get("water") == "unchanged"),
            "no_rows": sum(1 for s in statuses if s.get("water") == "no_rows"),
            "error": sum(1 for s in statuses if s.get("water") == "error"),
            "invalid_iso3": sum(1 for s in statuses if s.get("water") == "invalid_iso3"),
        },
        "sanitation": {
            "written": sum(1 for s in statuses if s.get("sanitation") == "written"),
            "unchanged": sum(1 for s in statuses if s.get("sanitation") == "unchanged"),
            "no_rows": sum(1 for s in statuses if s.get("sanitation") == "no_rows"),
            "error": sum(1 for s in statuses if s.get("sanitation") == "error"),
            "invalid_iso3": sum(1 for s in statuses if s.get("sanitation") == "invalid_iso3"),
        },
        "benchmark_water": {
            "written": sum(1 for s in statuses if s.get("benchmark_water") == "written"),
            "unchanged": sum(1 for s in statuses if s.get("benchmark_water") == "unchanged"),
            "error": sum(1 for s in statuses if s.get("benchmark_water") == "error"),
            "invalid_iso3": sum(1 for s in statuses if s.get("benchmark_water") == "invalid_iso3"),
        },
        "benchmark_sanitation": {
            "written": sum(1 for s in statuses if s.get("benchmark_sanitation") == "written"),
            "unchanged": sum(1 for s in statuses if s.get("benchmark_sanitation") == "unchanged"),
            "error": sum(1 for s in statuses if s.get("benchmark_sanitation") == "error"),
            "invalid_iso3": sum(1 for s in statuses if s.get("benchmark_sanitation") == "invalid_iso3"),
        },
        "errors": [
            {
                "file": s.get("file"),
                "iso3": s.get("iso3"),
                "error": s.get("error"),
            }
            for s in statuses
            if s.get("error")
        ],
    }

    summary_path = ROOT / "extraction/20_drafts/runs/jmp_status_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(str(result_path.relative_to(ROOT)).replace('\\\\', '/'))
    print(str(summary_path.relative_to(ROOT)).replace('\\\\', '/'))


if __name__ == "__main__":
    main()
