import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from extraction_pipeline.country_inputs.cli import list_geo_iso3s, run_geo_example


def main() -> None:
    iso3s, _ = list_geo_iso3s()
    results = [run_geo_example(iso3, 0, True) for iso3 in iso3s]
    summary = {
        "ok": all(r.get("ok", False) for r in results),
        "count": len(results),
        "success": sum(1 for r in results if r.get("ok", False)),
        "failed": [r for r in results if not r.get("ok", False)],
    }
    out = Path("extraction/20_drafts/runs/geo_all_run_summary.json")
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(out.as_posix())


if __name__ == "__main__":
    main()
