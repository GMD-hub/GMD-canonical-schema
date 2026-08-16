"""Tests for review_agents.run_all_agents runner."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.run_all_agents import run


DRAFTS_DIR = Path("extraction/20_drafts")


class TestRunner:
    def test_runs_against_calibration_drafts(self, tmp_path):
        findings, exit_code = run(DRAFTS_DIR, tmp_path)
        assert len(findings) > 0

    def test_produces_summary_md(self, tmp_path):
        run(DRAFTS_DIR, tmp_path)
        summary = tmp_path / "SUMMARY.md"
        assert summary.exists()
        content = summary.read_text()
        assert "Agent Review Summary" in content
        assert "Results Table" in content

    def test_produces_per_artifact_yml(self, tmp_path):
        run(DRAFTS_DIR, tmp_path)
        yml_files = list(tmp_path.glob("*.yml"))
        assert len(yml_files) > 0

    def test_exit_code_reflects_errors(self, tmp_path):
        _, exit_code = run(DRAFTS_DIR, tmp_path)
        assert exit_code in (0, 1)

    def test_empty_drafts_dir(self, tmp_path):
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        findings, exit_code = run(empty_dir, tmp_path)
        assert findings == []
        assert exit_code == 0