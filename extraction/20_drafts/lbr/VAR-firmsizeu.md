---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-firmsizeu
canonical_label: Firm size (upper bracket), primary job (7-day ref period)
variable_name: firmsize_u
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
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
  - number of employees
  - upper bracket
  - size of establishment
  typical_section_names:
  - Employment
  - Primary job
  - Firm size
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    firmsize_u
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Upper bracket of firm size.
---
## Definition

`firmsize_u` is a numeric/continuous variable recording the upper bracket of the firm size for persons employed in the last 7 days in the main job. If continuous, records the number of people working for the same employer; if categorical, the upper boundary of the bracket; if the right bracket is open, this variable should be missing.

## Conceptual intent

firmsize_u provides the upper bound of establishment size.

## Construction notes

Record the number of workers at the establishment. When the upper bound is open-ended, code as missing.

## Consistency checks

- If the right bracket is open, firmsize_u must be missing.
- firmsize_u must not be lower than firmsize_l.

## Escalation triggers

- An open-ended firm-size bracket is assigned a finite value.

## Common mistakes

- Coding an open upper bracket as a finite number.
- Setting firmsize_u below firmsize_l.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
