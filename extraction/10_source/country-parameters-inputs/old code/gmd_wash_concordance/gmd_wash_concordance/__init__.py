"""
gmd_wash_concordance
====================
JMP country household workbook  ->  GMD System 9 country WASH instruction.

    from gmd_wash_concordance import extract
    result = extract("JMP_2025_IND_India_0.xlsx", out="out/")

or from the shell::

    python -m gmd_wash_concordance inspect JMP_2025_IND_India_0.xlsx
    python -m gmd_wash_concordance extract JMP_2025_IND_India_0.xlsx --out out/
"""
from __future__ import annotations

__version__ = "1.0.0"

from .reader import read                                   # noqa: E402,F401
from .load import load_instruction, find_instructions      # noqa: E402,F401
from .validate import (                                    # noqa: E402,F401
    validate, validate_extract, verdict, summarise,
)
from .emit import write_all
from . import registry
from .viewer import build as build_viewer
from .viewer import scan as scan_outputs, serve as serve_viewer                                # noqa: E402,F401


def extract(path, out=None, iso3=None, country=None, version="v1.0",
            sources="microdata", domains="both"):
    """Read one workbook into **one instruction per domain**, validate each,
    optionally write the artefacts.

    Returns ``{extract, binding, domains: {water: {...}, sanitation: {...}},
    artifacts}`` where each domain entry carries its own instruction,
    findings, verdict, counts and fingerprint.  Water and sanitation are
    separate all the way down; nothing here merges them.
    """
    ex, binding = read(path, iso3=iso3, country=country, version=version,
                       sources=sources, domains=domains)
    by_dom = validate_extract(ex, binding)
    result = {"extract": ex, "binding": binding, "domains": {}}
    for inst in ex.instructions():
        findings = by_dom[inst.domain]
        v = verdict(findings)
        inst.status = "draft" if v != "blocked" else "rejected"
        result["domains"][inst.domain] = {
            "instruction": inst,
            "findings": findings,
            "verdict": v,
            "counts": summarise(findings),
            "fingerprint": inst.content_fingerprint(),
        }
    result["artifacts"] = write_all(ex, binding, by_dom, out) if out else []
    return result


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


__all__ = ["extract", "check", "read", "load_instruction", "find_instructions",
           "validate", "validate_extract", "verdict", "summarise",
           "write_all", "build_viewer", "registry", "serve_viewer", "scan_outputs", "__version__"]
