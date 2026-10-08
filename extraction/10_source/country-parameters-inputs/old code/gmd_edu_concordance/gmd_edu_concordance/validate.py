"""
gmd_edu_concordance.validate
============================
Seventeen rules, E-00 … E-16.  Every finding carries a rule id, a level and
the source row that produced it.

BLOCK  the version cannot be published.
WARN   publishable, but the warning must be acknowledged in writing at approval.
INFO   recorded, no action.

The rule that earns its keep is E-03.  A UIS mapping documents one school year;
treating it as the latest era leaves every cohort before it uncovered, and the
temptation is to let those cohorts fall through to the only era there is.  That
is the single most common way a country concordance goes quietly wrong -- a
2023 survey scoring a seventy-year-old against the 2023 curriculum -- so the
gap is declared, loudly, rather than defaulted.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from .schema import (
    Finding, GMD_EDUC_ATTAINMENT, GMD_EDUC_LEVELS, ISCED_LEVELS, Instruction,
    value_of,
)


def _f(rule, level, message, where="", row=None):
    return Finding(rule=rule, level=level, message=message, where=where,
                   source_row=row)


def validate(inst: Instruction, binding=None) -> List[Finding]:
    out: List[Finding] = []
    rows = inst.rows

    # -- E-00  summary -----------------------------------------------------
    out.append(_f("E-00", "INFO",
                  f"{len(rows)} programme(s) read from sheet "
                  f"{inst.source.sheet!r} header row {inst.source.header_row}; "
                  f"structure {inst.structure.get('cycle') or '?'}; "
                  f"grades {inst.structure.get('ladder_grades') or '-'}; "
                  f"school year reference {inst.source.reference_year}"))

    # -- E-01  identity ----------------------------------------------------
    if not inst.iso3 or len(inst.iso3) != 3:
        out.append(_f("E-01", "BLOCK",
                      "the country could not be determined from the banner or "
                      "the filename; a mis-attributed concordance is not caught "
                      "downstream", where="country"))

    # -- E-02  binding -----------------------------------------------------
    if binding is not None:
        for p in binding.problems:
            out.append(_f("E-02", "BLOCK", p, where="binding"))
        for f in binding.unbound:
            out.append(_f("E-02", "WARN",
                          f"column {f!r} did not bind; add the real header "
                          f"string to the profile YAML", where="binding"))
    if not rows:
        out.append(_f("E-02", "BLOCK", "no programme rows were read",
                      where="rows"))
        return out

    # -- E-03  cohort coverage --------------------------------------------
    cov = inst.coverage or {}
    if cov.get("gap_before"):
        out.append(_f("E-03", "WARN",
                      f"this version covers cohorts who left school from "
                      f"{cov['gap_before']} onwards. Earlier cohorts have no "
                      f"era and MUST NOT be defaulted into this one: they are "
                      f"an escalation (ED-01), not a fallback",
                      where="eras"))
    else:
        out.append(_f("E-03", "BLOCK",
                      "no era window could be placed: the school-year "
                      "reference is missing", where="eras"))

    # -- E-04  eras must not overlap ---------------------------------------
    spans = sorted((value_of(e.from_year), value_of(e.to_year), e.id)
                   for e in inst.eras)
    for (a_from, a_to, a_id), (b_from, b_to, b_id) in zip(spans, spans[1:]):
        if b_from <= a_to:
            out.append(_f("E-04", "BLOCK",
                          f"eras {a_id} and {b_id} overlap "
                          f"({a_from}-{a_to} / {b_from}-{b_to})", where="eras"))

    # -- E-05 / E-06  the two numbers the grade ladder is built from -------
    for r in rows:
        if not r.entrance_age:
            out.append(_f("E-05", "WARN",
                          f"'{r.programme}' has no theoretical entrance age; "
                          f"its place on the grade ladder cannot be derived",
                          where=f"rows.{r.programme_id}", row=r.source_row))
        if not r.duration_years:
            out.append(_f("E-06", "WARN",
                          f"'{r.programme}' has no theoretical duration; the "
                          f"number of grades and years in the level is unknown",
                          where=f"rows.{r.programme_id}", row=r.source_row))

    # -- E-07  ranges stay ranges ------------------------------------------
    for r in rows:
        d = r.duration_years
        if d and d["range"]:
            out.append(_f("E-07", "WARN",
                          f"'{r.programme}' lasts {d['raw']} years, so its "
                          f"grade range and cumulative years are ranges too "
                          f"({value_of(r.grades)} / "
                          f"{value_of(r.years_at_completion)}); the resolver "
                          f"needs a rule for the ambiguous years",
                          where=f"rows.{r.programme_id}", row=r.source_row))

    # -- E-08  the grade ladder needs an origin ----------------------------
    if not inst.structure.get("grade_origin"):
        out.append(_f("E-08", "BLOCK",
                      "no ISCED 1 programme with a theoretical entrance age; "
                      "grade 1 cannot be placed and no grade can be derived",
                      where="rows"))

    # -- E-09  more than one programme claims a grade ----------------------
    for step in inst.ladder:
        if step.alternatives:
            out.append(_f("E-09", "WARN",
                          f"grade {step.grade} is claimed by "
                          f"{len(step.alternatives) + 1} programmes "
                          f"({step.programme}; "
                          f"{'; '.join(step.alternatives)}); the general track "
                          f"is taken as the main path and the others are "
                          f"listed as alternatives",
                          where=f"ladder.{step.grade}"))

    # -- E-10  holes in the ladder -----------------------------------------
    gs = [s.grade for s in inst.ladder]
    holes = [g for g in range(min(gs), max(gs) + 1) if g not in gs] if gs else []
    if holes:
        out.append(_f("E-10", "BLOCK",
                      f"the grade ladder has hole(s) at "
                      f"{', '.join(map(str, holes))}; a pupil in that grade "
                      f"resolves to nothing", where="ladder"))

    # -- E-11  entrance ages must be monotone with the level ---------------
    by_level: Dict[str, List] = defaultdict(list)
    for r in rows:
        if r.entrance_age:
            by_level[r.isced].append(r)
    lows = {lvl: min(r.entrance_age["min"] for r in rs)
            for lvl, rs in by_level.items()}
    for a, b in zip("012345678", "12345678"):
        if a in lows and b in lows and lows[b] < lows[a]:
            out.append(_f("E-11", "WARN",
                          f"ISCED {b} starts at age {lows[b]:g}, earlier than "
                          f"ISCED {a} at {lows[a]:g}; check the entrance-age "
                          f"column", where="rows"))

    # -- E-12  duplicate programme names -----------------------------------
    seen: Dict[str, List[int]] = defaultdict(list)
    for r in rows:
        seen[r.programme.strip().lower()].append(r.programme_id or 0)
    for name, ids in seen.items():
        if len(ids) > 1 and name:
            out.append(_f("E-12", "INFO",
                          f"programme name {name!r} appears {len(ids)} times "
                          f"(ids {', '.join(map(str, ids))})", where="rows"))

    # -- E-13 / E-14  controlled lists -------------------------------------
    for r in rows:
        if r.isced not in ISCED_LEVELS:
            out.append(_f("E-13", "BLOCK",
                          f"'{r.isced}' is not an ISCED 2011 level",
                          where=f"rows.{r.programme_id}", row=r.source_row))
        if r.gmd not in GMD_EDUC_LEVELS:
            out.append(_f("E-14", "BLOCK",
                          f"'{r.gmd}' is not in the GMD education controlled "
                          f"list", where=f"rows.{r.programme_id}",
                          row=r.source_row))

    # -- E-15  a level with no completion point ----------------------------
    for r in rows:
        if r.isced in ("1", "2", "3") and r.completion == "na" and not r.complete_at:
            out.append(_f("E-15", "WARN",
                          f"'{r.programme}' records neither a completion "
                          f"status nor a qualification; completed cannot be "
                          f"told from in progress",
                          where=f"rows.{r.programme_id}", row=r.source_row))

    # -- E-16  the 3-digit codes must agree with the level -----------------
    for r in rows:
        for fld, code in (("isced_p", r.isced_p), ("isced_a", r.isced_a)):
            if code and code[0] != r.isced and fld == "isced_p":
                out.append(_f("E-16", "WARN",
                              f"'{r.programme}' is ISCED {r.isced} but its "
                              f"ISCED-P code is {code}; the first digit should "
                              f"be the level",
                              where=f"rows.{r.programme_id}", row=r.source_row))

    # -- E-19  attainment, not just level ---------------------------------
    for r in rows:
        for fld in ("attainment_on_completion", "attainment_in_progress"):
            v = getattr(r, fld, "")
            if v and v not in GMD_EDUC_ATTAINMENT:
                out.append(_f("E-19", "BLOCK",
                              f"'{v}' is not in the GMD attainment controlled "
                              f"list", where=f"rows.{r.programme_id}",
                              row=r.source_row))
    unsettled = [r for r in rows
                 if r.gmd not in ("none", "pre_primary", "other")
                 and getattr(r, "attainment_on_completion", "") == r.gmd]
    if unsettled:
        out.append(_f("E-19", "WARN",
                      f"{len(unsettled)} programme(s) leave completion "
                      f"unsettled (e.g. '{unsettled[0].programme}'), so a "
                      f"cohort in them resolves to the bare level and cannot "
                      f"be told complete from incomplete", where="rows"))
    for step in inst.ladder:
        if not step.attainment:
            out.append(_f("E-19", "WARN",
                          f"grade {step.grade} carries no attainment value",
                          where=f"ladder.{step.grade}"))

    # -- E-20  the country's own wording, and what is missing --------------
    needs = [r for r in rows if getattr(r, "needs_translation", False)]
    if needs:
        std = [r for r in needs if r.programme_en_source == "isced_standard"]
        gone = [r for r in needs if r.programme_en_source == "absent"]
        if std:
            out.append(_f("E-20", "WARN",
                          f"{len(std)} programme(s) have no English name in "
                          f"the workbook (e.g. "
                          f"'{std[0].programme_national}'); the ISCED level's "
                          f"standard label stands in, marked as such, and a "
                          f"real translation is still needed",
                          where="language"))
        if gone:
            out.append(_f("E-20", "BLOCK",
                          f"{len(gone)} programme(s) have no name in any "
                          f"language", where="language"))

    # -- E-18  programmes that are not on the ladder ----------------------
    off = [r for r in rows if getattr(r, "off_ladder", False)]
    if off:
        # Name them all. This is the list a reviewer reads first, and one
        # example does not let them tell a correct exclusion from a mistake.
        shown = off[:8]
        names = "; ".join(
            f"ISCED {r.isced} '{r.programme or r.programme_national}' "
            f"(entrance age {(r.entrance_age or {}).get('raw')!r})"
            for r in shown)
        more = f"; and {len(off) - len(shown)} more" if len(off) > len(shown) else ""
        out.append(_f("E-18", "WARN",
                      f"{len(off)} programme(s) are not rungs on the grade "
                      f"ladder — they admit across an age band, enter well "
                      f"after the level below finishes, or are named as an "
                      f"adult or second-chance route: {names}{more}. They "
                      f"carry no grade, and a cohort in one resolves by "
                      f"qualification rather than by grade. Each row's "
                      f"'grades' evidence gives its own reason",
                      where="rows"))

    # -- E-17  the country's own wording ----------------------------------
    lang = inst.language or {}
    cols = lang.get("national_columns") or {}
    if not cols:
        out.append(_f("E-17", "WARN",
                      "no national-language column bound; the country's own "
                      "wording for its programmes is not being kept, and "
                      "nothing downstream can recover it",
                      where="language"))
    else:
        for name, meta in cols.items():
            if meta.get("rows_with_text", 0) == 0:
                out.append(_f("E-17", "WARN",
                              f"column {name!r} ({meta.get('header')!r}) is "
                              f"present but empty for every programme; the "
                              f"country's own wording was not supplied",
                              where="language"))
        n = lang.get("rows_with_national_text", 0)
        if n:
            nl = lang.get("national_language")
            named = (", ".join(nl["value"]) if isinstance(nl, dict) else
                     "language not stated")
            out.append(_f("E-17", "INFO",
                          f"{n} programme(s) carry the country's own wording "
                          f"({named}); "
                          f"{lang.get('non_latin_or_accented_values', 0)} "
                          f"value(s) use non-ASCII characters",
                          where="language"))

    # -- reform signals in the workbook's own notes ------------------------
    for s in inst.structure.get("reform_signals", []):
        out.append(_f("E-03", "WARN",
                      f"a note on '{s['programme']}' names {s['year']} in "
                      f"reform language ({s['phrase']!r}); this workbook may "
                      f"not be the only era this country needs",
                      where="eras", row=s.get("source_row")))

    for u in inst.unmapped:
        out.append(_f("E-13", "WARN", f"{u.reason}: '{u.value}'",
                      where=u.where, row=u.source_row))
    return out


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
