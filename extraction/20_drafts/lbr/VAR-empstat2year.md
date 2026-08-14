---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-empstat2year
canonical_label: Employment status, secondary job (12-month ref period)
variable_name: empstat_2_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
unit_of_analysis: individual
mapping_role: atomic
data_type: categorical
value_codes:
- value: 1
  label: Paid Employee
- value: 2
  label: Non-Paid Employee
- value: 3
  label: Employer
- value: 4
  label: Self-employed
- value: 5
  label: Other, workers not classifiable by status
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
- VAR-wagenc2year
- VAR-wagetotal2year
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - employment status
  - second job
  - 12 months
  typical_section_names:
  - Labor
  - Secondary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 12-month reference
    period, empstat_2_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Secondary job family, 12-month reference period. See 7-day empstat for definitions.
---
## Definition

`empstat_2_year` is a categorical variable recording the main employment status in the last 12 months of any individual with a job (LSTATUS_YEAR=1). Five categories after harmonization.

## Conceptual intent

empstat_2_year classifies the status in employment of the 12-month secondary job.

## Construction notes

Construct for all individuals with a job (LSTATUS_YEAR=1); missing otherwise. See empstat definitions.

## Consistency checks

- empstat_2_year must be an integer in [1,5] where non-missing.
- Should be non-missing only where lstatus_year == 1.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
