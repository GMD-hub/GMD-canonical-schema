"""
gmd_wash_concordance.load
=========================
An emitted instruction, read back.

The point is the standalone validator.  A country instruction that a person
edited by hand -- a label corrected, a target changed, a row removed -- can be
checked against the same rules that produced it, with no access to the source
workbook and no re-extraction.  If the rules only ever run at extraction time,
the first hand edit escapes them.
"""
from __future__ import annotations

import os
from typing import List, Optional

import yaml

from .schema import (
    DataSource, Instruction, Section, SourceConcordance, SourceFile, Unmapped,
    WashRow,
)


def _fields(cls):
    return {f.name for f in cls.__dataclass_fields__.values()}


def _pick(cls, d: dict):
    return cls(**{k: v for k, v in (d or {}).items() if k in _fields(cls)})


def load_instruction(path: str) -> Instruction:
    """Read a ``{ISO3}_{domain}_{version}.yaml`` back into an Instruction."""
    with open(path, encoding="utf-8") as fh:
        d = yaml.safe_load(fh) or {}
    country = d.get("country") or {}
    inst = Instruction(
        domain=d.get("domain", "water"),
        iso3=country.get("iso3", ""),
        country=country.get("name", ""),
        version=d.get("version", "v1.0"),
        status=d.get("status", "draft"),
        family=d.get("family", "wash"),
        frame=d.get("frame", ""),
        schema=d.get("schema", ""),
        schema_version=d.get("schema_version", ""),
        cvs_release=d.get("cvs_release", ""),
        language=d.get("language", ""),
        owner=d.get("owner", ""),
        note=d.get("note", ""),
        source=_pick(SourceFile, d.get("source")),
        selection=d.get("selection") or {},
        sources=[_pick(DataSource, s) for s in d.get("sources") or []],
        rows=[_pick(WashRow, r) for r in d.get("rows") or []],
        classifications=d.get("classifications") or [],
        facility_types=d.get("facility_types") or [],
        sections=[_pick(Section, s) for s in d.get("sections") or []],
        ladder=d.get("ladder") or [],
        vintage=d.get("vintage") or {},
        unmapped=[_pick(Unmapped, u) for u in d.get("unmapped") or []],
    )
    # per-source is only in the sources sidecar; rebuild what the rules need
    side = os.path.join(os.path.dirname(path), f"{inst.stem()}_sources.json")
    if os.path.exists(side):
        import json
        with open(side, encoding="utf-8") as fh:
            sd = json.load(fh)
        inst.per_source = [
            SourceConcordance(
                source=_pick(DataSource, ps.get("source")),
                rows=[_pick(WashRow, r) for r in ps.get("rows") or []],
                data_used=ps.get("data_used_for_estimates") or [])
            for ps in sd.get("per_source") or []
        ]
    return inst


def find_instructions(target: str) -> List[str]:
    """A file, or every instruction YAML under a directory."""
    if os.path.isfile(target):
        return [target]
    out = []
    for root, _dirs, files in os.walk(target):
        for f in files:
            if f.endswith(".yaml") and ("_water_v" in f or "_sanitation_v" in f):
                out.append(os.path.join(root, f))
    return sorted(out)
