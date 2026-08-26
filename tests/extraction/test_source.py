"""Focused checkout revision and governed-byte tests."""

from pathlib import Path
import subprocess
from unittest.mock import Mock

import pytest

import extraction_pipeline.source as source
from extraction_pipeline.hashing import hash_file


PATHS = [
    "chapters/chapter2-IDN.qmd", "chapters/chapter3-GEO.qmd", "chapters/chapter4-DEM.qmd",
    "chapters/chapter5-LMR.qmd", "chapters/chapter6-UTL.qmd", "chapters/chapter7-DWL.qmd",
    "chapters/chapter8-CONS.qmd", "docs/GMD_household_survey_harmonization.md",
]
COMMIT = "a" * 40


@pytest.fixture
def checkout(tmp_path: Path) -> Path:
    root = tmp_path / "checkout"
    for index, path in enumerate(PATHS):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(f"content-{index}".encode())
    return root


@pytest.fixture
def manifest(checkout: Path) -> dict:
    entries = [{"path": path, "scope": "welfare-excluded" if "chapter8" in path else "included", "sha256": hash_file(checkout / path)} for path in PATHS[:7]]
    return {
        "manifest_version": "1.0",
        "repository": {"url": "https://github.com/GMD-hub/GMD-guidelines", "commit_sha": COMMIT},
        "source_files": entries,
        "supporting_files": [{"path": PATHS[7], "scope": "supporting", "sha256": hash_file(checkout / PATHS[7])}],
    }


def git_result(commit: str = COMMIT) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], 0, commit + "\n", "")


def test_resolves_commit_and_all_eight_bytes_in_order(checkout: Path, manifest: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    run = Mock(return_value=git_result())
    monkeypatch.setattr(source.subprocess, "run", run)
    result = source.resolve_source(checkout, manifest, "2026-08-26T12:00:00Z")
    assert result.verified_sha256 is True
    assert [entry.path for entry in result.source_files] == PATHS[:7]
    assert [entry.path for entry in result.supporting_files] == PATHS[7:]
    run.assert_called_once()


@pytest.mark.parametrize("kind,message", [("missing", "does not exist"), ("file", "not a directory")])
def test_invalid_checkout_root(tmp_path: Path, manifest: dict, kind: str, message: str) -> None:
    root = tmp_path / kind
    if kind == "file":
        root.write_text("x", encoding="utf-8")
    with pytest.raises(source.SourceResolutionError, match=message):
        source.resolve_source_directory(root, manifest)


def test_missing_supporting_and_nonfile_source_fail(checkout: Path, manifest: dict) -> None:
    (checkout / PATHS[7]).unlink()
    with pytest.raises(source.SourceResolutionError, match="not found") as caught:
        source.resolve_source_directory(checkout, manifest)
    assert caught.value.__cause__ is not None
    target = checkout / PATHS[7]
    target.mkdir()
    with pytest.raises(source.SourceResolutionError, match="not a file"):
        source.resolve_source_directory(checkout, manifest)


def test_symlink_escape_fails(checkout: Path, manifest: dict, tmp_path: Path) -> None:
    outside = tmp_path / "outside.qmd"
    outside.write_text("outside", encoding="utf-8")
    target = checkout / PATHS[0]
    target.unlink()
    target.symlink_to(outside)
    with pytest.raises(source.SourceResolutionError, match="escapes checkout"):
        source.resolve_source_directory(checkout, manifest)


def test_wrong_head_and_git_failures_block(checkout: Path, manifest: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(source.subprocess, "run", Mock(return_value=git_result("b" * 40)))
    with pytest.raises(source.SourceResolutionError, match="HEAD mismatch"):
        source.resolve_source(checkout, manifest, "now")
    failure = FileNotFoundError("git")
    monkeypatch.setattr(source.subprocess, "run", Mock(side_effect=failure))
    with pytest.raises(source.SourceResolutionError, match="Unable to verify") as caught:
        source.resolve_source(checkout, manifest, "now")
    assert caught.value.__cause__ is failure
    monkeypatch.setattr(source.subprocess, "run", Mock(return_value=subprocess.CompletedProcess([], 1, "", "bad")))
    with pytest.raises(source.SourceResolutionError, match="Git failed") as caught:
        source.resolve_source(checkout, manifest, "now")
    assert isinstance(caught.value.__cause__, subprocess.CalledProcessError)


def test_checkout_head_timeout_is_chained(
    checkout: Path, manifest: dict, monkeypatch: pytest.MonkeyPatch
) -> None:
    failure = subprocess.TimeoutExpired(["git"], 10)
    monkeypatch.setattr(source.subprocess, "run", Mock(side_effect=failure))
    with pytest.raises(source.SourceResolutionError, match="Unable to verify") as caught:
        source.resolve_source(checkout, manifest, "now")
    assert caught.value.__cause__ is failure


def test_hash_mismatch_and_read_failure_are_path_specific(checkout: Path, manifest: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    manifest["source_files"][0]["sha256"] = "f" * 64
    with pytest.raises(source.SourceResolutionError, match=PATHS[0]):
        source.verify_source_hashes(checkout, manifest)
    failure = PermissionError("denied")
    monkeypatch.setattr(source, "hash_file", Mock(side_effect=failure))
    with pytest.raises(source.SourceResolutionError, match="Unable to read") as caught:
        source.verify_source_hashes(checkout, manifest)
    assert caught.value.__cause__ is failure
