---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-firmsizel2
canonical_label: Firm size (lower bracket), secondary job (7-day ref period)
variable_name: firmsize_l_2
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric_continuous
value_codes: null
allowed_range:
  min: 0
  max: 999999
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
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - firm size
  - second job firm size
  - employees
  typical_section_names:
  - Employment
  - Secondary job
  - Firm size
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    firmsize_l_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Lower bracket of firm size for the secondary job.
---
## Definition

`firmsize_l_2` is a numeric/continuous variable recording the lower bracket of the firm size for persons who are employed. If continuous, records the number of people working for the same employer; if categorical, the lower boundary of the bracket.

## Conceptual intent

firmsize_l_2 provides the lower bound of establishment size for the secondary job.

## Construction notes

Record the number of workers at the secondary-job establishment; when categorical, record the lower boundary.

## Consistency checks

- firmsize_l_2 must be non-negative.
- firmsize_u_2 must not be lower than firmsize_l_2.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
