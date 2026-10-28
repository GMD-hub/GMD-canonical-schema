"""Models for universal variable specifications."""

import re
from typing import Annotated, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
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


class Gate(BaseModel):
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


_RECODE_KEY_PATTERN = re.compile(r"^\d+(/\d+)?$")


class ExternalStandardAnchor(BaseModel):
    """method=external_standard: GMD code placed from an international standard's levels
    (e.g. ISCED-2011 level -> educat7, JMP node -> water_source). The one universal anchor the
    family builds from; lives with the anchored variable, not in a code-side table. A map value
    is one code, or the list of codes a coarse standard level spans (the code itself is then
    undetermined); a standard level absent from the map has no code of this variable."""

    model_config = ConfigDict(extra="forbid")

    method: Literal["external_standard"]
    standard: str
    level: str
    map: dict[str, int | list[int]]


class Recode(BaseModel):
    """method=recode: universal code->code recode from a parent GMD variable, matching the
    Stata recode in the construction notes / rule. Each map key is a single code ("3") or an
    inclusive range ("3/7"). The single consumable source the resolver reads, instead of a
    parallel code-side rolldown table that can drift."""

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    method: Literal["recode"]
    from_: str = Field(alias="from")
    map: dict[str, int]

    @field_validator("from_")
    @classmethod
    def validate_from(cls, value: str) -> str:
        if not VARIABLE_ID_PATTERN.fullmatch(value):
            raise ValueError("recode.from must match VAR-<lowercase-name>")
        return value

    @field_validator("map")
    @classmethod
    def validate_map_keys(cls, value: dict[str, int]) -> dict[str, int]:
        invalid = sorted(key for key in value if not _RECODE_KEY_PATTERN.fullmatch(key))
        if invalid:
            raise ValueError(f"recode.map keys must be a code or lo/hi range: {invalid}")
        return value


class CategoryField(BaseModel):
    """method=category_field: read a numeric field off the matched national category
    (never a string label), e.g. educy <- cum_years_schooling."""

    model_config = ConfigDict(extra="forbid")

    method: Literal["category_field"]
    field: str

    @field_validator("field")
    @classmethod
    def validate_field(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("category_field requires a non-empty 'field'")
        return value


class Alias(BaseModel):
    """method=alias: reuse another variable's value-codes and mapping unchanged, e.g. a
    reference-period or second-job variant (empstat_2 <- empstat)."""

    model_config = ConfigDict(extra="forbid")

    method: Literal["alias"]
    of: str

    @field_validator("of")
    @classmethod
    def validate_of(cls, value: str) -> str:
        if not VARIABLE_ID_PATTERN.fullmatch(value):
            raise ValueError("alias.of must match VAR-<lowercase-name>")
        return value


CorrespondenceOutput = Annotated[
    ExternalStandardAnchor | Recode | CategoryField | Alias,
    Field(discriminator="method"),
]
"""Single polymorphic construction recipe the layered-correspondence resolver reads to
build a variable's value-map, instead of hardcoding per-variable branches. The ``method``
discriminator selects the mechanism; higher-level policy (path priority, fallback cascade,
missing-value codes, prohibitions) stays in the governing RULE, which references this recipe
rather than restating it.

A variable with several derivation paths carries a LIST of ``recode`` recipes, one per parent,
in the preference order of ``derived_from`` (e.g. educat4 from educat7, else from educat5): the
first recipe whose parent is constructed for the survey applies. The list may end with one
``external_standard`` recipe, the direct path for a category no parent recode decides (e.g.
imp_san_rec for a JMP node with no sanitation_source code)."""


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
    correspondence_output: CorrespondenceOutput | list[CorrespondenceOutput] | None = None
    country_parameters: list[str]
    gates: list[Gate]
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
    def validate_correspondence_parents(self) -> "VariableDefinition":
        recipes = self.correspondence_output
        if recipes is None:
            return self
        listed = recipes if isinstance(recipes, list) else [recipes]
        levels = [recipe.level for recipe in listed if isinstance(recipe, ExternalStandardAnchor)]
        if any(level != self.variable_name for level in levels):
            raise ValueError(f"external_standard level must be this variable's name: {levels}")
        if isinstance(recipes, list):
            if not recipes:
                raise ValueError("correspondence_output list must not be empty")
            direct = isinstance(recipes[-1], ExternalStandardAnchor)
            recodes = [recipe for recipe in recipes if isinstance(recipe, Recode)]
            if not recodes or len(recodes) != len(recipes) - direct:
                raise ValueError("a correspondence_output list holds recode recipes, optionally "
                                 "followed by one external_standard recipe")
            parents = [recipe.from_ for recipe in recodes]
            if len(set(parents)) != len(parents):
                raise ValueError(f"correspondence_output recodes repeat a parent: {parents}")
        else:
            parents = [recipes.from_] if isinstance(recipes, Recode) else []
        undeclared = [parent for parent in parents if parent not in self.derived_from]
        if undeclared:
            raise ValueError(f"correspondence_output recode parents not in derived_from: {undeclared}")
        order = [self.derived_from.index(parent) for parent in parents]
        if order != sorted(order):
            raise ValueError("correspondence_output recodes must follow the derived_from preference order")
        return self

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
            item.variable_id for item in self.gates
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
        item.variable_id for item in variable.gates
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
