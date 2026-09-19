---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.2
# ================================================================

parameter_id: PARAM-GEO-GMD-CROSSWALK
parameter_name: "Country geography crosswalk rows"
module_id: MOD-GEO
schema_version: "0.2"
status: draft
authority: "GPID Team"

kind: construction
value_type: table
value_schema: null
row_schema:
  survey_labels: string
  survey_variables: string
  gmd_subnatid1: string
  gmd_subnatid2: string
  gmd_subnatid3: string
  gmd_subnatid4: string
  is_rep_subnat1: boolean
  is_rep_subnat2: boolean
  is_rep_subnat3: boolean
  is_rep_subnat4: boolean
  representative_level: integer
  gmd_subnatidsurvey: string
  geo_year: string
  geo_source: string
  geo_level: string
  geo_idvar: string
  geo_id: string
  geo_nvar: string
  geo_name: string
  source_row: integer

applies_to_variables:
  - VAR-subnatid1
  - VAR-subnatid2
  - VAR-subnatid3
  - VAR-subnatid4
  - VAR-subnatidsurvey

fallback_policy: block_and_escalate
global_default: null

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-09-18"
  human_reviewed: false
  reviewer: null
  notes: "Canonical contract for row-based country geography crosswalk values."
---

## Definition

Defines row-level country geography crosswalk records that map survey labels
and source geography fields to GMD subnational identifiers and the survey-level
geography anchor.

## Parameter notes

- This parameter is row-based (`value_type: table`) because country source
  workbooks carry row-level crosswalk metadata.
- `survey_variables` stores one or more survey variables (`subnatid`,
  `subnatid1`, `subnatid2`, etc.) when rows are merged by geo identity.
- `survey_labels` stores one or more source label variants for the same
  geography identity.
- `gmd_subnatid1` to `gmd_subnatid4` are populated from `geo_code` according to
  the inferred representative level.
- `gmd_subnatidsurvey` stores the survey geography anchor used to align
  `VAR-subnatid1` to `VAR-subnatid4` across country implementations.
- `geo_year`, `geo_source`, `geo_level`, `geo_idvar`, `geo_id`, `geo_nvar`,
  and `geo_name` preserve source GEO metadata required for downstream
  crosswalking and diagnostics.
- `representative_level` and `is_rep_subnat*` preserve representativeness flags
  by subnational level.
- `source_row` preserves traceability to the source workbook row used in
  extraction.

## Fallback behavior

`block_and_escalate` is required when no valid country record exists.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-18 | 0.2 | Add table contract for geography crosswalk extraction | GPID Team |
