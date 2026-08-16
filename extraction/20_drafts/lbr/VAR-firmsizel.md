---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-firmsizel
canonical_label: Firm size (lower bracket), primary job (7-day ref period)
variable_name: firmsize_l
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
  - number of employees
  - size of establishment
  - workers in establishment
  typical_section_names:
  - Employment
  - Primary job
  - Firm size
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    firmsize_l
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Lower bracket of firm size.
---
## Definition

`firmsize_l` is a numeric/continuous variable recording the lower bracket of the firm size for persons employed in the last 7 days in the main job. If continuous, records the number of people working for the same employer; if categorical, the lower boundary of the bracket.

## Conceptual intent

firmsize_l provides the lower bound of establishment size, used as a formality proxy and in enterprise-size analysis.

## Construction notes

Record the number of workers at the establishment. When categorical, record the bracket's lower boundary.

## Consistency checks

- firmsize_l must be non-negative.
- firmsize_u must not be lower than firmsize_l.

## Escalation triggers

- Firm size is reported only subjectively (e.g. small/large) without numeric bounds.

## Common mistakes

- Confusing firmsize_l with firmsize_u.
- Recording categorical firm size as continuous.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
