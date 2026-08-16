"""Tests for review_agents.source_grounding agent."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.source_grounding import check_draft


DRAFTS_DIR = Path("extraction/20_drafts")


class TestSourceGrounding:
    def _findings_for(self, artifact_id: str) -> list:
        path = list(DRAFTS_DIR.rglob(f"{artifact_id}.md"))[0]
        result = check_draft(path)
        assert result.artifact_id == artifact_id
        return result.findings

    def test_var_male_passes(self):
        findings = self._findings_for("VAR-male")
        errors = [f for f in findings if f.severity == "error"]
        assert errors == [], f"Unexpected errors: {[f.message for f in errors]}"

    def test_provenance_source_document_present(self):
        findings = self._findings_for("VAR-male")
        empty_source = [f for f in findings if "source_document is empty" in f.message]
        assert empty_source == []

    def test_provenance_source_section_present(self):
        findings = self._findings_for("VAR-male")
        empty_section = [f for f in findings if "source_section is empty" in f.message]
        assert empty_section == []

    def test_derivation_dependency_mentioned_in_construction_notes(self):
        findings = self._findings_for("VAR-educy")
        warnings = [f for f in findings if "Derivation dependency" in f.message and "not mentioned" in f.message]
        for w in warnings:
            assert "VAR-educat7" in w.message or "VAR-educat5" in w.message or "VAR-educat4" in w.message

    def test_educat7_derived_from_empty_no_warnings(self):
        findings = self._findings_for("VAR-educat7")
        derivation_warnings = [f for f in findings if "Derivation dependency" in f.message]
        assert derivation_warnings == []