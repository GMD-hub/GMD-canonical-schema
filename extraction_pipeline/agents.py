"""Agent adapter — Phase 4 Step 10.

Provider-neutral typed adapter for extraction and critic agents.
Input: immutable evidence packet, candidate schema, governed constants,
versioned role and module instructions.
Output: schema-constrained JSON.
"""

from typing import Any, Literal, Protocol

from pydantic import BaseModel, ConfigDict, ValidationError, field_validator


class AgentResponse(BaseModel):
    """Schema-constrained agent output.

    See extraction/agents/extractor.md for the role contract. `fields` maps
    field name to value or None; `confidence` maps field to 0.0-1.0;
    `citations` maps field to citation IDs from the evidence packet;
    `blocking_issues` lists issues that prevent canonicalization.
    """

    model_config = ConfigDict(extra="forbid")

    agent_version: str
    inventory_id: str
    fields: dict[str, Any]  # field name -> value or None
    confidence: dict[str, float]  # field -> 0.0-1.0
    citations: dict[str, list[str]]  # field -> [citation IDs]
    blocking_issues: list[dict[str, Any]]  # issues found
    notes: str

    @field_validator("confidence")
    @classmethod
    def _validate_confidence_range(cls, value: dict[str, float]) -> dict[str, float]:
        """Ensure all confidence scores are in [0.0, 1.0]."""
        for field_name, score in value.items():
            if not isinstance(score, (int, float)):
                raise ValueError(
                    f"confidence['{field_name}'] must be a float, "
                    f"got {type(score).__name__}"
                )
            if not (0.0 <= float(score) <= 1.0):
                raise ValueError(
                    f"confidence['{field_name}'] = {score} is out of "
                    f"range [0.0, 1.0]"
                )
        return value


class CriticResponse(BaseModel):
    """Adversarial evidence critic output.

    See extraction/agents/evidence-critic.md for the role contract. `disposition`
    is one of accepted | challenged | rejected; `findings` is a list of
    {field, finding, severity} dicts.
    """

    model_config = ConfigDict(extra="forbid")

    critic_version: str
    inventory_id: str
    disposition: Literal["accepted", "challenged", "rejected"]
    findings: list[dict[str, Any]]  # [{field, finding, severity}]
    recommendations: list[str]
    notes: str


class AgentOutputInvalid(ValueError):
    """Terminal — agent output is not schema-valid. No retries."""


class Extractor(Protocol):
    """Protocol for extractor agent adapters."""

    def extract(self, evidence: dict) -> AgentResponse: ...


class Critic(Protocol):
    """Protocol for evidence critic agent adapters."""

    def review(
        self,
        candidate: dict,
        evidence: dict,
        role_instructions: str,
    ) -> CriticResponse: ...


def validate_agent_output(raw: dict, expected_agent_version: str) -> AgentResponse:
    """Validate raw agent output against the AgentResponse schema.

    Args:
        raw: unvalidated dict from the extractor agent.
        expected_agent_version: the agent version the orchestrator expects
            (e.g., ``"v1"``). If the response's ``agent_version`` does not
            match, ``AgentOutputInvalid`` is raised — this enforces the
            fail-loudly contract for schema-version mismatches.

    Returns:
        A validated AgentResponse.

    Raises:
        AgentOutputInvalid: on malformed, schema-invalid, empty results,
            or agent_version mismatch. Terminal — zero retries.
    """
    try:
        response = AgentResponse(**raw)
    except (ValidationError, TypeError) as exc:
        raise AgentOutputInvalid(
            f"Agent output failed schema validation: {exc}"
        ) from exc
    if response.agent_version != expected_agent_version:
        raise AgentOutputInvalid(
            f"Agent version mismatch: expected {expected_agent_version!r}, "
            f"got {response.agent_version!r}. The orchestrator and agent "
            f"must agree on the agent_version to enforce deterministic "
            f"extraction contracts."
        )
    return response
