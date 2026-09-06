"""
gmd_edu_concordance.derive
==========================
Grades, years and the era window.

The UIS mapping workbook records programmes, not grades.  It does record two
numbers per programme that are enough to place it on the national ladder:

    theoretical entrance age    when a pupil normally starts the programme
    theoretical duration        how many years the programme runs

Take the ISCED 1 programme's entrance age as the origin of the ladder.  Then
for any programme::

    years_before        = entrance_age - primary_entrance_age
    years_at_completion = years_before + duration
    grades              = years_before + 1  …  years_at_completion

so the duration column is exactly what says **how many grades, and how many
years, each level holds**.  Nigeria's Primary (age 6, six years) is grades
1-6; Junior secondary (age 12, three years) is 7-9; Senior secondary (age 15,
three years) is 10-12.  Viet Nam's five-year primary gives 1-5, lower
secondary 6-9, upper secondary 10-12.

Two things this deliberately does not do
----------------------------------------
It does not collapse a range.  A programme of "3-4" years produces a grade
range with a range end, and the finding says so, because a country whose
programme lasts three or four years does not have one answer.

It does not put a grade on a tertiary programme.  ISCED 5-8 carry years within
the level and a cumulative year count, which is what ``educ_years`` needs, but
a "grade" there would be an invention.

Everything here is emitted as inferred, with the arithmetic as its evidence.
"""
from __future__ import annotations

# An entrance age wider than this is a band, not a starting age: the programme
# admits adults across a range and does not sit at one rung of the ladder.
BAND_YEARS = 3

# How far above the level below a programme may start before it stops being a
# continuation of the ladder and becomes an in-service or second-career entry.
LADDER_TOLERANCE = 3

# Some routes are named for what they are.  A "basic cycle for adults" and a
# genuine extra rung such as Nigeria's IJMB A-level course can be numerically
# identical -- both are ISCED 3 entered the year the level below finishes --
# and only the name separates them.  The workbooks say so in their own
# language, so the name is read rather than guessed at.
ADULT_ROUTE_MARKERS = (
    "adult", "adults", "adulto", "adultos", "adulte", "adultes", "adulti",
    "second chance", "second-chance", "segunda oportunidad",
    "seconde chance", "segunda chance",
    "educacion de jovenes y adultos", "jeunes et adultes",
    "взросл", "вечерн",
)

from collections import defaultdict
from typing import Any, Dict, List, Optional

from . import parse as P
from .schema import (
    Era, EduRow, Instruction, ISCED_LEVELS, LadderStep, OPEN_ERA_END,
    attainment_of, inferred, value_of,
)


def _mid(d) -> Optional[float]:
    return None if not d else (d["min"] + d["max"]) / 2.0


def _primary_entrance(rows: List[EduRow]) -> Optional[Dict[str, Any]]:
    """The origin of the grade ladder: the ISCED 1 programme's entrance age."""
    cands = [r for r in rows if r.isced == "1" and r.entrance_age]
    if not cands:
        return None
    cands.sort(key=lambda r: (r.entrance_age["min"], r.programme_id or 0))
    r = cands[0]
    return {"age": r.entrance_age["min"], "programme": r.programme,
            "row": r.source_row}


def grades(inst: Instruction, grade_levels: List[str]) -> None:
    """Fill ``years_in_level``, ``grades``, ``years_before`` and
    ``years_at_completion`` on every row."""
    origin = _primary_entrance(inst.rows)
    inst.structure["grade_origin"] = origin
    for r in inst.rows:
        dur = r.duration_years
        if dur:
            r.years_in_level = inferred(
                P.fmt_range(dur["min"], dur["max"]), 1.0 if not dur["range"] else 0.6,
                f"theoretical duration column: {dur['raw']!r}")
        if origin is None or not r.entrance_age or not dur:
            # A programme missing either number cannot be placed. Say so as a
            # value rather than leaving the field empty, so a reader never has
            # to tell "not applicable" from "nobody filled this in".
            why = []
            if origin is None:
                why.append("no ISCED 1 programme fixes the start of the ladder")
            if not r.entrance_age:
                why.append("no theoretical entrance age")
            if not dur:
                why.append("no theoretical duration")
            r.grades = inferred("-", 1.0, "; ".join(why))
            continue
        before_lo = r.entrance_age["min"] - origin["age"]
        before_hi = r.entrance_age["max"] - origin["age"]
        at_lo = before_lo + dur["min"]
        at_hi = before_hi + dur["max"]
        ev = (f"theoretical entrance age {r.entrance_age['raw']!r} minus the "
              f"ISCED 1 entrance age {origin['age']:g} "
              f"({origin['programme']}), plus theoretical duration "
              f"{dur['raw']!r}")
        conf = 0.85 if not (r.entrance_age["range"] or dur["range"]) else 0.55
        r.years_before = inferred(P.fmt_range(before_lo, before_hi), conf, ev)
        r.years_at_completion = inferred(P.fmt_range(at_lo, at_hi), conf, ev)
        band = r.entrance_age["max"] - r.entrance_age["min"]
        if band > BAND_YEARS:
            r.grades = inferred(
                "-", 1.0,
                f"theoretical entrance age {r.entrance_age['raw']!r} is a band "
                f"of {band:g} years, so this programme admits across an age "
                f"range rather than sitting at one rung of the ladder "
                f"(adult or second-chance education)")
            r.off_ladder = True
        elif r.isced in grade_levels and before_lo >= 0 and at_hi >= 1:
            g_lo = int(before_lo) + 1
            g_hi = int(round(at_hi))
            if g_hi < g_lo:
                g_hi = g_lo
            r.grade_from = inferred(g_lo, conf, ev)
            r.grade_to = inferred(g_hi, conf, ev)
            r.grades = inferred(P.fmt_range(g_lo, g_hi), conf, ev)
        else:
            why = ("tertiary programmes carry years within the level, not "
                   "grades on the national ladder"
                   if r.isced not in grade_levels else
                   "the programme starts before the ISCED 1 entrance age")
            r.grades = inferred("-", 1.0, why)


def _adult_marker(r: EduRow) -> Optional[str]:
    """The adult/second-chance word a programme name carries, if any."""
    hay = " ".join(x for x in (r.programme, r.programme_national) if x)
    hay = P.norm(hay)
    for m in ADULT_ROUTE_MARKERS:
        if m in hay:
            return m
    return None


def consistency(inst: Instruction, grade_levels: List[str],
                tol: int = LADDER_TOLERANCE) -> None:
    """Drop programmes whose entry sits far above the level below them.

    A single starting age can be perfectly precise and still not be a rung.
    The Central African Republic's *Formation des conseillers pédagogiques* is
    ISCED 4 and admits at 30, because it is an in-service qualification that
    requires professional experience. Read as a ladder position it produced
    grades 25-26 and a ladder running to grade 26.

    The check is against the ladder rather than against an absolute age: you
    enter a level after finishing the one below, so a programme starting more
    than ``tol`` years after the level below finishes is entering from
    somewhere other than the ladder. Nigeria's IJMB A-level course starts three
    years after lower secondary ends and stays; a programme starting eleven
    years later does not.
    """
    def yb(r):
        v = value_of(r.years_before)
        try:
            return float(str(v).split("-")[0])
        except (TypeError, ValueError):
            return None

    def yac(r):
        v = value_of(r.years_at_completion)
        try:
            return float(str(v).split("-")[-1])
        except (TypeError, ValueError):
            return None

    # Named adult and second-chance routes leave first: they are parallel
    # provision, never a rung, and letting one stay would also let it raise
    # the baseline for the level above it.
    for r in inst.rows:
        if r.off_ladder or r.isced not in grade_levels:
            continue
        marker = _adult_marker(r)
        if not marker:
            continue
        r.off_ladder = True
        r.grade_from = None
        r.grade_to = None
        r.grades = inferred(
            "-", 0.9,
            f"the programme name {(r.programme_national or r.programme)!r} "
            f"marks it as an adult or second-chance route ({marker!r}), which "
            f"is provision parallel to the ladder rather than a grade on it")

    # Levels are settled from the bottom up. A programme that has just been
    # ruled off the ladder must not go on to raise the baseline for the level
    # above it -- Argentina's *Adults primary education* finishes at year 12
    # of schooling, and if that counted, adult lower secondary entering at 12
    # would look perfectly normal and keep grades 13-14.
    levels = sorted({r.isced for r in inst.rows if r.isced in grade_levels})
    for lvl in levels:
        prior = [yac(r) for r in inst.rows
                 if r.isced in grade_levels and r.isced < lvl
                 and not r.off_ladder and yac(r) is not None]
        baseline = max(prior) if prior else None

        here = [r for r in inst.rows
                if r.isced == lvl and not r.off_ladder and yb(r) is not None]
        if baseline is None:
            starts = [yb(r) for r in here]
            baseline = min(starts) if starts else None
        if baseline is None:
            continue

        for r in here:
            start = yb(r)
            if start <= baseline + tol:
                continue
            r.off_ladder = True
            r.grade_from = None
            r.grade_to = None
            r.grades = inferred(
                "-", 0.9,
                f"entry at year {start:g} of schooling is {start - baseline:g} "
                f"years after ISCED {lvl} would normally be entered "
                f"({baseline:g}); this is an adult, in-service or "
                f"second-chance route rather than a rung on the ladder")


def attainment(inst: Instruction) -> None:
    """What each programme confers, finished and unfinished.

    The workbook's completion column says whether finishing the programme
    completes the ISCED level -- *Full completion*, *Partial completion*,
    *Insufficient for completion*. That is the difference between
    ``upper_secondary_complete`` and ``upper_secondary_incomplete``, and it is
    the distinction a survey's highest-education variable actually carries.

    A programme whose completion column is empty leaves it unsettled, and the
    bare level is returned rather than a guess at *complete*. Rule E-15 already
    names those.
    """
    for r in inst.rows:
        finishes = {"full": True, "partial": False, "none": False}.get(
            r.completion)
        if finishes is None and r.completion == "na":
            # a level with no completion column may still be settled by its
            # attainment code: ISCED-A repeats the level when the level is
            # completed and drops below it when it is not
            if r.isced_a and r.isced and r.isced_a[0] == r.isced:
                finishes = True
            elif r.isced_a and r.isced and r.isced_a[0] < r.isced:
                finishes = False
        r.attainment_on_completion = attainment_of(r.gmd, finishes)
        r.attainment_in_progress = attainment_of(
            r.gmd, False if finishes is not None else None)


def ladder(inst: Instruction) -> None:
    """One entry per grade: what level it belongs to, what it maps to, and
    whether finishing it completes the level.  This is the table a cohort is
    resolved against."""
    by_grade: Dict[int, List[EduRow]] = defaultdict(list)
    for r in inst.rows:
        if not r.grade_from or not r.grade_to:
            continue
        for g in range(int(r.grade_from["value"]), int(r.grade_to["value"]) + 1):
            by_grade[g].append(r)
    steps: List[LadderStep] = []
    for g in sorted(by_grade):
        # the general track wins the grade; vocational alternatives are listed
        cands = sorted(by_grade[g], key=lambda r: (
            0 if r.orientation in ("general", "na", "pre_primary", "eced") else 1,
            r.isced, r.programme_id or 0))
        main = cands[0]
        yac = main.years_at_completion["value"] if main.years_at_completion else None
        last = g == int(main.grade_to["value"])
        steps.append(LadderStep(
            grade=g, isced=main.isced, isced_label=main.isced_label,
            gmd=main.gmd, programme=main.programme,
            completes_level=last,
            years_at_completion=(float(str(yac).split("-")[0]) if yac else None),
            attainment=(main.attainment_on_completion if last
                        else main.attainment_in_progress),
            attainment_if_left_here=(main.attainment_on_completion if last
                                     else main.attainment_in_progress),
            isced_a=main.isced_a,
            alternatives=[c.programme for c in cands[1:]],
        ))
    inst.ladder = steps
    inst.structure["ladder_grades"] = (
        f"{steps[0].grade}-{steps[-1].grade}" if steps else "")
    inst.structure["cycle"] = _cycle_string(inst)


def _cycle_string(inst: Instruction) -> str:
    """`6-3-3` for Nigeria, `5-4-3` for Viet Nam -- the shorthand a focal point
    recognises at a glance."""
    parts = []
    for lvl in ("1", "2", "3"):
        cands = [r for r in inst.rows
                 if r.isced == lvl and r.orientation in ("general", "na")
                 and r.duration_years and not getattr(r, "off_ladder", False)]
        if not cands:
            cands = [r for r in inst.rows if r.isced == lvl
                     and r.duration_years
                     and not getattr(r, "off_ladder", False)]
        if not cands:
            continue
        # the main track is the longest general programme at the level, not
        # whichever happens to be listed first
        d = max(cands, key=lambda r: r.duration_years["max"]).duration_years
        parts.append(P.fmt_range(d["min"], d["max"]))
    return "-".join(parts)


def era(inst: Instruction) -> None:
    """One era, and it is the latest one.

    A single mapping workbook documents the structure in force in one school
    year.  That structure is treated as the era running to the open end.  Its
    start is inferred from the reference year, and the cohorts before it are
    recorded as a declared gap -- never defaulted into this era, which is what
    rule E-03 exists to stop.

    If the workbook's own notes name earlier years in a way that reads like a
    reform, those are surfaced as signals, so a focal point can say whether a
    second era is needed rather than discovering it from a data anomaly.
    """
    ref = inst.source.reference_year
    signals = []
    for r in inst.rows:
        for blob in (r.notes, r.entrance_requirement, r.diploma):
            for s in P.reform_signals(blob):
                s["source_row"] = r.source_row
                s["programme"] = r.programme
                signals.append(s)
    earlier = sorted({s["year"] for s in signals if ref and s["year"] < ref})
    inst.structure["reform_signals"] = signals

    if ref is None:
        return
    start = ref
    conf = 0.5
    ev = (f"'School Year reference: {ref}' is the only vintage this workbook "
          f"documents; the workbook is taken as the latest era, so its window "
          f"runs to the open end")
    if earlier:
        start = earlier[-1]
        conf = 0.4
        ev += (f". A note in the workbook names {earlier[-1]} in reform "
               f"language, so the era may begin there rather than at {ref}")
    inst.eras = [Era(
        id=1,
        label=(inst.structure.get("cycle") or "ISCED 2011 mapping"),
        from_year=inferred(start, conf, ev),
        to_year=inferred(OPEN_ERA_END, 0.9,
                         "the latest era runs to the open end of the cohort "
                         "range"),
        reference_year=ref,
        latest=True,
        description=(f"National structure as mapped for the {ref} school year"
                     f"{' (' + inst.structure['cycle'] + ')' if inst.structure.get('cycle') else ''}."),
    )]
    inst.coverage = {
        "era_from": start,
        "era_to": OPEN_ERA_END,
        "gap_before": start,
        "note": (f"cohorts who left school before {start} have no era in this "
                 f"version; an earlier UIS mapping or a focal-point decision "
                 f"is required before they can be resolved"),
        "reform_signals": len(signals),
    }


def english(inst: Instruction, profile: dict) -> None:
    """Keep the country's own wording; supply English only where it exists.

    Some workbooks leave the English column empty for some or all rows. A
    programme name is not translatable from here -- there is no dictionary for
    *Trung cấp chuyên nghiệp* the way there is for a JMP phrase -- so nothing
    is invented. What is supplied instead is the **ISCED level's own English
    label**, clearly marked as a standard label rather than a translation, and
    the row is flagged as needing one.
    """
    for r in inst.rows:
        if r.programme and r.programme.strip():
            r.programme_en_source = "workbook"
            continue
        if r.programme_national:
            r.programme = ISCED_LEVELS.get(r.isced, "").strip()
            r.programme_en_source = "isced_standard"
            r.needs_translation = True
        else:
            r.programme_en_source = "absent"
            r.needs_translation = True
    n = sum(1 for r in inst.rows if r.needs_translation)
    inst.language["rows_needing_translation"] = n
    inst.language["english_from_workbook"] = sum(
        1 for r in inst.rows if r.programme_en_source == "workbook")


def run(inst: Instruction, profile: dict) -> None:
    english(inst, profile)
    grades(inst, profile["value_maps"]["grade_levels"])
    consistency(inst, profile["value_maps"]["grade_levels"])
    attainment(inst)
    ladder(inst)
    era(inst)
