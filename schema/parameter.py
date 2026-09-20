"""Models for universal parameter registry entries."""

import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


ParameterKind = Literal["construction", "validation"]
FallbackPolicy = Literal[
    "use_global_default",
    "skip_check",
    "block_and_escalate",
    "undecided",
]


class ParameterProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_document: str
    extraction_method: str
    extracted_on: str
    human_reviewed: Literal[False]
    reviewer: None = None
    notes: str


class ParameterDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parameter_id: str
    parameter_name: str
    module_id: str
    schema_version: str
    status: Literal["draft"]
    authority: str
    kind: ParameterKind
    value_type: Literal["integer", "mapping"]
    value_schema: dict[str, Literal["integer", "number"]] | None = None
    applies_to_variables: list[str]
    fallback_policy: FallbackPolicy
    global_default: Any = None
    provenance: ParameterProvenance

    @field_validator("parameter_id")
    @classmethod
    def validate_parameter_id(cls, value: str) -> str:
        if not re.fullmatch(r"PARAM-[A-Z]+-[A-Z0-9-]+", value):
            raise ValueError("parameter_id must match PARAM-<MODULE>-<DESCRIPTIVE>")
        return value

    @model_validator(mode="after")
    def validate_policy_and_schema(self) -> "ParameterDefinition":
        if self.fallback_policy == "skip_check" and self.kind != "validation":
            raise ValueError("skip_check is valid only for validation parameters")
        if self.fallback_policy == "use_global_default" and self.global_default is None:
            raise ValueError("use_global_default requires a non-null global_default")
        if self.value_type == "mapping" and not self.value_schema:
            raise ValueError("mapping parameters require value_schema")
        if self.value_type == "integer" and self.value_schema is not None:
            raise ValueError("integer parameters must not define value_schema")
        return self
