"""Test doubles for extraction agents — never calls a model.

These fakes live in the test package (not in production code) to keep the
production import surface clean. See P2.25/P3.5 in the review report.
"""

from extraction_pipeline.agents import AgentResponse, CriticResponse


class FakeExtractor:
    """Fake extractor adapter for testing — never calls a model."""

    def extract(
        self,
        evidence: dict,
    ) -> AgentResponse:
        """Return a valid but minimal response."""
        return AgentResponse(
            agent_version="fake-1.0",
            inventory_id=evidence.get("inventory_id", "UNKNOWN"),
            fields={},
            confidence={},
            citations={},
            blocking_issues=[],
            notes="Fake extractor response for testing",
        )


class FakeCritic:
    """Fake critic adapter for testing — never calls a model."""

    def review(
        self,
        candidate: dict,
        _evidence: dict,
        _role_instructions: str,
    ) -> CriticResponse:
        """Return a minimal accepted review."""
        return CriticResponse(
            critic_version="fake-1.0",
            inventory_id=candidate.get("inventory_id", "UNKNOWN"),
            disposition="accepted",
            findings=[],
            recommendations=[],
            notes="Fake critic response for testing",
        )


class FakeRejectingCritic:
    """Fake critic that rejects — for testing the BLOCKED state path."""

    def review(
        self,
        candidate: dict,
        _evidence: dict,
        _role_instructions: str,
    ) -> CriticResponse:
        """Return a rejection review."""
        return CriticResponse(
            critic_version="fake-1.0",
            inventory_id=candidate.get("inventory_id", "UNKNOWN"),
            disposition="rejected",
            findings=[
                {"field": "canonical_label", "finding": "unsupported", "severity": "high"}
            ],
            recommendations=["Review with human"],
            notes="Fake rejecting critic for testing",
        )
