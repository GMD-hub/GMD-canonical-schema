---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-thourstotal
canonical_label: Annualized hours worked in all jobs (7-day ref period)
variable_name: t_hours_total
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
- VAR-whours
- VAR-whours2
- VAR-thoursothers
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
  - annual hours
  typical_section_names:
  - Employment
  - Total earnings
  - Hours
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Employment Earnings, 7-day reference
    period, t_hours_total
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Total employment earnings family, 7-day reference period. All jobs including primary, secondary
    and others. Annualized hours worked in all jobs.
---
## Definition

`t_hours_total` is a numeric/continuous variable recording the hours of work in the last 12 months in all jobs including primary, secondary and others. This is the total across all jobs.

## Conceptual intent

t_hours_total aggregates annual hours across all jobs, providing a total labor-supply measure.

## Construction notes

Derived as the sum of hours across the primary, secondary, and other jobs.

## Consistency checks

- t_hours_total must be non-negative.
- Should equal whours + whours_2 + t_hours_others where data are complete.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
