from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from extraction_pipeline.review_agents.layer1_attestations import (
    EXPECTED_TOTAL,
    compile_attestation,
    write_attestation,
)
import extraction_pipeline.review_agents.layer1_attestations as compiler


ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def controlled_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    root = tmp_path / "repo"
    source = next((ROOT / "extraction/20_drafts/dem").glob("VAR-*.md"))
    targets = [
        (source, root / "extraction/20_drafts/dem" / source.name),
        (ROOT / compiler.COMPILER_PATH, root / compiler.COMPILER_PATH),
    ]
    for source_path, target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target)
    shutil.copytree(ROOT / "schema", root / "schema")
    shutil.copytree(ROOT / "knowledge/rules", root / "knowledge/rules")
    shutil.copytree(ROOT / "knowledge/parameters", root / "knowledge/parameters")
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    monkeypatch.setattr(compiler, "EXPECTED_TOTAL", 1)
    monkeypatch.setattr(compiler, "MODULE_COUNTS", {"dem": 1})
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "1787659200")
    return root


def test_compiler_requires_source_date_epoch(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    with pytest.raises(ValueError, match="SOURCE_DATE_EPOCH"):
        compile_attestation(ROOT)


def test_compiler_rejects_invalid_source_date_epoch(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "not-an-epoch")
    with pytest.raises(ValueError, match="SOURCE_DATE_EPOCH"):
        compile_attestation(ROOT)


def test_output_is_deterministic_and_covers_corpus(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "1787659200")
    first = tmp_path / "first.yml"
    second = tmp_path / "second.yml"
    write_attestation(ROOT, first)
    write_attestation(ROOT, second)
    assert first.read_bytes() == second.read_bytes()
    data = yaml.safe_load(first.read_text(encoding="utf-8"))
    assert len(data["artifacts"]) == EXPECTED_TOTAL
    assert len({item["source_path"] for item in data["artifacts"]}) == EXPECTED_TOTAL
    manifest_bytes = "".join(
        f"{item['path']}|{item['git_blob_sha']}|{item['content_sha256']}\n"
        for item in data["context_manifest"]
    ).encode()
    assert data["context_manifest_sha256"] == hashlib.sha256(manifest_bytes).hexdigest()
    assert all(item["pydantic_result"] in {"pass", "fail"} for item in data["artifacts"])


def test_controlled_repository_binds_every_input_and_timestamp(
    controlled_repo: Path,
) -> None:
    data = compile_attestation(controlled_repo)
    assert data["generated_at"] == "2026-08-25T12:00:00Z"
    paths = [item["path"] for item in data["context_manifest"]]
    assert paths == sorted(paths)
    assert compiler.COMPILER_PATH in paths
    assert any(path.startswith("schema/") for path in paths)
    assert any(path.startswith("knowledge/rules/") for path in paths)
    assert any(path.startswith("knowledge/parameters/") for path in paths)
    for item in data["context_manifest"]:
        raw = (controlled_repo / item["path"]).read_bytes()
        assert item["content_sha256"] == hashlib.sha256(raw).hexdigest()


def test_controlled_repository_detects_context_and_coverage_changes(
    controlled_repo: Path,
) -> None:
    before = compile_attestation(controlled_repo)
    schema_path = controlled_repo / "schema/__init__.py"
    schema_path.write_text(schema_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    after = compile_attestation(controlled_repo)
    assert before["context_manifest_sha256"] != after["context_manifest_sha256"]
    extra = controlled_repo / "extraction/20_drafts/dem/VAR-extra.md"
    extra.write_text(
        next((controlled_repo / "extraction/20_drafts/dem").glob("VAR-*.md")).read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="draft coverage mismatch"):
        compile_attestation(controlled_repo)


def test_atomic_writer_preserves_existing_output_on_compile_failure(
    controlled_repo: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    output = controlled_repo / "evidence.yml"
    output.write_text("preserve-me\n", encoding="utf-8")
    monkeypatch.delenv("SOURCE_DATE_EPOCH")
    with pytest.raises(ValueError, match="SOURCE_DATE_EPOCH"):
        write_attestation(controlled_repo, output)
    assert output.read_text(encoding="utf-8") == "preserve-me\n"
