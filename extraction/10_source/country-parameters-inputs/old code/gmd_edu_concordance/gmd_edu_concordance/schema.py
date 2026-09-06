"""
gmd_edu_concordance.schema
==========================
The fixed target schema for a country education instruction (GMD System 8).

The schema is FIXED.  A workbook that carries information the schema cannot
hold produces an entry in ``unmapped`` and a finding, never a new field.

Observed against inferred
-------------------------
The UIS mapping workbook records programmes, not grades, and one school year,
not a history of reforms.  Everything the package works out from those two
facts -- grade ranges, cumulative years, the era window -- is emitted as an
**inferred** field: ``{value, confidence, evidence}``, evidence mandatory.
An observed field is a plain value.  Nothing downstream has to consult
documentation to know which is which, and a focal point reviewing a draft can
see, per field, what the package inferred and from what.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional

SCHEMA = "gmd.country_instruction.education"
SCHEMA_VERSION = "2.0.0"
CVS_RELEASE = "4.8.2"
EXTRACTOR = "gmd_edu_concordance/1.0.0"

ISCED_LEVELS = {
    "0": "ISCED 0 Early childhood education",
    "1": "ISCED 1 Primary",
    "2": "ISCED 2 Lower secondary",
    "3": "ISCED 3 Upper secondary",
    "4": "ISCED 4 Post-secondary non-tertiary",
    "5": "ISCED 5 Short-cycle tertiary",
    "6": "ISCED 6 Bachelor or equivalent",
    "7": "ISCED 7 Master or equivalent",
    "8": "ISCED 8 Doctoral or equivalent",
    "9": "ISCED 9 Not elsewhere classified",
}

GMD_EDUC_LEVELS = [
    "none", "pre_primary", "primary", "lower_secondary", "upper_secondary",
    "post_secondary", "tertiary", "other",
]

# `educ_highest` says which level a person reached. It does not say whether
# they finished it, and "reached lower secondary" means something different
# depending on the answer. The attainment vocabulary is the level crossed with
# that question, which is what a survey's highest-education variable actually
# distinguishes.
GMD_EDUC_ATTAINMENT = [
    "none",
    "pre_primary",
    "primary_incomplete", "primary_complete",
    "lower_secondary_incomplete", "lower_secondary_complete",
    "upper_secondary_incomplete", "upper_secondary_complete",
    "post_secondary_incomplete", "post_secondary_complete",
    "tertiary_incomplete", "tertiary_complete",
    "other",
    # The bare level is a value in its own right: the person reached it and
    # the workbook does not settle whether they finished. It is not the same
    # as complete and must never be folded into it -- rule E-19 counts these.
    "primary", "lower_secondary", "upper_secondary", "post_secondary",
    "tertiary",
]

# Levels that are never split: finishing pre-primary is not an attainment a
# survey records, and "other" is a residual.
ATTAINMENT_UNSPLIT = {"none", "pre_primary", "other"}


def attainment_of(gmd: str, complete: Optional[bool]) -> str:
    """`("primary", False)` -> `"primary_incomplete"`.

    ``None`` means the level was reached but the workbook does not settle
    whether it was finished; that is returned as the bare level, never
    silently as complete.
    """
    if not gmd or gmd in ATTAINMENT_UNSPLIT:
        return gmd or ""
    if complete is None:
        return gmd
    return f"{gmd}_{'complete' if complete else 'incomplete'}"

COMPLETION = ["full", "partial", "none", "na"]
ORIENTATION = ["general", "vocational", "unspecified", "eced", "pre_primary", "na"]
STATUSES = ["draft", "in_review", "approved", "superseded", "rejected"]

OPEN_ERA_END = 2035


def inferred(value, confidence: float, evidence: str) -> Dict[str, Any]:
    """An inferred field.  Evidence is mandatory: an inferred value with no
    evidence is a defect, not a value."""
    if not evidence:
        raise ValueError("an inferred field must carry evidence")
    return {"value": value, "confidence": round(float(confidence), 2),
            "evidence": evidence}


def is_inferred(v) -> bool:
    return isinstance(v, dict) and set(v) >= {"value", "confidence", "evidence"}


def value_of(v):
    return v["value"] if is_inferred(v) else v


# --------------------------------------------------------------------------
@dataclass
class SourceFile:
    file: str = ""
    sha256: str = ""
    sheet: str = ""
    header_row: Optional[int] = None
    rows_read: int = 0
    profile: str = ""
    reference_year: Optional[int] = None
    extracted_at: str = ""
    extractor: str = EXTRACTOR

    @classmethod
    def of(cls, path, sheet, header_row, rows_read, profile,
           reference_year=None, now=None):
        h = hashlib.sha256()
        try:
            with open(path, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(chunk)
            digest = h.hexdigest()
        except OSError:
            digest = ""
        return cls(file=os.path.basename(str(path)), sha256=digest, sheet=sheet,
                   header_row=header_row, rows_read=rows_read, profile=profile,
                   reference_year=reference_year,
                   extracted_at=now or _dt.datetime.now(_dt.timezone.utc)
                   .replace(microsecond=0).isoformat())


@dataclass
class Era:
    """One schooling structure and the cohort window it governs.

    A single UIS mapping workbook documents one school year, so it yields one
    era, and that era is the **latest**: it runs to the open end.  Its start is
    inferred, and the cohorts before it are a declared gap, not a silent
    default -- see rule E-03.
    """
    id: int
    label: str
    from_year: Any                 # inferred
    to_year: Any                   # inferred
    reference_year: Optional[int] = None
    description: str = ""
    latest: bool = True


@dataclass
class EduRow:
    """One national education programme."""
    era: int
    programme: str                       # English name
    programme_national: str = ""
    isced: str = ""                      # "0".."9"
    isced_label: str = ""
    isced_p: str = ""                    # 3-digit ISCED-P
    isced_a: str = ""                    # 3-digit ISCED-A
    orientation: str = "na"
    completion: str = "na"
    position: str = ""                   # "First degree", "Long first degree", …
    access: Optional[bool] = None
    access_to: str = ""
    entrance_age: Any = None             # observed, parsed  {min,max,unit}
    duration_years: Any = None           # observed, parsed  {min,max}
    years_in_level: Any = None           # inferred, from the duration
    grades: Any = None                   # inferred, "1-6" | "7" | "-" 
    grade_from: Any = None               # inferred int
    grade_to: Any = None                 # inferred int
    years_before: Any = None             # inferred, years of schooling entering
    years_at_completion: Any = None      # inferred, cumulative years on finishing
    complete_at: str = ""                # the qualification that closes the level
    gmd: str = ""                        # GMD canonical target
    entrance_requirement: str = ""
    entrance_requirement_national: str = ""
    diploma: str = ""
    diploma_national: str = ""
    notes: str = ""
    attainment_on_completion: str = ""   # what finishing this programme confers
    attainment_in_progress: str = ""     # what leaving it part-way confers
    programme_en_source: str = "workbook"   # workbook | isced_standard | absent
    needs_translation: bool = False
    off_ladder: bool = False             # admits across an age band, not a rung
    programme_id: Optional[int] = None
    source_row: Optional[int] = None


@dataclass
class LadderStep:
    """One grade on the national ladder, and what reaching it means.

    This is the table System 10 resolves a cohort against: grade in, ISCED
    level, canonical value and **attainment** out. The attainment is the part
    a survey's highest-education variable actually distinguishes -- reaching
    grade 7 and finishing grade 9 are both "lower secondary" and are not the
    same answer.
    """
    grade: int
    isced: str
    isced_label: str
    gmd: str
    programme: str
    completes_level: bool
    years_at_completion: Optional[float]
    attainment: str = ""                 # primary_complete, …
    attainment_if_left_here: str = ""    # what a person who stopped here has
    isced_a: str = ""                    # the workbook's 3-digit attainment code
    alternatives: List[str] = field(default_factory=list)


@dataclass
class Unmapped:
    where: str
    source_row: Optional[int]
    value: str
    reason: str


@dataclass
class Finding:
    rule: str
    level: str
    message: str
    where: str = ""
    source_row: Optional[int] = None

    def as_dict(self):
        return asdict(self)


@dataclass
class Instruction:
    iso3: str = ""
    country: str = ""
    version: str = "v1.0"
    status: str = "draft"
    domain: str = "education"
    frame: str = "ISCED 2011 - UNESCO UIS national mapping"
    schema: str = SCHEMA
    schema_version: str = SCHEMA_VERSION
    cvs_release: str = CVS_RELEASE
    cohort_aware: bool = True
    era_selector: str = "year_last_in_school"
    fallback_selector: str = "survey_year - (age - theoretical_start_age - grade)"
    owner: str = ""
    note: str = ""
    source: SourceFile = field(default_factory=SourceFile)
    language: Dict[str, Any] = field(default_factory=dict)
    structure: Dict[str, Any] = field(default_factory=dict)
    eras: List[Era] = field(default_factory=list)
    rows: List[EduRow] = field(default_factory=list)
    ladder: List[LadderStep] = field(default_factory=list)
    coverage: Dict[str, Any] = field(default_factory=dict)
    unmapped: List[Unmapped] = field(default_factory=list)

    def filename(self) -> str:
        return f"{self.iso3}_edu_{self.version}.yaml"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema": self.schema,
            "schema_version": self.schema_version,
            "cvs_release": self.cvs_release,
            "country": {"iso3": self.iso3, "name": self.country},
            "version": self.version,
            "status": self.status,
            "domain": self.domain,
            "frame": self.frame,
            "cohort_aware": self.cohort_aware,
            "era_selector": self.era_selector,
            "fallback_selector": self.fallback_selector,
            "owner": self.owner,
            "note": self.note,
            "source": asdict(self.source),
            "language": self.language,
            "structure": self.structure,
            "coverage": self.coverage,
            "eras": [
                {"id": e.id, "label": e.label, "from": e.from_year,
                 "to": e.to_year, "reference_year": e.reference_year,
                 "latest": e.latest, "description": e.description}
                for e in self.eras
            ],
            "rows": [asdict(r) for r in self.rows],
            "ladder": [asdict(s) for s in self.ladder],
            "unmapped": [asdict(u) for u in self.unmapped],
        }

    def to_yaml(self) -> str:
        import yaml
        return yaml.safe_dump(self.to_dict(), sort_keys=False,
                              allow_unicode=True, width=120)

    def content_fingerprint(self) -> str:
        d = self.to_dict()
        for k in ("source", "version", "status", "owner", "note"):
            d.pop(k, None)
        return hashlib.sha256(
            json.dumps(d, sort_keys=True, ensure_ascii=False, default=str)
            .encode()).hexdigest()[:16]
