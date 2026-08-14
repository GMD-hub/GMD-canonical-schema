---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-firmsizel2year
canonical_label: Firm size (lower bracket), secondary job (12-month ref period)
variable_name: firmsize_l_2_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric_continuous
value_codes: null
allowed_range:
  min: 0
  max: 999999
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to: []
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - firm size
  - second job firm size
  - 12 months
  typical_section_names:
  - Labor
  - Secondary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 12-month reference
    period, firmsize_l_2_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Secondary job family, 12-month reference period. Lower bracket of firm size.
---
## Definition

`firmsize_l_2_year` is a numeric/continuous variable recording the lower bracket of the firm size for persons employed in the last 12 months in the main job. If continuous, records the number of workers; if categorical, the lower boundary of the bracket.

## Conceptual intent

firmsize_l_2_year provides the lower bound of establishment size for the 12-month secondary job.

## Construction notes

Record the number of workers; when categorical, record the lower boundary.

## Consistency checks

- firmsize_l_2_year must be non-negative.
- firmsize_u_2_year must not be lower than firmsize_l_2_year.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
