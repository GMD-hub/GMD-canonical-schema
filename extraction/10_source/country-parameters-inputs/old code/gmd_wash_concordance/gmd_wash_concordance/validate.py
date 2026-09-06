"""
gmd_wash_concordance.validate
=============================
Fifteen rules, W-00 … W-14.  Every finding carries a rule id, a level and the
source row that produced it, so a file can be returned to its sender with the
ids attached before any reviewer time is spent on it.

BLOCK  the version cannot be published.
WARN   the version can be published, but the warning must be acknowledged in
       writing at approval.
INFO   recorded, no action.

The rules that matter most are the ones that keep the country from deciding
something JMP decides.  Improvement status is copied from the master list and
W-02 checks that it still is; a ladder rung is never assigned at all, because
a rung depends on variables no source-mapping row can see.
"""
from __future__ import annotations

import re
from collections import defaultdict
from typing import Dict, List

from . import master as M
from .schema import (
    Finding, GMD_SANITATION_TYPES, GMD_WATER_SOURCES, Instruction,
    SAN_LADDER, WATER_LADDER,
)

MASTERS = {"water": M.water, "sanitation": M.sanitation}
TARGETS = {"water": set(GMD_WATER_SOURCES),
           "sanitation": set(GMD_SANITATION_TYPES)}

def _n(s) -> str:
    return " ".join(str(s or "").lower().split())


SERVICE_LEVEL_HINTS = [
    "shared", "sharing", "time to", "minutes", "on premises", "availability",
    "sufficient", "quality", "microbial", "fluoride", "arsenic", "continuous",
]


def _f(rule, level, message, where="", row=None):
    return Finding(rule=rule, level=level, message=message, where=where,
                   source_row=row)


def validate(inst: Instruction, binding=None) -> List[Finding]:
    """Run the rules over **one** domain instruction."""
    out: List[Finding] = []
    dom = inst.domain
    tree = MASTERS[dom]()
    targets = TARGETS[dom]
    rows = inst.rows

    # -- W-00  extraction summary -----------------------------------------
    out.append(_f("W-00", "INFO",
                  f"{dom}: {len(inst.sources)} source(s) selected "
                  f"({inst.selection.get('sources')}), {len(rows)} rows, "
                  f"vintage {inst.vintage.get('from')}-"
                  f"{inst.vintage.get('to')}, language "
                  f"{inst.language or 'unstated'}"))

    # -- W-01  identity ----------------------------------------------------
    if not inst.iso3 or len(inst.iso3) != 3:
        out.append(_f("W-01", "BLOCK",
                      "the country could not be determined from the workbook "
                      "or the filename; a mis-attributed concordance is not "
                      "caught downstream", where="country"))
    if not inst.country:
        out.append(_f("W-01", "WARN", "no country name found", where="country"))

    # -- W-02  improvement is never asserted by the country ----------------
    for r in rows:
        if r.improved_from != "jmp_master":
            out.append(_f("W-02", "BLOCK",
                          f"row '{r.label}' asserts improvement status itself; "
                          f"improvement is a property of the JMP class",
                          where=r.code, row=r.source_row))
            continue
        node = tree.by_id(r.jmp_id)
        if node is not None and r.improved != node.improved:
            out.append(_f("W-02", "BLOCK",
                          f"row '{r.label}' carries improved={r.improved} but "
                          f"JMP class '{r.jmp}' is improved={node.improved}",
                          where=r.code, row=r.source_row))
        if getattr(r, "rung", None):
            out.append(_f("W-02", "BLOCK",
                          f"row '{r.label}' assigns a ladder rung; the rung is "
                          f"derived downstream from several variables",
                          where=r.code, row=r.source_row))

    # The classification block is part of the instruction, so a hand edit
    # there has to be caught by the same rule -- otherwise the easiest place
    # to quietly flip an improvement flag is the one place nothing looks.
    for c in inst.classifications:
        node = tree.by_id(c.get("jmp_id"))
        if node is None:
            out.append(_f("W-02", "BLOCK",
                          f"classification '{c.get('classification')}' is not "
                          f"a JMP master category", where="classifications"))
            continue
        if c.get("improved") != node.improved:
            out.append(_f("W-02", "BLOCK",
                          f"classification '{c.get('classification')}' carries "
                          f"improved={c.get('improved')} but the JMP master "
                          f"says improved={node.improved}",
                          where="classifications"))
        for sg in c.get("subgroups") or []:
            sn = tree.by_id(sg.get("jmp_id"))
            if sn is None:
                out.append(_f("W-02", "BLOCK",
                              f"subgroup '{sg.get('label')}' is not a JMP "
                              f"master category", where="classifications"))
            elif sg.get("improved") != sn.improved:
                out.append(_f("W-02", "BLOCK",
                              f"subgroup '{sg.get('label')}' carries "
                              f"improved={sg.get('improved')} but the JMP "
                              f"master says improved={sn.improved}",
                              where="classifications"))

    # -- W-03  one national label, more than one JMP class, in one source --
    for sc in inst.per_source:
        byl: Dict[str, set] = defaultdict(set)
        for r in sc.rows:
            byl[r.label.strip().lower()].add(r.jmp)
        for lbl, classes in byl.items():
            if len(classes) > 1:
                out.append(_f("W-03", "WARN",
                              f"[{sc.source.code}] national category '{lbl}' "
                              f"maps to {len(classes)} JMP classes "
                              f"({'; '.join(sorted(classes))}); a splitting "
                              f"rule is required", where=sc.source.code))

    # -- W-04  the workbook's tree is the tree this package pins -----------
    if binding is not None:
        for misfit in (binding.tree_alignment or {}).get(dom, [])[:20]:
            out.append(_f("W-04", "BLOCK",
                          f"JMP category tree does not match the pinned master "
                          f"at position {misfit['ordinal']}: expected "
                          f"'{misfit['expected']}', found '{misfit['found']}' "
                          f"({misfit['reason']})", where=dom,
                          row=misfit.get("row")))
        for p in (binding.problems or []):
            out.append(_f("W-04", "BLOCK", p, where="binding"))

    # -- W-05  no row may claim a class outside the master -----------------
    for r in rows:
        if tree.by_id(r.jmp_id) is None:
            out.append(_f("W-05", "BLOCK", f"'{r.jmp}' is not a JMP master "
                          f"category", where=r.code, row=r.source_row))

    # -- W-06  protection status the source leaves open --------------------
    for r in rows:
        if r.improved is None and not r.spans:
            out.append(_f("W-06", "WARN",
                          f"'{r.label}' lands on '{r.jmp}', where JMP does not "
                          f"settle improvement status", where=r.code,
                          row=r.source_row))

    # -- W-07  service-level attributes are not facility types -------------
    #
    # A label such as "Septic tank (shared and public)" carries two things: a
    # facility type and a sharing attribute.  That is fine *when the workbook
    # put it on a shared node*, because the attribute is then recorded
    # separately and the facility type is unchanged.  It is a finding only
    # when the attribute has nowhere to go.
    n_absorbed = 0
    for r in rows:
        low = r.label.lower()
        if not (any(h in low for h in SERVICE_LEVEL_HINTS) and r.gmd):
            continue
        if r.shared is not None:
            n_absorbed += 1
            continue
        out.append(_f("W-07", "WARN",
                      f"'{r.label}' reads as a service-level attribute but "
                      f"carries the facility target '{r.gmd}' and no attribute "
                      f"to hold it; sharing, collection time and water quality "
                      f"belong to the ladder, not to the source mapping",
                      where=r.code, row=r.source_row))
    if n_absorbed:
        out.append(_f("W-07", "INFO",
                      f"{n_absorbed} row(s) name a service-level attribute in "
                      f"their label and land on a node that records it "
                      f"separately; the facility type is unaffected"))

    # -- W-08  sharing recorded as an attribute ----------------------------
    n_shared = sum(1 for r in rows if r.shared is not None)
    if n_shared:
        out.append(_f("W-08", "INFO",
                      f"{n_shared} row(s) carry sharing as an attribute; "
                      f"sharing never changes the facility type"))

    # -- W-09  every facility row needs a target, or a splitting rule ------
    for r in rows:
        if r.gmd:
            if r.gmd not in targets:
                out.append(_f("W-09", "BLOCK",
                              f"'{r.gmd}' is not in the {dom} controlled list",
                              where=r.code, row=r.source_row))
            continue
        node = tree.by_id(r.jmp_id)
        if node is not None and node.structural:
            out.append(_f("W-09", "BLOCK",
                          f"'{r.label}' sits on the structural row "
                          f"'{node.label}', which is not a facility type",
                          where=r.code, row=r.source_row))
        elif r.spans:
            out.append(_f("W-09", "WARN",
                          f"'{r.label}' spans {len(r.spans)} GMD targets "
                          f"({', '.join(r.spans)}); a splitting rule is "
                          f"required before it can be harmonized",
                          where=r.code, row=r.source_row))
        else:
            out.append(_f("W-09", "BLOCK",
                          f"'{r.label}' has no GMD target and spans none",
                          where=r.code, row=r.source_row))

    # -- W-10 / W-11  vintage: what a later instrument lost or gained ------
    order = [s.code for s in inst.sources]
    if len(order) >= 2:
        first, last = order[0], order[-1]
        gained = [r for r in rows if last in r.observed_in
                  and first not in r.observed_in]
        lost = [r for r in rows if first in r.observed_in
                and last not in r.observed_in]
        if gained:
            out.append(_f("W-10", "WARN",
                          f"{len(gained)} {dom} categor(ies) present in {last} "
                          f"and absent from {first} (e.g. {gained[0].label}); "
                          f"a comparability note is required", where=dom))
        if lost:
            out.append(_f("W-11", "WARN",
                          f"{len(lost)} {dom} categor(ies) present in {first} "
                          f"and absent from {last} (e.g. {lost[0].label}); "
                          f"a comparability note is required", where=dom))

    # -- W-12 / W-13  the ladder is JMP's, not the country's ---------------
    expect = (["Safely managed", "Basic", "Limited", "Unimproved",
               "Surface water"] if dom == "water" else
              ["Safely managed", "Basic", "Limited", "Unimproved",
               "Open defecation"])
    rule = "W-12" if dom == "water" else "W-13"
    if [r["rung"] for r in inst.ladder] != expect:
        out.append(_f(rule, "BLOCK", f"the {dom} ladder has been altered",
                      where="ladder"))

    # -- W-14  packaged or delivered water needs a secondary source --------
    if dom == "water":
        pkg = [r for r in rows if r.gmd in ("bottled", "tanker")]
        if pkg:
            out.append(_f("W-14", "WARN",
                          f"{len(pkg)} packaged or delivered water "
                          f"categor(ies) present (e.g. {pkg[0].label}); the "
                          f"rung cannot be derived without a secondary-source "
                          f"question", where="water"))

    # -- W-15  the classification -> facility type chain must close --------
    declared = {_n(f["name"]) for f in inst.facility_types}
    for r in rows:
        for ft in r.rolls_up_to:
            if _n(ft) not in declared:
                out.append(_f("W-15", "BLOCK",
                              f"'{r.label}' rolls up to facility type '{ft}', "
                              f"which this workbook does not declare",
                              where=r.code, row=r.source_row))
    for f in inst.facility_types:
        if not f["in_workbook"]:
            out.append(_f("W-15", "WARN",
                          f"facility type '{f['name']}' is in the pinned "
                          f"master but not in this workbook's Facility type "
                          f"estimates block", where="facility_types"))
    orphan = [r for r in rows
              if r.improved is True and not r.rolls_up_to]
    for r in orphan[:10]:
        out.append(_f("W-15", "WARN",
                      f"'{r.label}' is improved but feeds no facility-type "
                      f"aggregate; the chain classification -> subgroup -> "
                      f"facility type does not close", where=r.code,
                      row=r.source_row))

    # -- W-16  language ----------------------------------------------------
    if not inst.language:
        out.append(_f("W-16", "WARN",
                      "the workbook does not state its language; the national "
                      "denominations cannot be attributed to one",
                      where="language"))
    local = [r for r in rows if r.jmp_label_local
             and _n(r.jmp_label_local) != _n(r.jmp.split(">")[-1])]
    if local:
        out.append(_f("W-16", "INFO",
                      f"{len(local)} row(s) carry a JMP label in the "
                      f"workbook's own wording that differs from the pinned "
                      f"English", where="language"))

    # -- W-17  no survey-level data in the instruction ---------------------
    #
    # The benchmark exists precisely so the numbers have somewhere to live.
    # This asserts they did not leak back.
    STRUCTURAL_INTS = {"depth", "first_seen", "last_seen", "source_row"}
    leaked = []
    for r in rows:
        for k, v in r.__dict__.items():
            if isinstance(v, bool):
                continue              # a flag, not a measurement
            if isinstance(v, float) or (isinstance(v, int)
                                        and k not in STRUCTURAL_INTS):
                leaked.append(f"{r.code}.{k}")
    if leaked:
        out.append(_f("W-17", "BLOCK",
                      f"the instruction carries survey-level data in "
                      f"{len(leaked)} field(s) ({', '.join(leaked[:5])}); "
                      f"estimates belong in the benchmark artefact",
                      where="rows"))
    bench = (inst.benchmark or {}).get("summary") or {}
    if bench:
        out.append(_f("W-17", "INFO",
                      f"benchmark: {bench.get('categories_with_estimates', 0)} "
                      f"published estimate(s) across "
                      f"{bench.get('sources_with_estimates', 0)} of "
                      f"{bench.get('sources', 0)} source(s)"
                      + (", plus the country ladder"
                         if bench.get("has_country_ladder") else ""),
                      where="benchmark"))
    elif inst.sources:
        out.append(_f("W-17", "WARN",
                      "no published estimates were captured, so there is "
                      "nothing to review the mapping against",
                      where="benchmark"))

    # -- anything the reader could not place -------------------------------
    for u in inst.unmapped:
        out.append(_f("W-09", "WARN", f"[{u.source}] {u.reason}: '{u.value}'",
                      where=u.where, row=u.source_row))

    return out


def validate_extract(ex, binding=None) -> Dict[str, List[Finding]]:
    """Run the rules over every domain in an extract, keyed by domain."""
    return {i.domain: validate(i, binding) for i in ex.instructions()}


def verdict(findings: List[Finding]) -> str:
    if any(f.level == "BLOCK" for f in findings):
        return "blocked"
    if any(f.level == "WARN" for f in findings):
        return "awaiting_review"
    return "clean"


def summarise(findings: List[Finding]) -> Dict[str, int]:
    c = {"BLOCK": 0, "WARN": 0, "INFO": 0}
    for f in findings:
        c[f.level] = c.get(f.level, 0) + 1
    return c
