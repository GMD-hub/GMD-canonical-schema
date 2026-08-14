---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-thourstotalyear
canonical_label: Annualized hours worked in all jobs (12-month ref period)
variable_name: t_hours_total_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: derived
data_type: numeric_continuous
value_codes: null
allowed_range: null
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from:
- VAR-whoursyear
- VAR-whours2year
- VAR-thoursothersyear
derives_to:
- VAR-thoursannual
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - total hours
  - hours all jobs
  - 12 months
  typical_section_names:
  - Labor
  - Total earnings
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Employment Earnings, 12-month reference
    period, t_hours_total_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Total employment earnings family, 12-month reference period. All jobs. Annualized
    hours worked in all jobs.
---
## Definition

`t_hours_total_year` is a numeric/continuous variable recording the hours of work in the last 12 months in all jobs including primary, secondary and others. This is the total across all jobs.

## Conceptual intent

t_hours_total_year aggregates annual hours across all jobs for the 12-month reference period.

## Construction notes

Derived as the sum of hours across the primary, secondary, and other jobs.

## Consistency checks

- t_hours_total_year must be non-negative.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
