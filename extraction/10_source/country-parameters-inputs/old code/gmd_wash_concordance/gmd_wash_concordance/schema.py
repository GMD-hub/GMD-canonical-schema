"""
gmd_wash_concordance.schema
===========================
The fixed target schema for a country WASH instruction (GMD System 9).

The schema is FIXED.  A workbook that carries information the schema cannot
hold produces an entry in ``unmapped`` and a finding, never a new field.
Widening the shape is a System 4 decision, not a country's.

Two conventions carried from the System 1 profile schema:

  * an **observed** field is a plain value;
  * an **inferred** field is ``{value, confidence, evidence}`` and the evidence
    string is non-empty by construction.

Nothing downstream has to consult documentation to know which is which.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional

SCHEMA = "gmd.country_instruction.wash"
SCHEMA_VERSION = "2.0.0"
CVS_RELEASE = "4.8.2"
EXTRACTOR = "gmd_wash_concordance/1.0.0"

# --- controlled vocabularies (System 4 canonical variable schema) -----------
GMD_WATER_SOURCES = [
    "piped", "borehole", "protected_well", "unprotected_well",
    "protected_spring", "unprotected_spring", "rainwater", "bottled",
    "tanker", "surface", "other",
]

GMD_SANITATION_TYPES = [
    "flush_sewer", "flush_septic", "flush_pit", "flush_elsewhere", "vip",
    "pit_slab", "pit_noslab", "composting", "bucket", "hanging", "open",
    "other",
]

# The five JMP rungs.  Fixed by JMP, identical for every country, and NOT
# assignable per row -- a rung is derived downstream from several variables.
WATER_LADDER = [
    {"rung": "Safely managed", "needs": "improved source + on premises + available when needed + free from contamination"},
    {"rung": "Basic",          "needs": "improved source + round trip <= 30 minutes"},
    {"rung": "Limited",        "needs": "improved source + round trip > 30 minutes"},
    {"rung": "Unimproved",     "needs": "unprotected well or unprotected spring"},
    {"rung": "Surface water",  "needs": "river, dam, lake, pond, stream, canal, irrigation channel"},
]

SAN_LADDER = [
    {"rung": "Safely managed",  "needs": "improved facility, not shared + excreta safely disposed in situ or treated off site"},
    {"rung": "Basic",           "needs": "improved facility, not shared"},
    {"rung": "Limited",         "needs": "improved facility shared between two or more households"},
    {"rung": "Unimproved",      "needs": "pit latrine without slab, hanging latrine, bucket latrine"},
    {"rung": "Open defecation", "needs": "disposal in fields, forests, bushes, open water"},
]

STATUSES = ["draft", "in_review", "approved", "superseded", "rejected"]


def inferred(value, confidence: float, evidence: str) -> Dict[str, Any]:
    """An inferred field.  Evidence is mandatory: an inferred value with no
    evidence is a defect, not a value."""
    if not evidence:
        raise ValueError("an inferred field must carry evidence")
    return {"value": value, "confidence": round(float(confidence), 2),
            "evidence": evidence}


# --------------------------------------------------------------------------
@dataclass
class SourceFile:
    file: str = ""
    sha256: str = ""
    profile: str = ""
    language: str = ""
    vintage: str = ""
    extracted_at: str = ""
    extractor: str = EXTRACTOR

    @classmethod
    def of(cls, path, profile, language="", vintage="", now=None):
        h = hashlib.sha256()
        try:
            with open(path, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(chunk)
            digest = h.hexdigest()
        except OSError:
            digest = ""
        return cls(file=os.path.basename(str(path)), sha256=digest,
                   profile=profile, language=language, vintage=str(vintage),
                   extracted_at=now or _dt.datetime.now(_dt.timezone.utc)
                   .replace(microsecond=0).isoformat())


@dataclass
class DataSource:
    """One data source inside the country file -- a survey, census or admin
    series with its own concordance."""
    code: str                       # IND_2016_DHS
    year: Optional[int]
    series: str                     # DHS
    type: str                       # Survey with microdata
    name: str                       # Demographic and Health Survey 2015-16
    column: int                     # first column of the block
    n_rows: int = 0


@dataclass
class WashRow:
    """One national category, mapped onto one JMP class.

    ``improved`` is copied from the JMP master list, never asserted by the
    country -- see rule W-02.  ``rung`` does not exist: the rung is derived
    downstream from several variables, and a row that carried one would be
    asserting something it cannot know.
    """
    code: str                       # stable slug of the national label
    label: str                      # the original denomination, verbatim
    jmp: str                        # JMP class path, e.g. "Ground water > Protected well"
    jmp_id: str                     # stable id of the JMP node
    gmd: str                        # GMD canonical target, "" when it spans several
    spans: List[str] = field(default_factory=list)   # the targets it spans, when gmd is ""
    classification: str = ""        # the JMP classification group, top of the chain
    subgroup: str = ""              # the class inside that group, "" at group level
    depth: int = 0                  # 0 group, 1 class, 2 sub-class, 3 below that
    rolls_up_to: List[str] = field(default_factory=list)  # facility-type aggregates fed
    improved: Optional[bool] = None # from the JMP master list
    improved_from: str = "jmp_master"
    shared: Optional[bool] = None   # service-level attribute, never a facility type
    observed_in: List[str] = field(default_factory=list)   # source codes
    first_seen: Optional[int] = None
    last_seen: Optional[int] = None
    source_row: Optional[int] = None
    jmp_label_local: str = ""       # the JMP label in the workbook's own language
    language: str = ""              # the language that label is written in


@dataclass
class Section:
    """One of the blocks the workbook stacks above the concordance table:
    *Facility type estimates*, *Service level estimate*, *Data used for
    estimates*.  Kept because the chain a reviewer follows runs
    classification -> subgroup -> facility type, and the last link is the
    workbook's own vocabulary, in the workbook's own language."""
    name: str
    name_local: str = ""
    row: Optional[int] = None
    items: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class SourceConcordance:
    """The concordance a single data source supplies, for one domain."""
    source: DataSource
    rows: List[WashRow] = field(default_factory=list)
    data_used: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class Unmapped:
    where: str
    source: str
    source_row: Optional[int]
    value: str
    reason: str


@dataclass
class Finding:
    rule: str
    level: str                      # BLOCK | WARN | INFO
    message: str
    where: str = ""
    source_row: Optional[int] = None

    def as_dict(self):
        return asdict(self)


@dataclass
class Instruction:
    """**One country, one domain, one version.**

    Water and sanitation are separate instructions and separate files. They are
    answered by different survey questions, they move between vintages
    independently, and a focal point signs one without being asked to sign the
    other. Carrying them in one object made a reviewer approve two things at
    once, which is exactly what the approval step is supposed to prevent.
    """
    domain: str = "water"                 # "water" | "sanitation"
    iso3: str = ""
    country: str = ""
    version: str = "v1.0"
    status: str = "draft"
    family: str = "wash"
    frame: str = "JMP service ladders (WHO/UNICEF)"
    schema: str = ""
    schema_version: str = SCHEMA_VERSION
    cvs_release: str = CVS_RELEASE
    language: str = ""                    # the workbook's own language
    owner: str = ""
    note: str = ""
    source: SourceFile = field(default_factory=SourceFile)
    selection: Dict[str, Any] = field(default_factory=dict)
    translation: Dict[str, Any] = field(default_factory=dict)
    sources: List[DataSource] = field(default_factory=list)
    rows: List[WashRow] = field(default_factory=list)
    classifications: List[Dict[str, Any]] = field(default_factory=list)
    facility_types: List[Dict[str, Any]] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
    per_source: List[SourceConcordance] = field(default_factory=list)
    ladder: List[Dict[str, str]] = field(default_factory=list)
    # What JMP published. Deliberately NOT part of to_dict(): the instruction
    # may not carry survey-level data, so this travels in its own artefact.
    benchmark: Dict[str, Any] = field(default_factory=dict)
    vintage: Dict[str, Any] = field(default_factory=dict)
    unmapped: List[Unmapped] = field(default_factory=list)

    def __post_init__(self):
        if not self.schema:
            self.schema = f"{SCHEMA}.{self.domain}"
        if not self.ladder:
            self.ladder = (WATER_LADDER if self.domain == "water"
                           else SAN_LADDER)

    def filename(self) -> str:
        return f"{self.iso3}_{self.domain}_{self.version}.yaml"

    def stem(self) -> str:
        return f"{self.iso3}_{self.domain}"

    # -- serialisation ----------------------------------------------------
    def to_dict(self, per_source: bool = False) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "schema": self.schema,
            "schema_version": self.schema_version,
            "cvs_release": self.cvs_release,
            "country": {"iso3": self.iso3, "name": self.country},
            "domain": self.domain,
            "family": self.family,
            "version": self.version,
            "status": self.status,
            "frame": self.frame,
            "language": self.language,
            "owner": self.owner,
            "note": self.note,
            "source": asdict(self.source),
            "selection": self.selection,
            "translation": self.translation,
            "vintage": self.vintage,
            "sources": [asdict(s) for s in self.sources],
            "classifications": self.classifications,
            "facility_types": self.facility_types,
            "sections": [asdict(x) for x in self.sections],
            "rows": [asdict(r) for r in self.rows],
            "ladder": self.ladder,
            "unmapped": [asdict(u) for u in self.unmapped],
        }
        if per_source:
            d["per_source"] = [
                {"source": asdict(sc.source),
                 "rows": [asdict(r) for r in sc.rows],
                 "data_used": sc.data_used}
                for sc in self.per_source
            ]
        return d

    def to_yaml(self) -> str:
        import yaml
        return yaml.safe_dump(self.to_dict(), sort_keys=False,
                              allow_unicode=True, width=120)

    def content_fingerprint(self) -> str:
        """Hash of the substantive content only.  Re-extracting an unchanged
        workbook produces the same fingerprint, so the registry returns the
        version already in force rather than minting a new one."""
        d = self.to_dict()
        for k in ("source", "version", "status", "owner", "note"):
            d.pop(k, None)
        return hashlib.sha256(
            json.dumps(d, sort_keys=True, ensure_ascii=False, default=str)
            .encode()).hexdigest()[:16]


@dataclass
class Extract:
    """What one workbook yields: the two domain instructions, and the binding
    report they share."""
    iso3: str = ""
    country: str = ""
    language: str = ""
    water: Optional[Instruction] = None
    sanitation: Optional[Instruction] = None

    def instructions(self) -> List[Instruction]:
        return [i for i in (self.water, self.sanitation) if i is not None]
