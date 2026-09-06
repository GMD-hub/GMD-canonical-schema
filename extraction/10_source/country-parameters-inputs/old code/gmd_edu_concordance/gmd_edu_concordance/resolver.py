"""
gmd_edu_concordance.resolver
============================
Runs a candidate instruction, so a focal point never has to read YAML to know
whether it is right.

    grade  4 / left 2018  ->  primary          in progress   era 1 (6-3-3)
    grade  6 / left 2018  ->  primary          completed     Primary school leaving examination
    grade  4 / left 1975  ->  UNRESOLVED       1975 is before the era this version covers

Note which year drives the answer.  The era is selected from the year the
person was last in school, not from the survey year.  A 2023 survey
interviewing a seventy-year-old must use the ladder that existed when that
person was at school, and this package refuses to pretend it has one.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from .schema import Instruction, value_of


def resolve(inst: Instruction, grade: Optional[int] = None,
            year_last_in_school: Optional[int] = None,
            isced: Optional[str] = None) -> Dict[str, Any]:
    out: Dict[str, Any] = {"country": inst.iso3, "grade": grade,
                           "year_last_in_school": year_last_in_school}
    era = None
    if year_last_in_school is not None:
        for e in inst.eras:
            if value_of(e.from_year) <= year_last_in_school <= value_of(e.to_year):
                era = e
                break
        if era is None:
            lo = min((value_of(e.from_year) for e in inst.eras), default=None)
            out.update({
                "resolved": False,
                "why": (f"{year_last_in_school} is before {lo}, the earliest "
                        f"year this version covers. This is escalation ED-01, "
                        f"not a fallback to the latest era."),
            })
            return out
        out["era"] = {"id": era.id, "label": era.label}
    elif inst.eras:
        era = inst.eras[0]
        out["era"] = {"id": era.id, "label": era.label,
                      "assumed": "no year supplied; the latest era was used"}

    if isced is not None:
        rows = [r for r in inst.rows if r.isced == str(isced)]
        if not rows:
            out.update({"resolved": False,
                        "why": f"no programme at ISCED {isced}"})
            return out
        r = rows[0]
        out.update({"resolved": True, "programme": r.programme,
                    "isced": r.isced, "isced_label": r.isced_label,
                    "gmd": r.gmd, "complete": r.completion == "full",
                    "years_at_completion": value_of(r.years_at_completion),
                    "why": f"ISCED {isced} maps to {r.gmd}"})
        return out

    if grade is None:
        out.update({"resolved": False, "why": "no grade and no ISCED level"})
        return out

    step = next((s for s in inst.ladder if s.grade == grade), None)
    if step is None:
        gs = [s.grade for s in inst.ladder]
        out.update({
            "resolved": False,
            "why": (f"grade {grade} is outside the ladder "
                    f"{min(gs) if gs else '?'}-{max(gs) if gs else '?'} this "
                    f"version derives"),
        })
        return out
    out.update({
        "resolved": True,
        "programme": step.programme,
        "isced": step.isced,
        "isced_label": step.isced_label,
        "gmd": step.gmd,
        "attainment": step.attainment,
        "isced_a": step.isced_a,
        "complete": step.completes_level,
        "years_at_completion": step.years_at_completion,
        "alternatives": step.alternatives,
        "why": (f"grade {grade} sits in {step.programme}; "
                + ("it is the last grade of the level, so the level is "
                   "completed" if step.completes_level else
                   "the level is not finished at this grade")
                + f", which is {step.attainment or 'unsettled'}"),
    })
    return out


def probe(inst: Instruction, grades: Optional[List[int]] = None,
          years: Optional[List[int]] = None) -> List[Dict[str, Any]]:
    """A default probe set: the last grade of every level, one grade inside
    every level, and one cohort before the era starts."""
    out = []
    ref = inst.source.reference_year
    ys = years or [y for y in (ref, (ref - 30) if ref else None) if y]
    if grades is None:
        grades = []
        for s in inst.ladder:
            if s.completes_level or s.grade == 1:
                grades.append(s.grade)
            elif s.grade % 3 == 0:
                grades.append(s.grade)
        grades = sorted(set(grades))
    for y in ys:
        for g in grades:
            out.append(resolve(inst, grade=g, year_last_in_school=y))
    return out


def render(rows: List[Dict[str, Any]]) -> str:
    lines = []
    for r in rows:
        head = (f"grade {str(r.get('grade')):>3s} / left "
                f"{r.get('year_last_in_school')}")
        if not r.get("resolved"):
            lines.append(f"{head}  ->  {'UNRESOLVED':16s} {r['why']}")
        else:
            lines.append(f"{head}  ->  {(r.get('attainment') or r['gmd']):28s} "
                         f"{r['programme'][:38]}")
    return "\n".join(lines)
