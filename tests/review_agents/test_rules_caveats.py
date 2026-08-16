"""Tests for review_agents.rules_caveats agent."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.rules_caveats import check_draft


DRAFTS_DIR = Path("extraction/20_drafts")


class TestRulesCaveats:
    def _findings_for(self, artifact_id: str) -> list:
        path = list(DRAFTS_DIR.rglob(f"{artifact_id}.md"))[0]
        result = check_draft(path)
        assert result.artifact_id == artifact_id
        return result.findings

    def test_var_male_passes(self):
        findings = self._findings_for("VAR-male")
        errors = [f for f in findings if f.severity == "error"]
        assert errors == [], f"Unexpected errors: {[f.message for f in errors]}"

    def test_var_marital_stub_construction_notes(self):
        findings = self._findings_for("VAR-marital")
        stub_errors = [f for f in findings if "stub" in f.message.lower() and "construction_notes" in f.field]
        assert len(stub_errors) >= 1
        assert stub_errors[0].severity == "error"

    def test_var_educat7_todo_in_escalation(self):
        findings = self._findings_for("VAR-educat7")
        todo_warnings = [f for f in findings if "TODO" in f.message]
        assert len(todo_warnings) >= 1