"""
gmd_wash_concordance.benchmark
==============================
What JMP itself published, kept beside the mapping and out of it.

The instruction may not carry survey-level data -- System 9, *MUST NOT contain
survey-level data* -- and it does not. But the numbers are the most useful
thing in the workbook for a reviewer, and the only independent check on a
harmonization run that exists before the run happens:

* per source, the estimate JMP published for **every category** in the tree,
  urban / rural / total;
* the three aggregate blocks above the concordance -- *Facility type
  estimates*, *Service level estimate*, and the Yes/No *Data used for
  estimates* flags saying which of them JMP actually took from that source;
* the country's ladder from the ``Ladders`` sheet -- safely managed, basic,
  limited, unimproved, surface water / open defecation.

So a reviewer sees the mapping and the number it produced side by side, and a
later GMD run has something to be compared against. That is the benchmark: not
a target to reproduce exactly -- JMP models and interpolates, GMD harmonizes
microdata -- but the published answer for the same country, source and year,
which is the number someone will ask about.

Nothing here ever reaches the instruction. `W-17` asserts that.
"""
from __future__ import annotations

import unicodedata
from typing import Any, Dict, List, Optional


def norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.lower().split())


def num(v) -> Optional[float]:
    """A published estimate, or None. Text such as "No", "-" or "m" is not an
    estimate and must not become 0."""
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return round(float(v), 6)
    return None


def flag(v) -> Optional[str]:
    if v is None:
        return None
    s = str(v).strip()
    return s or None


def triple(ws, r: int, cols) -> Dict[str, Optional[float]]:
    u, rr, t = cols
    return {"urban": num(ws.cell(r, u).value),
            "rural": num(ws.cell(r, rr).value),
            "total": num(ws.cell(r, t).value)}


def has_any(d: Dict[str, Optional[float]]) -> bool:
    return any(v is not None for v in d.values())


# --------------------------------------------------------------------------
def ladder_estimates(wb, sheet_names=("Ladders",)) -> Dict[str, Any]:
    """The country ladder from the ``Ladders`` sheet.

    The layout is a small block: a header row of domains, a row of
    total/rural/urban under each, a row of years, then one row per rung. It is
    found by locating the rung names rather than by fixed row numbers.
    """
    name = next((s for s in sheet_names if s in wb.sheetnames), None)
    if name is None:
        return {}
    ws = wb[name]
    rungs = ["safely managed", "basic service", "limited service",
             "unimproved", "no service", "surface water", "open defecation"]
    first = None
    for r in range(1, (ws.max_row or 1) + 1):
        for c in range(1, min(ws.max_column or 1, 4) + 1):
            if norm(ws.cell(r, c).value) in rungs:
                first = (r, c)
                break
        if first:
            break
    if not first:
        return {}
    r0, c0 = first
    # the three rows above the first rung carry domain, split and year
    domains, splits, years = {}, {}, {}
    for c in range(c0 + 1, (ws.max_column or 1) + 1):
        for back, store in ((3, domains), (2, splits), (1, years)):
            v = ws.cell(r0 - back, c).value
            if v is not None and str(v).strip():
                store[c] = str(v).strip()
    # carry the domain across its columns
    cur = None
    for c in range(c0 + 1, (ws.max_column or 1) + 1):
        cur = domains.get(c, cur)
        domains[c] = cur

    out: Dict[str, Any] = {"sheet": name, "rungs": []}
    r = r0
    while r <= (ws.max_row or 1):
        label = ws.cell(r, c0).value
        if label is None or norm(label) not in rungs:
            if out["rungs"]:
                break
            r += 1
            continue
        rec = {"rung": str(label).strip(), "row": r, "values": []}
        for c in range(c0 + 1, (ws.max_column or 1) + 1):
            v = num(ws.cell(r, c).value)
            if v is None:
                continue
            rec["values"].append({
                "domain": domains.get(c) or "", "split": splits.get(c) or "",
                "year": years.get(c) or "", "value": v})
        if rec["values"]:
            out["rungs"].append(rec)
        r += 1
    return out


# --------------------------------------------------------------------------
def for_source(ws, tree, hdr: int, c_def: int, c_class: int, c_cat: int,
               cols, sections: List[Any], tr=None, fws=None) -> Dict[str, Any]:
    """The published numbers for one source block."""
    cats = []
    for i, node in enumerate(tree.nodes):
        r = hdr + 1 + i
        vals = triple(ws, r, cols)
        denom = ws.cell(r, c_def).value
        if not has_any(vals) and not denom:
            continue
        cats.append({
            "jmp_id": node.id, "jmp": node.path, "level": node.level,
            "structural": node.structural, "row": r,
            "national_label": (str(denom).strip() if denom else ""),
            "improved": node.improved, "gmd": node.gmd,
            "rolls_up_to": list(node.rolls_up_to),
            **vals,
        })
    blocks: Dict[str, List[dict]] = {}
    for sec in sections:
        key = norm(sec.name).replace(" ", "_")
        rows = []
        for it in sec.items:
            r = it.get("row")
            if r is None:
                continue
            vals = triple(ws, r, cols)
            rec = {"label": it.get("label"), "label_local": it.get("label_local"),
                   "row": r, **vals}
            if not has_any(vals):
                # the Yes/No block is text, not numbers
                rec.update({k: flag(ws.cell(r, c).value)
                            for k, c in zip(("urban", "rural", "total"), cols)})
            rows.append(rec)
        blocks[key] = rows
    return {"categories": cats, "blocks": blocks,
            "n_with_estimates": sum(1 for c in cats if has_any(c))}


def summarise(bench: Dict[str, Any]) -> Dict[str, Any]:
    """A few numbers a reviewer reads before anything else."""
    per = bench.get("per_source") or []
    with_est = [s for s in per if s.get("n_with_estimates")]
    years = [s["source"]["year"] for s in per if s["source"].get("year")]
    return {
        "sources": len(per),
        "sources_with_estimates": len(with_est),
        "categories_with_estimates": sum(s.get("n_with_estimates", 0)
                                         for s in per),
        "from": min(years) if years else None,
        "to": max(years) if years else None,
        "has_country_ladder": bool((bench.get("ladder") or {}).get("rungs")),
    }
