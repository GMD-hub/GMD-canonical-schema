"""Strict Pydantic models for extraction manifests.

Covers repository identity, locked sources, hashes, parser contract,
governance registries, output allowlists, and resolved-source facts.
"""

from typing import Literal
import re

from pydantic import BaseModel, ConfigDict, field_validator


class RepositoryIdentity(BaseModel):
    """Immutable source repository identity."""

    model_config = ConfigDict(extra="forbid")

    url: str
    commit_sha: str

    @field_validator("url")
    @classmethod
    def url_must_match_governed_repository(cls, value: str) -> str:
        if value != "https://github.com/GMD-hub/GMD-guidelines":
            raise ValueError("Repository URL must match the governed GMD-guidelines URL")
        return value

    @field_validator("commit_sha")
    @classmethod
    def sha_must_be_40_hex(cls, value: str) -> str:
        if not re.fullmatch(r"[0-9a-f]{40}", value):
            raise ValueError("commit_sha must be a lowercase 40-character hexadecimal string")
        return value


class SourceFileEntry(BaseModel):
    """A single source file in the manifest."""

    model_config = ConfigDict(extra="forbid")

    path: str
    scope: Literal["included", "supporting", "welfare-excluded"]
    sha256: str

    @field_validator("sha256")
    @classmethod
    def sha256_must_be_lowercase_hex(cls, value: str) -> str:
        if not re.fullmatch(r"[0-9a-f]{64}", value):
            raise ValueError("sha256 must be a lowercase 64-character hexadecimal string")
        return value


class ParserContract(BaseModel):
    """Locked parser tool and version."""

    model_config = ConfigDict(extra="forbid")

    tool: Literal["pandoc"]
    version: str
    installation_method: str
    reader: str
    writer: str
    normalization_version: str

    @field_validator("version", "installation_method")
    @classmethod
    def identity_fields_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Parser identity fields must be nonblank")
        return value


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

    @field_validator(
        "module_registry_version",
        "field_classification_version",
        "schema_version",
        "gmd_version",
    )
    @classmethod
    def versions_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Governance version references must be nonblank")
        return value


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
    supporting_files: list[SourceFileEntry]
    verified_sha256: bool
