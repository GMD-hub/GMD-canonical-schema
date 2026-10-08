"""
gmd_edu_concordance.load
========================
An emitted instruction, read back.

The point is the standalone validator.  A country instruction that a person
edited by hand -- a grade range corrected, an era window moved, a programme
removed -- can be checked against the same rules that produced it, with no
access to the source workbook and no re-extraction.  If the rules only ever
run at extraction time, the first hand edit escapes them.
"""
from __future__ import annotations

import os
from typing import List

import yaml

from .schema import (
    EduRow, Era, Instruction, LadderStep, SourceFile, Unmapped,
)


def _fields(cls):
    return {f.name for f in cls.__dataclass_fields__.values()}


def _pick(cls, d: dict):
    return cls(**{k: v for k, v in (d or {}).items() if k in _fields(cls)})


def _era(d: dict) -> Era:
    return Era(
        id=d.get("id", 1), label=d.get("label", ""),
        from_year=d.get("from"), to_year=d.get("to"),
        reference_year=d.get("reference_year"),
        description=d.get("description", ""),
        latest=d.get("latest", True),
    )


def load_instruction(path: str) -> Instruction:
    """Read a ``{ISO3}_edu_{version}.yaml`` back into an Instruction."""
    with open(path, encoding="utf-8") as fh:
        d = yaml.safe_load(fh) or {}
    country = d.get("country") or {}
    return Instruction(
        iso3=country.get("iso3", ""),
        country=country.get("name", ""),
        version=d.get("version", "v1.0"),
        status=d.get("status", "draft"),
        domain=d.get("domain", "education"),
        frame=d.get("frame", ""),
        schema=d.get("schema", ""),
        schema_version=d.get("schema_version", ""),
        cvs_release=d.get("cvs_release", ""),
        cohort_aware=d.get("cohort_aware", True),
        era_selector=d.get("era_selector", "year_last_in_school"),
        fallback_selector=d.get("fallback_selector", ""),
        owner=d.get("owner", ""),
        note=d.get("note", ""),
        source=_pick(SourceFile, d.get("source")),
        language=d.get("language") or {},
        structure=d.get("structure") or {},
        eras=[_era(e) for e in d.get("eras") or []],
        rows=[_pick(EduRow, r) for r in d.get("rows") or []],
        ladder=[_pick(LadderStep, s) for s in d.get("ladder") or []],
        coverage=d.get("coverage") or {},
        unmapped=[_pick(Unmapped, u) for u in d.get("unmapped") or []],
    )


def find_instructions(target: str) -> List[str]:
    """A file, or every education instruction YAML under a directory."""
    if os.path.isfile(target):
        return [target]
    out = []
    for root, _dirs, files in os.walk(target):
        for f in files:
            if f.endswith(".yaml") and "_edu_v" in f:
                out.append(os.path.join(root, f))
    return sorted(out)
