"""Tests for the mandatory extraction source-gate CLI."""

from datetime import UTC, datetime
from pathlib import Path
import subprocess
from unittest.mock import Mock

import pytest
import yaml

import extraction_pipeline.preflight as preflight
import extraction_pipeline.source as source
import extraction_pipeline.source_gate as gate


ARGS = ["--manifest", "m.yaml", "--governance", "g.yaml", "--checkout", "checkout"]


def test_gate_calls_preflight_then_resolution_with_one_utc_timestamp(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []
    manifest = {"manifest_version": "1"}
    monkeypatch.setattr(gate, "run_preflight", Mock(side_effect=lambda *args: calls.append("preflight") or manifest))
    resolver = Mock(side_effect=lambda *args: calls.append("resolve"))
    monkeypatch.setattr(gate, "resolve_source", resolver)
    clock = Mock(return_value=datetime(2026, 8, 26, 12, 30, tzinfo=UTC))
    assert gate.run(ARGS, clock=clock) == 0
    assert calls == ["preflight", "resolve"]
    resolver.assert_called_once_with(Path("checkout"), manifest, "2026-08-26T12:30:00Z")
    clock.assert_called_once()


def test_preflight_failure_prevents_resolution(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(gate, "run_preflight", Mock(side_effect=preflight.PreflightError("bad")))
    resolver = Mock()
    monkeypatch.setattr(gate, "resolve_source", resolver)
    assert gate.run(ARGS) == 1
    resolver.assert_not_called()


@pytest.mark.parametrize("failure", [source.SourceResolutionError("bad"), RuntimeError("unexpected")])
def test_source_and_unexpected_failures_return_nonzero(monkeypatch: pytest.MonkeyPatch, failure: Exception) -> None:
    monkeypatch.setattr(gate, "run_preflight", Mock(return_value={}))
    monkeypatch.setattr(gate, "resolve_source", Mock(side_effect=failure))
    assert gate.run(ARGS) == 1


def test_clock_failure_returns_nonzero_after_preflight(monkeypatch: pytest.MonkeyPatch) -> None:
    preflight_run = Mock(return_value={})
    monkeypatch.setattr(gate, "run_preflight", preflight_run)
    assert gate.run(ARGS, clock=Mock(side_effect=RuntimeError("clock failed"))) == 1
    preflight_run.assert_called_once_with(Path("m.yaml"), Path("g.yaml"))


def test_unexpected_failure_logs_without_traceback(monkeypatch: pytest.MonkeyPatch) -> None:
    messages: list[str] = []
    sink_id = gate.logger.add(messages.append, format="{message}")
    monkeypatch.setattr(gate, "run_preflight", Mock(side_effect=RuntimeError("unexpected")))
    try:
        assert gate.run(ARGS) == 1
    finally:
        gate.logger.remove(sink_id)
    output = "".join(messages)
    assert "Unexpected extraction source gate failure: unexpected" in output
    assert "Traceback" not in output


def test_argument_error_is_nonzero() -> None:
    with pytest.raises(SystemExit) as caught:
        gate.run([])
    assert caught.value.code != 0


def test_real_helpers_complete_eight_file_gate(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    checkout = tmp_path / "checkout"
    paths = [
        "chapters/chapter2-IDN.qmd", "chapters/chapter3-GEO.qmd", "chapters/chapter4-DEM.qmd",
        "chapters/chapter5-LMR.qmd", "chapters/chapter6-UTL.qmd", "chapters/chapter7-DWL.qmd",
        "chapters/chapter8-CONS.qmd", "docs/GMD_household_survey_harmonization.md",
    ]
    for index, path in enumerate(paths):
        target = checkout / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(f"bytes-{index}".encode())
    entries = [{"path": path, "scope": "welfare-excluded" if "chapter8" in path else "included", "sha256": source.hash_file(checkout / path)} for path in paths[:7]]
    manifest = {
        "manifest_version": "1.0", "repository": {"url": "https://github.com/GMD-hub/GMD-guidelines", "commit_sha": "a" * 40},
        "source_files": entries, "supporting_files": [{"path": paths[7], "scope": "supporting", "sha256": source.hash_file(checkout / paths[7])}],
        "governance": {"module_registry_version": "v1", "field_classification_version": "v1", "schema_version": "0.1", "gmd_version": "3.0"},
        "parser_contract": {"tool": "pandoc", "version": "3.1.12", "installation_method": "action@commit", "reader": "markdown", "writer": "json", "normalization_version": "1.0"},
        "output": {"root": "extraction/20_drafts/", "allowlist": ["extraction/20_drafts/runs/"]},
    }
    governance = {"schema_version": "0.1", "gmd_version": "3.0", "modules": [{"source_chapter": path} for path in paths[:6]]}
    manifest_path, governance_path = tmp_path / "manifest.yaml", tmp_path / "governance.yaml"
    manifest_path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
    governance_path.write_text(yaml.safe_dump(governance), encoding="utf-8")
    def process_result(command: list[str], **_: object) -> subprocess.CompletedProcess[str]:
        output = "pandoc 3.1.12\n" if command[0] == "pandoc" else "a" * 40 + "\n"
        return subprocess.CompletedProcess(command, 0, output, "")

    monkeypatch.setattr(subprocess, "run", process_result)
    monkeypatch.setattr(gate, "run_preflight", preflight.run_preflight)
    monkeypatch.setattr(gate, "resolve_source", source.resolve_source)
    args = ["--manifest", str(manifest_path), "--governance", str(governance_path), "--checkout", str(checkout)]
    assert gate.run(args, clock=lambda: datetime(2026, 8, 26, tzinfo=UTC)) == 0
