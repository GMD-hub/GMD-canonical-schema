---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-whoursyear
canonical_label: Hours of work in the last week, primary job (12-month ref period)
variable_name: whours_year
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
  max: 168
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to:
- VAR-wagetotalyear
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - hours
  - hours worked
  - 12 months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    whours_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Primary job family, 12-month reference period. Hours of work in the last
    week for the main job.
---
## Definition

`whours_year` is a numeric/continuous variable recording the hours of work last week for the main job of any individual with a job (LSTATUS_YEAR=1). The main job is the occupation to which the person dedicated the most time over the past week.

## Conceptual intent

whours_year measures weekly hours on the 12-month primary job.

## Construction notes

Apply the same conventions as whours (absent weeks, daily-hours x5, monthly-hours /4.3).

## Consistency checks

- whours_year must be non-negative and within [0,168].
- Should be non-missing only where lstatus_year == 1.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
