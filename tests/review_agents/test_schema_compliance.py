"""Tests for review_agents.schema_compliance agent."""

import pytest
from pathlib import Path

from extraction_pipeline.review_agents.schema_compliance import check_draft


DRAFTS_DIR = Path("extraction/20_drafts")

_VARIABLE_IDS = {"VAR-male", "VAR-educat7", "VAR-educat4", "VAR-educy", "VAR-marital", "VAR-urban"}
_RULE_IDS = {"RULE-SEX-001", "RULE-EDU-001", "RULE-EDU-002", "RULE-EDU-003", "RULE-EDU-999"}


class TestSchemaCompliance:
    def _findings_for(self, artifact_id: str) -> list:
        path = list(DRAFTS_DIR.rglob(f"{artifact_id}.md"))[0]
        result = check_draft(path, _VARIABLE_IDS, rule_ids=_RULE_IDS)
        assert result.artifact_id == artifact_id
        return result.findings

    def test_var_male_passes(self):
        findings = self._findings_for("VAR-male")
        errors = [f for f in findings if f.severity == "error"]
        assert errors == [], f"Unexpected errors: {[f.message for f in errors]}"

    def test_var_educy_parameter_error(self):
        findings = self._findings_for("VAR-educy")
        param_errors = [f for f in findings if "PARAM-EDU-YEARS-BY-LEVEL" in f.message]
        assert len(param_errors) >= 1
        assert param_errors[0].severity == "error"

    def test_var_marital_parameter_error(self):
        findings = self._findings_for("VAR-marital")
        param_errors = [f for f in findings if "PARAM-DEM-MIN-MARRIAGE-AGE" in f.message]
        assert len(param_errors) >= 1
        assert param_errors[0].severity == "error"

    def test_var_educat7_no_placeholder_warnings(self):
        findings = self._findings_for("VAR-educat7")
        placeholder_warnings = [f for f in findings if "TODO" in f.message]
        assert len(placeholder_warnings) == 0, f"Unexpected TODO warnings: {[f.message for f in placeholder_warnings]}"

    def test_required_sections_present(self):
        for vid in _VARIABLE_IDS:
            findings = self._findings_for(vid)
            missing = [f for f in findings if "Required section missing" in f.message]
            assert missing == [], f"{vid} missing sections: {[f.message for f in missing]}"

    def test_frontmatter_validates_for_male(self):
        findings = self._findings_for("VAR-male")
        pydantic_errors = [f for f in findings if "Pydantic validation failed" in f.message]
        assert pydantic_errors == []