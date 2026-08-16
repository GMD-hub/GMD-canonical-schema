"""Pydantic models for the agent review finding schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Finding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    field: str
    severity: str
    message: str
    line: int | None = None


class AgentSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    errors: int
    warnings: int
    passed: int


class AgentFindings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    agent: str
    artifact_id: str
    checked_at: str
    findings: list[Finding]
    summary: AgentSummary