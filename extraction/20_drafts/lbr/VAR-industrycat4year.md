---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat4year
canonical_label: 4-category industry classification, primary job (12-month ref period)
variable_name: industrycat4_year
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
  label: Agriculture
- value: 2
  label: Industry
- value: 3
  label: Services
- value: 4
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
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - industry
  - broad economic activity
  - 12 months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    industrycat4_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Primary job family, 12-month reference period. Broad Economic Activities.
---
## Definition

`industrycat4_year` is a categorical variable recording the 1-digit industry classification for Broad Economic Activities for the main job in the last 12 months. Four categories after harmonization.

## Conceptual intent

industrycat4_year aggregates 12-month primary industry into four broad categories.

## Construction notes

Created directly from data or from industrycat10_year.

## Consistency checks

- industrycat4_year must be an integer in [1,4] where non-missing.
- Must not conflict with industrycat10_year.

## Escalation triggers

- Aggregating industrycat10_year into industrycat4_year incorrectly.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
