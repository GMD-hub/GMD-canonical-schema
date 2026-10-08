"""
gmd_wash_concordance.cli
========================
Four commands.

  inspect   what bound where, and stop.  Run this first on any new file.
  extract   one workbook -> the five artefacts
  bulk      a directory of workbooks -> the same, plus a batch manifest
  sources   list the data sources in a workbook and their types
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from dataclasses import asdict

from . import __version__
from . import registry as REG
from .viewer import build as build_viewer
from .viewer import scan as scan_outputs, serve as serve_viewer
from .emit import write_all
from .load import find_instructions, load_instruction
from .reader import read
from .validate import summarise, validate, validate_extract, verdict
from . import master as M

LEVEL_ORDER = {"BLOCK": 0, "WARN": 1, "INFO": 2}


def _p(*a):
    print(*a)


# --------------------------------------------------------------------------
def cmd_inspect(args) -> int:
    ex, b = read(args.file, iso3=args.iso3, sources=args.sources,
                 domains=args.domains)
    src = (ex.instructions() or [None])[0]
    _p(f"file      : {src.source.file if src else os.path.basename(args.file)}")
    if src:
        _p(f"sha256    : {src.source.sha256[:16]}…")
    _p(f"profile   : {b.profile}")
    _p(f"country   : {ex.iso3 or '??'}  {ex.country or '(unknown)'}"
       f"   language {ex.language or '?'}")
    t = b.translation or {}
    if t:
        _p(f"labels    : {t.get('resolved_by', '?')}"
           f"   ({t.get('phrases', 0)} phrases from sheet "
           f"{t.get('sheet') or '?'!r}"
           + (f", {t['ambiguous_strings']} of them ambiguous as strings"
              if t.get("ambiguous_strings") else "") + ")")
    for inst in ex.instructions():
        dom = inst.domain
        _p(f"\n{dom}  ->  {inst.filename()}")
        _p(f"  sheet            : {b.sheets.get(dom) or '(not found)'}")
        _p(f"  concordance row  : {b.tree_header_row.get(dom)}")
        _p(f"  blocks in sheet  : {b.blocks.get(dom, 0)}")
        _p(f"  blocks selected  : {b.selected.get(dom, 0)}  ({args.sources})")
        mis = b.tree_alignment.get(dom) or []
        if dom not in b.tree_alignment:
            _p("  tree             : NOT CHECKED -- no concordance header was "
               "found, so the category tree was never compared")
        elif mis:
            _p(f"  TREE MISMATCH    : {len(mis)} position(s) differ from the "
               f"pinned JMP master")
            for m in mis[:5]:
                _p(f"      row {m['row']}: expected {m['expected']!r}, "
                   f"found {m['found']!r}")
            _p("      -> the template changed. Update the master data file "
               "before trusting this extract.")
        else:
            _p(f"  tree             : matches the pinned JMP master "
               f"({len(M.load('jmp_%s_master.yaml' % dom))} nodes)")
        _p(f"  sections         : "
           + ", ".join(f"{x.name} ({len(x.items)})" for x in inst.sections))
        _p(f"  classifications  : {len(inst.classifications)} group(s), "
           f"{sum(len(c['subgroups']) for c in inst.classifications)} subgroup(s)")
        _p(f"  facility types   : "
           + ", ".join(f"{f['name']}"
                       + ("" if f["in_workbook"] else " (NOT IN WORKBOOK)")
                       for f in inst.facility_types))
        _p(f"  rows             : {len(inst.rows)}")
    for prob in b.problems:
        _p(f"\nPROBLEM   : {prob}")
    return 1 if b.problems else 0


def cmd_sources(args) -> int:
    ex, b = read(args.file, iso3=args.iso3, sources="all", domains="both")
    _p(f"{ex.iso3}  {ex.country}   language {ex.language or '?'}")
    for inst in ex.instructions():
        _p(f"\n{inst.domain}   {len(inst.sources)} source(s)")
        _p(f"  {'code':26s} {'year':6s} {'type':26s} rows  name")
        for s in inst.sources:
            _p(f"  {s.code:26s} {str(s.year or ''):6s} {s.type[:26]:26s} "
               f"{s.n_rows:4d}  {s.name[:42]}")
    return 0


def cmd_chain(args) -> int:
    """classification -> subgroup -> facility type, for one domain."""
    ex, b = read(args.file, iso3=args.iso3, sources=args.sources,
                 domains=args.domain)
    for inst in ex.instructions():
        _p(f"{inst.iso3}  {inst.country}  ·  {inst.domain}  ·  "
           f"language {inst.language or '?'}")
        _p(f"facility types: "
           + ", ".join(f["name"] for f in inst.facility_types))
        for c in inst.classifications:
            _p(f"\n{c['classification'].upper()}"
               f"   [{', '.join(c['rolls_up_to']) or '—'}]"
               f"   {c['n_national_categories']} national categor(ies)")
            for sg in c["subgroups"]:
                nat = sg["national_categories"]
                if args.used and not nat:
                    continue
                pad = "  " * sg["depth"]
                imp = {True: "improved", False: "unimproved",
                       None: "unsettled"}[sg["improved"]]
                _p(f"  {pad}{sg['label'][:38]:40s} {imp:11s} "
                   f"{(sg['gmd'] or '·'):18s} "
                   f"[{', '.join(sg['rolls_up_to']) or '—'}]")
                for n in nat:
                    _p(f"  {pad}    ← {n}")
    return 0


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


def cmd_derive(args) -> int:
    from dataclasses import asdict
    from . import gmd as GMD
    ex, b = read(args.file, iso3=getattr(args, "iso3", None),
                 country=getattr(args, "country", None),
                 version=getattr(args, "version", None),
                 sources=getattr(args, "sources", "microdata"),
                 domains=args.domain)
    inst = [i for i in ex.instructions() if i.domain == args.domain]
    if not inst:
        _p(f"no {args.domain} instruction in this workbook")
        return 1
    inst = inst[0]
    d = GMD.build([asdict(r) for r in inst.rows], inst.iso3, inst.country,
                  inst.version, inst.domain)
    if args.stata:
        _p(d["stata"])
        return 0
    cap = d["capability"]
    _p(f"{inst.iso3}  {inst.country}  {inst.domain}")
    _p(f"finest canonical variable this concordance supports: {cap['finest'] or 'none'}")
    _p("")
    for k, v in cap.items():
        if not isinstance(v, dict):
            continue
        _p(f"  {'yes' if v['ok'] else 'NO '}  {k:18s} {v.get('why') or v.get('note') or ''}")
    _p("")
    _p(f"  {'national category':<38s} {'code':>5s}  {'improved':>8s}  GMD label")
    for r in d["crosswalk"]:
        _p(f"  {r['label'][:38]:<38s} {str(r['gmd_code'] or '-'):>5s}  "
           f"{str(r['improved'] if r['improved'] is not None else '-'):>8s}  "
           f"{r['gmd_label'][:32]}"
           + (f"   SPANS {r['spans']}" if r["spans"] else "")
           + ("   ** differs from JMP" if r["disagrees_with_jmp"] else ""))
    return 0


def cmd_extract(args) -> int:
    ex, b = read(args.file, iso3=args.iso3, country=args.country,
                 version=args.version, sources=args.sources,
                 domains=args.domains)
    by_dom = validate_extract(ex, b)
    worst = 0
    for inst in ex.instructions():
        findings = by_dom[inst.domain]
        v = verdict(findings)
        inst.status = "draft" if v != "blocked" else "rejected"
        c = summarise(findings)
        _p(f"{inst.iso3}  {inst.country}  ·  {inst.domain:11s} {v:16s} "
           f"BLOCK {c['BLOCK']}  WARN {c['WARN']}  INFO {c['INFO']}   "
           f"fingerprint {inst.content_fingerprint()}")
        for f in sorted(findings, key=lambda f: LEVEL_ORDER[f.level])[:args.show]:
            row = f" row {f.source_row}" if f.source_row else ""
            _p(f"    {f.level:5s} {f.rule}  {f.where}{row}  {f.message}")
        if len(findings) > args.show:
            _p(f"    … {len(findings) - args.show} more, see the findings file")
        worst = max(worst, 2 if v == "blocked" else 0)
    for p in write_all(ex, b, by_dom, args.out):
        _p(f"  wrote {p}")
    return worst


def cmd_bulk(args) -> int:
    files = sorted(glob.glob(os.path.join(args.dir, "*.xlsx")))
    files = [f for f in files if not os.path.basename(f).startswith("~$")]
    manifest, tally, seen = [], {}, {}
    for f in files:
        try:
            ex, b = read(f, sources=args.sources, version=args.version,
                         domains=args.domains)
        except Exception as exc:                       # noqa: BLE001
            manifest.append({"file": os.path.basename(f), "outcome": "error",
                             "error": str(exc)})
            tally["error"] = tally.get("error", 0) + 1
            continue
        if not ex.instructions() and not b.sheets.get("water"):
            manifest.append({"file": os.path.basename(f),
                             "outcome": "not_this_family",
                             "note": "no Water Data / Sanitation Data sheet"})
            tally["not_this_family"] = tally.get("not_this_family", 0) + 1
            _p(f"{os.path.basename(f)[:44]:46s} {'--':4s} {'not_this_family':16s}")
            continue
        by_dom = validate_extract(ex, b)
        entry = {"file": os.path.basename(f), "iso3": ex.iso3,
                 "country": ex.country, "language": ex.language, "domains": {}}
        outcome = "clean"
        for inst in ex.instructions():
            findings = by_dom[inst.domain]
            v = verdict(findings)
            if not ex.iso3:
                v = "needs_identity"
            elif (ex.iso3, inst.domain) in seen:
                v = "collision"
            else:
                seen[(ex.iso3, inst.domain)] = os.path.basename(f)
            inst.status = "draft" if v not in ("blocked", "rejected") else "rejected"
            entry["domains"][inst.domain] = {
                "outcome": v, "counts": summarise(findings),
                "sources": len(inst.sources), "rows": len(inst.rows),
                "vintage": inst.vintage,
                "fingerprint": inst.content_fingerprint()}
            tally[v] = tally.get(v, 0) + 1
            if v != "clean":
                outcome = v if outcome == "clean" else outcome
            _p(f"{os.path.basename(f)[:36]:38s} {ex.iso3 or '???':4s} "
               f"{inst.domain:11s} {v:16s} {len(inst.sources):3d} src "
               f"{len(inst.rows):4d} rows")
        entry["outcome"] = outcome
        entry["artifacts"] = write_all(ex, b, by_dom, args.out)
        manifest.append(entry)
    os.makedirs(args.out, exist_ok=True)
    mpath = os.path.join(args.out, "wash_batch_manifest.json")
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
        prog="gmd_wash_concordance",
        description="JMP country workbook -> GMD System 9 country WASH "
                    "instruction.")
    ap.add_argument("--version-info", action="version",
                    version=f"gmd_wash_concordance {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, with_out=True):
        p.add_argument("--iso3", default=None, help="override the country code")
        p.add_argument("--sources", default="microdata",
                       help="microdata (default) | survey | census | admin | "
                            "all, or a comma-separated combination")
        p.add_argument("--domains", default="both",
                       help="both (default) | water | sanitation")
        if with_out:
            p.add_argument("--out", default="out", help="output directory")
            p.add_argument("--version", default="v1.0")

    p = sub.add_parser("inspect", help="what bound where, then stop")
    p.add_argument("file")
    common(p, with_out=False)
    p.set_defaults(fn=cmd_inspect)

    p = sub.add_parser("sources", help="list the data sources in the workbook")
    p.add_argument("file")
    p.add_argument("--iso3", default=None)
    p.set_defaults(fn=cmd_sources)

    p = sub.add_parser("derive", help="the GMD canonical variables this "
                       "country's categories can support, and the code that makes them")
    p.add_argument("file")
    p.add_argument("--domain", choices=["water", "sanitation"], default="water")
    p.add_argument("--sources", default="microdata")
    p.add_argument("--stata", action="store_true")
    p.add_argument("--iso3", default=None)
    p.add_argument("--country", default=None)
    p.add_argument("--version", default=None)
    p.set_defaults(fn=cmd_derive)

    p = sub.add_parser("extract", help="one workbook -> the five artefacts")
    p.add_argument("file")
    p.add_argument("--country", default=None)
    p.add_argument("--show", type=int, default=12,
                   help="how many findings to print")
    common(p)
    p.set_defaults(fn=cmd_extract)

    p = sub.add_parser("bulk", help="a directory of workbooks")
    p.add_argument("dir")
    common(p)
    p.set_defaults(fn=cmd_bulk)

    p = sub.add_parser("chain", help="classification -> subgroup -> facility "
                                     "type, printed")
    p.add_argument("file")
    p.add_argument("--domain", default="water",
                   help="water (default) | sanitation | both")
    p.add_argument("--used", action="store_true",
                   help="only subgroups this country actually used")
    p.add_argument("--iso3", default=None)
    p.add_argument("--sources", default="microdata")
    p.set_defaults(fn=cmd_chain)

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
    return ap


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
