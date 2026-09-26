"""Models for country parameter value files."""

import re
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator, model_validator

from schema.parameter import ParameterDefinition


ISO3_PATTERN = re.compile(r"^[A-Z]{3}$")

ENTRY_ID_SEGMENT_BY_PARAMETER = {
    "PARAM-EDU-LEVEL-CROSSWALK": "EDU",
    "PARAM-WASH-WATER-CROSSWALK": "WAS",
    "PARAM-WASH-SANITATION-CROSSWALK": "SAN",
    "PARAM-GEO-GMD-CROSSWALK": "SUBNAT",
}


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
    selectors: dict[str, str | int | bool] | None = None
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
    focal_point: str | None = None
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
            self._validate_value(record.value, definition, self.iso3, record.parameter_id)
        return self

    @staticmethod
    def _validate_value(
        value: Any,
        definition: ParameterDefinition,
        iso3: str,
        parameter_id: str,
    ) -> None:
        if definition.value_type == "integer":
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{definition.parameter_id} value must be an integer")
            return

        if definition.value_type == "table":
            if not isinstance(value, list):
                raise ValueError(f"{definition.parameter_id} value must be a list of rows")

            schema = definition.row_schema or {}
            expected = set(schema.keys())
            expected_entry_segment = ENTRY_ID_SEGMENT_BY_PARAMETER.get(parameter_id)
            seen_entry_ids: set[str] = set()
            for index, row in enumerate(value):
                if not isinstance(row, dict):
                    raise ValueError(
                        f"{definition.parameter_id} row {index} must be a mapping"
                    )
                if set(row.keys()) != expected:
                    raise ValueError(
                        f"{definition.parameter_id} row {index} keys must be {sorted(expected)}"
                    )
                for key, expected_type in schema.items():
                    item = row[key]
                    if expected_type == "integer":
                        if isinstance(item, bool) or not isinstance(item, int):
                            raise ValueError(
                                f"{definition.parameter_id} row {index} field {key} must be an integer"
                            )
                    elif expected_type == "string":
                        if not isinstance(item, str):
                            raise ValueError(
                                f"{definition.parameter_id} row {index} field {key} must be a string"
                            )
                    elif expected_type == "boolean":
                        if not isinstance(item, bool):
                            raise ValueError(
                                f"{definition.parameter_id} row {index} field {key} must be a boolean"
                            )

                if expected_entry_segment is None:
                    continue

                entry_id = row.get("country_entry_id")
                if not isinstance(entry_id, str) or not entry_id:
                    raise ValueError(
                        f"{definition.parameter_id} row {index} field country_entry_id must be a non-empty string"
                    )

                expected_pattern = rf"^{iso3}-{expected_entry_segment}-\d{{2,}}$"
                if not re.fullmatch(expected_pattern, entry_id):
                    raise ValueError(
                        f"{definition.parameter_id} row {index} country_entry_id must match {iso3}-{expected_entry_segment}-NN"
                    )

                if entry_id in seen_entry_ids:
                    raise ValueError(f"{definition.parameter_id} duplicate country_entry_id: {entry_id}")
                seen_entry_ids.add(entry_id)
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
