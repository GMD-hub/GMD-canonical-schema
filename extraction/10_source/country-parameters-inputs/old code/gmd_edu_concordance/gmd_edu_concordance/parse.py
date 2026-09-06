"""
gmd_edu_concordance.parse
=========================
The small parsers.  Every one of them returns a structured value or ``None``
and never guesses: ``"3-4"`` is a range and stays a range all the way to the
grade table, because a country whose programme lasts three or four years does
not have a single answer and pretending otherwise is how a concordance goes
quietly wrong.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Dict, List, Optional

DASHES = "‐‑‒–—―−"


def norm(s) -> str:
    s = "" if s is None else str(s)
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    for d in DASHES:
        s = s.replace(d, "-")
    s = s.replace("’", "'").replace(" ", " ")
    return " ".join(s.lower().split())


def is_na(s, na_tokens) -> bool:
    return norm(s) in {norm(t) for t in na_tokens} or norm(s) == ""


def _months_to_years(n: float) -> float:
    return round(n / 12.0, 3)


def duration(raw, na_tokens=()) -> Optional[Dict[str, Any]]:
    """``"6"`` -> 6..6 ; ``"3-4"`` -> 3..4 ; ``"6 Months"`` -> 0.5..0.5."""
    if is_na(raw, na_tokens):
        return None
    s = norm(raw)
    months = "month" in s or "mois" in s
    nums = [float(x) for x in re.findall(r"\d+(?:[.,]\d+)?", s.replace(",", "."))]
    if not nums:
        return None
    lo, hi = min(nums), max(nums)
    if months:
        lo, hi = _months_to_years(lo), _months_to_years(hi)
    return {"min": lo, "max": hi, "unit": "years",
            "range": lo != hi, "raw": str(raw).strip()}


def entrance_age(raw, na_tokens=()) -> Optional[Dict[str, Any]]:
    """``"6"`` / ``"6 years old"`` -> 6 ; ``"3 months"`` -> 0.25."""
    d = duration(raw, na_tokens)
    if d is None:
        return None
    return {"min": d["min"], "max": d["max"], "unit": "years",
            "range": d["range"], "raw": d["raw"]}


def isced_code(raw, label="") -> str:
    """The level digit.  Accepts ``1``, ``"1"``, ``"ISCED 1"``, ``"Level 1"``."""
    for cand in (raw, label):
        s = norm(cand)
        if not s:
            continue
        m = re.search(r"(?:isced\s*)?(?:level\s*)?\b([0-8])\b", s)
        if m:
            return m.group(1)
    return ""


def three_digit(raw) -> str:
    s = re.sub(r"\D", "", str(raw or ""))
    return s if len(s) == 3 else ""


def _match_map(value, mapping: Dict[str, List[str]], default="na") -> str:
    v = norm(value)
    if not v:
        return default
    for key, cands in mapping.items():
        for c in cands:
            c = norm(c)
            if v == c or v.startswith(c + " ") or v.startswith(c + ":"):
                return key
    return default


def completion(raw, mapping, na_tokens=()) -> Dict[str, str]:
    """``"Full completion: First degree (3-4 years)"`` ->
    ``{"completion": "full", "position": "First degree (3-4 years)"}``."""
    if is_na(raw, na_tokens):
        return {"completion": "na", "position": ""}
    s = str(raw).strip()
    head, _, tail = s.partition(":")
    return {"completion": _match_map(head, mapping),
            "position": tail.strip()}


ACCESS_TAIL = re.compile(r"(?:^|[,;])\s*(?:to|au|aux|a|à|al|hasta)\s+(.*)$",
                         re.I)


def access(raw, na_tokens=(), mapping=None) -> Dict[str, Any]:
    """``"Yes, to ISCED 3"`` -> ``{"access": True, "to": "ISCED 3"}``.

    The yes/no words come from the profile, because *Oui* and *Sí* are yes in
    exactly the same sense and a hard-coded ``startswith("yes")`` reads a
    French workbook as "access unknown" for every row.
    """
    if is_na(raw, na_tokens):
        return {"access": None, "to": ""}
    mapping = mapping or {"yes": ["yes"], "no": ["no"]}
    s = norm(raw)
    first = s.split(",")[0].split(";")[0].strip()
    yes = [norm(x) for x in mapping.get("yes", [])]
    no = [norm(x) for x in mapping.get("no", [])]
    def _hit(words):
        return any(first == w or first.startswith(w + " ") for w in words if w)
    if _hit(yes):
        m = ACCESS_TAIL.search(str(raw).strip())
        return {"access": True, "to": (m.group(1).strip() if m else "")}
    if _hit(no):
        return {"access": False, "to": ""}
    return {"access": None, "to": str(raw).strip()}


def orientation(raw, mapping, na_tokens=()) -> str:
    if is_na(raw, na_tokens):
        return "na"
    return _match_map(raw, mapping)


def fmt_range(lo, hi) -> str:
    def f(x):
        return str(int(x)) if float(x).is_integer() else str(x)
    return f(lo) if lo == hi else f"{f(lo)}-{f(hi)}"


REFORM_RE = re.compile(
    r"(?i)\b(reform|introduced|since|until|prior to|before|from|replaced|"
    r"phased out|abolished|new curriculum|old system)\b[^.]{0,60}?"
    r"\b((?:19|20)\d{2})\b")


def reform_signals(text: str) -> List[Dict[str, Any]]:
    """Years mentioned in a note in a way that reads like a structural change.

    A single mapping workbook documents one school year.  When its own notes
    name an earlier or later structure, that is the only in-file evidence that
    more than one era exists, and it belongs in front of the focal point rather
    than in a comment.
    """
    out = []
    for m in REFORM_RE.finditer(text or ""):
        out.append({"year": int(m.group(2)), "phrase": m.group(0).strip()})
    return out
