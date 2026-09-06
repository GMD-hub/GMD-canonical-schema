"""GMD canonical education variables, derived from the ladder.

The architecture is explicit that agents map *atomic* variables only and that
derived variables are computed in code (Architecture Overview, "Atomic
mapping").  For education the atomic result of this package is the ladder:
grade -> ISCED level -> attainment.  Everything GMD actually publishes --
``educat7``, ``educat5``, ``educat4`` and ``educy`` -- is a deterministic
function of that, and this module is that function.

Definitions are taken verbatim from *GMD 2.0 List of Variables* (25 Nov 2019),
sheet "GMD 1.5":

  educat7  1 no education / 2 primary incomplete / 3 primary complete /
           4 secondary incomplete / 5 secondary complete /
           6 higher than secondary but not university /
           7 university incomplete or complete
  educat5  1 no education / 2 primary incomplete /
           3 primary complete but secondary incomplete / 4 secondary complete /
           5 some tertiary/post-secondary
  educat4  1 no education / 2 primary (complete or incomplete) /
           3 secondary (complete or incomplete) / 4 tertiary (complete or incomplete)
  educy    years of completed education

Two GMD conventions matter and are easy to get wrong.  GMD *secondary* is
"everything from the end of primary to before tertiary", so ISCED 2 and ISCED 3
are one category, not two.  And ISCED 4 and ISCED 5 are "higher than secondary
but not university": short-cycle tertiary is category 6, not 7.

Not every workbook supports every variable.  A ladder that never distinguishes
lower from upper secondary cannot produce ``educat7``; one with no theoretical
durations cannot produce ``educy``.  Rather than emit a plausible-looking
number, this module resolves what the country can actually support and says
what is missing.  A country that can only reach ``educat4`` is a normal
outcome, not a failure.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

# --------------------------------------------------------------------------
# value labels, so the generated code and the viewer never drift apart
# --------------------------------------------------------------------------

EDUCAT7 = {
    1: "No education",
    2: "Primary incomplete",
    3: "Primary complete",
    4: "Secondary incomplete",
    5: "Secondary complete",
    6: "Higher than secondary but not university",
    7: "University incomplete or complete",
}
EDUCAT5 = {
    1: "No education",
    2: "Primary incomplete",
    3: "Primary complete but secondary incomplete",
    4: "Secondary complete",
    5: "Some tertiary/post-secondary",
}
EDUCAT4 = {
    1: "No education",
    2: "Primary (complete or incomplete)",
    3: "Secondary (complete or incomplete)",
    4: "Tertiary (complete or incomplete)",
}

# educat7 -> educat5 -> educat4.  The collapses are fixed by the GMD
# definitions above; they are not a country choice.
SEVEN_TO_FIVE = {1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 6: 5, 7: 5}
SEVEN_TO_FOUR = {1: 1, 2: 2, 3: 2, 4: 3, 5: 3, 6: 4, 7: 4}

# educat5 -> educat4 is lossy at one point and it matters.  educat5 category 3
# is "primary complete but secondary incomplete", which merges two educat4
# answers: someone who finished primary and stopped is educat4 = 2, someone who
# started secondary is educat4 = 3.  There is no way back once the merge has
# happened, so this map exists to be *read*, never to be used as a derivation
# path.  Where educat7 is available educat4 comes from it; where it is not,
# educat4 comes from the ladder directly, which still knows which side of the
# primary boundary each grade sits on.
FIVE_TO_FOUR = {1: 1, 2: 2, 3: None, 4: 3, 5: 4}
FIVE_TO_FOUR_LOSSY = {3: "merges 'primary complete' (educat4=2) with 'secondary "
                         "incomplete' (educat4=3); derive educat4 from the ladder instead"}

# The GMD level an ISCED level belongs to.  ISCED 2 and 3 are both "secondary"
# because GMD secondary runs from the end of primary to the start of tertiary.
ISCED_TO_GMD_BAND = {
    "0": "pre_primary",
    "1": "primary",
    "2": "secondary",
    "3": "secondary",
    "4": "post_secondary",
    "5": "post_secondary",   # short-cycle tertiary is educat7 = 6
    "6": "university",
    "7": "university",
    "8": "university",
    "9": "other",
}


def educat7_of(isced: str, complete: Optional[bool]) -> Optional[int]:
    """ISCED level plus "did they finish it" -> educat7.

    ``complete is None`` means the source does not settle completion.  That is
    resolvable only where the two answers fall in the same educat7 category,
    which is true for ISCED 4/5 and 6/7/8 and false for 1, 2 and 3 -- so those
    return ``None`` rather than guessing.
    """
    band = ISCED_TO_GMD_BAND.get(str(isced or "").strip()[:1] or "9", "other")
    if band in ("pre_primary",):
        return 1
    if band == "primary":
        if complete is None:
            return None
        return 3 if complete else 2
    if band == "secondary":
        if complete is None:
            return None
        # only finishing ISCED 3 completes GMD secondary; finishing ISCED 2
        # leaves the person inside secondary, which is "secondary incomplete"
        if str(isced).strip()[:1] == "2":
            return 4
        return 5 if complete else 4
    if band == "post_secondary":
        return 6
    if band == "university":
        return 7
    return None


def _years_at_level_end(step: Dict[str, Any]) -> Optional[float]:
    v = step.get("years_at_completion")
    if isinstance(v, dict):
        v = v.get("value")
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def cumulative_years(ladder: List[Dict[str, Any]]) -> Dict[int, float]:
    """Years of schooling accumulated by the end of each grade.

    The ladder carries ``years_at_completion`` for the *level*, not for the
    grade: every rung of a five-year primary cycle says 5.  Years at grade g
    are therefore the level's total minus the grades still to run in it, which
    needs the last grade of each contiguous run of the same programme.
    """
    steps = sorted([s for s in ladder if s.get("grade") is not None],
                   key=lambda s: s["grade"])
    out: Dict[int, float] = {}
    i = 0
    while i < len(steps):
        key = (str(steps[i].get("isced") or "")[:1], steps[i].get("programme", ""))
        j = i
        while j + 1 < len(steps) and \
              (str(steps[j + 1].get("isced") or "")[:1],
               steps[j + 1].get("programme", "")) == key:
            j += 1
        end = steps[j]
        total = _years_at_level_end(end)
        if total is not None:
            last_grade = end["grade"]
            for k in range(i, j + 1):
                g = steps[k]["grade"]
                out[g] = round(total - (last_grade - g), 2)
        i = j + 1
    return out


def educy_of(step: Dict[str, Any]) -> Optional[float]:
    """Backwards-compatible single-step reading: the level total."""
    return _years_at_level_end(step)


# --------------------------------------------------------------------------
# capability: what this country's ladder can actually support
# --------------------------------------------------------------------------

def capability(ladder: List[Dict[str, Any]], rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Decide which canonical variables this concordance can produce.

    Returns a dict per variable with ``ok`` and, when it is not ok, ``why``.
    The finest variable the country supports is reported as ``finest``.
    """
    isced_seen = {str(s.get("isced") or "")[:1] for s in ladder if s.get("isced")}
    isced_seen |= {str(r.get("isced") or "")[:1] for r in rows if r.get("isced")}
    isced_seen.discard("")

    has_primary = "1" in isced_seen
    has_lower = "2" in isced_seen
    has_upper = "3" in isced_seen
    has_post = bool(isced_seen & {"4", "5"})
    has_tert = bool(isced_seen & {"6", "7", "8"})

    completes = [bool(s.get("completes_level")) for s in ladder]
    has_completion = any(completes)
    has_years = bool(cumulative_years(ladder))

    out: Dict[str, Any] = {}

    # educat4 needs only the band, which any ladder with a primary rung has
    if has_primary and (has_lower or has_upper or has_tert or has_post):
        out["educat4"] = {"ok": True}
    elif has_primary:
        out["educat4"] = {"ok": True, "note":
            "only primary rungs are present; anyone above primary will be missing, not miscoded"}
    else:
        out["educat4"] = {"ok": False, "why":
            "the ladder has no ISCED 1 rung, so primary cannot be separated from anything else"}

    # educat5 additionally needs "did they finish primary" and "did they finish secondary"
    if not out["educat4"]["ok"]:
        out["educat5"] = {"ok": False, "why": "educat4 could not be produced"}
    elif not has_completion:
        out["educat5"] = {"ok": False, "why":
            "no rung on the ladder is marked as completing its level, so complete cannot be "
            "separated from incomplete"}
    elif not has_upper:
        out["educat5"] = {"ok": False, "why":
            "the workbook has no ISCED 3 programme, so 'secondary complete' has no rung to attach to"}
    else:
        out["educat5"] = {"ok": True}

    # educat7 additionally needs primary complete separated from secondary
    # incomplete, which needs both an ISCED 1 completion rung and ISCED 2 or 3
    if not out["educat5"]["ok"]:
        out["educat7"] = {"ok": False, "why": "educat5 could not be produced"}
    elif not (has_lower or has_upper):
        out["educat7"] = {"ok": False, "why":
            "no lower or upper secondary programme, so 'primary complete' and "
            "'secondary incomplete' cannot be told apart"}
    elif not has_post and not has_tert:
        out["educat7"] = {"ok": True, "note":
            "no post-secondary or tertiary programme in the workbook; categories 6 and 7 "
            "will never be produced for this country"}
    else:
        out["educat7"] = {"ok": True}

    if has_years:
        out["educy"] = {"ok": True}
    else:
        out["educy"] = {"ok": False, "why":
            "the workbook gives no theoretical duration, so cumulative years cannot be computed"}

    finest = "educat7" if out["educat7"]["ok"] else \
             "educat5" if out["educat5"]["ok"] else \
             "educat4" if out["educat4"]["ok"] else None
    out["finest"] = finest
    out["isced_levels"] = sorted(isced_seen)
    return out


# --------------------------------------------------------------------------
# the crosswalk: one row per ladder grade, carrying every canonical value
# --------------------------------------------------------------------------

def crosswalk(ladder: List[Dict[str, Any]], cap: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Grade -> educat7/5/4/educy, with the reason each value was chosen.

    One rule is applied on top of the raw lookup: educat7 may not fall as the
    grade rises.  Where a workbook documents two tracks over the same grades --
    a four-year general upper secondary beside a part-time one, say -- the
    ladder takes one as the main path, and the other can make a later grade
    look like a lower attainment than an earlier one.  More schooling cannot
    mean less education, so the value is carried forward and the carry is
    recorded rather than hidden.
    """
    cum = cumulative_years(ladder)
    out: List[Dict[str, Any]] = []
    prev7 = 0
    for s in sorted([s for s in ladder if s.get("grade") is not None],
                    key=lambda s: s["grade"]):
        isced = str(s.get("isced") or "")[:1]
        complete = bool(s.get("completes_level"))
        raw7 = educat7_of(isced, complete)
        if raw7 is None:
            raw7 = educat7_of(isced, False)
        carried = False
        e7 = raw7
        if e7 is not None and e7 < prev7:
            e7, carried = prev7, True
        if e7 is not None:
            prev7 = e7
        e5 = SEVEN_TO_FIVE.get(e7) if e7 else None
        # educat4 always from educat7, never through educat5
        e4 = SEVEN_TO_FOUR.get(e7) if e7 else None
        yrs = cum.get(s["grade"])
        band = ISCED_TO_GMD_BAND.get(isced, "other")
        why = (
            f"grade {s.get('grade')} sits in ISCED {isced} ({band}); the level is "
            f"{'finished' if complete else 'not finished'} at this grade"
        )
        if carried:
            why += (f"; the raw lookup gave {raw7} but an earlier grade already "
                    f"reached {e7}, so the higher value is carried forward")
        out.append({
            "grade": s.get("grade"),
            "isced": isced,
            "isced_a": s.get("isced_a", ""),
            "programme": s.get("programme", ""),
            "completes_level": complete,
            "attainment": s.get("attainment_if_left_here") or s.get("attainment", ""),
            "alternatives": s.get("alternatives") or [],
            "educat7": e7 if cap["educat7"]["ok"] else None,
            "educat5": e5 if cap["educat5"]["ok"] else None,
            "educat4": e4 if cap["educat4"]["ok"] else None,
            "educy": yrs if cap["educy"]["ok"] else None,
            "educat7_raw": raw7,
            "carried_forward": carried,
            "educat7_label": EDUCAT7.get(e7 or 0, ""),
            "why": why,
        })
    return out


# --------------------------------------------------------------------------
# generated Stata
# --------------------------------------------------------------------------

def stata(iso3: str, country: str, version: str, ladder: List[Dict[str, Any]],
          cap: Dict[str, Any], xw: List[Dict[str, Any]],
          era_from: Optional[int] = None, era_to: Optional[int] = None,
          grade_var: str = "educ_grade", attend_var: str = "atschool",
          level_var: str = "educ_level") -> str:
    """The derivation, as code a harmonizer can read and run.

    The generated file takes two survey inputs -- the highest grade the person
    reached and whether they are currently attending -- and produces the GMD
    canonical variables.  It is deliberately a long list of explicit
    ``replace`` statements rather than a clever loop: this file is read by
    reviewers far more often than it is run.
    """
    L: List[str] = []
    a = L.append
    a("*" + "=" * 74)
    a(f"* {country} ({iso3}) - GMD canonical education variables")
    a(f"* Generated from the national concordance {iso3}_edu_{version}")
    if era_from:
        a(f"* Era: cohorts who left school {era_from}"
          + (f"-{era_to}" if era_to else " onwards"))
    a("*")
    a("* Atomic input : the national grade the person completed, and whether")
    a("*                they are still attending.")
    a("* Derived here : educat7, educat5, educat4, educy.")
    a("*")
    a("* Do not edit. Change the concordance and regenerate; an edit here is a")
    a("* rule that exists in one survey and nowhere else.")
    a("*" + "=" * 74)
    a("")
    a("* ---- the grade actually completed -------------------------------------")
    a("* A person still in grade g has completed g-1. A person who has left has")
    a("* completed the grade they reached.")
    a("tempvar gcomp")
    a(f"gen `gcomp' = {grade_var}")
    a(f"replace `gcomp' = {grade_var} - 1 if {attend_var} == 1")
    a("replace `gcomp' = 0 if `gcomp' < 0")
    a("")

    if cap["educat7"]["ok"]:
        a("* ---- educat7 ----------------------------------------------------------")
        a("gen byte educat7 = .")
        a("replace educat7 = 1 if `gcomp' == 0")
        for r in xw:
            if r["educat7"] is None:
                continue
            note = f"ISCED {r['isced']} - {r['programme'][:40]}"
            if r.get("carried_forward"):
                note += f" [carried from grade below; raw {r['educat7_raw']}]"
            a(f"replace educat7 = {r['educat7']} if `gcomp' == {r['grade']}   // {note}")
        a('label define educat7 ' + ' '.join(
            f'{k} "{v}"' for k, v in EDUCAT7.items()) + ', replace')
        a("label values educat7 educat7")
        a('label var educat7 "Highest level of education completed (7 categories)"')
        a("")
    else:
        a("* ---- educat7 ----------------------------------------------------------")
        a(f"* NOT PRODUCED: {cap['educat7'].get('why','')}")
        a("gen byte educat7 = .")
        a('label var educat7 "Highest level of education completed (7 categories)"')
        a("")

    if cap["educat5"]["ok"]:
        a("* ---- educat5 ----------------------------------------------------------")
        if cap["educat7"]["ok"]:
            a("* collapsed from educat7; the collapse is the GMD definition, not a choice")
            a("gen byte educat5 = .")
            for k, v in SEVEN_TO_FIVE.items():
                a(f"replace educat5 = {v} if educat7 == {k}")
        else:
            a("gen byte educat5 = .")
            for r in xw:
                if r["educat5"] is None:
                    continue
                a(f"replace educat5 = {r['educat5']} if `gcomp' == {r['grade']}")
        a('label define educat5 ' + ' '.join(
            f'{k} "{v}"' for k, v in EDUCAT5.items()) + ', replace')
        a("label values educat5 educat5")
        a('label var educat5 "Highest level of education completed (5 categories)"')
        a("")
    else:
        a("* ---- educat5 ----------------------------------------------------------")
        a(f"* NOT PRODUCED: {cap['educat5'].get('why','')}")
        a("gen byte educat5 = .")
        a("")

    a("* ---- educat4 ----------------------------------------------------------")
    if cap["educat4"]["ok"]:
        a("gen byte educat4 = .")
        if cap["educat7"]["ok"]:
            for k, v in SEVEN_TO_FOUR.items():
                a(f"replace educat4 = {v} if educat7 == {k}")
        else:
            # deliberately from the ladder, not from educat5: the educat5
            # collapse loses the primary/secondary boundary at category 3
            a("* from the ladder, not from educat5 - educat5 category 3 merges")
            a("* 'primary complete' and 'secondary incomplete', which are"
              " different educat4 answers")
            for r in xw:
                if r["educat4"] is None:
                    continue
                a(f"replace educat4 = {r['educat4']} if `gcomp' == {r['grade']}")
        a('label define educat4 ' + ' '.join(
            f'{k} "{v}"' for k, v in EDUCAT4.items()) + ', replace')
        a("label values educat4 educat4")
        a('label var educat4 "Highest level of education completed (4 categories)"')
    else:
        a(f"* NOT PRODUCED: {cap['educat4'].get('why','')}")
        a("gen byte educat4 = .")
    a("")

    a("* ---- educy ------------------------------------------------------------")
    if cap["educy"]["ok"]:
        a("* cumulative theoretical years at the last grade completed")
        a("gen educy = .")
        a("replace educy = 0 if `gcomp' == 0")
        for r in xw:
            if r["educy"] is None:
                continue
            y = int(r["educy"]) if float(r["educy"]).is_integer() else r["educy"]
            a(f"replace educy = {y} if `gcomp' == {r['grade']}")
        a('label var educy "Years of completed education"')
    else:
        a(f"* NOT PRODUCED: {cap['educy'].get('why','')}")
        a("gen educy = .")
    a("")
    a("* ---- the checks that make the four agree ------------------------------")
    a("assert inrange(educat7,1,7) | missing(educat7)")
    a("assert inrange(educat5,1,5) | missing(educat5)")
    a("assert inrange(educat4,1,4) | missing(educat4)")
    if cap["educat7"]["ok"] and cap["educat5"]["ok"]:
        a("assert educat5 == cond(inlist(educat7,3,4),3, "
          "cond(inlist(educat7,6,7),5, cond(educat7==5,4,educat7))) if !missing(educat7)")
    a("")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# the block that goes into the country instruction and the view bundle
# --------------------------------------------------------------------------

def build(inst_ladder: List[Dict[str, Any]], inst_rows: List[Dict[str, Any]],
          iso3: str, country: str, version: str,
          era_from: Optional[int] = None, era_to: Optional[int] = None) -> Dict[str, Any]:
    cap = capability(inst_ladder, inst_rows)
    xw = crosswalk(inst_ladder, cap)
    return {
        "schema": "gmd.derivation.education",
        "frame": "GMD 2.0 List of Variables (25 Nov 2019), sheet 'GMD 1.5'",
        "atomic": ["isced_a", "grade completed", "atschool"],
        "derived": ["educat7", "educat5", "educat4", "educy"],
        "capability": cap,
        "labels": {"educat7": EDUCAT7, "educat5": EDUCAT5, "educat4": EDUCAT4},
        "collapse": {"educat7_to_educat5": SEVEN_TO_FIVE,
                     "educat7_to_educat4": SEVEN_TO_FOUR,
                     "educat5_to_educat4": FIVE_TO_FOUR,
                     "educat5_to_educat4_lossy": FIVE_TO_FOUR_LOSSY},
        "crosswalk": xw,
        "stata": stata(iso3, country, version, inst_ladder, cap, xw, era_from, era_to),
    }
