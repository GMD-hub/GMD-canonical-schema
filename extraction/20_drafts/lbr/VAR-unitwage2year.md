---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-unitwage2year
canonical_label: Time unit of last wage payment, secondary job (12-month ref period)
variable_name: unitwage_2_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
data_type: categorical
value_codes:
- value: 1
  label: Daily
- value: 2
  label: Weekly
- value: 3
  label: Every two weeks
- value: 4
  label: Every two months
- value: 5
  label: Monthly
- value: 6
  label: Quarterly
- value: 7
  label: Every six months
- value: 8
  label: Annually
- value: 9
  label: Hourly
- value: 10
  label: Other
allowed_range: null
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to:
- VAR-wagetotal2year
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
- variable_id: VAR-empstat2year
  condition: empstat_2_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - payment period
  - second job
  typical_section_names:
  - Labor
  - Secondary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 12-month reference
    period, unitwage_2_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Secondary job family, 12-month reference period. Time reference for wage_nc_2_year.
---
## Definition

`unitwage_2_year` is a categorical variable recording the time reference for the wage_nc_2_year variable. Ten categories after harmonization, identical to unitwage.

## Conceptual intent

unitwage_2_year records the time unit of the 12-month secondary wage for annualization.

## Construction notes

Record the unit corresponding to the period over which the wage applies.

## Consistency checks

- unitwage_2_year must be an integer in [1,10] where non-missing.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
