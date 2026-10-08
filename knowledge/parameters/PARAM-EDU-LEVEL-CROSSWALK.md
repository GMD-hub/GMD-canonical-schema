---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.3
# ================================================================

parameter_id: PARAM-EDU-LEVEL-CROSSWALK
parameter_name: "Country education crosswalk rows"
module_id: MOD-EDU
schema_version: "0.3"
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
  parent_country_entry_ids: array_of_string
  cum_years_schooling: integer_or_null
  cum_years_computation_path: array_of_string
  cum_years_status: string
  review_flags: array_of_string

applies_to_variables:
  - VAR-educat4
  - VAR-educy

fallback_policy: block_and_escalate
global_default: null

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-09-06"
  human_reviewed: false
  reviewer: null
  notes: "v0.3 adds parent_country_entry_ids, cum_years_schooling,
          cum_years_computation_path, cum_years_status, and review_flags so
          RULE-EDU-003 (v0.2) can resolve VAR-educy directly from a matched
          country_entry_id row instead of a fixed GMD-wide tertiary-year
          table. Derived fields are computed by
          extraction_pipeline/country_inputs/education_pathways.py from the
          pre-existing isced_level, duration_years, and national_label_en
          fields already present in every country's parameters.md.
          cum_years_status is 'computed' or 'review_required'; rows with
          multiple candidate parent paths are flagged in review_flags with
          the minimum-path assumption used and remain visible for future
          correction rather than hidden. A full 206-country sweep
          (2026-09-30) produced 0 review_required and 0 failures; 176
          countries were flagged 'ambiguous' (multi-parent tertiary
          branches) and are promoted with review_flags intact pending
          further review."
---

## Definition

Defines row-level country crosswalk records that map national education labels
and ISCED levels to GMD education targets.

## Parameter notes

- This parameter is row-based (`value_type: table`) rather than a compact
  mapping because country source workbooks carry row-level metadata.
- `source_row` preserves traceability to the source workbook row used in
  extraction.
- `parent_country_entry_ids`, `cum_years_schooling`,
  `cum_years_computation_path`, `cum_years_status`, and `review_flags` are
  derived fields: they are computed from `isced_level`, `duration_years`,
  and `national_label_en` already present in the row, not independently
  sourced. `cum_years_schooling` is `null` when `cum_years_status` is
  `review_required`.
- Rows at `isced_level: '0'` are excluded from `cum_years_schooling`
  totals (early childhood education is not counted as school years).
- When a row has more than one plausible parent (e.g., multiple tertiary
  entry tracks), the derivation selects the minimum-years parent path and
  records this assumption in `review_flags`.

## Fallback behavior

`block_and_escalate` is required when no valid country record exists, or
when a reported national level cannot be matched to any `country_entry_id`
for the survey's ISO3 code and survey ID year.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-06 | 0.2 | Add table contract for education crosswalk extraction | GPID Team |
| 2026-09-30 | 0.3 | Add derived years-of-schooling fields and VAR-educy to applies_to_variables, to support RULE-EDU-003 v0.2 | GPID Team |
