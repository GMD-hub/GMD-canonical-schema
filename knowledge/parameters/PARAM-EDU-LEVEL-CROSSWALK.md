---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.2
# ================================================================

parameter_id: PARAM-EDU-LEVEL-CROSSWALK
parameter_name: "Country education crosswalk rows"
module_id: MOD-EDU
schema_version: "0.2"
status: draft
authority: "GPID Team"

kind: construction
value_type: table
value_schema: null
row_schema:
  country_entry_id: string
  national_label_en: string
  national_label_local: string
  entry_age: integer
  duration_years: integer
  isced_level: string
  isced_label: string
  gmd_educat4_target: string
  gmd_educat5_target: string
  gmd_educat7_target: string
  source_row: integer

applies_to_variables:
  - VAR-educat4

fallback_policy: block_and_escalate
global_default: null

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-09-06"
  human_reviewed: false
  reviewer: null
  notes: "Canonical contract for row-based country education crosswalk values."
---

## Definition

Defines row-level country crosswalk records that map national education labels
and ISCED levels to GMD education targets.

## Parameter notes

- This parameter is row-based (`value_type: table`) rather than a compact
  mapping because country source workbooks carry row-level metadata.
- `source_row` preserves traceability to the source workbook row used in
  extraction.

## Fallback behavior

`block_and_escalate` is required when no valid country record exists.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-06 | 0.2 | Add table contract for education crosswalk extraction | GPID Team |
