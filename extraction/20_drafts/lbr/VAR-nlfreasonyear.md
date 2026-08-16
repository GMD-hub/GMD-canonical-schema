---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-nlfreasonyear
canonical_label: Reason not in the labor force (12-month ref period)
variable_name: nlfreason_year
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
  label: Student
- value: 2
  label: Housewife
- value: 3
  label: Retired
- value: 4
  label: Disabled
- value: 5
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
derives_to: []
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 3
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - reason not in labor force
  - 12 months
  - inactive reason
  typical_section_names:
  - Labor
  - Labor status
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 12-month reference period,
    nlfreason_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. See 7-day nlfreason for definitions.
---
## Definition

`nlfreason_year` is a categorical variable recording the reason an individual was not in the labor force in the last 12 months. Constructed for those not employed and not looking for work (LSTATUS_YEAR=3); missing otherwise.

## Conceptual intent

nlfreason_year characterizes 12-month inactivity by reason.

## Construction notes

Five categories after harmonization, identical to nlfreason. See 7-day nlfreason for definitions.

## Consistency checks

- nlfreason_year should only be non-missing where lstatus_year == 3.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
