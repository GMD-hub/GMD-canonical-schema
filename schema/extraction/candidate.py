"""Extraction candidate and issue models — Phase 3 Step 6.

Nullable candidate model for items with missing evidence.
Blocking issue model for items that cannot be canonicalized.
"""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


# Fields classified as `source-explicit` in field-classification.v1.yaml that
# are required for canonical emission. When any is None, the candidate must
# record a blocking issue — incomplete candidates cannot be canonicalized.
REQUIRED_SOURCE_EXPLICIT_FIELDS = (
    "canonical_label",
    "tier",
    "value_codes",
    "allowed_range",
    "missing_codes",
)


class ExtractionCandidate(BaseModel):
    """A nullable extraction candidate — may be promoted to canonical after gates."""

    model_config = ConfigDict(extra="forbid")

    inventory_id: str
    module_code: str
    variable_name: str
    canonical_label: str | None = None
    tier: str | None = None
    unit_of_analysis: str | None = None
    mapping_role: str | None = None
    data_type: str | None = None
    value_codes: list[dict[str, Any]] | None = None
    allowed_range: dict[str, int] | None = None
    missing_codes: list[dict[str, Any]] | None = None
    derived_from: list[str] | None = None
    derives_to: list[str] | None = None
    country_parameters: list[str] | None = None
    prerequisites: list[dict[str, str]] | None = None
    rules: list[str] | None = None
    exceptions: list[str] | None = None
    external_standards: list[dict[str, str]] | None = None
    source_hints: dict[str, Any] | None = None
    field_classifications: dict[str, str]  # field -> classification class
    evidence_ids: dict[str, list[str]]  # field -> [citation IDs]
    confidence_scores: dict[str, float] | None = None  # field -> 0.0-1.0
    critic_disposition: Literal["accepted", "challenged", "rejected"] | None = None  # from evidence critic
    blocking_issue_ids: list[str]  # issues that block canonicalization

    @field_validator("confidence_scores")
    @classmethod
    def _validate_confidence_range(cls, value: dict[str, float] | None) -> dict[str, float] | None:
        """Ensure all confidence scores are in [0.0, 1.0].

        Confidence scores represent evidence quality. Values outside [0.0, 1.0]
        are invalid and would silently propagate into critic review and gate
        decisions, violating the fail-loudly contract.
        """
        if value is None:
            return value
        for field_name, score in value.items():
            if not isinstance(score, (int, float)):
                raise ValueError(
                    f"confidence_scores['{field_name}'] must be a float, "
                    f"got {type(score).__name__}"
                )
            if not (0.0 <= float(score) <= 1.0):
                raise ValueError(
                    f"confidence_scores['{field_name}'] = {score} is out of "
                    f"range [0.0, 1.0]"
                )
        return value

    @model_validator(mode="after")
    def _check_required_fields_have_blocking_issues(self) -> "ExtractionCandidate":
        """Ensure null required source-explicit fields are linked to blocking issues.

        Per field-classification.v1.yaml, fields classified `source-explicit`
        must be copied from cited evidence. When any is None (unresolved),
        the candidate must record at least one blocking issue — otherwise
        an incomplete candidate could be silently canonicalized, violating
        the fail-loudly contract.
        """
        missing_required = [
            field
            for field in REQUIRED_SOURCE_EXPLICIT_FIELDS
            if getattr(self, field) is None
        ]
        if missing_required and not self.blocking_issue_ids:
            raise ValueError(
                f"Required source-explicit fields are null "
                f"({', '.join(missing_required)}) but blocking_issue_ids is empty. "
                f"Null required fields must be linked to a blocking issue "
                f"to prevent silent canonicalization of incomplete candidates."
            )
        return self


class BlockingIssue(BaseModel):
    """A machine-readable blocking issue that prevents canonical emission."""

    model_config = ConfigDict(extra="forbid")

    issue_id: str
    inventory_id: str
    severity: Literal["blocking", "informational"]
    category: Literal[
        "missing-evidence",
        "invalid-citation",
        "unsupported-claim",
        "missing-field",
        "missing-section",
        "governance-block",
        "agent-output-invalid",
        "graph-error",
        "welfare-leakage",
    ]
    description: str
    owner: str  # agent, critic, orchestrator, human
    disposition: Literal["open", "accepted", "deferred"]
