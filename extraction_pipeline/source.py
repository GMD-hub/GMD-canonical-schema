"""Fail-closed resolution of governed source bytes."""

from pathlib import Path
import subprocess
from typing import Any

from loguru import logger

from extraction_pipeline.hashing import hash_file
from schema.extraction.manifest import ResolvedSource, SourceFileEntry


class SourceResolutionError(Exception):
    """A blocking source resolution failure."""


def _governed_entries(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return [*manifest["source_files"], *manifest["supporting_files"]]


def resolve_source_directory(checkout_root: Path, manifest: dict[str, Any]) -> Path:
    """Validate the checkout root and every governed path."""
    try:
        if not checkout_root.exists():
            raise SourceResolutionError(f"Checkout root does not exist: {checkout_root}")
        if not checkout_root.is_dir():
            raise SourceResolutionError(f"Checkout root is not a directory: {checkout_root}")
        root = checkout_root.resolve(strict=True)
    except SourceResolutionError:
        raise
    except OSError as exc:
        raise SourceResolutionError(f"Unable to resolve checkout root: {checkout_root}") from exc
    for entry in _governed_entries(manifest):
        candidate = checkout_root / entry["path"]
        try:
            resolved = candidate.resolve(strict=True)
        except FileNotFoundError as exc:
            raise SourceResolutionError(f"Governed source file not found: {entry['path']}") from exc
        except OSError as exc:
            raise SourceResolutionError(f"Unable to resolve governed source: {entry['path']}") from exc
        if not resolved.is_relative_to(root):
            raise SourceResolutionError(f"Governed source escapes checkout: {entry['path']}")
        if not resolved.is_file():
            raise SourceResolutionError(f"Governed source is not a file: {entry['path']}")
    return root


def _verify_checkout_head(checkout_root: Path, expected: str) -> None:
    try:
        result = subprocess.run(
            ["git", "-C", str(checkout_root), "rev-parse", "--verify", "HEAD"],
            shell=False,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SourceResolutionError("Unable to verify checkout HEAD") from exc
    if result.returncode != 0:
        cause = subprocess.CalledProcessError(result.returncode, result.args, result.stdout, result.stderr)
        raise SourceResolutionError("Git failed while verifying checkout HEAD") from cause
    actual = result.stdout.strip()
    if actual != expected:
        raise SourceResolutionError(f"Checkout HEAD mismatch: expected {expected}, got {actual}")


def verify_source_hashes(
    checkout_root: Path, manifest: dict[str, Any]
) -> tuple[list[SourceFileEntry], list[SourceFileEntry]]:
    """Verify all source and supporting entries without changing order."""
    verified: list[SourceFileEntry] = []
    for entry in _governed_entries(manifest):
        path = checkout_root / entry["path"]
        try:
            actual = hash_file(path)
        except OSError as exc:
            raise SourceResolutionError(f"Unable to read governed source: {entry['path']}") from exc
        if actual != entry["sha256"]:
            raise SourceResolutionError(
                f"SHA-256 mismatch for {entry['path']}: expected {entry['sha256']}, got {actual}"
            )
        verified.append(SourceFileEntry.model_validate(entry))
        logger.info("Governed source hash verified", path=entry["path"])
    source_count = len(manifest["source_files"])
    return verified[:source_count], verified[source_count:]


def resolve_source(
    checkout_root: Path,
    manifest: dict[str, Any],
    resolved_at: str,
) -> ResolvedSource:
    """Prove checkout revision and all governed bytes, then emit facts."""
    root = resolve_source_directory(checkout_root, manifest)
    _verify_checkout_head(root, manifest["repository"]["commit_sha"])
    source_files, supporting_files = verify_source_hashes(root, manifest)
    return ResolvedSource(
        manifest_version=manifest["manifest_version"],
        repository=manifest["repository"],
        resolved_at=resolved_at,
        source_files=source_files,
        supporting_files=supporting_files,
        verified_sha256=True,
    )
