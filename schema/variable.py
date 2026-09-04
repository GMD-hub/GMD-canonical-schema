"""Models for universal variable specifications."""

import re
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    ValidationInfo,
    field_validator,
    model_validator,
)


VARIABLE_ID_PATTERN = re.compile(r"^VAR-[a-z][a-z0-9]*$")
MODULE_ID_PATTERN = re.compile(r"^MOD-[A-Z][A-Z0-9-]*$")
RULE_ID_PATTERN = re.compile(r"^RULE-[A-Z][A-Z0-9-]*$")
PARAMETER_ID_PATTERN = re.compile(r"^PARAM-[A-Z]+-[A-Z0-9-]+$")


class ValueCode(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: int
    label: str


class AllowedRange(BaseModel):
    model_config = ConfigDict(extra="forbid")

    min: int
    max: int

    @model_validator(mode="after")
    def validate_range(self) -> "AllowedRange":
        if self.min > self.max:
            raise ValueError("min must be less than or equal to max")
        return self


class MissingCode(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str
    label: str


class Prerequisite(BaseModel):
    model_config = ConfigDict(extra="forbid")

    variable_id: str
    condition: str

    @field_validator("variable_id")
    @classmethod
    def validate_variable_id(cls, value: str) -> str:
        if not VARIABLE_ID_PATTERN.fullmatch(value):
            raise ValueError("variable_id must match VAR-<lowercase-name>")
        return value


class ExternalStandard(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    url: str


class SourceHints(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question_keywords: list[str]
    typical_section_names: list[str]


class VariableProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_document: str
    source_section: str
    extraction_method: str
    extracted_on: str
    human_reviewed: StrictBool
    reviewer: str | None = None
    notes: str | None

    @model_validator(mode="after")
    def validate_reviewer(self) -> "VariableProvenance":
        if self.human_reviewed and not (self.reviewer and self.reviewer.strip()):
            raise ValueError("reviewer is required when human_reviewed is true")
        if not self.human_reviewed and self.reviewer is not None:
            raise ValueError("reviewer must be null when human_reviewed is false")
        return self


class VariableDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    variable_id: str
    canonical_label: str
    variable_name: str
    module_id: str
    gmd_version: str
    schema_version: str
    status: Literal["draft", "approved"]
    tier: int
    unit_of_analysis: str
    mapping_role: Literal["atomic", "derived", "derived_preferred"]
    data_type: str
    value_codes: list[ValueCode] | None
    allowed_range: AllowedRange | None
    missing_codes: list[MissingCode]
    derived_from: list[str]
    derives_to: list[str]
    country_parameters: list[str]
    prerequisites: list[Prerequisite]
    rules: list[str]
    exceptions: list[str]
    external_standards: list[ExternalStandard]
    source_hints: SourceHints
    provenance: VariableProvenance

    @field_validator("variable_id")
    @classmethod
    def validate_variable_id(cls, value: str) -> str:
        if not VARIABLE_ID_PATTERN.fullmatch(value):
            raise ValueError("variable_id must match VAR-<lowercase-name>")
        return value

    @field_validator("module_id")
    @classmethod
    def validate_module_id(cls, value: str) -> str:
        if not MODULE_ID_PATTERN.fullmatch(value):
            raise ValueError("module_id must match MOD-<UPPERCASE-NAME>")
        return value

    @field_validator("derived_from", "derives_to")
    @classmethod
    def validate_variable_references(cls, values: list[str]) -> list[str]:
        invalid = sorted(value for value in values if not VARIABLE_ID_PATTERN.fullmatch(value))
        if invalid:
            raise ValueError(f"invalid variable IDs: {invalid}")
        return values

    @field_validator("country_parameters")
    @classmethod
    def validate_parameter_references(cls, values: list[str]) -> list[str]:
        invalid = sorted(value for value in values if not PARAMETER_ID_PATTERN.fullmatch(value))
        if invalid:
            raise ValueError(f"invalid parameter IDs: {invalid}")
        return values

    @field_validator("rules")
    @classmethod
    def validate_rule_references(cls, values: list[str]) -> list[str]:
        invalid = sorted(value for value in values if not RULE_ID_PATTERN.fullmatch(value))
        if invalid:
            raise ValueError(f"invalid rule IDs: {invalid}")
        return values

    @model_validator(mode="after")
    def validate_references(self, info: ValidationInfo) -> "VariableDefinition":
        if self.status == "approved" and not self.provenance.human_reviewed:
            raise ValueError("approved status requires human_reviewed provenance")
        if self.status == "draft" and self.provenance.human_reviewed:
            raise ValueError("draft status requires unreviewed provenance")

        context = info.context or {}
        variable_ids: set[str] = context.get("variable_ids", set())
        parameter_ids: set[str] = context.get("parameter_ids", set())
        rule_ids: set[str] = context.get("rule_ids", set())

        referenced_variables = set(self.derived_from) | set(self.derives_to) | {
            item.variable_id for item in self.prerequisites
        }
        unknown_variables = referenced_variables - variable_ids
        allow_unresolved_draft = (
            self.status == "draft" and context.get("allow_unresolved_draft", False)
        )
        if unknown_variables and not allow_unresolved_draft:
            raise ValueError(f"unknown variable IDs: {sorted(unknown_variables)}")

        unknown_parameters = set(self.country_parameters) - parameter_ids
        if unknown_parameters:
            raise ValueError(f"unknown parameter IDs: {sorted(unknown_parameters)}")

        unknown_rules = set(self.rules) - rule_ids
        if unknown_rules:
            raise ValueError(f"unknown rule IDs: {sorted(unknown_rules)}")
        return self


def unresolved_variable_references(
    variable: VariableDefinition, variable_ids: set[str]
) -> set[str]:
    references = set(variable.derived_from) | set(variable.derives_to) | {
        item.variable_id for item in variable.prerequisites
    }
    return references - variable_ids


def validate_acyclic_derivation_graph(variables: list[VariableDefinition]) -> None:
    graph = {variable.variable_id: set(variable.derived_from) for variable in variables}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(variable_id: str) -> None:
        if variable_id in visiting:
            raise ValueError(f"derivation graph contains a cycle at {variable_id}")
        if variable_id in visited:
            return
        visiting.add(variable_id)
        for dependency_id in graph.get(variable_id, set()):
            if dependency_id in graph:
                visit(dependency_id)
        visiting.remove(variable_id)
        visited.add(variable_id)

    for variable_id in graph:
        visit(variable_id)
