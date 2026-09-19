import json
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

RESULT_PATH = ROOT / "extraction/20_drafts/runs/extract_force_all_result.json"
ERROR_PATH = ROOT / "extraction/20_drafts/runs/extract_force_all_error.txt"


def main() -> int:
    from extraction_pipeline.country_inputs.cli import run_extract

    try:
        result = run_extract(force=True)
    except Exception:
        ERROR_PATH.write_text(traceback.format_exc(), encoding="utf-8")
        print(str(ERROR_PATH.relative_to(ROOT)).replace("\\", "/"))
        return 1

    RESULT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    if ERROR_PATH.exists():
        ERROR_PATH.unlink()
    print(str(RESULT_PATH.relative_to(ROOT)).replace("\\", "/"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
