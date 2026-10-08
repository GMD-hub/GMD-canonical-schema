"""
gmd_wash_concordance.emit
=========================
**One set of files per domain.**  Water and sanitation never share an
artefact, because they are never approved together.

Into ``out/{ISO3}/``, for each of ``water`` and ``sanitation``:

  {ISO3}_{domain}_{version}.yaml   the country instruction     -> S10, S11
  {ISO3}_{domain}_sources.json     what each source supplied   -> S13 vintage
  {ISO3}_{domain}_rows.csv         one flat row per mapping    -> human review
  {ISO3}_{domain}_findings.json    rule ids, levels, rows      -> S11 queue
  {ISO3}_{domain}_benchmark.json   what JMP published          -> human review, S13
  {ISO3}_{domain}_view.json        the viewer bundle           -> the viewer app

and once per workbook:

  {ISO3}_wash_binding.json         what bound where            -> the wizard
"""
from __future__ import annotations

import csv
import json
import os
from dataclasses import asdict
from typing import List

from . import gmd as GMD
from . import registry as REG
from .schema import Extract, Instruction
from .validate import summarise, verdict

ROW_FIELDS = ["domain", "code", "label", "classification", "subgroup", "depth",
              "jmp", "jmp_id", "jmp_label_local", "rolls_up_to", "gmd",
              "spans", "improved", "shared", "observed_in", "n_sources",
              "first_seen", "last_seen", "source_row"]


def signature(inst: Instruction) -> dict:
    """The fields a change in which can move a person between GMD categories."""
    return {
        "gmd": "|".join(f"{r.code}:{r.gmd}" for r in inst.rows),
        "improved": "|".join(f"{r.code}:{r.improved}" for r in inst.rows),
        "spans": "|".join(f"{r.code}:{','.join(r.spans)}" for r in inst.rows),
        "rolls_up_to": "|".join(f"{r.code}:{','.join(r.rolls_up_to)}"
                                for r in inst.rows),
    }


def _capability_slice(inst) -> dict:
    d = _derivation(inst)
    cap = d["capability"]
    src = "water_source" if inst.domain == "water" else "sanitation_source"
    keys = [k for k in cap if k != "finest"]
    return {
        "finest": cap.get("finest"),
        "produces": [k for k in keys if cap[k].get("ok")],
        "blocked": {k: cap[k].get("why", "") for k in keys if not cap[k].get("ok")},
        "residual": sum(1 for r in d["crosswalk"] if r["gmd_code"] == 14),
        "spanning": sum(1 for r in d["crosswalk"] if r["spans"]),
        "disagrees_with_jmp": len(d["disagreements"]),
    }


def register(inst: Instruction, findings, outdir: str) -> dict:
    entry = REG.record(outdir, {
        "iso3": inst.iso3, "domain": inst.domain, "country": inst.country,
        "file": inst.source.file, "sha256": inst.source.sha256,
        "profile": inst.source.profile,
        "release": inst.source.vintage,
        # A JMP country file is one release covering many survey years, so the
        # "era" is the release; the survey vintage lives in `vintage`.
        "era": str(inst.source.vintage or ""),
        "cohort_era": False,  # a release window, not a schooling structure
        "era_from": (inst.vintage or {}).get("from"),
        "era_to": (inst.vintage or {}).get("to"),
        "language": inst.language,
        "sources": len(inst.sources), "rows": len(inst.rows),
        "gmd": _capability_slice(inst),
        "fingerprint": inst.content_fingerprint(),
        "verdict": verdict(findings), "counts": summarise(findings),
        "status": inst.status,
        "extracted_at": inst.source.extracted_at,
        "signature": signature(inst),
    })
    inst.version = entry["version"]
    return entry


def root_of(outdir: str) -> str:
    return os.path.dirname(os.path.abspath(outdir))


def _registry_slice(inst: Instruction, root: str) -> dict:
    doc = REG.load(root)
    for c in doc.get("countries", []):
        if c["iso3"] == inst.iso3 and c["domain"] == inst.domain:
            return c
    return {}


def _mkdir(p):
    os.makedirs(p, exist_ok=True)
    return p


def write_instruction(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, inst.filename())
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(inst.to_yaml())
    return path


def write_sources(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.stem()}_sources.json")
    doc = {
        "country": {"iso3": inst.iso3, "name": inst.country},
        "domain": inst.domain,
        "language": inst.language,
        "file": asdict(inst.source),
        "selection": inst.selection,
        "vintage": inst.vintage,
        "sections": [asdict(s) for s in inst.sections],
        "per_source": [
            {"source": asdict(sc.source),
             "data_used_for_estimates": sc.data_used,
             "rows": [asdict(r) for r in sc.rows]}
            for sc in inst.per_source
        ],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return path


def write_rows_csv(inst: Instruction, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.stem()}_rows.csv")
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=ROW_FIELDS)
        w.writeheader()
        for r in inst.rows:
            w.writerow({
                "domain": inst.domain, "code": r.code, "label": r.label,
                "classification": r.classification, "subgroup": r.subgroup,
                "depth": r.depth, "jmp": r.jmp, "jmp_id": r.jmp_id,
                "jmp_label_local": r.jmp_label_local,
                "rolls_up_to": "|".join(r.rolls_up_to),
                "gmd": r.gmd, "spans": "|".join(r.spans),
                "improved": "" if r.improved is None else r.improved,
                "shared": "" if r.shared is None else r.shared,
                "observed_in": "|".join(r.observed_in),
                "n_sources": len(r.observed_in),
                "first_seen": r.first_seen or "",
                "last_seen": r.last_seen or "",
                "source_row": r.source_row or "",
            })
    return path


def write_findings(inst: Instruction, findings, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.stem()}_findings.json")
    doc = {
        "country": {"iso3": inst.iso3, "name": inst.country},
        "domain": inst.domain,
        "version": inst.version,
        "verdict": verdict(findings),
        "counts": summarise(findings),
        "fingerprint": inst.content_fingerprint(),
        "findings": [f.as_dict() for f in findings],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
    return path


def write_benchmark(inst: Instruction, outdir: str) -> str:
    """What JMP published, in its own file.

    Separate because the instruction may not carry survey-level data, and
    because these are the numbers a reviewer wants beside the mapping and a
    later run wants to be measured against."""
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.stem()}_benchmark.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(inst.benchmark or {}, fh, indent=1, ensure_ascii=False,
                  default=str)
    return path


def write_benchmark_csv(inst: Instruction, outdir: str) -> str:
    """The same thing flat, because a reviewer will open it in Excel."""
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.stem()}_benchmark.csv")
    fields = ["domain", "source", "year", "source_type", "block", "jmp_id",
              "jmp", "national_label", "gmd", "improved", "rolls_up_to",
              "urban", "rural", "total", "source_row"]
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for ps in (inst.benchmark or {}).get("per_source", []):
            src = ps.get("source", {})
            base = {"domain": inst.domain, "source": src.get("code"),
                    "year": src.get("year"), "source_type": src.get("type")}
            for c in ps.get("categories", []):
                w.writerow({**base, "block": "category",
                            "jmp_id": c.get("jmp_id"), "jmp": c.get("jmp"),
                            "national_label": c.get("national_label"),
                            "gmd": c.get("gmd"),
                            "improved": "" if c.get("improved") is None
                                        else c["improved"],
                            "rolls_up_to": "|".join(c.get("rolls_up_to") or []),
                            "urban": c.get("urban"), "rural": c.get("rural"),
                            "total": c.get("total"),
                            "source_row": c.get("row")})
            for block, rows in (ps.get("blocks") or {}).items():
                for x in rows:
                    w.writerow({**base, "block": block,
                                "jmp": x.get("label"),
                                "national_label": x.get("label_local"),
                                "urban": x.get("urban"), "rural": x.get("rural"),
                                "total": x.get("total"),
                                "source_row": x.get("row")})
    return path


def write_view(inst: Instruction, findings, outdir: str) -> str:
    """The viewer bundle.  Everything the viewer app needs and nothing it does
    not: no frequencies, no per-source row dumps, no file paths."""
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.stem()}_view.json")
    doc = {
        "kind": "wash",
        "domain": inst.domain,
        "country": {"iso3": inst.iso3, "name": inst.country},
        "version": inst.version,
        "status": inst.status,
        "language": inst.language,
        "frame": inst.frame,
        "schema": inst.schema,
        "source": {"file": inst.source.file, "sha256": inst.source.sha256[:16],
                   "profile": inst.source.profile,
                   "vintage": inst.source.vintage,
                   "extracted_at": inst.source.extracted_at},
        "selection": inst.selection,
        "translation": inst.translation,
        "vintage": inst.vintage,
        "registry": _registry_slice(inst, root_of(outdir)),
        "verdict": verdict(findings),
        "counts": summarise(findings),
        "fingerprint": inst.content_fingerprint(),
        "ladder": inst.ladder,
        "facility_types": inst.facility_types,
        "classifications": inst.classifications,
        "sections": [{"name": s.name, "items": [i["label"] for i in s.items]}
                     for s in inst.sections],
        "sources": [asdict(s) for s in inst.sources],
        "rows": [asdict(r) for r in inst.rows],
        "data_used": {sc.source.code: sc.data_used for sc in inst.per_source},
        "derivation": _derivation(inst),
        "benchmark": inst.benchmark or {},
        "findings": [f.as_dict() for f in findings],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return path


def _derivation(inst) -> dict:
    return GMD.build([asdict(r) for r in inst.rows], inst.iso3, inst.country,
                     inst.version, inst.domain)


def write_derivation(inst, outdir: str) -> str:
    """`{ISO3}_{domain}_derivation.json` - the GMD canonical code list, which
    national category lands on which code, and what the country still has to
    rule on."""
    _mkdir(outdir)
    d = _derivation(inst)
    path = os.path.join(outdir, f"{inst.iso3}_{inst.domain}_derivation.json")
    doc = {k: v for k, v in d.items() if k != "stata"}
    doc["country"] = {"iso3": inst.iso3, "name": inst.country}
    doc["version"] = inst.version
    doc["domain"] = inst.domain
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return path


def write_derive_do(inst, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{inst.iso3}_{inst.domain}_derive.do")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(_derivation(inst)["stata"])
    return path


def write_binding(ex: Extract, binding, outdir: str) -> str:
    _mkdir(outdir)
    path = os.path.join(outdir, f"{ex.iso3 or 'UNKNOWN'}_wash_binding.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(binding.as_dict(), fh, indent=1, ensure_ascii=False)
    return path


def write_all(ex: Extract, binding, findings_by_domain, outdir: str) -> List[str]:
    root = outdir
    outdir = os.path.join(outdir, ex.iso3 or "UNKNOWN")
    paths = []
    for inst in ex.instructions():
        f = findings_by_domain.get(inst.domain, [])
        register(inst, f, root)
        paths += [
            write_instruction(inst, outdir),
            write_sources(inst, outdir),
            write_rows_csv(inst, outdir),
            write_findings(inst, f, outdir),
            write_benchmark(inst, outdir),
            write_benchmark_csv(inst, outdir),
            write_view(inst, f, outdir),
            write_derivation(inst, outdir),
            write_derive_do(inst, outdir),
        ]
    paths.append(write_binding(ex, binding, outdir))
    paths.append(os.path.join(root, REG.REGISTRY))
    return paths
