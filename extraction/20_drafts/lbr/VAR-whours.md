---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-whours
canonical_label: Hours of work in the last week, primary job (7-day ref period)
variable_name: whours
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
- VAR-wagetotal
- VAR-twageothers
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
  - hours worked
  - hours per week
  - hours of work
  - working time
  typical_section_names:
  - Employment
  - Primary job
  - Hours
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    whours
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Hours of work in the last week for the main job.
---
## Definition

`whours` is a numeric/continuous variable recording the hours of work last week for the main job of any individual with a job (LSTATUS=1). The main job is defined as the occupation to which the person dedicated the most time over the past week.

## Conceptual intent

whours measures weekly hours on the main job, required for hourly earnings, labor-intensity analysis, and wage annualization.

## Construction notes

If the respondent was absent (holidays, vacation, sick leave) record hours worked in the previous 7 days actually worked. If hours are given per day with no days-worked information, multiply by 5. If hours per month are given, divide by 4.3.

## Consistency checks

- whours must be non-negative and reasonable for one week (0-168).
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- Hours are reported only as a range or a category, not continuous.

## Common mistakes

- Multiplying/dividing hours by the wrong factor when converting from daily or monthly figures.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
