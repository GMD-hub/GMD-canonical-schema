---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-unemplduruyear
canonical_label: Unemployment duration (months) upper bracket (12-month ref period)
variable_name: unempldur_u_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric_continuous
value_codes: null
allowed_range:
  min: 0
  max: 120
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
  condition: lstatus_year == 2
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - unemployment duration
  - 12 months
  - upper bracket
  typical_section_names:
  - Labor
  - Labor status
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 12-month reference period,
    unempldur_u_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Upper bracket of unemployment duration.
---
## Definition

`unempldur_u_year` is a numeric/continuous variable recording the duration of unemployment in months (upper bracket) in the last 12 months. Constructed for all unemployed persons (LSTATUS_YEAR=2); missing otherwise; open-ended upper bracket is missing.

## Conceptual intent

unempldur_u_year records the upper boundary of 12-month unemployment duration.

## Construction notes

If duration is continuous, unempldur_l_year and unempldur_u_year take the same value. If the upper range is open-ended, unempldur_u_year is missing.

## Consistency checks

- If continuous, unempldur_u_year == unempldur_l_year.
- Open-ended upper bracket must be missing.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
