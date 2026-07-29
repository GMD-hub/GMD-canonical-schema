"""Models for universal decision rules."""

from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from schema.variable import MODULE_ID_PATTERN, RULE_ID_PATTERN, VARIABLE_ID_PATTERN


class RuleDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rule_id: str
    rule_name: str
    scope: Literal["module"]
    module_id: str
    applies_to_variables: list[str]
    priority: int = Field(ge=0, le=100)
    version: str
    status: Literal["draft"]
    authority: str
    effective_from: date
    effective_to: date | None

    @field_validator("rule_id")
    @classmethod
    def validate_rule_id(cls, value: str) -> str:
        if not RULE_ID_PATTERN.fullmatch(value):
            raise ValueError("rule_id must match RULE-<UPPERCASE-NAME>")
        return value

    @field_validator("module_id")
    @classmethod
    def validate_module_id(cls, value: str) -> str:
        if not MODULE_ID_PATTERN.fullmatch(value):
            raise ValueError("module_id must match MOD-<UPPERCASE-NAME>")
        return value

    @field_validator("applies_to_variables")
    @classmethod
    def validate_variable_ids(cls, values: list[str]) -> list[str]:
        invalid = sorted(value for value in values if not VARIABLE_ID_PATTERN.fullmatch(value))
        if invalid:
            raise ValueError(f"invalid variable IDs: {invalid}")
        return values