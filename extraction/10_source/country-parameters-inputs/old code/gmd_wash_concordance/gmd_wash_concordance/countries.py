"""
gmd_wash_concordance.countries
==============================
Country name -> ISO 3166-1 alpha-3.

A country workbook names its country in whatever language it was written in --
*España*, *Sénégal*, *Российская Федерация* -- and a hand-kept list of twenty
names is how a Spanish file ends up filed under no country at all. The table in
``data/iso3166.yaml`` carries every ISO 3166-1 country in English, French,
Spanish, Portuguese, Russian, Arabic, German and Italian, plus the aliases the
data world actually uses.

Matching is accent- and case-insensitive and tolerates the decoration a banner
row puts around a name: *Sri Lanka - ISCED 2011 Mapping* is Sri Lanka.
"""
from __future__ import annotations

import os
import re
import unicodedata
from typing import Dict, List, Optional, Tuple

import yaml

DATA = os.path.join(os.path.dirname(__file__), "data")

# Decoration a banner row wraps a country name in.
_STRIP = re.compile(
    r"(?i)\b(isced\s*2011\s*mapping|isced\s*mapping|cartographie\s+de\s+la\s+cite"
    r"|mapping|cartographie|jmp|\d{4})\b")
_PUNCT = re.compile(r"^[\s\-–—:·,]+|[\s\-–—:·,]+$")

_CACHE: Optional[Dict[str, str]] = None
_NAMES: Optional[Dict[str, List[str]]] = None
_EN: Optional[Dict[str, str]] = None


def norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.lower().replace("’", "'").split())


def _load():
    global _CACHE, _NAMES, _EN
    if _CACHE is None:
        with open(os.path.join(DATA, "iso3166.yaml"), encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        _NAMES = doc["names"]
        _EN = doc.get("english") or {}
        _CACHE = {}
        for iso, names in _NAMES.items():
            for n in names:
                _CACHE.setdefault(norm(n), iso)
    return _CACHE


def clean(name: str) -> str:
    """Strip the decoration a banner row puts around a country name."""
    s = _STRIP.sub(" ", str(name or ""))
    s = _PUNCT.sub("", " ".join(s.split()))
    return s


def match(name: str) -> Tuple[Optional[str], str]:
    """(alpha-3, the span that matched) for a country named anywhere in the
    string, or (None, "").

    The country is not always the whole string and not always at the front:
    *Cartographie de la CITE 2011 du Sénégal* names it last. Every contiguous
    run of words is tried, longest first, so the longest real country name
    wins over a shorter one inside it (*Papua New Guinea* over *Guinea*).

    It never guesses. A string with no country in the table returns None, so
    the caller stops rather than filing the concordance under the wrong
    country -- which is not caught downstream.
    """
    if not name:
        return None, ""
    table = _load()
    for cand in (str(name), clean(name)):
        k = norm(cand)
        if k and k in table:
            return table[k], cand.strip()
    words = clean(name).split()
    for n in range(len(words), 0, -1):
        for i in range(len(words) - n + 1):
            span = " ".join(words[i:i + n])
            iso = table.get(norm(span))
            if iso:
                return iso, span
    return None, ""


def to_iso3(name: str) -> Optional[str]:
    return match(name)[0]


def english_name(iso3: str) -> str:
    """The canonical English name, not whichever translation sorts first."""
    _load()
    iso3 = (iso3 or "").upper()
    got = (_EN or {}).get(iso3)
    if got:
        return got
    names = (_NAMES or {}).get(iso3) or []
    return names[0] if names else ""


def resolve(name: str, filename: str = "") -> Tuple[str, str]:
    """(iso3, the country's name).  Falls back to the filename.

    The name returned is the span that actually matched, so a banner keeps the
    country's own spelling -- *España*, not *Spain*. When only the filename
    resolved, the canonical English name is used, because the banner text was
    not a country name and repeating it would be misleading.
    """
    iso, span = match(name)
    if iso:
        return iso, span
    if filename:
        stem = os.path.splitext(os.path.basename(filename))[0]
        stem = re.sub(r"\s*\(\d+\)$", "", stem)
        parts = [p for p in re.split(r"[_\-\s]+", stem) if p]
        for p in parts:
            if re.fullmatch(r"[A-Z]{3}", p) and english_name(p):
                return p, english_name(p)
        iso, span = match(" ".join(parts))
        if iso:
            return iso, span
    return "", clean(name)
