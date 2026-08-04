"""Strict Pydantic models for extraction manifests — Phase 2 Step 3.

Covers repository identity, locked sources, hashes, parser contract,
governance registries, output allowlists, and resolved-source facts.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator


class RepositoryIdentity(BaseModel):
    """Immutable source repository identity."""

    model_config = ConfigDict(extra="forbid")

    url: str
    commit_sha: str

    @field_validator("url")
    @classmethod
    def url_must_be_https(cls, value: str) -> str:
        if not value.startswith("https://"):
            raise ValueError("Repository URL must use HTTPS")
        return value

    @field_validator("commit_sha")
    @classmethod
    def sha_must_be_40_hex(cls, value: str) -> str:
        if len(value) != 40 or not all(c in "0123456789abcdef" for c in value.lower()):
            raise ValueError("commit_sha must be a 40-character hex string")
        return value.lower()


class SourceFileEntry(BaseModel):
    """A single source file in the manifest."""

    model_config = ConfigDict(extra="forbid")

    path: str
    scope: Literal["included", "supporting", "welfare-excluded"]
    sha256: str | None = None


class ParserContract(BaseModel):
    """Locked parser tool and version."""

    model_config = ConfigDict(extra="forbid")

    tool: str
    version: str
    reader: str
    writer: str
    normalization_version: str


class OutputConfig(BaseModel):
    """Output root and allowlist configuration."""

    model_config = ConfigDict(extra="forbid")

    root: str
    allowlist: list[str]


class GovernanceRefs(BaseModel):
    """References to governance configuration versions."""

    model_config = ConfigDict(extra="forbid")

    module_registry_version: str
    field_classification_version: str
    schema_version: str
    gmd_version: str


class SourceManifest(BaseModel):
    """Complete, validated source manifest."""

    model_config = ConfigDict(extra="forbid")

    manifest_version: str
    repository: RepositoryIdentity
    source_files: list[SourceFileEntry]
    supporting_files: list[SourceFileEntry]
    governance: GovernanceRefs
    parser_contract: ParserContract
    output: OutputConfig


class ResolvedSource(BaseModel):
    """Deterministic source facts after successful resolution."""

    model_config = ConfigDict(extra="forbid")

    manifest_version: str
    repository: RepositoryIdentity
    resolved_at: str  # ISO-8601 timestamp — volatile, goes to run ledger
    source_files: list[SourceFileEntry]
    verified_sha256: bool
