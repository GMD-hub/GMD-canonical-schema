---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat10year
canonical_label: 1-digit industry classification, primary job (12-month ref period)
variable_name: industrycat10_year
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
  label: Agriculture, Hunting, Fishing, etc.
- value: 2
  label: Mining
- value: 3
  label: Manufacturing
- value: 4
  label: Public Utility Services
- value: 5
  label: Construction
- value: 6
  label: Commerce
- value: 7
  label: Transport and Communications
- value: 8
  label: Financial and Business Services
- value: 9
  label: Public Administration
- value: 10
  label: Other Services, Unspecified
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
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards:
- name: ISIC Rev. 3.1/4.0 (International Standard Industrial Classification)
  url: https://unstats.un.org/unsd/classifications/Econ/ISIC
source_hints:
  question_keywords:
  - industry
  - 1 digit industry
  - 12 months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    industrycat10_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Primary job family, 12-month reference period. Based on ISIC Rev. 3.1/4.0.
---
## Definition

`industrycat10_year` is a categorical variable recording the 1-digit industry classification in the last 12 months for the main job. Ten categories after harmonization, based on the UN ISIC.

## Conceptual intent

industrycat10_year provides a comparable 1-digit industry classification for the 12-month primary job.

## Construction notes

See the 7-day industrycat10 definitions. If all 10 categories cannot be identified, set missing and create industrycat4_year.

## Consistency checks

- industrycat10_year must be an integer in [1,10] where non-missing.
- Should be non-missing only where lstatus_year == 1.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
