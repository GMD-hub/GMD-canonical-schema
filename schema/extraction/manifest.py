"""Strict Pydantic models for extraction manifests and source proofs.

Covers repository identity, locked sources, hashes, parser contract,
governance registries, output allowlists, and resolved-source facts.
"""

import hashlib
import json
from pathlib import PurePosixPath
import re
from typing import Literal
from urllib.parse import urlsplit

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


_GIT_SHA1_PATTERN = re.compile(r"[0-9a-f]{40}")
_SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")
_SCOPE_PATTERN = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")


def validate_repository_relative_path(value: str) -> str:
    """Return a canonical safe path or raise ``ValueError``."""
    candidate = PurePosixPath(value)
    if (
        not value
        or value == "."
        or value.startswith("/")
        or "\\" in value
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
        or ".." in candidate.parts
        or candidate.as_posix() != value
    ):
        raise ValueError("path must be a safe canonical repository-relative path")
    return value


class RepositoryIdentity(BaseModel):
    """Immutable source repository identity."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    url: str
    commit_sha: str

    @field_validator("url")
    @classmethod
    def url_must_be_https(cls, value: str) -> str:
        parsed = urlsplit(value)
        if (
            not value.startswith("https://")
            or parsed.scheme != "https"
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.query
            or parsed.fragment
            or parsed.path in ("", "/")
        ):
            raise ValueError(
                "Repository URL must be an HTTPS repository identity without "
                "credentials, query, or fragment"
            )
        return value

    @field_validator("commit_sha")
    @classmethod
    def sha_must_be_40_hex(cls, value: str) -> str:
        if _GIT_SHA1_PATTERN.fullmatch(value) is None:
            raise ValueError(
                "commit_sha must be a lowercase 40-character Git SHA-1"
            )
        return value


class SourceFileEntry(BaseModel):
    """A single source file in the manifest."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    path: str
    scope: str
    sha256: str

    @field_validator("path")
    @classmethod
    def path_must_be_safe(cls, value: str) -> str:
        return validate_repository_relative_path(value)

    @field_validator("scope")
    @classmethod
    def scope_must_be_generic_identifier(cls, value: str) -> str:
        if _SCOPE_PATTERN.fullmatch(value) is None:
            raise ValueError("scope must be a lowercase kebab-case identifier")
        return value

    @field_validator("sha256")
    @classmethod
    def sha256_must_be_lowercase_hex(cls, value: str) -> str:
        if _SHA256_PATTERN.fullmatch(value) is None:
            raise ValueError("sha256 must be a lowercase 64-character identity")
        return value


class ParserContract(BaseModel):
    """Locked parser tool and version."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    tool: str
    version: str
    reader: str
    writer: str
    normalization_version: str

    @field_validator("tool", "version", "reader", "writer", "normalization_version")
    @classmethod
    def identity_fields_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Parser identity fields must be nonblank")
        return value


class OutputConfig(BaseModel):
    """Output root and allowlist configuration."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    root: str
    run_root: str
    allowlist: list[str]


class GovernanceRefs(BaseModel):
    """References to governance configuration versions."""

    model_config = ConfigDict(extra="forbid", frozen=True)

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
            raise ValueError("Governance identity fields must be nonblank")
        return value


class SourceManifest(BaseModel):
    """Complete, validated source manifest."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    manifest_version: str
    repository: RepositoryIdentity
    source_files: tuple[SourceFileEntry, ...]
    supporting_files: tuple[SourceFileEntry, ...]
    governance: GovernanceRefs
    parser_contract: ParserContract
    output: OutputConfig

    @field_validator("manifest_version")
    @classmethod
    def manifest_version_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("manifest_version must be nonblank")
        return value

    @model_validator(mode="after")
    def selected_paths_must_be_unique(self) -> "SourceManifest":
        if not self.source_files:
            raise ValueError("source_files must select at least one path")
        paths = [
            entry.path for entry in (*self.source_files, *self.supporting_files)
        ]
        if len(paths) != len(set(paths)):
            raise ValueError("selected source paths must be unique")
        return self


def source_manifest_sha256(
    manifest: SourceManifest | dict[str, object],
) -> str:
    """Return the canonical SHA-256 identity of a complete source manifest."""
    policy = SourceManifest.model_validate(manifest)
    serialized = json.dumps(
        policy.model_dump(mode="json"),
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("ascii")
    return hashlib.sha256(serialized).hexdigest()


class ResolvedSourceFile(SourceFileEntry):
    """One verified regular Git blob and its immutable content."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        ser_json_bytes="base64",
        val_json_bytes="base64",
    )

    blob_sha: str
    content: bytes

    @field_validator("blob_sha")
    @classmethod
    def blob_sha_must_be_40_hex(cls, value: str) -> str:
        if _GIT_SHA1_PATTERN.fullmatch(value) is None:
            raise ValueError("blob_sha must be a lowercase 40-character Git SHA-1")
        return value

    @model_validator(mode="after")
    def content_must_match_identities(self) -> "ResolvedSourceFile":
        actual_sha256 = hashlib.sha256(self.content).hexdigest()
        if actual_sha256 != self.sha256:
            raise ValueError("content does not match sha256 identity")

        git_blob = f"blob {len(self.content)}\0".encode("ascii") + self.content
        actual_blob_sha = hashlib.sha1(
            git_blob, usedforsecurity=False
        ).hexdigest()
        if actual_blob_sha != self.blob_sha:
            raise ValueError("content does not match Git blob identity")
        return self


class ResolvedSource(BaseModel):
    """Self-validating proof of immutable source bytes and policy identities."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        ser_json_bytes="base64",
        val_json_bytes="base64",
    )

    proof_version: Literal["1.0"] = "1.0"
    manifest_version: str
    manifest_sha256: str
    repository: RepositoryIdentity
    parser_contract: ParserContract
    governance: GovernanceRefs
    resolved_at: str
    source_files: tuple[ResolvedSourceFile, ...]
    supporting_files: tuple[ResolvedSourceFile, ...] = ()
    verified_sha256: Literal[True]

    @field_validator("manifest_version", "resolved_at")
    @classmethod
    def proof_identity_fields_must_be_nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Source proof identity fields must be nonblank")
        return value

    @field_validator("manifest_sha256")
    @classmethod
    def manifest_sha256_must_be_lowercase_hex(cls, value: str) -> str:
        if _SHA256_PATTERN.fullmatch(value) is None:
            raise ValueError(
                "manifest_sha256 must be a lowercase 64-character identity"
            )
        return value

    @model_validator(mode="after")
    def proof_must_be_complete_and_unique(self) -> "ResolvedSource":
        if not self.source_files:
            raise ValueError("source proof must contain at least one source file")
        paths = [
            entry.path for entry in (*self.source_files, *self.supporting_files)
        ]
        if len(paths) != len(set(paths)):
            raise ValueError("resolved source paths must be unique")
        return self

    def get_bytes(self, path: str) -> bytes:
        """Return the exact verified bytes for one selected path."""
        return self.get_file(path).content

    def get_file(self, path: str) -> ResolvedSourceFile:
        """Return the verified file proof for one selected path."""
        for entry in (*self.source_files, *self.supporting_files):
            if entry.path == path:
                return entry
        raise KeyError(f"Path is not present in the resolved source proof: {path}")

    def proof_sha256(self) -> str:
        """Return a deterministic digest that binds all proof facts and bytes."""
        serialized = json.dumps(
            self.model_dump(mode="json"),
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("ascii")
        return hashlib.sha256(serialized).hexdigest()
