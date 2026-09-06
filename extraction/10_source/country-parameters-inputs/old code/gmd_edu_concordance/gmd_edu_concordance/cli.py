"""
gmd_edu_concordance.cli
=======================
Five commands.

  inspect   what bound where, and stop.  Run this first on any new file.
  extract   one workbook -> the six artefacts
  bulk      a directory of workbooks -> the same, plus a batch manifest
  ladder    print the derived grade ladder
  resolve   answer one cohort question against a workbook
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

from . import __version__
from . import registry as REG
from .viewer import build as build_viewer
from .viewer import scan as scan_outputs, serve as serve_viewer
from .derive import run as derive_run
from .emit import write_all
from .load import find_instructions, load_instruction
from .reader import load_profile, load_profiles, read
from .resolver import probe, render, resolve
from .schema import value_of
from .validate import summarise, validate, verdict

LEVEL_ORDER = {"BLOCK": 0, "WARN": 1, "INFO": 2}


def _p(*a):
    print(*a)


def _load(args):
    inst, b = read(args.file, iso3=getattr(args, "iso3", None),
                   country=getattr(args, "country", None),
                   version=getattr(args, "version", "v1.0"),
                   reference_year=getattr(args, "reference_year", None),
                   sheet=getattr(args, "sheet", None))
    profs = {p["profile"]: p for p in load_profiles()}
    derive_run(inst, profs.get(b.profile) or load_profile())
    return inst, b


# --------------------------------------------------------------------------
def cmd_inspect(args) -> int:
    inst, b = _load(args)
    _p(f"file      : {inst.source.file}")
    _p(f"sha256    : {inst.source.sha256[:16]}…")
    _p(f"profile   : {b.profile}")
    _p(f"country   : {inst.iso3 or '??'}  {inst.country or '(unknown)'}")
    _p(f"sheet     : {b.sheet!r}   header row {b.header_row}   "
       f"{b.rows_read} programme row(s)")
    cands = b.candidates_considered or []
    if len(cands) > 1:
        _p("")
        _p(f"  {len(cands)} sheet/profile pair(s) scored; the table is the one "
           f"whose required columns bind and whose rows parse:")
        for c in cands[:8]:
            mark = "->" if (b.score and c is b.score) or (
                b.score and c["sheet"] == b.score["sheet"]
                and c["profile"] == b.score["profile"]) else "  "
            _p(f"   {mark} {c['profile'][:22]:24s} {c['sheet'][:24]:26s} "
               f"{c['rows_parsed']:4d} parsed  {c['bound']:2d} bound  "
               f"score {c['score']:5d}"
               + (f"  MISSING {', '.join(c['required_missing'])}"
                  if c["required_missing"] else "")
               + ("  (reads as prose)" if c.get("prose") else ""))
    _p(f"reference : school year {inst.source.reference_year}")
    _p(f"structure : {inst.structure.get('cycle') or '?'}   "
       f"grades {inst.structure.get('ladder_grades') or '-'}")
    _p("")
    for fld in ["programme_national", "programme_en", "entrance_req_en",
                "diploma_en", "entrance_age", "duration", "isced_label",
                "isced_code", "orientation", "completion", "access", "notes",
                "isced_p", "isced_a"]:
        c = b.columns.get(fld)
        h = b.headers.get(fld, "")
        _p(f"  {fld:22s} <- col {str(c or '--'):>3s}  {h[:56]!r}")
    for fld in b.unbound:
        _p(f"\n  UNBOUND {fld}: candidate headers in this sheet")
        for c, h in b.candidates.get(fld, []):
            _p(f"      col {c:>3d}  {h[:60]!r}")
        _p("      -> add the real header string to the profile YAML. "
           "No Python changes.")
    for prob in b.problems:
        _p(f"\nPROBLEM   : {prob}")
    return 1 if b.problems else 0


def cmd_ladder(args) -> int:
    inst, _ = _load(args)
    _p(f"{inst.iso3}  {inst.country}   structure "
       f"{inst.structure.get('cycle')}   reference "
       f"{inst.source.reference_year}")
    _p(f"{'grade':6s} {'isced':6s} {'gmd':17s} {'ends level':11s} "
       f"{'cum yrs':8s} programme")
    for s in inst.ladder:
        _p(f"{s.grade:<6d} {s.isced:6s} {s.gmd:17s} "
           f"{('yes' if s.completes_level else ''):11s} "
           f"{str(s.years_at_completion or ''):8s} {s.programme[:44]}")
    _p("\nyears in level (from the theoretical duration column)")
    for r in inst.rows:
        _p(f"  ISCED {r.isced}  {value_of(r.years_in_level) or '?':>5s} yr  "
           f"grades {str(value_of(r.grades)):>6s}  "
           f"cum {str(value_of(r.years_at_completion)):>6s}  "
           f"{r.orientation:12s} {r.programme[:40]}")
    return 0


def cmd_derive(args) -> int:
    """What GMD canonical variables this country can produce, and the code."""
    from dataclasses import asdict
    from . import gmd as GMD
    inst, _ = _load(args)
    cov = inst.coverage or {}
    d = GMD.build([asdict(x) for x in inst.ladder], [asdict(r) for r in inst.rows],
                  inst.iso3, inst.country, inst.version,
                  cov.get("era_from"), cov.get("era_to"))
    if args.stata:
        _p(d["stata"])
        return 0
    cap = d["capability"]
    _p(f"{inst.iso3}  {inst.country}   ISCED levels present: "
       f"{', '.join(cap['isced_levels'])}")
    _p(f"finest canonical variable this concordance supports: "
       f"{cap['finest'] or 'none'}")
    _p("")
    for k in ("educat4", "educat5", "educat7", "educy"):
        v = cap[k]
        mark = "yes" if v["ok"] else "NO "
        _p(f"  {mark}  {k:10s} {v.get('why') or v.get('note') or ''}")
    _p("")
    _p(f"  {'grade':6s} {'isced':6s} {'e7':4s} {'e5':4s} {'e4':4s} {'educy':7s} label")
    for r in d["crosswalk"]:
        _p(f"  {r['grade']:<6d} {r['isced']:6s} "
           f"{str(r['educat7'] or '-'):4s} {str(r['educat5'] or '-'):4s} "
           f"{str(r['educat4'] or '-'):4s} {str(r['educy'] if r['educy'] is not None else '-'):7s} "
           f"{r['educat7_label'][:44]}"
           + ("   [carried]" if r["carried_forward"] else ""))
    return 0


def cmd_resolve(args) -> int:
    inst, _ = _load(args)
    if args.grade is None and args.isced is None:
        _p(render(probe(inst)))
        return 0
    r = resolve(inst, grade=args.grade, year_last_in_school=args.year,
                isced=args.isced)
    _p(json.dumps(r, indent=1, ensure_ascii=False, default=str))
    return 0 if r.get("resolved") else 1


def cmd_check(args) -> int:
    """Re-run the rules over instruction files already emitted."""
    files = find_instructions(args.target)
    if not files:
        _p(f"no instruction files under {args.target}")
        return 1
    worst = 0
    for f in files:
        inst = load_instruction(f)
        findings = validate(inst)
        v = verdict(findings)
        c = summarise(findings)
        _p(f"{os.path.basename(f)[:40]:42s} {v:16s} "
           f"BLOCK {c['BLOCK']}  WARN {c['WARN']}  INFO {c['INFO']}")
        for x in sorted(findings, key=lambda x: LEVEL_ORDER[x.level]):
            if x.level == "INFO" and not args.verbose:
                continue
            row = f" row {x.source_row}" if x.source_row else ""
            _p(f"    {x.level:5s} {x.rule}  {x.where}{row}  {x.message}")
        worst = max(worst, 2 if v == "blocked" else 0)
    return worst


def cmd_extract(args) -> int:
    inst, b = _load(args)
    findings = validate(inst, b)
    v = verdict(findings)
    inst.status = "draft" if v != "blocked" else "rejected"
    paths = write_all(inst, b, findings, args.out)
    c = summarise(findings)
    _p(f"{inst.iso3}  {inst.country}   {v}   "
       f"BLOCK {c['BLOCK']}  WARN {c['WARN']}  INFO {c['INFO']}")
    _p(f"structure {inst.structure.get('cycle')}   grades "
       f"{inst.structure.get('ladder_grades')}   fingerprint "
       f"{inst.content_fingerprint()}")
    for f in sorted(findings, key=lambda f: LEVEL_ORDER[f.level])[:args.show]:
        row = f" row {f.source_row}" if f.source_row else ""
        _p(f"  {f.level:5s} {f.rule}  {f.where}{row}  {f.message}")
    if len(findings) > args.show:
        _p(f"  … {len(findings) - args.show} more, see the findings file")
    for p in paths:
        _p(f"  wrote {p}")
    return 2 if v == "blocked" else 0


def cmd_bulk(args) -> int:
    files = sorted(glob.glob(os.path.join(args.dir, "*.xlsx")))
    files = [f for f in files if not os.path.basename(f).startswith("~$")]
    manifest, tally, seen = [], {}, {}
    for f in files:
        try:
            inst, b = read(f, version=args.version)
            profs = {p["profile"]: p for p in load_profiles()}
            derive_run(inst, profs.get(b.profile) or load_profile())
        except Exception as exc:                          # noqa: BLE001
            manifest.append({"file": os.path.basename(f), "outcome": "error",
                             "error": str(exc)})
            continue
        if not inst.rows and b.header_row is None:
            # not a UIS ISCED mapping at all -- say so and write nothing
            manifest.append({"file": os.path.basename(f),
                             "outcome": "not_this_family",
                             "note": "no ISCED mapping header row in any sheet"})
            tally["not_this_family"] = tally.get("not_this_family", 0) + 1
            _p(f"{os.path.basename(f)[:44]:46s} {'--':4s} "
               f"{'not_this_family':16s}")
            continue
        findings = validate(inst, b)
        v = verdict(findings)
        if not inst.iso3:
            v = "needs_identity"
        elif inst.iso3 in seen:
            v = "collision"
        else:
            seen[inst.iso3] = os.path.basename(f)
        inst.status = "draft" if v not in ("blocked", "rejected") else "rejected"
        paths = write_all(inst, b, findings, args.out)
        tally[v] = tally.get(v, 0) + 1
        manifest.append({
            "file": os.path.basename(f), "iso3": inst.iso3,
            "country": inst.country, "outcome": v,
            "reference_year": inst.source.reference_year,
            "structure": inst.structure.get("cycle"),
            "programmes": len(inst.rows),
            "fingerprint": inst.content_fingerprint(),
            "counts": summarise(findings), "artifacts": paths,
        })
        _p(f"{os.path.basename(f)[:44]:46s} {inst.iso3 or '???':4s} "
           f"{v:16s} {inst.structure.get('cycle') or '':10s} "
           f"{len(inst.rows):3d} prog")
    os.makedirs(args.out, exist_ok=True)
    mpath = os.path.join(args.out, "edu_batch_manifest.json")
    with open(mpath, "w", encoding="utf-8") as fh:
        json.dump({"files": len(files), "tally": tally,
                   "entries": manifest}, fh, indent=1, ensure_ascii=False)
    _p(f"\n{len(files)} file(s) read")
    for k, n in tally.items():
        _p(f"  {k:18s}: {n}")
    _p(f"manifest: {mpath}")
    return 2 if tally.get("blocked") else 0


# --------------------------------------------------------------------------
def cmd_viewer(args) -> int:
    """Serve a folder, or write the page.

    Serving is the mode to use while iterating: the server re-reads the
    directory on every request, so re-running the extractor and hitting reload
    shows the new output. Nothing is cached and nothing is baked in.
    """
    if args.serve:
        target = args.target or "out"
        if not os.path.isdir(target):
            _p(f"{target} is not a directory")
            return 1
        sc = scan_outputs(target)
        _p(f"serving {sc['root']}")
        if not sc["countries"]:
            _p("  (no *_view.json yet -- run extract or bulk first; "
               "the page will pick them up on reload)")
        for c in sc["countries"]:
            _p(f"  {c['iso3']:5s} {c['dir'] or '.':22s} "
               + ", ".join(f"{d['domain']} ({d['verdict']})"
                           for d in c["domains"]))
        _, url = serve_viewer(target, port=args.port, open_browser=args.open,
                              title=args.title, block=False)
        _p(f"\n  {url}")
        _p("  re-reads the folder on every request -- rerun the extractor, "
           "then reload")
        _p("  loopback only; ctrl-c to stop")
        try:
            import time
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            _p("\nstopped")
        return 0

    target = None if args.picker else (args.target or "out")
    if target and not args.embed and not os.path.isdir(target):
        _p(f"{target} is not a directory")
        return 1
    path = build_viewer(target, args.out, title=args.title, embed=args.embed)
    size = os.path.getsize(path)
    _p(f"wrote {path}  ({size / 1024:.0f} KB)")
    if args.embed:
        _p("frozen snapshot: the bundles are inlined, so it needs nothing at "
           "all -- but it will not change when you rerun the extractor")
    else:
        _p("open it and choose a country folder (or drop one on the page); "
           "it reads whatever is there, so it never goes stale")
    return 0


def cmd_registry(args) -> int:
    """What has been ingested, in what version, covering which era."""
    doc = REG.load(args.out)
    rows = doc.get("countries") or REG.summarise(doc)
    if not rows:
        _p(f"nothing recorded in {os.path.join(args.out, REG.REGISTRY)}")
        return 1
    _p(f"{len(doc.get('entries', []))} ingest(s) recorded in "
       f"{os.path.join(args.out, REG.REGISTRY)}\n")
    for c in rows:
        _p(f"{c['iso3']}  {c['country'][:24]:26s} {c['domain']:11s} "
           f"{c['n_eras']} era(s), {c['ingests']} ingest(s)")
        for e in c["eras"]:
            span = (f"{e['from']}-{e['to']}" if e.get("from") is not None
                    else "(no window)")
            kind = "cohorts" if e.get("cohort_era") else "surveys"
            _p(f"    {e['era'] or '-':8s} {span:12s} {kind:8s} "
               f"{e['version']:6s} {e['status']:10s} {e['file'][:34]}")
            if e.get("gap_before"):
                _p(f"      cohorts before {e['gap_before']} have no era")
            if e.get("to_inferred"):
                _p(f"      window closed because {e['to_inferred']}")
    if args.verbose:
        _p("")
        for e in doc.get("entries", []):
            _p(f"  {e.get('recorded_at', '')[:19]}  {e['iso3']} "
               f"{e['domain']:11s} {e['version']:6s} "
               f"{e['change']['kind']:10s} {e.get('file', '')[:36]}"
               + (f"  breaking: {', '.join(e['change']['changed'])}"
                  if e["change"].get("changed") else ""))
    return 0


def build_parser():
    ap = argparse.ArgumentParser(
        prog="gmd_edu_concordance",
        description="ISCED 2011 UIS national mapping workbook -> GMD System 8 "
                    "country education instruction.")
    ap.add_argument("--version-info", action="version",
                    version=f"gmd_edu_concordance {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def ident(p):
        p.add_argument("--iso3", default=None)
        p.add_argument("--country", default=None)
        p.add_argument("--sheet", default=None,
                       help="force a sheet instead of the best-scoring one")
        p.add_argument("--reference-year", type=int, default=None,
                       dest="reference_year",
                       help="override the School Year reference")

    p = sub.add_parser("inspect", help="what bound where, then stop")
    p.add_argument("file")
    ident(p)
    p.set_defaults(fn=cmd_inspect)

    p = sub.add_parser("ladder", help="print the derived grade ladder")
    p.add_argument("file")
    ident(p)
    p.set_defaults(fn=cmd_ladder)

    p = sub.add_parser("resolve", help="answer a cohort question")
    p.add_argument("file")
    p.add_argument("--grade", type=int, default=None)
    p.add_argument("--year", type=int, default=None,
                   help="the year the person was LAST IN SCHOOL")
    p.add_argument("--isced", default=None)
    ident(p)
    p.set_defaults(fn=cmd_resolve)

    p = sub.add_parser("derive", help="the GMD canonical variables this "
                       "country's ladder can support, and the code that makes them")
    p.add_argument("file")
    p.add_argument("--stata", action="store_true",
                   help="print the generated do-file instead of the summary")
    ident(p)
    p.set_defaults(fn=cmd_derive)

    p = sub.add_parser("extract", help="one workbook -> the eight artefacts")
    p.add_argument("file")
    p.add_argument("--out", default="out")
    p.add_argument("--version", default="v1.0")
    p.add_argument("--show", type=int, default=12)
    ident(p)
    p.set_defaults(fn=cmd_extract)

    p = sub.add_parser("viewer", help="review the output: serve a folder, or "
                                      "write the page")
    p.add_argument("target", nargs="?", default=None,
                   help="the output directory (default: out)")
    p.add_argument("--serve", action="store_true",
                   help="run a loopback review server that re-reads the "
                        "folder on every request")
    p.add_argument("--port", type=int, default=8765,
                   help="preferred port for --serve (the next free one is "
                        "used if it is taken)")
    p.add_argument("--open", action="store_true",
                   help="open a browser once the server is up")
    p.add_argument("--embed", action="store_true",
                   help="freeze the bundles into the page -- a snapshot to "
                        "send on, not a review tool")
    p.add_argument("--picker", action="store_true",
                   help="write the page with no folder attached")
    p.add_argument("--out", default=None,
                   help="output HTML path (default: "
                        "<target>/concordance_viewer.html)")
    p.add_argument("--title", default="GMD country concordance")
    p.set_defaults(fn=cmd_viewer)

    p = sub.add_parser("registry", help="what has been ingested, in what "
                                        "version, covering which era")
    p.add_argument("--out", default="out", help="the output directory")
    p.add_argument("--verbose", action="store_true",
                   help="every ingest, not just the summary")
    p.set_defaults(fn=cmd_registry)

    p = sub.add_parser("check", help="re-run the rules over emitted "
                                     "instruction files")
    p.add_argument("target", help="an instruction YAML, or a directory")
    p.add_argument("--verbose", action="store_true", help="show INFO too")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("bulk", help="a directory of workbooks")
    p.add_argument("dir")
    p.add_argument("--out", default="out")
    p.add_argument("--version", default="v1.0")
    p.set_defaults(fn=cmd_bulk)
    return ap


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
