"""
gmd_edu_concordance.emit
========================
Six artefacts per workbook.

  {ISO3}_edu_{version}.yaml    the country instruction         -> S10, S11
  {ISO3}_edu_ladder.json       grade -> level -> canonical     -> S10 cohort resolution
  {ISO3}_edu_rows.csv          one flat row per programme      -> human review
  {ISO3}_edu_findings.json     rule ids, levels, source rows   -> S11 queue
  {ISO3}_edu_binding.json      what bound where                -> the wizard
  {ISO3}_edu_probe.txt         the instruction answering       -> the reviewer
  {ISO3}_edu_derivation.json   canonical GMD variables         -> S11 mapping
  {ISO3}_edu_derive.do         the derivation, as Stata        -> S13 code production
                               real questions in plain language
  {ISO3}_edu_view.json         the viewer bundle               -> the viewer app
"""
from __future__ import annotations

import csv
import json
import os
from dataclasses import asdict
from typing import List

from . import registry as REG
from .resolver import probe, render
from .schema import Instruction, value_of
from .validate import summarise, verdict

ROW_FIELDS = [
    "programme_id", "era", "programme", "programme_national",
    "programme_en_source", "needs_translation", "isced",
    "isced_label", "isced_p", "isced_a", "orientation", "completion",
    "position", "access", "access_to", "entrance_age", "duration_years",
    "years_in_level", "grades", "grade_from", "grade_to", "years_before",
    "years_at_completion", "gmd", "attainment_on_completion",
    "attainment_in_progress", "complete_at", "notes", "source_row",
    "derived_from",
]


from . import gmd as GMD


def _derivation(inst) -> dict:
    """The GMD canonical block for this country instruction."""
    ladder = [asdict(x) for x in inst.ladder]
    rows = [asdict(r) for r in inst.rows]
    cov = inst.coverage or {}
    return GMD.build(ladder, rows, inst.iso3, inst.country, inst.version,
                     cov.get("era_from"), cov.get("era_to"))


def write_derivation(inst, outdir: str) -> str:
    """`{ISO3}_edu_derivation.json` - which canonical variables this country
    can support, the grade crosswalk, and why."""
    _mkdir(outdir)
    d = _derivation(inst)
    path = os.path.join(outdir, f"{inst.iso3}_edu_derivation.json")
    doc = {k: v for k, v in d.items() if k != "stata"}
    doc["country"] = {"iso3": inst.iso3, "name": inst.country}
    doc["version"] = inst.version
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return path


def write_derive_do(inst, outdir: str) -> str:
    """`{ISO3}_edu_derive.do` - the derivation as runnable Stata."""
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_derive.do")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(_derivation(inst)["stata"])
    return path


def root_of(outdir: str) -> str:
    return os.path.dirname(os.path.abspath(outdir))


def _registry_slice(inst: Instruction, root: str) -> dict:
    """This country's eras, as the registry knows them."""
    doc = REG.load(root)
    for c in doc.get("countries", []):
        if c["iso3"] == inst.iso3 and c["domain"] == "education":
            return c
    return {}


def _mkdir(p):
    os.makedirs(p, exist_ok=True)
    return p


def _flat(v):
    if v is None:
        return ""
    if isinstance(v, dict):
        if "value" in v:
            return v["value"]
        if "raw" in v:
            return v["raw"]
    return v


def write_instruction(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, inst.filename())
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(inst.to_yaml())
    return path


def write_ladder(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_ladder.json")
    doc = {
        "country": {"iso3": inst.iso3, "name": inst.country},
        "version": inst.version,
        "structure": inst.structure,
        "coverage": inst.coverage,
        "registry": _registry_slice(inst, root_of(outdir)),
        "era": ({"id": e.id, "label": e.label,
                 "from": value_of(e.from_year), "to": value_of(e.to_year),
                 "reference_year": e.reference_year, "latest": e.latest}
                for e in inst.eras),
        "steps": [asdict(s) for s in inst.ladder],
        "attainment": [
            {"grade": s.grade, "isced": s.isced, "gmd": s.gmd,
             "attainment": s.attainment, "completes_level": s.completes_level,
             "isced_a": s.isced_a}
            for s in inst.ladder
        ],
        "years_in_level": [
            {"isced": r.isced, "isced_label": r.isced_label,
             "programme": r.programme, "orientation": r.orientation,
             "years": value_of(r.years_in_level),
             "grades": value_of(r.grades),
             "years_at_completion": value_of(r.years_at_completion),
             "gmd": r.gmd}
            for r in inst.rows
        ],
    }
    doc["era"] = list(doc["era"])
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return path


def write_rows_csv(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_rows.csv")
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=ROW_FIELDS)
        w.writeheader()
        for r in inst.rows:
            d = asdict(r)
            row = {k: _flat(d.get(k)) for k in ROW_FIELDS if k != "derived_from"}
            row["derived_from"] = (r.grades or {}).get("evidence", "") \
                if isinstance(r.grades, dict) else ""
            w.writerow(row)
    return path


def write_findings(inst: Instruction, findings, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_findings.json")
    doc = {
        "country": {"iso3": inst.iso3, "name": inst.country},
        "version": inst.version,
        "verdict": verdict(findings),
        "counts": summarise(findings),
        "fingerprint": inst.content_fingerprint(),
        "findings": [f.as_dict() for f in findings],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
    return path


def write_binding(inst: Instruction, binding, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_binding.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(binding.as_dict(), fh, indent=1, ensure_ascii=False)
    return path


def write_probe(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_probe.txt")
    head = (f"{inst.iso3}  {inst.country}   {inst.version}\n"
            f"structure {inst.structure.get('cycle') or '?'}   "
            f"school year reference {inst.source.reference_year}\n"
            f"era selected from the year the person was LAST IN SCHOOL, "
            f"not the survey year\n\n")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(head + render(probe(inst)) + "\n")
    return path


def write_view(inst: Instruction, findings, outdir: str) -> str:
    """The viewer bundle.  Everything the viewer app needs and nothing it does
    not."""
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_edu_view.json")
    doc = {
        "kind": "education",
        "domain": "education",
        "country": {"iso3": inst.iso3, "name": inst.country},
        "version": inst.version,
        "status": inst.status,
        "frame": inst.frame,
        "schema": inst.schema,
        "cohort_aware": inst.cohort_aware,
        "era_selector": inst.era_selector,
        "source": {"file": inst.source.file, "sha256": inst.source.sha256[:16],
                   "sheet": inst.source.sheet,
                   "header_row": inst.source.header_row,
                   "profile": inst.source.profile,
                   "rows_read": inst.source.rows_read,
                   "reference_year": inst.source.reference_year,
                   "extracted_at": inst.source.extracted_at},
        "language": inst.language,
        "structure": inst.structure,
        "coverage": inst.coverage,
        "registry": _registry_slice(inst, root_of(outdir)),
        "verdict": verdict(findings),
        "counts": summarise(findings),
        "fingerprint": inst.content_fingerprint(),
        "eras": [{"id": e.id, "label": e.label,
                  "from": value_of(e.from_year), "to": value_of(e.to_year),
                  "from_evidence": (e.from_year or {}).get("evidence", "")
                  if isinstance(e.from_year, dict) else "",
                  "reference_year": e.reference_year, "latest": e.latest,
                  "description": e.description}
                 for e in inst.eras],
        "rows": [{**asdict(r),
                  "grades_v": value_of(r.grades),
                  "years_in_level_v": value_of(r.years_in_level),
                  "years_at_completion_v": value_of(r.years_at_completion),
                  "grade_from_v": value_of(r.grade_from),
                  "grade_to_v": value_of(r.grade_to)}
                 for r in inst.rows],
        "ladder": [asdict(s) for s in inst.ladder],
        "derivation": _derivation(inst),
        "probe": probe(inst),
        "findings": [f.as_dict() for f in findings],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return path


def signature(inst: Instruction) -> dict:
    """The fields a change in which can move a person between GMD categories.

    Everything else is wording, and wording is a MINOR.
    """
    era = inst.eras[0] if inst.eras else None
    return {
        "gmd": "|".join(sorted({r.gmd for r in inst.rows})),
        "isced": "|".join(sorted({r.isced for r in inst.rows})),
        "grades": "|".join(f"{r.programme_id}:{value_of(r.grades)}"
                           for r in inst.rows),
        "attainment_on_completion": "|".join(
            f"{r.programme_id}:{r.attainment_on_completion}"
            for r in inst.rows),
        "era_from": value_of(era.from_year) if era else None,
        "era_to": value_of(era.to_year) if era else None,
    }


def _capability_slice(inst) -> dict:
    """What the registry needs to say, per country, about which GMD canonical
    variables this concordance can support.  A country that only reaches
    ``educat4`` is a normal outcome and the registry has to be able to show it
    without anyone opening the country."""
    cap = _derivation(inst)["capability"]
    return {
        "finest": cap.get("finest"),
        "produces": [k for k in ("educat4", "educat5", "educat7", "educy")
                     if cap.get(k, {}).get("ok")],
        "blocked": {k: cap[k].get("why", "") for k in ("educat4", "educat5", "educat7", "educy")
                    if not cap.get(k, {}).get("ok")},
    }


def register(inst: Instruction, findings, outdir: str) -> dict:
    """Record this ingest against everything ingested before it."""
    era = inst.eras[0] if inst.eras else None
    entry = REG.record(outdir, {
        "iso3": inst.iso3, "domain": "education", "country": inst.country,
        "file": inst.source.file, "sha256": inst.source.sha256,
        "profile": inst.source.profile,
        "release": inst.source.reference_year,
        "era": str(inst.source.reference_year or ""),
        "cohort_era": True,   # a schooling structure; cohorts fall inside it
        "era_from": value_of(era.from_year) if era else None,
        "era_to": value_of(era.to_year) if era else None,
        "structure": inst.structure.get("cycle"),
        "programmes": len(inst.rows),
        "gmd": _capability_slice(inst),
        "fingerprint": inst.content_fingerprint(),
        "verdict": verdict(findings), "counts": summarise(findings),
        "status": inst.status,
        "extracted_at": inst.source.extracted_at,
        "signature": signature(inst),
    })
    inst.version = entry["version"]
    return entry


def write_all(inst: Instruction, binding, findings, outdir: str) -> List[str]:
    entry = register(inst, findings, outdir)
    root = outdir
    outdir = os.path.join(outdir, inst.iso3 or "UNKNOWN")
    return [
        write_instruction(inst, outdir),
        write_ladder(inst, outdir),
        write_rows_csv(inst, outdir),
        write_findings(inst, findings, outdir),
        write_binding(inst, binding, outdir),
        write_probe(inst, outdir),
        write_derivation(inst, outdir),
        write_derive_do(inst, outdir),
        write_view(inst, findings, outdir),
        os.path.join(root, REG.REGISTRY),
    ]
