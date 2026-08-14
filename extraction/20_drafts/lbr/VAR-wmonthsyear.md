---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wmonthsyear
canonical_label: Months worked in the last 12 months, primary job (12-month ref period)
variable_name: wmonths_year
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
  max: 12
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
- VAR-lincnc
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - months worked
  - 12 months
  - months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    wmonths_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Primary job family, 12-month reference period. Months worked in the last
    12 months for the main job.
---
## Definition

`wmonths_year` is a numeric/continuous variable recording the number of months worked in the last 12 months for the main job of any individual with a job (LSTATUS_YEAR=1). The main job is the occupation with the most time over the past week.

## Conceptual intent

wmonths_year captures months of work in the 12-month primary job for annualization.

## Construction notes

Record the number of months; do not assume full-year work.

## Consistency checks

- wmonths_year must lie in [0,12].
- Should be non-missing only where lstatus_year == 1.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
