"""Models for country exception files."""

import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator, model_validator

from schema.country_parameters import ISO3_PATTERN


class CountryExceptionProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source: str
    approved_by: None = None
    approved_on: None = None
    human_reviewed: Literal[False]


class CountryExceptionRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    exception_id: str
    applies_to_variables: list[str]
    effective_from: int | None
    effective_to: int | None
    condition: str
    action: str
    rationale: str
    provenance: CountryExceptionProvenance

    @model_validator(mode="after")
    def validate_window(self) -> "CountryExceptionRecord":
        if (
            self.effective_from is not None
            and self.effective_to is not None
            and self.effective_from > self.effective_to
        ):
            raise ValueError("effective_from must be less than or equal to effective_to")
        return self


class CountryExceptionFile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    country_id: str
    iso3: str
    schema_version: str
    status: Literal["draft"]
    exceptions: list[CountryExceptionRecord]

    @field_validator("iso3")
    @classmethod
    def validate_iso3(cls, value: str) -> str:
        if not ISO3_PATTERN.fullmatch(value):
            raise ValueError("iso3 must contain exactly three uppercase letters")
        return value

    @model_validator(mode="after")
    def validate_references(self, info: ValidationInfo) -> "CountryExceptionFile":
        if self.country_id != f"CTY-{self.iso3}":
            raise ValueError("country_id must equal CTY-<iso3>")

        variable_ids: set[str] = (info.context or {}).get("variable_ids", set())
        pattern = re.compile(rf"^EXC-{self.iso3}-\d{{3}}$")
        for exception in self.exceptions:
            if not pattern.fullmatch(exception.exception_id):
                raise ValueError(
                    f"exception_id must match EXC-{self.iso3}-<NNN>"
                )
            unknown = set(exception.applies_to_variables) - variable_ids
            if unknown:
                raise ValueError(f"unknown variable IDs: {sorted(unknown)}")
        return self
