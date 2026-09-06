"""GMD canonical water and sanitation variables, derived from the JMP tree.

Same division of labour as the education package.  The atomic mapping this
package produces is the national category -> JMP classification link.  What
GMD publishes is a small fixed code list, and that code list is a
deterministic function of the JMP node a category sits on:

  water_source       1..14, *GMD 2.0 List of Variables*, sheet "GMD 1.5"
  imp_wat_rec        1 if water_source in 1..8, 0 if 9..13, country call at 14
  pipedwater_acc     0 no / 1 yes in premise / 2 yes not in premise / 3 unstated
  watertype_quest    survey-level: 1 drinking / 2 general / 3 both / 4 other
  sanitation_source  1..14
  imp_san_rec        1 if sanitation_source in 1..8, 0 if 9..13, country call at 14
  toilet_acc         0 no / 1 yes in premise / 2 yes not in premise / 3 unstated

The improved/unimproved rule is a *range* rule, not a per-category judgement:
the GMD code list is ordered so that improved sources occupy 1-8 and
unimproved 9-13, and 14 is the residual a country has to rule on.  That is why
this module never asks JMP whether a category is improved -- it maps to the GMD
code and lets the range decide.  Where the two disagree, that disagreement is a
finding worth seeing, and it is reported.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

WATER_SOURCE = {
    1: "Piped water into dwelling",
    2: "Piped water to yard/plot",
    3: "Public tap or standpipe",
    4: "Tubewell or borehole",
    5: "Protected dug well",
    6: "Protected spring",
    7: "Bottled water",
    8: "Rainwater",
    9: "Unprotected spring",
    10: "Unprotected dug well",
    11: "Cart with small tank/drum",
    12: "Tanker-truck",
    13: "Surface water",
    14: "Other",
}
SANITATION_SOURCE = {
    1: "A flush toilet",
    2: "A piped sewer system",
    3: "A septic tank",
    4: "Pit latrine",
    5: "Ventilated improved pit latrine (VIP)",
    6: "Pit latrine with slab",
    7: "Composting toilet",
    8: "Special case",
    9: "A flush/pour flush to elsewhere",
    10: "A pit latrine without slab",
    11: "Bucket",
    12: "Hanging toilet or hanging latrine",
    13: "No facilities or bush or field",
    14: "Other",
}
IMPROVED_YES = set(range(1, 9))
IMPROVED_NO = set(range(9, 14))
RESIDUAL = 14

PIPEDWATER_ACC = {0: "No", 1: "Yes, in premise", 2: "Yes, but not in premise",
                  3: "Yes, unstated whether in or outside premise"}
TOILET_ACC = {0: "No", 1: "Yes, in premise",
              2: "Yes, but not in premise including public toilet",
              3: "Yes, unstated whether in or outside premise"}
WATERTYPE_QUEST = {1: "drinking water", 2: "general water", 3: "both", 4: "others"}

# --------------------------------------------------------------------------
# JMP node -> GMD code.  Matched on the jmp_id path, most specific first, so
# `ground_water.protected_well.public` resolves before `ground_water`.
# --------------------------------------------------------------------------

WATER_RULES: List[tuple] = [
    (r"piped_water_into_dwelling|piped_into_dwelling|piped_to_dwelling", 1),
    (r"piped_water_to_yard|piped_to_yard|yard_plot", 2),
    (r"public_tap|standpipe|public_standpost", 3),
    (r"tubewell|borehole|tube_well|tube well", 4),
    # unprotected must be tested before protected: "unprotected_spring" contains
    # "protected_spring", and a well that is read as protected because of that is
    # a household counted as having improved water when it does not
    (r"unprotected_spring", 9),
    (r"unprotected_dug_well|unprotected_well|unprotected_ground_water", 10),
    (r"(?<!un)protected_dug_well|(?<!un)protected_well", 5),
    (r"(?<!un)protected_spring", 6),
    (r"bottled|packaged_water|sachet", 7),
    (r"rainwater", 8),
    (r"cart|small_tank|drum", 11),
    (r"tanker", 12),
    (r"surface_water|river|dam|lake|pond|stream|canal|irrigation", 13),
    # nodes that are real but do not resolve to one code
    (r"piped_on_premises", 1),
    (r"tap_water\.other|tap_water$", 3),
]
SANITATION_RULES: List[tuple] = [
    (r"to_piped_sewer_system|piped_sewer", 2),
    (r"to_septic_tank|septic", 3),
    (r"ventilated_improved|(^|\.)vip(\.|$)", 5),
    # "without_slab" contains "with_slab": a pit latrine without a slab is
    # unimproved and must be tested first, exactly as unprotected is for water
    (r"without_slab|open_pit|no_slab", 10),
    (r"(?<!with)(?<!out)with_slab|(?<!out_)slab", 6),
    (r"composting|twin_pit", 7),
    (r"to_pit(_latrine)?", 4),
    (r"flush_and_pour_flush\.to_elsewhere|to_elsewhere|to_open_drain|to_unknown", 9),
    (r"bucket", 11),
    (r"hanging", 12),
    (r"open_defecation|no_facility|bush|field", 13),
    (r"flush_and_pour_flush|flush", 1),
    (r"pit_latrine", 4),
    (r"other", 14),
]

# JMP nodes that stand for a whole branch and cannot carry one GMD code
WATER_SPAN = {
    "ground_water": [4, 5, 6, 9, 10],
    "ground_water.all_wells": [4, 5, 10],
    "ground_water.protected_ground_water": [4, 5, 6],
    "ground_water.unprotected_ground_water": [9, 10],
    "ground_water.protected_wells_or_springs": [5, 6],
    "ground_water.unprotected_wells_or_springs": [9, 10],
    "ground_water.wells_or_springs": [4, 5, 6, 9, 10],
    "ground_water.traditional_wells": [5, 10],
    "delivered_water": [11, 12],
    "other_improved_sources": [7, 8],
}
SANITATION_SPAN = {
    "pit_latrine": [4, 6, 10],
    "flush_and_pour_flush.to_unknown_place": [1, 9],
}


def _match(jmp_id: str, label: str, rules: List[tuple]) -> Optional[int]:
    hay = f"{jmp_id} {label}".lower().replace("/", "_").replace("-", "_")
    hay = re.sub(r"[^a-z0-9_. ]+", " ", hay)
    for pattern, code in rules:
        if re.search(pattern, hay):
            return code
    return None


def map_water(jmp_id: str, label: str = "") -> Dict[str, Any]:
    """One JMP water node -> a GMD ``water_source`` code, or a span."""
    key = (jmp_id or "").strip()
    if key in WATER_SPAN:
        return {"code": None, "spans": WATER_SPAN[key],
                "why": f"'{key}' is a branch of the JMP tree covering "
                       f"{len(WATER_SPAN[key])} GMD codes; it needs a splitting rule"}
    code = _match(key, label, WATER_RULES)
    if code is None:
        return {"code": RESIDUAL, "spans": [],
                "why": "no JMP node matched a GMD code; falls to 14 (Other), which is the "
                       "country's call on whether it is improved"}
    return {"code": code, "spans": [],
            "why": f"JMP node '{key}' maps to GMD water_source {code} "
                   f"({WATER_SOURCE[code]})"}


def map_sanitation(jmp_id: str, label: str = "") -> Dict[str, Any]:
    key = (jmp_id or "").strip()
    if key in SANITATION_SPAN:
        return {"code": None, "spans": SANITATION_SPAN[key],
                "why": f"'{key}' is a branch of the JMP tree covering "
                       f"{len(SANITATION_SPAN[key])} GMD codes; it needs a splitting rule"}
    code = _match(key, label, SANITATION_RULES)
    if code is None:
        return {"code": RESIDUAL, "spans": [],
                "why": "no JMP node matched a GMD code; falls to 14 (Other)"}
    return {"code": code, "spans": [],
            "why": f"JMP node '{key}' maps to GMD sanitation_source {code} "
                   f"({SANITATION_SOURCE[code]})"}


def improved_of(code: Optional[int]) -> Optional[int]:
    if code is None:
        return None
    if code in IMPROVED_YES:
        return 1
    if code in IMPROVED_NO:
        return 0
    return None            # 14 is a country call, never a default


def pipedwater_acc_of(code: Optional[int]) -> Optional[int]:
    """Piped access from the source code alone.

    Only codes 1, 2 and 3 say anything about piping.  Everything else is 0
    except the residual, which says nothing at all.
    """
    if code is None or code == RESIDUAL:
        return None
    if code == 1:
        return 1
    if code in (2, 3):
        return 2
    return 0


def toilet_acc_of(code: Optional[int]) -> Optional[int]:
    if code is None or code == RESIDUAL:
        return None
    if code in (1, 2, 3):
        return 1        # a flush toilet connected to sewer or septic, on premises
    if code == 9:
        return 2        # flush to elsewhere
    return 0


# --------------------------------------------------------------------------
# capability
# --------------------------------------------------------------------------

def capability(rows: List[Dict[str, Any]], domain: str) -> Dict[str, Any]:
    mapped = [r for r in rows if r.get("_gmd_code")]
    spans = [r for r in rows if r.get("_gmd_spans")]
    residual = [r for r in rows if r.get("_gmd_code") == RESIDUAL]
    n = len(rows)
    out: Dict[str, Any] = {}
    src = "water_source" if domain == "water" else "sanitation_source"
    imp = "imp_wat_rec" if domain == "water" else "imp_san_rec"
    acc = "pipedwater_acc" if domain == "water" else "toilet_acc"

    if not n:
        out[src] = {"ok": False, "why": "no national category was read from the workbook"}
    elif len(mapped) < n * 0.5:
        out[src] = {"ok": False, "why":
            f"only {len(mapped)} of {n} categories resolved to a GMD code; the tree this "
            f"country reports on is too coarse to map"}
    else:
        out[src] = {"ok": True}
        if spans:
            out[src]["note"] = (f"{len(spans)} categor{'y' if len(spans)==1 else 'ies'} span "
                                f"more than one GMD code and need a splitting rule")

    if not out[src]["ok"]:
        out[imp] = {"ok": False, "why": f"{src} could not be produced"}
        out[acc] = {"ok": False, "why": f"{src} could not be produced"}
    else:
        out[imp] = {"ok": True}
        if residual:
            out[imp]["note"] = (f"{len(residual)} categor{'y' if len(residual)==1 else 'ies'} "
                                f"fell to code 14, which the range rule cannot decide; a "
                                f"country ruling is required before imp_{'wat' if domain=='water' else 'san'}"
                                f"_rec is complete")
        out[acc] = {"ok": True}

    if domain == "water":
        out["watertype_quest"] = {"ok": False, "why":
            "the type of water question asked is a property of the survey instrument, not of "
            "the country concordance; it is set by the survey-level mapping"}
    out["finest"] = src if out[src]["ok"] else None
    return out


# --------------------------------------------------------------------------
# crosswalk + code
# --------------------------------------------------------------------------

def crosswalk(rows: List[Dict[str, Any]], domain: str) -> List[Dict[str, Any]]:
    fn = map_water if domain == "water" else map_sanitation
    labels = WATER_SOURCE if domain == "water" else SANITATION_SOURCE
    out = []
    for r in rows:
        m = fn(r.get("jmp_id", ""), r.get("jmp", "") or r.get("label", ""))
        code = m["code"]
        r["_gmd_code"] = code
        r["_gmd_spans"] = m["spans"]
        imp = improved_of(code)
        jmp_imp = r.get("improved")
        disagree = (imp is not None and jmp_imp is not None and bool(imp) != bool(jmp_imp))
        note = ""
        if disagree:
            if code in (11, 12):
                note = ("JMP counts delivered water as improved; the GMD 1.5 code list puts "
                        "carts (11) and tanker trucks (12) in the unimproved range 9-13. This is "
                        "a difference between the two frames, not a mapping error, and the GMD "
                        "range governs here because imp_wat_rec is a GMD variable.")
            elif code == 7:
                note = ("JMP treats packaged water as improved only where the household also has "
                        "an improved source for other uses; GMD code 7 is unconditionally in the "
                        "improved range.")
            else:
                note = ("the JMP node and the GMD code list disagree on whether this category is "
                        "improved; the GMD range rule governs, and the difference is recorded so "
                        "a reviewer can see it rather than discover it later.")
        out.append({
            "code": r.get("code", ""),
            "label": r.get("label", ""),
            "jmp": r.get("jmp", ""),
            "jmp_id": r.get("jmp_id", ""),
            "gmd_code": code,
            "gmd_label": labels.get(code, "") if code else "",
            "spans": m["spans"],
            "improved": imp,
            "jmp_improved": jmp_imp,
            "disagrees_with_jmp": disagree,
            "disagreement_note": note,
            "access": pipedwater_acc_of(code) if domain == "water" else toilet_acc_of(code),
            "why": m["why"],
            "observed_in": r.get("observed_in", []),
            "source_row": r.get("source_row"),
        })
    return out


def stata(iso3: str, country: str, version: str, domain: str,
          xw: List[Dict[str, Any]], cap: Dict[str, Any],
          src_var: str = None) -> str:
    src = "water_source" if domain == "water" else "sanitation_source"
    imp = "imp_wat_rec" if domain == "water" else "imp_san_rec"
    acc = "pipedwater_acc" if domain == "water" else "toilet_acc"
    labels = WATER_SOURCE if domain == "water" else SANITATION_SOURCE
    acc_labels = PIPEDWATER_ACC if domain == "water" else TOILET_ACC
    raw = src_var or ("w_source" if domain == "water" else "s_facility")

    L: List[str] = []
    a = L.append
    a("*" + "=" * 74)
    a(f"* {country} ({iso3}) - GMD canonical {domain} variables")
    a(f"* Generated from the national concordance {iso3}_{domain}_{version}")
    a("*")
    a(f"* Atomic input : the survey's own {domain} category, already mapped to the")
    a("*                JMP tree by the concordance.")
    a(f"* Derived here : {src}, {imp}, {acc}.")
    a("*")
    a("* improved is a RANGE rule on the GMD code list, not a per-category")
    a(f"* judgement: 1-8 improved, 9-13 not, 14 is the country's own call.")
    a("*" + "=" * 74)
    a("")

    if not cap[src]["ok"]:
        a(f"* {src.upper()} NOT PRODUCED: {cap[src].get('why','')}")
        a(f"gen byte {src} = .")
        a(f"gen byte {imp} = .")
        a(f"gen byte {acc} = .")
        return "\n".join(L) + "\n"

    a(f"* ---- {src} " + "-" * (58 - len(src)))
    a(f"gen byte {src} = .")
    seen = set()
    for r in sorted(xw, key=lambda x: (x["gmd_code"] or 99, x["label"])):
        if r["gmd_code"] is None:
            continue
        key = (r["code"], r["gmd_code"])
        if key in seen:
            continue
        seen.add(key)
        a(f'replace {src} = {r["gmd_code"]} if {raw} == "{r["code"]}"'
          f'   // {r["label"][:38]}')
    spans = [r for r in xw if r["spans"]]
    if spans:
        a("")
        a("* These categories cover more than one GMD code and are deliberately left")
        a("* missing. A splitting rule has to come from a second question in the")
        a("* instrument or from an agreement with the country team - not from here.")
        for r in spans:
            a(f'*   {r["code"]:<28} spans {r["spans"]}   {r["label"][:36]}')
    a("")
    a(f'label define {src} ' + ' '.join(f'{k} "{v}"' for k, v in labels.items()) + ', replace')
    a(f"label values {src} {src}")
    a(f'label var {src} "{"Sources of drinking water" if domain=="water" else "Main sanitation facility"} (14 categories)"')
    a("")

    a(f"* ---- {imp} " + "-" * (58 - len(imp)))
    a(f"gen byte {imp} = .")
    a(f"replace {imp} = 1 if inrange({src}, 1, 8)")
    a(f"replace {imp} = 0 if inrange({src}, 9, 13)")
    res = [r for r in xw if r["gmd_code"] == RESIDUAL]
    if res:
        a(f"* {src} == 14 is left missing on purpose. {len(res)} categor"
          f"{'y' if len(res)==1 else 'ies'} landed there and the country has to rule on")
        a("* whether they count as improved:")
        for r in res:
            a(f'*   {r["label"][:60]}')
    a(f'label define yesno 0 "No" 1 "Yes", replace')
    a(f"label values {imp} yesno")
    a(f'label var {imp} "{"Improved water" if domain=="water" else "Improved sanitation facility"}"')
    a("")

    a(f"* ---- {acc} " + "-" * (58 - len(acc)))
    a(f"gen byte {acc} = .")
    if domain == "water":
        a(f"replace {acc} = 1 if {src} == 1")
        a(f"replace {acc} = 2 if inlist({src}, 2, 3)")
        a(f"replace {acc} = 0 if inrange({src}, 4, 13)")
    else:
        a(f"replace {acc} = 1 if inlist({src}, 1, 2, 3)")
        a(f"replace {acc} = 2 if {src} == 9")
        a(f"replace {acc} = 0 if inlist({src}, 4, 5, 6, 7, 8, 10, 11, 12, 13)")
    a(f'label define {acc} ' + ' '.join(f'{k} "{v}"' for k, v in acc_labels.items()) + ', replace')
    a(f"label values {acc} {acc}")
    a(f'label var {acc} "{"Access to piped water" if domain=="water" else "Access to flushed toilet"}"')
    a("")
    if domain == "water":
        a("* ---- watertype_quest --------------------------------------------------")
        a("* Not derivable from the concordance: it records what the survey asked,")
        a("* not what the country's categories mean. Set it in the survey mapping.")
        a("* 1 drinking water  2 general water  3 both  4 others")
        a("gen byte watertype_quest = .")
        a("")
    a("* ---- checks -----------------------------------------------------------")
    a(f"assert inrange({src},1,14) | missing({src})")
    a(f"assert inlist({imp},0,1) | missing({imp})")
    a(f"assert {imp} == 1 if inrange({src},1,8)")
    a(f"assert {imp} == 0 if inrange({src},9,13)")
    a("")
    return "\n".join(L) + "\n"


def build(rows: List[Dict[str, Any]], iso3: str, country: str, version: str,
          domain: str) -> Dict[str, Any]:
    xw = crosswalk(rows, domain)
    cap = capability(rows, domain)
    src = "water_source" if domain == "water" else "sanitation_source"
    return {
        "schema": f"gmd.derivation.wash.{domain}",
        "frame": "GMD 2.0 List of Variables (25 Nov 2019), sheet 'GMD 1.5'",
        "atomic": ["the survey category, mapped to a JMP node"],
        "derived": ([ "water_source", "imp_wat_rec", "pipedwater_acc", "watertype_quest"]
                    if domain == "water" else
                    ["sanitation_source", "imp_san_rec", "toilet_acc"]),
        "capability": cap,
        "labels": {src: WATER_SOURCE if domain == "water" else SANITATION_SOURCE,
                   "pipedwater_acc" if domain == "water" else "toilet_acc":
                       PIPEDWATER_ACC if domain == "water" else TOILET_ACC,
                   **({"watertype_quest": WATERTYPE_QUEST} if domain == "water" else {})},
        "improved_rule": {"yes": [1, 8], "no": [9, 13], "country_call": 14},
        "crosswalk": xw,
        "disagreements": [r for r in xw if r["disagrees_with_jmp"]],
        "stata": stata(iso3, country, version, domain, xw, cap),
    }
