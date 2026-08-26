"""Compile deterministic, source-bound Pydantic Layer 1 attestations.

This artifact is the sole upstream Pydantic authority for the review app.
Aggregate review-agent summaries are intentionally excluded.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import tempfile
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from schema.frontmatter import load_markdown
from schema.variable import VariableDefinition

from .helpers import list_drafts

SCHEMA_VERSION = "1.0"
VALIDATOR_ID = "cvs-pydantic-variable-v1"
EXPECTED_TOTAL = 267
MODULE_COUNTS = {"idn": 9, "geo": 14, "dem": 24, "lbr": 90, "utl": 61, "dwl": 69}
COMPILER_PATH = "extraction_pipeline/review_agents/layer1_attestations.py"


def _run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _generated_at() -> str:
    raw = os.environ.get("SOURCE_DATE_EPOCH")
    if raw is None or not raw.isdigit():
        raise ValueError("SOURCE_DATE_EPOCH must be a non-negative integer")
    return datetime.fromtimestamp(int(raw), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _registry_ids(paths: list[Path], field: str) -> set[str]:
    values: set[str] = set()
    for path in paths:
        data, _ = load_markdown(path)
        value = data.get(field)
        if value:
            values.add(str(value))
    return values


def _manifest_paths(root: Path) -> list[Path]:
    drafts = list_drafts(root / "extraction/20_drafts")
    paths = [root / COMPILER_PATH]
    paths.extend(sorted((root / "schema").rglob("*.py")))
    paths.extend(drafts)
    paths.extend(sorted((root / "knowledge/rules").rglob("*.md")))
    paths.extend(sorted((root / "knowledge/parameters").glob("*.md")))
    return sorted(set(paths), key=lambda path: path.relative_to(root).as_posix())


def compile_attestation(root: Path) -> dict[str, Any]:
    root = root.resolve()
    generated_at = _generated_at()
    drafts = list_drafts(root / "extraction/20_drafts")
    counts: dict[str, int] = {}
    for path in drafts:
        module = path.parent.name
        counts[module] = counts.get(module, 0) + 1
    if len(drafts) != EXPECTED_TOTAL or counts != MODULE_COUNTS:
        raise ValueError(f"draft coverage mismatch: total={len(drafts)}, modules={counts}")

    rule_paths = sorted((root / "knowledge/rules").rglob("*.md"))
    parameter_paths = sorted((root / "knowledge/parameters").glob("*.md"))
    variable_ids = {load_markdown(path)[0]["variable_id"] for path in drafts}
    rule_ids = _registry_ids(rule_paths, "rule_id")
    parameter_ids = _registry_ids(parameter_paths, "parameter_id")

    manifest = []
    for path in _manifest_paths(root):
        relative = path.relative_to(root).as_posix()
        data = path.read_bytes()
        manifest.append({
            "path": relative,
            "git_blob_sha": _run_git(root, "hash-object", relative),
            "content_sha256": _sha256(data),
        })
    manifest_identity = "".join(
        f"{item['path']}|{item['git_blob_sha']}|{item['content_sha256']}\n"
        for item in manifest
    ).encode()

    artifacts = []
    for path in drafts:
        relative = path.relative_to(root).as_posix()
        raw = path.read_bytes()
        data, _ = load_markdown(path)
        failures: list[str] = []
        try:
            VariableDefinition.model_validate(
                data,
                context={
                    "variable_ids": variable_ids,
                    "parameter_ids": parameter_ids,
                    "rule_ids": rule_ids,
                    "allow_unresolved_draft": True,
                },
            )
        except ValidationError as error:
            failures = [item["msg"] for item in error.errors()]
        entry: dict[str, Any] = {
            "artifact_id": data.get("variable_id", path.stem),
            "source_path": relative,
            "source_git_blob_sha": _run_git(root, "hash-object", relative),
            "source_content_sha256": _sha256(raw),
            "pydantic_result": "fail" if failures else "pass",
        }
        if failures:
            entry["failure_details"] = failures
        artifacts.append(entry)

    compiler = next(item for item in manifest if item["path"] == COMPILER_PATH)
    return {
        "schema_version": SCHEMA_VERSION,
        "validator_id": VALIDATOR_ID,
        "validator_code_sha256": compiler["content_sha256"],
        "validation_options": {"allow_unresolved_draft": True},
        "generated_at": generated_at,
        "packages": {"pydantic": version("pydantic"), "pyyaml": version("PyYAML")},
        "context_manifest_sha256": _sha256(manifest_identity),
        "context_manifest": manifest,
        "artifacts": artifacts,
    }


def write_attestation(root: Path, output: Path) -> None:
    payload = yaml.safe_dump(
        compile_attestation(root), sort_keys=False, allow_unicode=False, width=1000
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=output.parent, delete=False
    ) as handle:
        handle.write(payload)
        temporary = Path(handle.name)
    temporary.replace(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    write_attestation(args.root, args.output)


if __name__ == "__main__":
    main()
