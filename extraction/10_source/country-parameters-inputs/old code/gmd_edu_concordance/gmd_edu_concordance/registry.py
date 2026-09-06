"""
gmd_edu_concordance.registry
============================
What has been ingested, in what version, covering which era.

A country instruction is not a file you overwrite. A new workbook arrives and
one of three things is true, and the registry is what tells them apart:

**Nothing changed.** The content fingerprint matches the version in force. No
new version; the registry returns the one already there. Re-running the
extractor over an unchanged folder must not mint versions.

**The same era, described differently.** A correction, a reworded label, a
target that moved. That is a new *version* of the era already on file --
MINOR when nothing can move a person between GMD categories, MAJOR when
something can, because a MAJOR is what forces already-harmonized surveys to
rerun. The distinction is **computed**, never declared: an author cannot call
a breaking change cosmetic to avoid the reruns.

**A different era.** For education this is the common case and the important
one. A 2014 mapping and a 2023 mapping for the same country are not two
versions of one instruction; they are two eras of one country, and a cohort is
resolved against whichever was in force when that person was last in school.
The registry keeps both and closes the window between them -- which is the
only way rule E-03's declared gap ever gets closed.

The registry is a plain JSON file in the output folder. Nothing is ever
overwritten in it: every ingest appends, and the current version is the latest
entry that was approved, or the latest entry if none has been.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
from typing import Any, Dict, List, Optional, Tuple

REGISTRY = "concordance_registry.json"
SCHEMA = "gmd.concordance_registry"
SCHEMA_VERSION = "1.0.0"

# A change in any of these can move a person between GMD categories, so it is
# breaking and forces a MAJOR. Everything else is cosmetic.
BREAKING_FIELDS = ("gmd", "isced", "improved", "grades", "spans",
                   "rolls_up_to", "attainment_on_completion", "era_from",
                   "era_to")


def now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


def _path(outdir: str) -> str:
    return os.path.join(outdir, REGISTRY)


def load(outdir: str) -> Dict[str, Any]:
    p = _path(outdir)
    if not os.path.exists(p):
        return {"schema": SCHEMA, "schema_version": SCHEMA_VERSION,
                "entries": []}
    with open(p, encoding="utf-8") as fh:
        d = json.load(fh)
    d.setdefault("entries", [])
    return d


def save(outdir: str, doc: Dict[str, Any]) -> str:
    os.makedirs(outdir, exist_ok=True)
    p = _path(outdir)
    doc["updated_at"] = now()
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False, default=str)
    return p


def history(doc: Dict[str, Any], iso3: str, domain: str) -> List[dict]:
    return [e for e in doc.get("entries", [])
            if e.get("iso3") == iso3 and e.get("domain") == domain]


def current(doc: Dict[str, Any], iso3: str, domain: str,
            era: Optional[str] = None) -> Optional[dict]:
    """The version in force: the latest approved, else the latest."""
    hs = history(doc, iso3, domain)
    if era is not None:
        hs = [e for e in hs if str(e.get("era") or "") == str(era)]
    if not hs:
        return None
    approved = [e for e in hs if e.get("status") == "approved"]
    return (approved or hs)[-1]


def _parse(v: str) -> Tuple[int, int]:
    v = (v or "v1.0").lstrip("vV")
    try:
        major, _, minor = v.partition(".")
        return int(major), int(minor or 0)
    except ValueError:
        return 1, 0


def bump(previous: Optional[str], breaking: bool) -> str:
    if previous is None:
        return "v1.0"
    major, minor = _parse(previous)
    return f"v{major + 1}.0" if breaking else f"v{major}.{minor + 1}"


def classify(before: Optional[dict], after: dict) -> Dict[str, Any]:
    """Is this the same content, a cosmetic change, or a breaking one?"""
    if before is None:
        return {"kind": "first", "breaking": False, "changed": []}
    if before.get("fingerprint") == after.get("fingerprint"):
        return {"kind": "identical", "breaking": False, "changed": []}
    changed = sorted(k for k in BREAKING_FIELDS
                     if (before.get("signature") or {}).get(k)
                     != (after.get("signature") or {}).get(k))
    return {"kind": "breaking" if changed else "cosmetic",
            "breaking": bool(changed), "changed": changed}


def record(outdir: str, entry: Dict[str, Any]) -> Dict[str, Any]:
    """Append one ingest and decide its version.

    Returns the entry as stored, with ``version``, ``change`` and
    ``supersedes`` filled in. An identical re-ingest is recorded as an event
    but keeps the version already in force -- the point of the fingerprint.
    """
    doc = load(outdir)
    era = entry.get("era")
    before = current(doc, entry["iso3"], entry["domain"], era)
    ch = classify(before, entry)
    if ch["kind"] == "identical":
        entry["version"] = before["version"]
        entry["status"] = before.get("status", "draft")
        entry["supersedes"] = None
    else:
        entry["version"] = bump(before["version"] if before else None,
                                ch["breaking"])
        entry["supersedes"] = before["version"] if before else None
    entry["change"] = ch
    entry["recorded_at"] = now()
    doc["entries"].append(entry)
    doc["countries"] = summarise(doc)
    save(outdir, doc)
    return entry


def summarise(doc: Dict[str, Any]) -> List[dict]:
    """One row per country and domain, with its eras and the version in force."""
    seen: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for e in doc.get("entries", []):
        key = (e.get("iso3", ""), e.get("domain", ""))
        rec = seen.setdefault(key, {
            "iso3": key[0], "domain": key[1], "country": e.get("country", ""),
            "eras": {}, "ingests": 0})
        rec["ingests"] += 1
        rec["country"] = e.get("country") or rec["country"]
        era = str(e.get("era") or "")
        era_rec = rec["eras"].setdefault(era, {
            "era": era, "from": e.get("era_from"), "to": e.get("era_to"),
            "version": None, "status": "draft", "file": "", "ingests": 0})
        era_rec["ingests"] += 1
        era_rec["version"] = e.get("version")
        era_rec["status"] = e.get("status", "draft")
        era_rec["file"] = e.get("file", "")
        era_rec["from"] = e.get("era_from", era_rec["from"])
        era_rec["to"] = e.get("era_to", era_rec["to"])
        era_rec["cohort_era"] = bool(e.get("cohort_era"))
        rec["cohort_eras"] = rec.get("cohort_eras") or bool(e.get("cohort_era"))
    out = []
    for rec in seen.values():
        eras = sorted(rec["eras"].values(),
                      key=lambda x: (x["from"] is None, x["from"], x["era"]))
        rec["eras"] = tile(eras)
        rec["n_eras"] = len(eras)
        out.append(rec)
    return sorted(out, key=lambda r: (r["iso3"], r["domain"]))


def tile(eras: List[dict], open_end: int = 2035) -> List[dict]:
    """Close the window between consecutive eras.

    Two mappings, 2014 and 2023, mean the 2014 structure governed cohorts who
    left school up to 2022 and the 2023 one governs from 2023 on. Neither file
    says that; it is what having both of them implies, and it is what turns
    two declared gaps into one covered range. The result is marked inferred so
    a focal point can see it was worked out rather than stated.
    """
    dated = [e for e in eras if e.get("from") is not None]
    for i, e in enumerate(dated):
        nxt = dated[i + 1] if i + 1 < len(dated) else None
        if nxt is not None:
            e["to"] = int(nxt["from"]) - 1
            e["to_inferred"] = (
                f"the next era on file starts in {nxt['from']}")
        else:
            e["to"] = open_end
            e["to_inferred"] = "the latest era runs to the open end"
    # Only a schooling era leaves a cohort uncovered. A JMP release window is
    # the span of the surveys inside it, and nobody "falls before" it.
    if dated and dated[0].get("cohort_era"):
        dated[0]["gap_before"] = dated[0]["from"]
    return eras
