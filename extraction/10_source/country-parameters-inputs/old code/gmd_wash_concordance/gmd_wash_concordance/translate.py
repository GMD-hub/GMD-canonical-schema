"""
gmd_wash_concordance.translate
==============================
The workbook's own dictionary.

Every label in a JMP country file is a lookup, not a literal::

    C37: =HLOOKUP(Introduction!$G$4, nametranslations, 183, FALSE)

``nametranslations`` is the ``Key`` sheet: one row per phrase, one column per
language, with **English in the first column**. A Russian country file carries
the whole matrix, not just Russian -- so the file that arrives in a language
nobody on the team reads also arrives with its own translation of every phrase
in it.

That is what this module uses. Rather than shipping a hand-kept list of
Russian and Spanish strings -- which is wrong the moment JMP adds Chinese, and
silently wrong the moment a phrase is reworded -- every label is resolved back
to English through the table the workbook itself was rendered from.

Two consequences worth having:

* binding stops depending on language at all. The concordance anchor, the
  section names and the category tree are matched in English no matter what
  the file is written in;
* the local wording is still kept, because it is what the country actually
  reads and nothing downstream can recover it.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Dict, List, Optional

# The named range JMP uses, and where it lives if the name has been lost.
NAMED_RANGE = "nametranslations"
FALLBACK_SHEET = "Key"

_HLOOKUP = re.compile(r"HLOOKUP\s*\(", re.I)


def _args(formula: str, start: int) -> List[str]:
    """Split the arguments of a call whose "(" is at ``start``."""
    depth, cur, out, inq = 0, [], [], False
    for ch in formula[start:]:
        if ch == '"':
            inq = not inq
        if not inq:
            if ch == "(":
                depth += 1
                if depth == 1:
                    continue
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    break
            elif ch == "," and depth == 1:
                out.append("".join(cur).strip())
                cur = []
                continue
        cur.append(ch)
    out.append("".join(cur).strip())
    return out


def phrase_index(formula) -> Optional[int]:
    """The translation-table row a label cell reads, from its formula.

    Both spellings appear in the same workbook::

        =HLOOKUP(Introduction!$G$4, nametranslations, 183, FALSE)
        =HLOOKUP(Introduction!$G$4, Key!$A$1:$G$395, 248, FALSE)

    so the row is taken as HLOOKUP's third argument rather than by matching
    the range, which would resolve one form and silently fall back to string
    matching for the other.

    This is the exact identifier of a phrase. Matching the *rendered string*
    cannot be: a translation is many-to-one -- the Russian for "Other" is also
    the Russian for "Unimproved sanitation" -- so a string map has to pick one
    and will sometimes pick the wrong one.
    """
    if not isinstance(formula, str):
        return None
    m = _HLOOKUP.search(formula)
    if not m:
        return None
    args = _args(formula, m.end() - 1)
    if len(args) < 3:
        return None
    try:
        return int(args[2])
    except ValueError:
        return None


def norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.lower().replace("’", "'").split())


class Dictionary:
    """local phrase -> English phrase, from one workbook."""

    def __init__(self, language: str = "", languages: Optional[List[str]] = None,
                 to_en: Optional[Dict[str, str]] = None, rows: int = 0,
                 sheet: str = "", by_row: Optional[Dict[int, str]] = None,
                 ambiguous: int = 0):
        self.language = language or ""
        self.languages = languages or []
        self._to_en = to_en or {}
        self.by_row = by_row or {}
        self.rows = rows
        self.sheet = sheet
        self.ambiguous = ambiguous

    def __len__(self):
        return len(self._to_en)

    @property
    def available(self) -> bool:
        return bool(self._to_en)

    @property
    def is_english(self) -> bool:
        return norm(self.language) in ("", "english")

    def en(self, value) -> str:
        """The English phrase for ``value``, or ``value`` unchanged.

        Unchanged is the right answer for anything the dictionary does not
        hold: a country's own denomination is not a JMP phrase and must never
        be translated. An English workbook is never translated at all -- there
        is nothing to gain and a many-to-one map to lose.
        """
        if value is None:
            return ""
        s = str(value).strip()
        if self.is_english:
            return s
        return self._to_en.get(norm(s), s)

    def is_phrase(self, value) -> bool:
        """True when this is a JMP phrase rather than a country's own text."""
        return norm(value) in self._to_en

    def en_of(self, value, formula=None) -> str:
        """The English phrase for a cell.

        The formula is consulted first because it is exact; the rendered
        string is the fallback for a cell that was typed rather than looked
        up.
        """
        if self.is_english:
            return "" if value is None else str(value).strip()
        n = phrase_index(formula)
        if n is not None and n in self.by_row:
            return self.by_row[n]
        return self.en(value)


COL = re.compile(r"\$?([A-Z]{1,3})(?:\$?\d+)?:\$?([A-Z]{1,3})", re.I)


def _col_index(letters: str) -> int:
    n = 0
    for ch in letters.upper():
        n = n * 26 + (ord(ch) - 64)
    return n


def _range_for(wb, named=NAMED_RANGE):
    """(sheet, last_column) for the translation matrix.

    The last column matters. The ``Key`` sheet carries a *second* table beyond
    the matrix -- a language/ISO3 lookup -- and folding those columns in
    produces mappings like "Census" -> "Safely managed drinking water", which
    is how an English workbook stopped binding. The named range says where the
    matrix ends; trust it.
    """
    fallback = (FALLBACK_SHEET if FALLBACK_SHEET in wb.sheetnames else None, 0)
    try:
        dn = wb.defined_names[named]
    except (KeyError, TypeError):
        return fallback
    for sheet, ref in dn.destinations:
        if sheet not in wb.sheetnames:
            continue
        m = COL.search(str(ref or ""))
        return sheet, (_col_index(m.group(2)) if m else 0)
    return fallback


def load(wb, language: str = "", max_cols: int = 8) -> Dictionary:
    """Read the translation matrix out of a JMP country workbook.

    Every language column is folded into the map, not just the one the file is
    set to. A workbook whose labels were pasted in from another language still
    resolves, and it costs nothing.
    """
    sheet, last_col = _range_for(wb)
    if sheet is None:
        return Dictionary(language=language)
    ws = wb[sheet]
    ncol = min(ws.max_column or 1, last_col or max_cols)
    langs = [str(ws.cell(1, c).value).strip()
             for c in range(1, ncol + 1) if ws.cell(1, c).value]
    if not langs or norm(langs[0]) != "english":
        # not the matrix we expected -- say nothing rather than mis-translate
        return Dictionary(language=language, sheet=sheet)
    to_en: Dict[str, str] = {}
    by_row: Dict[int, str] = {}
    rows = 0
    ambiguous = 0
    for r in range(2, (ws.max_row or 1) + 1):
        en = ws.cell(r, 1).value
        if en is None or not str(en).strip():
            continue
        en = str(en).strip()
        rows += 1
        by_row[r] = en
        for c in range(1, len(langs) + 1):
            v = ws.cell(r, c).value
            if v is None or not str(v).strip():
                continue
            k = norm(v)
            if k in to_en:
                if to_en[k] != en:
                    ambiguous += 1
                continue
            to_en[k] = en
    return Dictionary(language=language, languages=langs, to_en=to_en,
                      rows=rows, sheet=sheet, by_row=by_row,
                      ambiguous=ambiguous)
