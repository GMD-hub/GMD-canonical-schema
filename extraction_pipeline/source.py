"""Verified source resolution — Phase 2 Step 3.

Resolves source files from a local Git checkout at a pinned commit,
verifies file hashes against the manifest, and emits resolved-source facts.
Never accepts branch names, tags, or symbolic revisions.
"""

from pathlib import Path
from typing import Any

from loguru import logger

from schema.extraction.manifest import ResolvedSource, SourceFileEntry
from extraction_pipeline.hashing import hash_file


class SourceResolutionError(Exception):
    """A blocking source resolution failure."""


def resolve_source_directory(checkout_root: Path, manifest: dict[str, Any]) -> Path:
    """Validate and return the resolved source directory.

    The checkout must be a directory containing all manifest source files.
    """
    if not checkout_root.exists():
        raise SourceResolutionError(f"Checkout root does not exist: {checkout_root}")
    if not checkout_root.is_dir():
        raise SourceResolutionError(f"Checkout root is not a directory: {checkout_root}")

    for entry in manifest.get("source_files", []):
        file_path = checkout_root / entry["path"]
        if not file_path.exists():
            raise SourceResolutionError(f"Source file not found: {entry['path']}")
        if not file_path.is_file():
            raise SourceResolutionError(f"Path is not a file: {entry['path']}")

    return checkout_root.resolve()


def verify_source_hashes(
    checkout_root: Path, manifest: dict[str, Any]
) -> tuple[list[SourceFileEntry], bool]:
    """Verify every manifest source file hash against local content.

    Returns a tuple of (verified entries, all_hashes_matched_against_expected).
    Files with null sha256 in the manifest are hashed and recorded but
    not verified against a pre-existing value. If any expected hash was null,
    the second return value is False, signaling that the source gate should
    not claim full verification.
    """
    verified: list[SourceFileEntry] = []
    all_verified_against_expected = True
    for entry in manifest.get("source_files", []):
        file_path = checkout_root / entry["path"]
        actual_sha256 = hash_file(file_path)
        expected = entry.get("sha256")
        if expected is None:
            all_verified_against_expected = False
            logger.warning(
                "Source file hashed but not verified against expected",
                path=entry["path"],
                sha256=actual_sha256[:12],
            )
        elif actual_sha256 != expected:
            raise SourceResolutionError(
                f"SHA-256 mismatch for {entry['path']}: "
                f"expected {expected[:12]}..., got {actual_sha256[:12]}..."
            )
        else:
            logger.info("Source file hash verified", path=entry["path"])
        verified.append(
            SourceFileEntry(
                path=entry["path"],
                scope=entry["scope"],
                sha256=actual_sha256,
            )
        )
    return verified, all_verified_against_expected


def resolve_source(
    checkout_root: Path,
    manifest: dict[str, Any],
    resolved_at: str,
) -> ResolvedSource:
    """Full source resolution: validate directory, verify hashes, emit facts.

    `verified_sha256` is True only when every source file had a non-null
    expected hash in the manifest that matched the local content. When any
    expected hash was null (hashed but not verified against a pinned value),
    `verified_sha256` is False — the source gate must not pass.
    """
    resolve_source_directory(checkout_root, manifest)
    verified_files, all_verified = verify_source_hashes(checkout_root, manifest)

    return ResolvedSource(
        manifest_version=manifest["manifest_version"],
        repository={
            "url": manifest["repository"]["url"],
            "commit_sha": manifest["repository"]["commit_sha"],
        },
        resolved_at=resolved_at,
        source_files=[f.model_dump() for f in verified_files],
        verified_sha256=all_verified,
    )
