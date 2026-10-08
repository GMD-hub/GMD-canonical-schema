"""
gmd_edu_concordance
===================
UIS "ISCED 2011 Mapping" workbook  ->  GMD System 8 country education
instruction.

    from gmd_edu_concordance import extract
    result = extract("ISCED_2011_Mapping_Nigeria.xlsx", out="out/")

or from the shell::

    python -m gmd_edu_concordance inspect ISCED_2011_Mapping_Nigeria.xlsx
    python -m gmd_edu_concordance extract ISCED_2011_Mapping_Nigeria.xlsx --out out/
    python -m gmd_edu_concordance ladder  ISCED_2011_Mapping_Nigeria.xlsx
"""
from __future__ import annotations

__version__ = "1.0.0"

from .reader import read, load_profile, load_profiles   # noqa: E402,F401
from .load import load_instruction, find_instructions   # noqa: E402,F401
from .derive import run as derive               # noqa: E402,F401
from .validate import validate, verdict, summarise   # noqa: E402,F401
from .resolver import resolve, probe, render    # noqa: E402,F401
from .emit import write_all
from . import registry
from .viewer import build as build_viewer
from .viewer import scan as scan_outputs, serve as serve_viewer                     # noqa: E402,F401


def extract(path, out=None, iso3=None, country=None, version="v1.0",
            reference_year=None, sheet=None):
    """Read one workbook, derive the grade ladder, validate, optionally write.

    Returns ``{instruction, binding, findings, verdict, counts,
    fingerprint, artifacts}``.
    """
    inst, binding = read(path, iso3=iso3, country=country, version=version,
                         reference_year=reference_year, sheet=sheet)
    profiles = {p["profile"]: p for p in load_profiles()}
    derive(inst, profiles.get(binding.profile) or load_profile())
    findings = validate(inst, binding)
    v = verdict(findings)
    inst.status = "draft" if v != "blocked" else "rejected"
    artifacts = write_all(inst, binding, findings, out) if out else []
    return {
        "instruction": inst,
        "binding": binding,
        "findings": findings,
        "verdict": v,
        "counts": summarise(findings),
        "fingerprint": inst.content_fingerprint(),
        "artifacts": artifacts,
    }


def check(target):
    """Re-run the rules over instruction files already emitted.  Returns one
    entry per file: ``{path, instruction, findings, verdict, counts}``."""
    out = []
    for f in find_instructions(target):
        inst = load_instruction(f)
        findings = validate(inst)
        out.append({"path": f, "instruction": inst, "findings": findings,
                    "verdict": verdict(findings),
                    "counts": summarise(findings)})
    return out


__all__ = ["extract", "check", "read", "derive", "validate", "verdict",
           "summarise", "resolve", "probe", "render", "write_all", "build_viewer", "registry", "serve_viewer", "scan_outputs",
           "load_instruction", "find_instructions", "__version__"]
