"""Extraction evidence models — Phase 3 Step 6.

Strict Pydantic models for citations, claim-evidence links, evidence packets,
and evidence validation.
"""

import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from schema.extraction.manifest import validate_repository_relative_path


_GIT_SHA1_PATTERN = re.compile(r"[0-9a-f]{40}")
_SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")


class CitationInput(BaseModel):
    """Strict citation claim that must be checked against proof bytes."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    citation_id: str
    source_path: str
    excerpt: str
    expected_excerpt_sha256: str

    @field_validator("citation_id", "excerpt")
    @classmethod
    def text_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("citation_id and excerpt must be nonblank")
        return value

    @field_validator("source_path")
    @classmethod
    def source_path_must_be_safe(cls, value: str) -> str:
        return validate_repository_relative_path(value)

    @field_validator("expected_excerpt_sha256")
    @classmethod
    def excerpt_sha256_must_be_valid(cls, value: str) -> str:
        if _SHA256_PATTERN.fullmatch(value) is None:
            raise ValueError(
                "expected_excerpt_sha256 must be a lowercase 64-character identity"
            )
        return value


class VerifiedCitation(BaseModel):
    """Citation whose hash and line bounds were checked against proof bytes."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    citation_id: str
    source_path: str
    excerpt: str
    excerpt_sha256: str
    line_start: int
    line_end: int

    @field_validator("citation_id", "excerpt")
    @classmethod
    def verified_text_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Verified citation text fields must be nonblank")
        return value

    @field_validator("source_path")
    @classmethod
    def verified_path_must_be_safe(cls, value: str) -> str:
        return validate_repository_relative_path(value)

    @field_validator("excerpt_sha256")
    @classmethod
    def verified_excerpt_sha256_must_be_valid(cls, value: str) -> str:
        if _SHA256_PATTERN.fullmatch(value) is None:
            raise ValueError("Verified citation SHA-256 identity is invalid")
        return value

    @model_validator(mode="after")
    def line_bounds_must_be_valid(self) -> "VerifiedCitation":
        if self.line_start < 1 or self.line_end < self.line_start:
            raise ValueError("Verified citation line bounds are invalid")
        return self


class CollectedEvidencePacket(BaseModel):
    """Evidence identities and citations bound to one source proof."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    inventory_id: str
    source_path: str
    source_sha256: str
    source_blob_sha: str
    source_commit_sha: str
    source_proof_sha256: str
    citations: tuple[VerifiedCitation, ...]

    @field_validator("inventory_id")
    @classmethod
    def inventory_id_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("inventory_id must be nonblank")
        return value

    @field_validator("source_path")
    @classmethod
    def packet_path_must_be_safe(cls, value: str) -> str:
        return validate_repository_relative_path(value)

    @field_validator("source_sha256", "source_proof_sha256")
    @classmethod
    def sha256_identities_must_be_valid(cls, value: str) -> str:
        if _SHA256_PATTERN.fullmatch(value) is None:
            raise ValueError("Evidence SHA-256 identities must be lowercase and complete")
        return value

    @field_validator("source_blob_sha", "source_commit_sha")
    @classmethod
    def git_identities_must_be_valid(cls, value: str) -> str:
        if _GIT_SHA1_PATTERN.fullmatch(value) is None:
            raise ValueError("Evidence Git identities must be lowercase SHA-1 values")
        return value

    @model_validator(mode="after")
    def citations_must_be_present_and_unique(self) -> "CollectedEvidencePacket":
        if not self.citations:
            raise ValueError("Evidence packet must contain at least one citation")
        citation_ids = [citation.citation_id for citation in self.citations]
        if len(citation_ids) != len(set(citation_ids)):
            raise ValueError("Evidence citation IDs must be unique")
        if any(citation.source_path != self.source_path for citation in self.citations):
            raise ValueError("Evidence citations must use the packet source_path")
        return self


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
