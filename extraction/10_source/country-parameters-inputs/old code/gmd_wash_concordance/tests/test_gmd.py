"""The GMD canonical water and sanitation derivation."""
import json
import os

import pytest

from gmd_wash_concordance import gmd


# --------------------------------------------------------------------------
# the range rule
# --------------------------------------------------------------------------

def test_improved_is_a_range_on_the_gmd_code_list():
    for c in range(1, 9):
        assert gmd.improved_of(c) == 1
    for c in range(9, 14):
        assert gmd.improved_of(c) == 0


def test_code_14_is_never_defaulted_either_way():
    """14 is the country's own call.  Returning 0 would report households as
    lacking improved water on the strength of a residual category."""
    assert gmd.improved_of(14) is None
    assert gmd.pipedwater_acc_of(14) is None
    assert gmd.toilet_acc_of(14) is None


def test_unprotected_is_never_read_as_protected():
    """"unprotected_spring" contains "protected_spring".  A regex ordered the
    wrong way round turns an unimproved source into an improved one, which is
    a household counted as having safe water when it does not."""
    assert gmd.map_water("ground_water.unprotected_spring")["code"] == 9
    assert gmd.map_water("ground_water.unprotected_well")["code"] == 10
    assert gmd.map_water("ground_water.protected_spring")["code"] == 6
    assert gmd.map_water("ground_water.protected_well")["code"] == 5
    assert gmd.improved_of(gmd.map_water("ground_water.unprotected_spring")["code"]) == 0


@pytest.mark.parametrize("node,code", [
    ("tap_water.piped_on_premises.piped_water_into_dwelling", 1),
    ("tap_water.piped_on_premises.piped_water_to_yard_plot", 2),
    ("tap_water.public_tap_standpipe", 3),
    ("ground_water.tubewell_borehole", 4),
    ("packaged_water.bottled_water", 7),
    ("rainwater", 8),
    ("delivered_water.tanker_truck", 12),
    ("surface_water", 13),
])
def test_water_nodes_land_on_the_documented_code(node, code):
    assert gmd.map_water(node)["code"] == code


@pytest.mark.parametrize("node,code", [
    ("flush_and_pour_flush.to_piped_sewer_system", 2),
    ("flush_and_pour_flush.to_septic_tank", 3),
    ("flush_and_pour_flush.to_pit", 4),
    ("flush_and_pour_flush.to_elsewhere", 9),
    ("pit_latrine.ventilated_improved_pit_latrine", 5),
    ("pit_latrine.with_slab", 6),
    ("pit_latrine.without_slab_open_pit", 10),
    ("composting_toilets", 7),
    ("bucket", 11),
    ("hanging_toilet", 12),
    ("open_defecation", 13),
])
def test_sanitation_nodes_land_on_the_documented_code(node, code):
    assert gmd.map_sanitation(node)["code"] == code


def test_a_branch_node_spans_rather_than_guessing():
    m = gmd.map_water("ground_water")
    assert m["code"] is None
    assert set(m["spans"]) == {4, 5, 6, 9, 10}
    assert "splitting rule" in m["why"]


def test_access_follows_the_source_code():
    assert gmd.pipedwater_acc_of(1) == 1     # into dwelling
    assert gmd.pipedwater_acc_of(2) == 2     # to yard
    assert gmd.pipedwater_acc_of(3) == 2     # public tap
    assert gmd.pipedwater_acc_of(4) == 0
    assert gmd.toilet_acc_of(2) == 1
    assert gmd.toilet_acc_of(9) == 2
    assert gmd.toilet_acc_of(13) == 0


# --------------------------------------------------------------------------
# capability
# --------------------------------------------------------------------------

def _rows(nodes):
    return [{"code": n.split(".")[-1], "label": n, "jmp_id": n, "jmp": n,
             "improved": None, "observed_in": [], "source_row": i}
            for i, n in enumerate(nodes)]


def test_a_country_with_no_rows_produces_nothing():
    cap = gmd.capability([], "water")
    assert cap["finest"] is None
    assert not cap["water_source"]["ok"]


def test_a_mappable_country_produces_the_three_variables():
    rows = _rows(["tap_water.piped_on_premises.piped_water_into_dwelling",
                  "ground_water.tubewell_borehole", "surface_water"])
    gmd.crosswalk(rows, "water")
    cap = gmd.capability(rows, "water")
    assert cap["finest"] == "water_source"
    assert cap["imp_wat_rec"]["ok"] and cap["pipedwater_acc"]["ok"]


def test_watertype_quest_is_declared_out_of_scope():
    """It records what the survey asked, which the country concordance cannot
    know.  Saying so is better than emitting a plausible constant."""
    rows = _rows(["rainwater"])
    gmd.crosswalk(rows, "water")
    cap = gmd.capability(rows, "water")
    assert not cap["watertype_quest"]["ok"]
    assert "survey instrument" in cap["watertype_quest"]["why"]


def test_residual_categories_are_reported_not_hidden():
    rows = _rows(["something_the_tree_does_not_have"])
    xw = gmd.crosswalk(rows, "water")
    assert xw[0]["gmd_code"] == 14
    cap = gmd.capability(rows, "water")
    assert "country ruling" in cap["imp_wat_rec"].get("note", "")


# --------------------------------------------------------------------------
# the JMP disagreement
# --------------------------------------------------------------------------

def test_delivered_water_disagreement_is_recorded_with_its_reason():
    """JMP counts tanker trucks as improved; the GMD 1.5 code list puts them in
    the unimproved range.  Neither side is a bug and the difference has to be
    visible."""
    rows = [{"code": "tanker", "label": "Tanker truck",
             "jmp_id": "delivered_water.tanker_truck", "jmp": "Delivered water > Tanker truck",
             "improved": True, "observed_in": [], "source_row": 1}]
    xw = gmd.crosswalk(rows, "water")
    assert xw[0]["gmd_code"] == 12
    assert xw[0]["improved"] == 0
    assert xw[0]["disagrees_with_jmp"] is True
    assert "delivered water" in xw[0]["disagreement_note"]


# --------------------------------------------------------------------------
# generated code
# --------------------------------------------------------------------------

def test_generated_stata_encodes_the_range_rule_not_a_lookup():
    rows = _rows(["tap_water.piped_on_premises.piped_water_into_dwelling", "surface_water"])
    xw = gmd.crosswalk(rows, "water")
    cap = gmd.capability(rows, "water")
    code = gmd.stata("XXX", "Test", "v1.0", "water", xw, cap)
    assert "replace imp_wat_rec = 1 if inrange(water_source, 1, 8)" in code
    assert "replace imp_wat_rec = 0 if inrange(water_source, 9, 13)" in code
    assert "assert imp_wat_rec == 1 if inrange(water_source,1,8)" in code


def test_spanning_categories_are_left_missing_and_listed():
    rows = _rows(["ground_water", "rainwater", "surface_water"])
    xw = gmd.crosswalk(rows, "water")
    cap = gmd.capability(rows, "water")
    code = gmd.stata("XXX", "Test", "v1.0", "water", xw, cap)
    assert "spans" in code
    assert 'replace water_source = None' not in code


# --------------------------------------------------------------------------
# against real countries
# --------------------------------------------------------------------------

ROOT = "/mnt/user-data/uploads/gmd_ai/National concordance/ALB"


@pytest.mark.skipif(not os.path.exists(ROOT), reason="real Albania bundles not staged")
@pytest.mark.parametrize("domain", ["water", "sanitation"])
def test_albania_end_to_end(domain):
    b = json.load(open(f"{ROOT}/ALB_{domain}_view.json", encoding="utf-8"))
    d = gmd.build(b["rows"], "ALB", "Albania", "v1.0", domain)
    src = "water_source" if domain == "water" else "sanitation_source"
    assert d["capability"][src]["ok"]
    for r in d["crosswalk"]:
        if r["gmd_code"] is not None:
            assert 1 <= r["gmd_code"] <= 14
        if r["improved"] is not None:
            assert (r["improved"] == 1) == (r["gmd_code"] in range(1, 9))
