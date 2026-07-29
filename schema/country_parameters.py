"""Models for country parameter value files."""

import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator, model_validator

from schema.parameter import ParameterDefinition


ISO3_PATTERN = re.compile(r"^[A-Z]{3}$")


class CountryValueProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source: str
    verified_on: None = None
    human_reviewed: Literal[False]
    reviewer: None = None


class CountryParameterRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    parameter_id: str
    effective_from: int | None
    effective_to: int | None
    value: Any
    provenance: CountryValueProvenance

    @model_validator(mode="after")
    def validate_window(self) -> "CountryParameterRecord":
        if (
            self.effective_from is not None
            and self.effective_to is not None
            and self.effective_from > self.effective_to
        ):
            raise ValueError("effective_from must be less than or equal to effective_to")
        return self


class CountryParameterFile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    country_id: str
    country_name: str
    iso3: str
    schema_version: str
    status: Literal["draft"]
    parameters: list[CountryParameterRecord]

    @field_validator("iso3")
    @classmethod
    def validate_iso3(cls, value: str) -> str:
        if not ISO3_PATTERN.fullmatch(value):
            raise ValueError("iso3 must contain exactly three uppercase letters")
        return value

    @model_validator(mode="after")
    def validate_identity_and_values(self, info: ValidationInfo) -> "CountryParameterFile":
        if self.country_id != f"CTY-{self.iso3}":
            raise ValueError("country_id must equal CTY-<iso3>")

        registry: dict[str, ParameterDefinition] = (info.context or {}).get("registry", {})
        for record in self.parameters:
            definition = registry.get(record.parameter_id)
            if definition is None:
                raise ValueError(f"unknown parameter_id: {record.parameter_id}")
            self._validate_value(record.value, definition)
        return self

    @staticmethod
    def _validate_value(value: Any, definition: ParameterDefinition) -> None:
        if definition.value_type == "integer":
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{definition.parameter_id} value must be an integer")
            return

        if not isinstance(value, dict):
            raise ValueError(f"{definition.parameter_id} value must be a mapping")
        expected = set((definition.value_schema or {}).keys())
        if set(value.keys()) != expected:
            raise ValueError(
                f"{definition.parameter_id} value keys must be {sorted(expected)}"
            )
        if any(isinstance(item, bool) or not isinstance(item, int) for item in value.values()):
            raise ValueError(f"{definition.parameter_id} mapping values must be integers")
