"""Tests for review_agents.models."""

import pytest

from extraction_pipeline.review_agents.models import AgentFindings, AgentSummary, Finding


class TestFinding:
    def test_valid_finding(self):
        f = Finding(field="test", severity="error", message="msg")
        assert f.field == "test"
        assert f.line is None

    def test_finding_with_line(self):
        f = Finding(field="body", severity="warning", message="msg", line=42)
        assert f.line == 42

    def test_extra_field_rejected(self):
        with pytest.raises(Exception):
            Finding(field="x", severity="e", message="m", extra="nope")


class TestAgentSummary:
    def test_counts(self):
        s = AgentSummary(errors=2, warnings=1, passed=0)
        assert s.errors == 2
        assert s.passed == 0


class TestAgentFindings:
    def test_roundtrip(self):
        af = AgentFindings(
            agent="test_agent",
            artifact_id="VAR-male",
            checked_at="2026-08-15T00:00:00+00:00",
            findings=[Finding(field="x", severity="warning", message="m")],
            summary=AgentSummary(errors=0, warnings=1, passed=0),
        )
        data = af.model_dump()
        restored = AgentFindings.model_validate(data)
        assert restored.agent == af.agent
        assert len(restored.findings) == 1

    def test_empty_findings_is_passed(self):
        af = AgentFindings(
            agent="a",
            artifact_id="V",
            checked_at="2026-01-01T00:00:00+00:00",
            findings=[],
            summary=AgentSummary(errors=0, warnings=0, passed=1),
        )
        assert af.summary.passed == 1