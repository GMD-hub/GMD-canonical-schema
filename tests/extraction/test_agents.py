"""Tests for agent adapters — Phase 4 Step 10."""

import pytest

from extraction_pipeline.agents import (
    AgentOutputInvalid,
    AgentResponse,
    CriticResponse,
    validate_agent_output,
)
from tests.extraction.fakes import FakeCritic, FakeExtractor

class TestAgentResponse:
    def test_valid_response(self) -> None:
        response = AgentResponse(
            agent_version="v1",
            inventory_id="INV-IDN-001",
            fields={"age": 18},
            confidence={"age": 0.95},
            citations={"age": ["CIT-001"]},
            blocking_issues=[],
            notes="ok",
        )
        assert response.inventory_id == "INV-IDN-001"
        assert response.agent_version == "v1"
        assert response.fields == {"age": 18}
        assert response.confidence == {"age": 0.95}
        assert response.citations == {"age": ["CIT-001"]}
        assert response.blocking_issues == []
        assert response.notes == "ok"

    def test_empty_fields_ok(self) -> None:
        response = AgentResponse(
            agent_version="v1",
            inventory_id="INV-IDN-001",
            fields={},
            confidence={},
            citations={},
            blocking_issues=[],
            notes="no fields extracted",
        )
        assert response.fields == {}

    def test_confidence_out_of_range_raises(self) -> None:
        """confidence above 1.0 must raise (P1.3 fix)."""
        with pytest.raises(ValueError, match="out of range"):
            AgentResponse(
                agent_version="v1",
                inventory_id="INV-IDN-001",
                fields={},
                confidence={"age": 1.7},
                citations={},
                blocking_issues=[],
                notes="",
            )

    def test_confidence_negative_raises(self) -> None:
        """confidence below 0.0 must raise (P1.3 fix)."""
        with pytest.raises(ValueError, match="out of range"):
            AgentResponse(
                agent_version="v1",
                inventory_id="INV-IDN-001",
                fields={},
                confidence={"age": -0.3},
                citations={},
                blocking_issues=[],
                notes="",
            )


class TestCriticResponse:
    def test_accepted(self) -> None:
        response = CriticResponse(
            critic_version="v1",
            inventory_id="INV-IDN-001",
            disposition="accepted",
            findings=[],
            recommendations=[],
            notes="all good",
        )
        assert response.disposition == "accepted"
        assert response.critic_version == "v1"
        assert response.inventory_id == "INV-IDN-001"
        assert response.findings == []
        assert response.recommendations == []
        assert response.notes == "all good"

    def test_challenged(self) -> None:
        response = CriticResponse(
            critic_version="v1",
            inventory_id="INV-IDN-001",
            disposition="challenged",
            findings=[
                {"field": "canonical_label", "finding": "ambiguous", "severity": "medium"}
            ],
            recommendations=["Review label with human"],
            notes="needs review",
        )
        assert response.disposition == "challenged"
        assert len(response.findings) == 1


class TestValidateAgentOutput:
    def test_valid_output_passes(self) -> None:
        raw = {
            "agent_version": "v1",
            "inventory_id": "INV-IDN-001",
            "fields": {},
            "confidence": {},
            "citations": {},
            "blocking_issues": [],
            "notes": "",
        }
        result = validate_agent_output(raw, "v1")
        assert isinstance(result, AgentResponse)

    def test_malformed_json_raises(self) -> None:
        with pytest.raises(AgentOutputInvalid):
            validate_agent_output({"not": "valid"}, "v1")

    def test_empty_input_raises(self) -> None:
        with pytest.raises(AgentOutputInvalid):
            validate_agent_output({}, "v1")

    def test_missing_required_field_raises(self) -> None:
        raw = {
            "agent_version": "v1",
            "inventory_id": "INV-IDN-001",
            # missing fields, confidence, citations
        }
        with pytest.raises(AgentOutputInvalid):
            validate_agent_output(raw, "v1")

    def test_version_mismatch_raises(self) -> None:
        """An agent_version mismatch must raise AgentOutputInvalid."""
        raw = {
            "agent_version": "v2",
            "inventory_id": "INV-IDN-001",
            "fields": {},
            "confidence": {},
            "citations": {},
            "blocking_issues": [],
            "notes": "",
        }
        with pytest.raises(AgentOutputInvalid, match="version mismatch"):
            validate_agent_output(raw, "v1")

    def test_matching_version_passes(self) -> None:
        """A matching agent_version must validate successfully."""
        raw = {
            "agent_version": "v1",
            "inventory_id": "INV-IDN-001",
            "fields": {},
            "confidence": {},
            "citations": {},
            "blocking_issues": [],
            "notes": "",
        }
        result = validate_agent_output(raw, "v1")
        assert result.agent_version == "v1"


class TestFakeAdapters:
    def test_fake_extractor(self) -> None:
        extractor = FakeExtractor()
        evidence = {"inventory_id": "INV-IDN-001"}
        response = extractor.extract(evidence)
        assert isinstance(response, AgentResponse)
        assert response.inventory_id == "INV-IDN-001"

    def test_fake_critic(self) -> None:
        critic = FakeCritic()
        candidate = {"inventory_id": "INV-IDN-001"}
        response = critic.review(candidate, {}, "instructions")
        assert isinstance(response, CriticResponse)
        assert response.disposition == "accepted"
