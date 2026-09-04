from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[2]
OLD_CODE_ROOT = ROOT / "extraction" / "10_source" / "country-parameters-inputs" / "old code"
EDU_PKG_ROOT = OLD_CODE_ROOT / "gmd_edu_concordance"
WASH_PKG_ROOT = OLD_CODE_ROOT / "gmd_wash_concordance"


def _import_from_path(path: Path, module_name: str) -> ModuleType:
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)
    return importlib.import_module(module_name)


def load_edu_module() -> ModuleType:
    return _import_from_path(EDU_PKG_ROOT, "gmd_edu_concordance")


def load_wash_module() -> ModuleType:
    return _import_from_path(WASH_PKG_ROOT, "gmd_wash_concordance")
