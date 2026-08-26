"""Fail-closed extraction source preflight validation."""

from pathlib import Path, PurePosixPath
import re
import subprocess
from typing import Any

from loguru import logger
from pydantic import ValidationError
import yaml

from schema.extraction.manifest import SourceManifest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST_PATH = PROJECT_ROOT / "extraction/config/source-manifest.v1.yaml"
DEFAULT_GOVERNANCE_PATH = PROJECT_ROOT / "extraction/config/extraction-governance.v1.yaml"
EXPECTED_SOURCE_FILES = [
    ("chapters/chapter2-IDN.qmd", "included"),
    ("chapters/chapter3-GEO.qmd", "included"),
    ("chapters/chapter4-DEM.qmd", "included"),
    ("chapters/chapter5-LMR.qmd", "included"),
    ("chapters/chapter6-UTL.qmd", "included"),
    ("chapters/chapter7-DWL.qmd", "included"),
    ("chapters/chapter8-CONS.qmd", "welfare-excluded"),
]
EXPECTED_SUPPORTING_FILES = [
    ("docs/GMD_household_survey_harmonization.md", "supporting")
]
EXPECTED_INCLUDED_PATHS = [path for path, scope in EXPECTED_SOURCE_FILES if scope == "included"]


class PreflightError(Exception):
    """A blocking preflight condition."""


def _load_yaml_mapping(path: Path, label: str) -> dict[str, Any]:
    try:
        if not path.exists():
            raise PreflightError(f"{label} not found: {path}")
        if not path.is_file():
            raise PreflightError(f"{label} is not a file: {path}")
        text = path.read_text(encoding="utf-8")
    except PreflightError:
        raise
    except (OSError, UnicodeError) as exc:
        raise PreflightError(f"Unable to read {label}: {path}") from exc
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise PreflightError(f"Invalid YAML in {label}: {path}") from exc
    if not isinstance(data, dict):
        raise PreflightError(f"{label} must be a YAML mapping")
    return data


def load_manifest(manifest_path: Path | None = None) -> dict[str, Any]:
    """Load, validate, and normalize the source manifest."""
    path = manifest_path or DEFAULT_MANIFEST_PATH
    data = _load_yaml_mapping(path, "Source manifest")
    try:
        return SourceManifest.model_validate(data).model_dump(mode="json")
    except ValidationError as exc:
        raise PreflightError(f"Source manifest schema validation failed: {path}") from exc


def _validate_safe_path(path: str) -> None:
    candidate = PurePosixPath(path)
    if candidate.is_absolute() or ".." in candidate.parts or str(candidate) != path:
        raise PreflightError(f"Unsafe governed path: {path}")


def check_source_files(manifest: dict[str, Any]) -> None:
    """Enforce exact paths, scopes, ordering, uniqueness, and path safety."""
    source = [(entry["path"], entry["scope"]) for entry in manifest["source_files"]]
    supporting = [
        (entry["path"], entry["scope"]) for entry in manifest["supporting_files"]
    ]
    paths = [path for path, _ in source + supporting]
    if len(paths) != len(set(paths)):
        raise PreflightError("Duplicate governed path across source and supporting files")
    for path in paths:
        _validate_safe_path(path)
    if source != EXPECTED_SOURCE_FILES:
        raise PreflightError("source_files must match the exact governed order and scopes")
    if supporting != EXPECTED_SUPPORTING_FILES:
        raise PreflightError("supporting_files must contain the canonical Markdown source")


def check_parser_contract(manifest: dict[str, Any]) -> None:
    """Require the installed Pandoc runtime to match exactly."""
    parser = manifest["parser_contract"]
    try:
        result = subprocess.run(
            [parser["tool"], "--version"],
            shell=False,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise PreflightError("Unable to execute the governed Pandoc runtime") from exc
    if result.returncode != 0:
        cause = subprocess.CalledProcessError(result.returncode, result.args, result.stdout, result.stderr)
        raise PreflightError("Pandoc version command failed") from cause
    first_line = result.stdout.splitlines()[0] if result.stdout.splitlines() else ""
    match = re.fullmatch(r"pandoc ([0-9]+(?:\.[0-9]+){1,3})", first_line)
    if match is None:
        raise PreflightError(f"Malformed Pandoc version output: {first_line!r}")
    if match.group(1) != parser["version"]:
        raise PreflightError(
            f"Pandoc version mismatch: expected {parser['version']}, got {match.group(1)}"
        )


def check_output_allowlist(manifest: dict[str, Any]) -> None:
    """Verify output configuration is within allowed draft paths."""
    output = manifest["output"]
    allowed_root = PurePosixPath("extraction/20_drafts")

    def require_draft_path(path: str, label: str) -> None:
        candidate = PurePosixPath(path)
        canonical = candidate.as_posix()
        if (
            candidate.is_absolute()
            or ".." in candidate.parts
            or path not in (canonical, f"{canonical}/")
            or candidate != allowed_root
            and not candidate.is_relative_to(allowed_root)
        ):
            raise PreflightError(f"{label} must be extraction/20_drafts or a descendant: {path}")

    require_draft_path(output["root"], "Output root")
    for path in output["allowlist"]:
        require_draft_path(path, "Allowlisted path")


def check_governance(manifest: dict[str, Any], governance: dict[str, Any]) -> None:
    """Cross-check governed versions and ordered module source paths."""
    for key in ("schema_version", "gmd_version"):
        value = governance.get(key)
        if not isinstance(value, str) or not value.strip():
            raise PreflightError(f"Governance {key} must be nonblank")
        if manifest["governance"][key] != value:
            raise PreflightError(f"Manifest/governance {key} mismatch")
    modules = governance.get("modules")
    if not isinstance(modules, list):
        raise PreflightError("Governance modules must be a list")
    paths = [module.get("source_chapter") if isinstance(module, dict) else None for module in modules]
    if paths != EXPECTED_INCLUDED_PATHS:
        raise PreflightError("Governance module source paths do not match included chapters")


def run_preflight(
    manifest_path: Path | None = None,
    governance_path: Path | None = None,
) -> dict[str, Any]:
    """Validate source identity, governance, output, and parser runtime."""
    manifest_path = manifest_path or DEFAULT_MANIFEST_PATH
    governance_path = governance_path or DEFAULT_GOVERNANCE_PATH
    logger.info("Starting extraction source preflight", manifest_path=str(manifest_path))
    manifest = load_manifest(manifest_path)
    governance = _load_yaml_mapping(governance_path, "Extraction governance")
    check_source_files(manifest)
    check_output_allowlist(manifest)
    check_governance(manifest, governance)
    check_parser_contract(manifest)
    logger.info("Extraction source preflight passed", commit_sha=manifest["repository"]["commit_sha"])
    return manifest
