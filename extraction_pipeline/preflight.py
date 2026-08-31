"""Preflight module — Phase 1 Step 2.

Validates source manifest, parser identity, and extraction preconditions.
Fails loudly on any precondition violation.
"""

from pathlib import Path, PurePosixPath
from typing import Any

import yaml
from loguru import logger
from pydantic import ValidationError

from schema.extraction.manifest import SourceFileEntry, SourceManifest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class PreflightError(Exception):
    """A blocking preflight condition."""


def load_manifest(manifest_path: Path | None = None) -> dict[str, Any]:
    """Load and return the source manifest configuration."""
    if manifest_path is None:
        manifest_path = (
            PROJECT_ROOT
            / "extraction"
            / "config"
            / "source-manifest.v1.yaml"
        )
    if not manifest_path.exists():
        raise PreflightError(f"Source manifest not found: {manifest_path}")
    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise PreflightError("Manifest must be a YAML mapping")
    required = ["manifest_version", "repository", "source_files", "parser_contract", "output"]
    for key in required:
        if key not in data:
            raise PreflightError(f"Manifest missing required key: {key}")
    return data


def check_source_files(manifest: dict[str, Any]) -> None:
    """Verify selected paths, scopes, hashes, and uniqueness generically."""
    source_files = manifest.get("source_files", [])
    supporting_files = manifest.get("supporting_files", [])
    if not isinstance(source_files, list) or not source_files:
        raise PreflightError("Manifest source_files must be a non-empty list")
    if not isinstance(supporting_files, list):
        raise PreflightError("Manifest supporting_files must be a list")

    paths_seen: set[str] = set()
    for raw_entry in (*source_files, *supporting_files):
        try:
            source_file = SourceFileEntry.model_validate(raw_entry)
        except ValidationError as exc:
            raise PreflightError("Invalid source file identity") from exc
        path = source_file.path
        if path in paths_seen:
            raise PreflightError(f"Duplicate source file path: {path}")
        paths_seen.add(path)


def check_parser_contract(manifest: dict[str, Any]) -> None:
    """Verify parser contract has required fields."""
    parser = manifest.get("parser_contract", {})
    if not parser.get("tool"):
        raise PreflightError("Parser contract missing 'tool'")
    if not parser.get("version"):
        raise PreflightError(
            "Parser contract missing 'version'. "
            "Set the approved parser version in the source manifest."
        )
    if not parser.get("reader"):
        raise PreflightError("Parser contract missing 'reader'")
    if not parser.get("writer"):
        raise PreflightError("Parser contract missing 'writer'")


def check_output_allowlist(manifest: dict[str, Any]) -> None:
    """Verify output paths are canonical and contained in the draft root."""
    output = manifest.get("output", {})
    root = output.get("root", "")
    run_root = output.get("run_root", "")
    draft_root = (PROJECT_ROOT / "extraction" / "20_drafts").resolve()

    def resolve_output_path(value: object, label: str) -> Path:
        if not isinstance(value, str) or not value:
            raise PreflightError(f"{label} must be a non-empty relative path")
        without_trailing_slash = value[:-1] if value.endswith("/") else value
        candidate = PurePosixPath(without_trailing_slash)
        if (
            not without_trailing_slash
            or candidate.is_absolute()
            or "\\" in value
            or ".." in candidate.parts
            or candidate.as_posix() != without_trailing_slash
        ):
            raise PreflightError(f"{label} must be a safe repository-relative path")
        resolved = (PROJECT_ROOT / candidate).resolve()
        try:
            resolved.relative_to(draft_root)
        except ValueError as exc:
            raise PreflightError(
                f"{label} must be under extraction/20_drafts/: {value}"
            ) from exc
        return resolved

    resolved_root = resolve_output_path(root, "Output root")
    resolved_run_root = resolve_output_path(run_root, "Run output root")
    try:
        resolved_run_root.relative_to(resolved_root)
    except ValueError as exc:
        raise PreflightError(
            f"Run output root must be inside the output root: {run_root}"
        ) from exc
    resolved_allowlist_roots: list[Path] = []
    for path in output.get("allowlist", []):
        resolved_allowlist = resolve_output_path(path, "Allowlisted path")
        resolved_allowlist_roots.append(resolved_allowlist)
        try:
            resolved_allowlist.relative_to(resolved_root)
        except ValueError as exc:
            raise PreflightError(
                f"Allowlisted path must be inside the output root: {path}"
            ) from exc
    if not any(
        resolved_run_root.is_relative_to(allowlist_root)
        for allowlist_root in resolved_allowlist_roots
    ):
        raise PreflightError("Run output root must be inside the output allowlist")


def check_governance_decisions(manifest: dict[str, Any]) -> None:
    """Verify the manifest declares a non-empty governance section.

    Note: This checks section presence only, not that referenced governance
    artifacts exist on disk. File-existence validation is a future enhancement.
    """
    governance = manifest.get("governance", {})
    if not governance:
        raise PreflightError("Manifest missing 'governance' section")


def check_repository_pin(manifest: dict[str, Any]) -> None:
    """Verify the source repository is pinned to an immutable commit SHA.

    A null or non-40-hex commit_sha means the pipeline cannot guarantee
    deterministic extraction — two runs could resolve different source
    revisions. This is a blocking precondition per AGENTS.md and the
    project charter.
    """
    try:
        SourceManifest.model_validate(manifest)
    except ValidationError as exc:
        raise PreflightError(
            "Source manifest schema validation failed"
        ) from exc


def run_preflight(manifest_path: Path | None = None) -> dict[str, Any]:
    """Run all preflight checks and return the manifest if they pass."""
    logger.info("Starting preflight checks", manifest_path=str(manifest_path))
    manifest = load_manifest(manifest_path)
    check_source_files(manifest)
    try:
        manifest = SourceManifest.model_validate(manifest).model_dump(mode="json")
    except ValidationError as exc:
        raise PreflightError("Source manifest schema validation failed") from exc
    check_parser_contract(manifest)
    check_output_allowlist(manifest)
    check_governance_decisions(manifest)
    check_repository_pin(manifest)
    logger.info("Preflight checks passed", commit_sha=manifest["repository"]["commit_sha"])
    return manifest
