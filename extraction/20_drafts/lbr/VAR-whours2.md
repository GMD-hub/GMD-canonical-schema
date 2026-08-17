---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-whours2
canonical_label: Hours of work in the last week, secondary job (7-day ref period)
variable_name: whours_2
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
- VAR-wagetotal2
- VAR-thourstotal
- VAR-thoursannual
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - hours
  - second job hours
  - hours per week secondary
  typical_section_names:
  - Employment
  - Secondary job
  - Hours
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    whours_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Hours of work in the last week for the secondary
    job.
---
## Definition

`whours_2` is a numeric/continuous variable recording the hours of work in the last week for the second job with reference period of the last 7 days. The second job is the occupation to which the person dedicated the second most time over the past week.

## Conceptual intent

whours_2 measures weekly hours on the secondary job.

## Construction notes

Apply the same conventions as whours: record actual hours if absent; multiply daily hours by 5; divide monthly hours by 4.3.

## Consistency checks

- whours_2 must be non-negative and reasonable for one week (0-168).
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- Hours are reported only categorically.
- The survey uses a reference period other than 7 days for hours worked.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
