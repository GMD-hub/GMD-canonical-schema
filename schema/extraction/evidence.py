"""Extraction evidence models — Phase 3 Step 6.

Strict Pydantic models for citations, claim-evidence links, evidence packets,
and evidence validation.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict


class Citation(BaseModel):
    """A single citation linking a claim to source evidence."""

    model_config = ConfigDict(extra="forbid")

    citation_id: str
    source_path: str
    node_id: str
    heading_anchor: str
    line_start: int
    line_end: int
    excerpt: str
    excerpt_sha256: str
    evidence_role: Literal["defines", "constrains", "exemplifies", "references"]


class EvidencePacket(BaseModel):
    """Bounded evidence packet for extraction agent consumption."""

    model_config = ConfigDict(extra="forbid")

    inventory_id: str
    module_code: str
    variable_name: str
    citations: list[Citation]
    source_document: str
    extraction_method_version: str


class CitationValidation(BaseModel):
    """Result of validating a single citation against pinned source bytes.

    On success, ``valid`` is True and ``line_start``/``line_end``/``source_path``
    are populated. On failure, ``valid`` is False and ``error`` describes
    the problem.
    """

    model_config = ConfigDict(extra="forbid")

    valid: bool
    line_start: int | None = None
    line_end: int | None = None
    source_path: str | None = None
    error: str | None = None
