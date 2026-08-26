"""Strict contracts for the versioned non-welfare inventory ledger."""

from __future__ import annotations

import hashlib
import re
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from schema.extraction.evidence import Citation

_VARIABLE_ID = re.compile(r"^VAR-[a-z][a-z0-9]*$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_SHA1 = re.compile(r"^[0-9a-f]{40}$")
_MODULES = {"MOD-IDN", "MOD-GEO", "MOD-DEM", "MOD-LBR", "MOD-UTL", "MOD-DWL"}
_CHAPTER_PATHS = {
    "chapters/chapter2-IDN.qmd",
    "chapters/chapter3-GEO.qmd",
    "chapters/chapter4-DEM.qmd",
    "chapters/chapter5-LMR.qmd",
    "chapters/chapter6-UTL.qmd",
    "chapters/chapter7-DWL.qmd",
    "chapters/chapter8-CONS.qmd",
}
_SOURCE_REPOSITORY = "https://github.com/GMD-hub/GMD-guidelines.git"


class RowDisposition(StrEnum):
    """Closed classification set for source occurrences."""

    CANONICAL_OUTPUT = "canonical_output"
    SHARED_IDENTIFIER_OCCURRENCE = "shared_identifier_occurrence"
    HELPER_OR_METADATA = "helper_or_metadata"
    WELFARE_EXCLUDED = "welfare_excluded"
    INVENTORY_ONLY = "inventory_only"
    UNRESOLVED_SOURCE_DISCREPANCY = "unresolved_source_discrepancy"


class SourceReference(BaseModel):
    """Stable source and occurrence identity."""

    model_config = ConfigDict(extra="forbid")

    source_name: str
    source_path: str
    table_key: str
    occurrence_key: str

    @field_validator("source_path")
    @classmethod
    def source_path_is_governed(cls, value: str) -> str:
        if not value.startswith("chapters/") or not value.endswith(".qmd"):
            raise ValueError("source_path must be a governed chapter path")
        return value


class InventoryOccurrence(BaseModel):
    """One classified occurrence from an authoritative source table."""

    model_config = ConfigDict(extra="forbid")

    occurrence_id: str
    occurrence_key: str
    source: SourceReference
    raw_name: str
    variable_id: str | None
    owner_module: str | None
    occurrence_module: str
    tier: int | None
    derivation_status: str
    disposition: RowDisposition
    counts_toward_denominator: bool
    citation: Citation
    draft_path: str | None
    reason: str | None

    @model_validator(mode="after")
    def validate_invariants(self) -> "InventoryOccurrence":
        if self.occurrence_key != self.source.occurrence_key:
            raise ValueError("occurrence_key must match source occurrence_key")
        if self.counts_toward_denominator != (
            self.disposition == RowDisposition.CANONICAL_OUTPUT
        ):
            raise ValueError("counts_toward_denominator must be true exactly for canonical_output")
        if self.variable_id is not None and not _VARIABLE_ID.fullmatch(self.variable_id):
            raise ValueError("variable_id must match ^VAR-[a-z][a-z0-9]*$")
        if self.disposition in {
            RowDisposition.CANONICAL_OUTPUT,
            RowDisposition.SHARED_IDENTIFIER_OCCURRENCE,
        } and (self.variable_id is None or self.owner_module not in _MODULES):
            raise ValueError("canonical/shared rows require a variable_id and valid owner")
        if self.disposition == RowDisposition.CANONICAL_OUTPUT and not self.draft_path:
            raise ValueError("canonical rows require a draft_path")
        if "chapter8-CONS.qmd" in self.source.source_path and self.disposition != RowDisposition.WELFARE_EXCLUDED:
            raise ValueError("Chapter 8 rows must be welfare_excluded")
        return self

    def validate_citation(self, source_bytes: bytes) -> None:
        """Validate line bounds, excerpt, path identity, and excerpt digest."""
        lines = source_bytes.decode("utf-8").splitlines()
        start, end = self.citation.line_start, self.citation.line_end
        if start < 1 or end < start or end > len(lines):
            raise ValueError("citation line bounds are outside source bytes")
        excerpt = "\n".join(lines[start - 1 : end])
        if excerpt != self.citation.excerpt:
            raise ValueError("citation excerpt does not match immutable source bytes")
        digest = hashlib.sha256(excerpt.encode("utf-8")).hexdigest()
        if digest != self.citation.excerpt_sha256:
            raise ValueError("citation excerpt SHA-256 mismatch")
        if self.citation.source_path != self.source.source_path:
            raise ValueError("citation source_path does not match occurrence source")


class ModuleCount(BaseModel):
    """Canonical denominator contribution for one owner module."""

    model_config = ConfigDict(extra="forbid")

    module: Literal["MOD-IDN", "MOD-GEO", "MOD-DEM", "MOD-LBR", "MOD-UTL", "MOD-DWL"]
    count: int


class InventoryDiscrepancy(BaseModel):
    """A count claim that is not an authoritative source occurrence."""

    model_config = ConfigDict(extra="forbid")

    discrepancy_id: str
    module: str
    claimed_count: int
    resolved_count: int
    status: Literal["retired_non_counting"]
    claim_citation: Citation
    claim_repository_commit: str
    claim_blob_sha256: str
    decision_reference: str
    decision_sha256: str
    explanation: str

    @field_validator("decision_sha256")
    @classmethod
    def decision_hash_is_sha256(cls, value: str) -> str:
        if not _SHA256.fullmatch(value):
            raise ValueError("decision_sha256 must be lowercase SHA-256")
        return value

    @field_validator("claim_blob_sha256")
    @classmethod
    def claim_blob_hash_is_sha256(cls, value: str) -> str:
        if not _SHA256.fullmatch(value):
            raise ValueError("claim_blob_sha256 must be lowercase SHA-256")
        return value

    @field_validator("claim_repository_commit")
    @classmethod
    def claim_commit_is_sha1(cls, value: str) -> str:
        if not _SHA1.fullmatch(value):
            raise ValueError("claim_repository_commit must be lowercase Git SHA-1")
        return value


class InventoryLedger(BaseModel):
    """Validated deterministic v1 inventory ledger."""

    model_config = ConfigDict(extra="forbid")

    inventory_version: Literal["v1"]
    status: Literal["draft_pending_human_inventory_review"]
    source_identity_status: Literal["pending_task_b_approval"]
    source_commit: str
    source_repository: Literal["https://github.com/GMD-hub/GMD-guidelines.git"]
    chapter_sha256: dict[str, str]
    normalization_contract: Literal["v1"]
    toolchain: dict[str, str]
    approval_plan: str
    approval_record_sha256: str
    denominator_decision_sha256: str
    source_row_count: int
    non_counting_row_count: int
    denominator: int
    module_counts: list[ModuleCount]
    occurrences: list[InventoryOccurrence]
    discrepancies: list[InventoryDiscrepancy]

    @field_validator("approval_record_sha256", "denominator_decision_sha256")
    @classmethod
    def section_hash_is_sha256(cls, value: str) -> str:
        if not _SHA256.fullmatch(value):
            raise ValueError("section hash must be lowercase SHA-256")
        return value

    @field_validator("source_commit")
    @classmethod
    def source_commit_is_sha1(cls, value: str) -> str:
        if not _SHA1.fullmatch(value):
            raise ValueError("source_commit must be lowercase Git SHA-1")
        return value

    @field_validator("chapter_sha256")
    @classmethod
    def chapter_hashes_are_complete(cls, value: dict[str, str]) -> dict[str, str]:
        if set(value) != _CHAPTER_PATHS:
            raise ValueError("chapter_sha256 must contain the seven governed chapter paths")
        if any(not _SHA256.fullmatch(digest) for digest in value.values()):
            raise ValueError("chapter_sha256 values must be lowercase SHA-256")
        return value

    @model_validator(mode="after")
    def validate_totals_and_uniqueness(self) -> "InventoryLedger":
        occurrence_ids = [row.occurrence_id for row in self.occurrences]
        occurrence_keys = [row.occurrence_key for row in self.occurrences]
        if len(occurrence_ids) != len(set(occurrence_ids)):
            raise ValueError("duplicate occurrence ID")
        if len(occurrence_keys) != len(set(occurrence_keys)):
            raise ValueError("duplicate occurrence key")
        canonical = [row for row in self.occurrences if row.disposition == RowDisposition.CANONICAL_OUTPUT]
        canonical_ids = [row.variable_id for row in canonical]
        if len(canonical_ids) != len(set(canonical_ids)):
            raise ValueError("duplicate canonical normalized ID")
        true_count = sum(row.counts_toward_denominator for row in self.occurrences)
        aggregate = sum(item.count for item in self.module_counts)
        if not (len(canonical) == true_count == aggregate == self.denominator):
            raise ValueError("canonical, true-count, aggregate, and denominator totals must match")
        aggregate_modules = [item.module for item in self.module_counts]
        if len(aggregate_modules) != len(set(aggregate_modules)):
            raise ValueError("duplicate module count")
        actual_by_owner = {
            module: sum(row.owner_module == module for row in canonical)
            for module in _MODULES
        }
        declared_by_owner = {item.module: item.count for item in self.module_counts}
        if declared_by_owner != actual_by_owner:
            raise ValueError("module counts must match canonical owner_module totals")
        return self
