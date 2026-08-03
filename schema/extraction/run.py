"""Extraction run-state and module models — Phase 3 Step 6."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ModuleDefinition(BaseModel):
    """A governed module definition from the extraction registry."""

    model_config = ConfigDict(extra="forbid")

    module_id: str
    module_name: str
    tier: str
    source_chapter: str
    description: str
    provenance: str | None = None  # optional per Decision 9; governance constant


GateResult = Literal["passed", "failed", "blocked", "pending"]


class GateReport(BaseModel):
    """Result of a single gate check."""

    model_config = ConfigDict(extra="forbid")

    gate: str
    result: GateResult
    details: str
    affected_items: list[str] = Field(default_factory=list)


class ContentRunManifest(BaseModel):
    """Content lineage manifest written at finalization."""

    model_config = ConfigDict(extra="forbid")

    execution_id: str
    content_run_id: str
    manifest_version: str
    source_commit_sha: str
    parser_version: str
    normalization_version: str
    governance_versions: dict[str, str]
    agent_response_hashes: list[str]
    finalized_at: str


class RunLedgerEvent(BaseModel):
    """A single volatile event recorded in the run ledger (not content)."""

    model_config = ConfigDict(extra="forbid")

    execution_id: str
    timestamp: str
    event_type: str
    details: str


class CompletenessReport(BaseModel):
    """Machine-readable completeness report for an extraction run.

    Every inventory item must have a disposition (canonical or blocked).
    """

    model_config = ConfigDict(extra="forbid")

    complete: bool
    total_items: int
    canonical_count: int
    blocked_count: int
    undisposed_count: int
    undisposed_ids: list[str] = Field(default_factory=list)
    canonical_ids: list[str] = Field(default_factory=list)
    blocked_ids: list[str] = Field(default_factory=list)
