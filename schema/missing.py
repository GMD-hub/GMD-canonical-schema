"""Models for missing value definitions."""

import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


MISSING_ID_PATTERN = re.compile(r"^MISS-[A-Z][A-Z0-9-]*$")
MISSING_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
# A Stata extended missing value: a dot and one lowercase letter (`.a` to `.z`).
STATA_EXTENDED_MISSING_PATTERN = re.compile(r"^\.[a-z]$")

# column: describes a variable as a whole in a survey; cell: describes one observation of a variable.
MissingLevel = Literal["column", "cell"]
# global: applies to every variable, and no variable lists it;
# variable: applies only where a variable lists it in its `missing_codes`.
MissingScope = Literal["global", "variable"]


class MissingRepresentations(BaseModel):
    """What an output format writes for a missing value.

    A format that has no field here writes the definition's `missing_name`.
    """

    model_config = ConfigDict(extra="forbid")

    stata: str

    @field_validator("stata")
    @classmethod
    def validate_stata(cls, value: str) -> str:
        if not STATA_EXTENDED_MISSING_PATTERN.fullmatch(value):
            raise ValueError("stata must be an extended missing value: a dot and one lowercase letter")
        return value


class MissingProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_document: str
    source_section: str | None = None
    extraction_method: str
    extracted_on: str
    human_reviewed: Literal[False]
    reviewer: None = None
    notes: str


class MissingDefinition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    missing_id: str
    missing_name: str
    canonical_label: str
    schema_version: str
    status: Literal["draft"]
    authority: str
    level: MissingLevel
    scope: MissingScope
    representations: MissingRepresentations
    provenance: MissingProvenance

    @field_validator("missing_id")
    @classmethod
    def validate_missing_id(cls, value: str) -> str:
        if not MISSING_ID_PATTERN.fullmatch(value):
            raise ValueError("missing_id must match MISS-<UPPERCASE-NAME>")
        return value

    @field_validator("missing_name")
    @classmethod
    def validate_missing_name(cls, value: str) -> str:
        if not MISSING_NAME_PATTERN.fullmatch(value):
            raise ValueError("missing_name must be lowercase words joined by underscores")
        return value

    @field_validator("canonical_label")
    @classmethod
    def validate_label(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("canonical_label must not be empty")
        return value

    @model_validator(mode="after")
    def validate_id_matches_name(self) -> "MissingDefinition":
        expected = "MISS-" + self.missing_name.upper().replace("_", "-")
        if self.missing_id != expected:
            raise ValueError(
                f"missing_id {self.missing_id!r} does not match missing_name "
                f"{self.missing_name!r} (expected {expected!r})"
            )
        return self

    @model_validator(mode="after")
    def validate_column_scope(self) -> "MissingDefinition":
        if self.level == "column" and self.scope != "global":
            raise ValueError("a column-level missing value applies to every variable: scope must be global")
        return self


def global_missing_ids(definitions: list[MissingDefinition]) -> set[str]:
    """The IDs that apply to every variable (scope global): a variable does not list them."""
    return {item.missing_id for item in definitions if item.scope == "global"}


def validate_missing_set(definitions: list[MissingDefinition]) -> None:
    """Raise when two definitions share an ID, a name or a Stata value.

    One column of a Stata file can hold column-level and cell-level values side by side,
    so a Stata value is unique across both levels.
    """
    for field, read in (
        ("missing_id", lambda item: item.missing_id),
        ("missing_name", lambda item: item.missing_name),
        ("representations.stata", lambda item: item.representations.stata),
    ):
        seen: dict[str, str] = {}
        for item in definitions:
            value = read(item)
            if value in seen:
                raise ValueError(
                    f"{field} {value!r} is used by both {seen[value]} and {item.missing_id}"
                )
            seen[value] = item.missing_id
