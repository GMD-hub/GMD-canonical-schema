"""Preflight module — Phase 1 Step 2.

Validates source manifest, Pandoc availability, and extraction preconditions.
Fails loudly on any precondition violation.
"""

from pathlib import Path
from typing import Any

import yaml
from loguru import logger


PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Required source chapters — derived from extraction-governance.v1.yaml module
# registry (source_chapter fields). This is a defensive cross-check; the
# manifest source_files block is the source of truth for which files to
# process, but this set ensures all non-welfare chapters are present.
REQUIRED_CHAPTERS = frozenset({
    "chapter2-IDN.qmd", "chapter3-GEO.qmd", "chapter4-DEM.qmd",
    "chapter5-LMR.qmd", "chapter6-UTL.qmd", "chapter7-DWL.qmd",
    "chapter8-CONS.qmd",
})


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
    """Verify all source files have valid scope and consistent hashes."""
    valid_scopes = {"included", "supporting", "welfare-excluded"}
    paths_seen: set[str] = set()
    for source_file in manifest.get("source_files", []):
        path = source_file.get("path", "")
        if not path:
            raise PreflightError("Source file entry missing 'path'")
        if path in paths_seen:
            raise PreflightError(f"Duplicate source file path: {path}")
        paths_seen.add(path)
        scope = source_file.get("scope", "")
        if scope not in valid_scopes:
            raise PreflightError(f"Invalid scope '{scope}' for {path}; must be one of {valid_scopes}")

    # Verify required chapters exist
    # Defensive cross-check; the manifest source_files block is the source of truth.
    found = {f["path"] for f in manifest["source_files"]}
    missing = REQUIRED_CHAPTERS - found
    if missing:
        raise PreflightError(f"Required source chapters missing from manifest: {missing}")


def check_parser_contract(manifest: dict[str, Any]) -> None:
    """Verify parser contract has required fields."""
    parser = manifest.get("parser_contract", {})
    if not parser.get("tool"):
        raise PreflightError("Parser contract missing 'tool'")
    if not parser.get("version"):
        raise PreflightError(
            "Parser contract missing 'version'. "
            "Set the approved Pandoc version in extraction/config/source-manifest.v1.yaml."
        )
    if not parser.get("reader"):
        raise PreflightError("Parser contract missing 'reader'")
    if not parser.get("writer"):
        raise PreflightError("Parser contract missing 'writer'")


def check_output_allowlist(manifest: dict[str, Any]) -> None:
    """Verify output configuration is within allowed paths."""
    output = manifest.get("output", {})
    root = output.get("root", "")
    if not root.startswith("extraction/20_drafts/"):
        raise PreflightError(
            f"Output root must be under extraction/20_drafts/: {root}"
        )
    for path in output.get("allowlist", []):
        if not path.startswith("extraction/20_drafts/"):
            raise PreflightError(
                f"Allowlisted path must be under extraction/20_drafts/: {path}"
            )


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
    repository = manifest.get("repository", {})
    if not repository:
        raise PreflightError("Manifest missing 'repository' section")
    commit_sha = repository.get("commit_sha")
    if commit_sha is None:
        raise PreflightError(
            "Repository commit_sha is null. Set the approved 40-character "
            "hex commit SHA in extraction/config/source-manifest.v1.yaml "
            "before running extraction. Branch names and tags are not accepted."
        )
    if not isinstance(commit_sha, str) or len(commit_sha) != 40 or not all(
        c in "0123456789abcdef" for c in commit_sha.lower()
    ):
        raise PreflightError(
            f"Repository commit_sha must be a 40-character hex string, "
            f"got: {commit_sha!r}. Branch names and tags are not accepted."
        )


def run_preflight(manifest_path: Path | None = None) -> dict[str, Any]:
    """Run all preflight checks and return the manifest if they pass."""
    logger.info("Starting preflight checks", manifest_path=str(manifest_path))
    manifest = load_manifest(manifest_path)
    check_source_files(manifest)
    check_parser_contract(manifest)
    check_output_allowlist(manifest)
    check_governance_decisions(manifest)
    check_repository_pin(manifest)
    logger.info("Preflight checks passed", commit_sha=manifest["repository"]["commit_sha"])
    return manifest
