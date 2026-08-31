"""Resolve source bytes from immutable Git objects and emit a typed proof."""

from pathlib import Path
import os
import subprocess
from typing import Any

from loguru import logger
from pydantic import ValidationError

from extraction_pipeline.hashing import hash_bytes
from schema.extraction.manifest import (
    ResolvedSource,
    ResolvedSourceFile,
    SourceFileEntry,
    SourceManifest,
    source_manifest_sha256,
)


class SourceResolutionError(Exception):
    """A blocking source resolution failure."""


def _validated_manifest(manifest: SourceManifest | dict[str, Any]) -> SourceManifest:
    source = (
        manifest.model_dump()
        if isinstance(manifest, SourceManifest)
        else manifest
    )
    try:
        return SourceManifest.model_validate(source)
    except ValidationError as exc:
        raise SourceResolutionError("Source manifest validation failed") from exc


def resolve_source_directory(
    repository_root: Path,
    manifest: SourceManifest | dict[str, Any],
) -> Path:
    """Validate and return the canonical Git repository root."""
    _validated_manifest(manifest)
    try:
        root = repository_root.resolve(strict=True)
        if not root.is_dir():
            raise SourceResolutionError(
                f"Repository root is not a directory: {repository_root}"
            )
    except SourceResolutionError:
        raise
    except FileNotFoundError as exc:
        raise SourceResolutionError(
            f"Repository root does not exist: {repository_root}"
        ) from exc
    except OSError as exc:
        raise SourceResolutionError(
            f"Unable to resolve repository root: {repository_root}"
        ) from exc
    return root


def _run_git(
    repository_root: Path,
    *arguments: str,
    operation: str,
) -> bytes:
    command = [
        "git",
        "--no-replace-objects",
        "--literal-pathspecs",
        "-C",
        str(repository_root),
        *arguments,
    ]
    environment = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith("GIT_")
    }
    environment.update({"GIT_TERMINAL_PROMPT": "0", "LC_ALL": "C"})
    try:
        result = subprocess.run(
            command,
            shell=False,
            capture_output=True,
            timeout=10,
            check=False,
            env=environment,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SourceResolutionError(f"Unable to {operation}") from exc
    if result.returncode != 0:
        cause = subprocess.CalledProcessError(
            result.returncode,
            result.args,
            result.stdout,
            result.stderr,
        )
        raise SourceResolutionError(f"Git failed to {operation}") from cause
    return result.stdout


def _decode_identity(value: bytes, label: str) -> str:
    try:
        decoded = value.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SourceResolutionError(f"Git returned an invalid {label}") from exc
    identity = decoded.removesuffix("\n")
    if "\n" in identity or "\r" in identity:
        raise SourceResolutionError(f"Git returned an invalid {label}")
    return identity


def _verify_repository(repository_root: Path, manifest: SourceManifest) -> None:
    top_level = _decode_identity(
        _run_git(
            repository_root,
            "rev-parse",
            "--show-toplevel",
            operation="identify the repository root",
        ),
        "repository root",
    )
    try:
        actual_root = Path(top_level).resolve(strict=True)
    except OSError as exc:
        raise SourceResolutionError(
            "Git returned an invalid repository root"
        ) from exc
    if actual_root != repository_root:
        raise SourceResolutionError(
            f"Repository root mismatch: expected {repository_root}, got {actual_root}"
        )

    object_format = _decode_identity(
        _run_git(
            repository_root,
            "rev-parse",
            "--show-object-format",
            operation="identify the Git object format",
        ),
        "Git object format",
    )
    if object_format != "sha1":
        raise SourceResolutionError(
            f"Unsupported Git object format: expected sha1, got {object_format}"
        )

    repository_url = _decode_identity(
        _run_git(
            repository_root,
            "config",
            "--get",
            "remote.origin.url",
            operation="read the origin repository identity",
        ),
        "origin repository identity",
    )
    if repository_url != manifest.repository.url:
        raise SourceResolutionError(
            "Origin repository identity does not match the source manifest"
        )

    object_type = _decode_identity(
        _run_git(
            repository_root,
            "cat-file",
            "-t",
            manifest.repository.commit_sha,
            operation="resolve the explicit source commit",
        ),
        "commit object type",
    )
    if object_type != "commit":
        raise SourceResolutionError("The explicit source identity is not a commit")


def _read_git_blob(
    repository_root: Path,
    commit_sha: str,
    entry: SourceFileEntry,
) -> ResolvedSourceFile:
    tree_output = _run_git(
        repository_root,
        "ls-tree",
        "-z",
        "--full-tree",
        commit_sha,
        "--",
        entry.path,
        operation=f"resolve governed path {entry.path}",
    )
    records = [record for record in tree_output.split(b"\0") if record]
    if len(records) != 1:
        raise SourceResolutionError(
            f"Governed path is missing or ambiguous at the source commit: {entry.path}"
        )
    try:
        metadata, raw_path = records[0].split(b"\t", 1)
        mode, object_type, raw_blob_sha = metadata.split(b" ", 2)
        resolved_path = raw_path.decode("utf-8")
        blob_sha = raw_blob_sha.decode("ascii")
    except (UnicodeDecodeError, ValueError) as exc:
        raise SourceResolutionError(
            f"Invalid Git tree entry for governed path: {entry.path}"
        ) from exc
    if resolved_path != entry.path:
        raise SourceResolutionError(
            f"Git resolved a different governed path: {entry.path}"
        )
    if object_type != b"blob" or mode not in (b"100644", b"100755"):
        raise SourceResolutionError(
            "Governed path must be a regular Git blob, not a symlink or tree: "
            f"{entry.path}"
        )

    content = _run_git(
        repository_root,
        "cat-file",
        "blob",
        blob_sha,
        operation=f"read immutable Git blob for {entry.path}",
    )
    actual_sha256 = hash_bytes(content)
    if actual_sha256 != entry.sha256:
        raise SourceResolutionError(
            f"SHA-256 mismatch for {entry.path}: "
            f"expected {entry.sha256}, got {actual_sha256}"
        )
    try:
        return ResolvedSourceFile(
            path=entry.path,
            scope=entry.scope,
            sha256=actual_sha256,
            blob_sha=blob_sha,
            content=content,
        )
    except ValidationError as exc:
        raise SourceResolutionError(
            f"Invalid Git blob identity for governed path: {entry.path}"
        ) from exc


def _resolve_entries(
    repository_root: Path,
    manifest: SourceManifest,
) -> tuple[list[ResolvedSourceFile], list[ResolvedSourceFile]]:
    _verify_repository(repository_root, manifest)
    source_files = [
        _read_git_blob(
            repository_root,
            manifest.repository.commit_sha,
            entry,
        )
        for entry in manifest.source_files
    ]
    supporting_files = [
        _read_git_blob(
            repository_root,
            manifest.repository.commit_sha,
            entry,
        )
        for entry in manifest.supporting_files
    ]
    return source_files, supporting_files


def verify_source_hashes(
    repository_root: Path,
    manifest: SourceManifest | dict[str, Any],
) -> tuple[list[ResolvedSourceFile], bool]:
    """Verify all selected Git blobs and preserve the legacy success flag."""
    policy = _validated_manifest(manifest)
    root = resolve_source_directory(repository_root, policy)
    source_files, supporting_files = _resolve_entries(root, policy)
    return [*source_files, *supporting_files], True


def resolve_source(
    repository_root: Path,
    manifest: SourceManifest | dict[str, Any],
    resolved_at: str,
) -> ResolvedSource:
    """Read the explicit commit's blobs and return a self-validating proof."""
    policy = _validated_manifest(manifest)
    root = resolve_source_directory(repository_root, policy)
    source_files, supporting_files = _resolve_entries(root, policy)
    try:
        proof = ResolvedSource(
            manifest_version=policy.manifest_version,
            manifest_sha256=source_manifest_sha256(policy),
            repository=policy.repository,
            parser_contract=policy.parser_contract,
            governance=policy.governance,
            resolved_at=resolved_at,
            source_files=source_files,
            supporting_files=supporting_files,
            verified_sha256=True,
        )
    except ValidationError as exc:
        raise SourceResolutionError("ResolvedSource proof validation failed") from exc
    logger.info(
        "Immutable source proof created",
        commit_sha=proof.repository.commit_sha,
        selected_paths=len(proof.source_files) + len(proof.supporting_files),
    )
    return proof


def verify_resolved_source(
    repository_root: Path,
    manifest: SourceManifest,
    proof: ResolvedSource,
) -> ResolvedSource:
    """Rebuild and compare a proof from trusted policy and Git objects."""
    expected = resolve_source(repository_root, manifest, proof.resolved_at)
    if expected != proof:
        raise SourceResolutionError(
            "ResolvedSource proof does not match the source manifest and Git objects"
        )
    return proof
