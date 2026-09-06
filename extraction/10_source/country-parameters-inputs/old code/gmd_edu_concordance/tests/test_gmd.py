"""The GMD canonical education derivation.

These tests are about the *definitions*, not the plumbing.  Every one of them
would fail if someone quietly changed what "secondary complete" means.
"""
import json
import os

import pytest

from gmd_edu_concordance import gmd


# --------------------------------------------------------------------------
# the definitions themselves
# --------------------------------------------------------------------------

def test_isced_2_and_3_are_both_gmd_secondary():
    """GMD secondary runs from the end of primary to the start of tertiary.

    Finishing ISCED 2 is therefore *not* secondary complete -- it leaves the
    person inside secondary.  This is the single easiest thing to get wrong.
    """
    assert gmd.educat7_of("2", True) == 4      # finished lower secondary
    assert gmd.educat7_of("3", True) == 5      # finished upper secondary
    assert gmd.educat7_of("2", False) == 4
    assert gmd.educat7_of("3", False) == 4


def test_short_cycle_tertiary_is_not_university():
    """"Higher than secondary but not university" is category 6, and ISCED 4
    and 5 both live there."""
    assert gmd.educat7_of("4", True) == 6
    assert gmd.educat7_of("5", True) == 6
    assert gmd.educat7_of("6", False) == 7
    assert gmd.educat7_of("8", True) == 7


def test_primary_completion_is_never_guessed():
    """Where the source does not settle completion and the answer changes the
    category, the derivation returns nothing rather than picking one."""
    assert gmd.educat7_of("1", None) is None
    assert gmd.educat7_of("2", None) is None
    # ...but ISCED 4/5 and 6/7/8 land in one category either way, so they resolve
    assert gmd.educat7_of("5", None) == 6
    assert gmd.educat7_of("7", None) == 7


@pytest.mark.parametrize("seven,five,four", [
    (1, 1, 1), (2, 2, 2), (3, 3, 2), (4, 3, 3), (5, 4, 3), (6, 5, 4), (7, 5, 4)])
def test_collapses_match_the_gmd_definitions(seven, five, four):
    assert gmd.SEVEN_TO_FIVE[seven] == five
    assert gmd.SEVEN_TO_FOUR[seven] == four


def test_educat5_to_educat4_is_lossy_exactly_once_and_says_so():
    """educat5 category 3 merges "primary complete" with "secondary
    incomplete", which are different educat4 answers.  Everywhere else the two
    routes to educat4 agree; at category 3 the map refuses to answer rather
    than picking a side, and the derivation goes via the ladder instead."""
    for s in range(1, 8):
        five = gmd.SEVEN_TO_FIVE[s]
        direct = gmd.SEVEN_TO_FOUR[s]
        via = gmd.FIVE_TO_FOUR[five]
        if via is None:
            assert five == 3
        else:
            assert direct == via, f"educat7={s} disagrees between the two routes"
    assert 3 in gmd.FIVE_TO_FOUR_LOSSY


def test_educat4_never_comes_through_educat5_in_generated_code():
    lad = _ladder([(g, "1" if g <= 6 else "3", "P" if g <= 6 else "S",
                    g in (6, 12), 6 if g <= 6 else 12) for g in range(1, 13)])
    cap = gmd.capability(lad, [])
    cap["educat7"] = {"ok": False, "why": "test"}
    cap["educat5"] = {"ok": True}
    code = gmd.stata("XXX", "Test", "v1.0", lad, cap, gmd.crosswalk(lad, cap))
    assert "if educat5 ==" not in code
    assert "educat5 category 3 merges" in code


# --------------------------------------------------------------------------
# years
# --------------------------------------------------------------------------

def _ladder(spec):
    """spec: list of (grade, isced, programme, completes, level_total_years)"""
    return [{"grade": g, "isced": i, "programme": p, "completes_level": c,
             "years_at_completion": y, "isced_a": "", "alternatives": []}
            for g, i, p, c, y in spec]


def test_educy_counts_grades_not_levels():
    """The ladder carries the *level's* total years on every rung of it.  Years
    at grade 3 of a six-year primary cycle are 3, not 6."""
    lad = _ladder([(g, "1", "Primary", g == 6, 6) for g in range(1, 7)])
    cum = gmd.cumulative_years(lad)
    assert [cum[g] for g in range(1, 7)] == [1, 2, 3, 4, 5, 6]


def test_educy_carries_across_levels():
    lad = _ladder([(g, "1", "Primary", g == 6, 6) for g in range(1, 7)] +
                  [(g, "2", "Lower", g == 9, 9) for g in range(7, 10)])
    cum = gmd.cumulative_years(lad)
    assert cum[7] == 7 and cum[9] == 9


def test_educy_absent_when_the_workbook_gives_no_duration():
    lad = _ladder([(g, "1", "Primary", g == 6, None) for g in range(1, 7)])
    cap = gmd.capability(lad, [])
    assert cap["educy"]["ok"] is False
    assert "duration" in cap["educy"]["why"]


# --------------------------------------------------------------------------
# capability: not every country reaches educat7
# --------------------------------------------------------------------------

def test_a_ladder_with_no_completion_flags_stops_at_educat4():
    lad = _ladder([(g, "1" if g <= 6 else "3", "P" if g <= 6 else "S", False, 6 if g <= 6 else 12)
                   for g in range(1, 13)])
    cap = gmd.capability(lad, [])
    assert cap["finest"] == "educat4"
    assert cap["educat4"]["ok"] and not cap["educat5"]["ok"]
    assert "completing its level" in cap["educat5"]["why"]


def test_a_ladder_with_no_upper_secondary_stops_at_educat4():
    lad = _ladder([(g, "1" if g <= 6 else "2", "P" if g <= 6 else "L",
                    g in (6, 9), 6 if g <= 6 else 9) for g in range(1, 10)])
    cap = gmd.capability(lad, [])
    assert cap["finest"] == "educat4"
    assert "ISCED 3" in cap["educat5"]["why"]


def test_a_full_ladder_reaches_educat7():
    lad = _ladder([(g, "1" if g <= 6 else "2" if g <= 9 else "3", "P" if g <= 6 else "L" if g <= 9 else "U",
                    g in (6, 9, 12), 6 if g <= 6 else 9 if g <= 9 else 12)
                   for g in range(1, 13)] +
                  [(13, "6", "Bachelor", True, 16)])
    cap = gmd.capability(lad, [])
    assert cap["finest"] == "educat7"
    assert cap["educy"]["ok"]


def test_blocked_variables_are_not_silently_produced():
    lad = _ladder([(g, "1", "Primary", False, 6) for g in range(1, 7)])
    cap = gmd.capability(lad, [])
    xw = gmd.crosswalk(lad, cap)
    assert all(r["educat7"] is None for r in xw)
    assert all(r["educat5"] is None for r in xw)
    assert all(r["educat4"] is not None for r in xw)


# --------------------------------------------------------------------------
# monotonicity
# --------------------------------------------------------------------------

def test_educat7_never_falls_as_the_grade_rises():
    """A workbook with a part-time track running past the general one used to
    produce 'secondary complete' at grade 12 and 'secondary incomplete' at 13.
    More schooling cannot mean less education."""
    lad = _ladder([(g, "3", "General", g == 12, 12) for g in range(10, 13)] +
                  [(13, "3", "Part-time", False, 14), (14, "3", "Part-time", True, 14)])
    cap = gmd.capability(
        _ladder([(g, "1", "P", g == 6, 6) for g in range(1, 7)]) + lad, [])
    xw = gmd.crosswalk(lad, cap)
    vals = [r["educat7"] for r in xw]
    assert vals == sorted(vals)
    carried = [r for r in xw if r["carried_forward"]]
    assert carried and "carried forward" in carried[0]["why"]


# --------------------------------------------------------------------------
# generated code
# --------------------------------------------------------------------------

def test_generated_stata_declares_what_it_cannot_produce():
    lad = _ladder([(g, "1", "Primary", False, 6) for g in range(1, 7)])
    cap = gmd.capability(lad, [])
    code = gmd.stata("XXX", "Test", "v1.0", lad, cap, gmd.crosswalk(lad, cap))
    assert "NOT PRODUCED" in code
    assert "gen byte educat7 = ." in code


def test_generated_stata_labels_every_category_it_produces():
    lad = _ladder([(g, "1" if g <= 6 else "3", "P" if g <= 6 else "S",
                    g in (6, 12), 6 if g <= 6 else 12) for g in range(1, 13)])
    cap = gmd.capability(lad, [])
    code = gmd.stata("XXX", "Test", "v1.0", lad, cap, gmd.crosswalk(lad, cap))
    for k, v in gmd.EDUCAT7.items():
        assert f'{k} "{v}"' in code
    assert "assert inrange(educat7,1,7)" in code


# --------------------------------------------------------------------------
# against a real country
# --------------------------------------------------------------------------

REAL = "/mnt/user-data/uploads/gmd_ai/National concordance/ALB/ALB_edu_view.json"


@pytest.mark.skipif(not os.path.exists(REAL), reason="real Albania bundle not staged")
def test_albania_end_to_end():
    b = json.load(open(REAL, encoding="utf-8"))
    d = gmd.build(b["ladder"], b["rows"], "ALB", "Albania", "v1.0", 2024, 2035)
    assert d["capability"]["finest"] == "educat7"
    by_grade = {r["grade"]: r for r in d["crosswalk"]}
    assert by_grade[5]["educat7"] == 3      # 5-year primary, finished
    assert by_grade[9]["educat7"] == 4      # lower secondary finished is still incomplete
    assert by_grade[12]["educat7"] == 5     # upper secondary finished
    assert by_grade[12]["educy"] == 12
    assert by_grade[1]["educy"] == 1
