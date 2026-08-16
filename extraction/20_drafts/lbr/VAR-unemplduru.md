---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-unemplduru
canonical_label: Unemployment duration (months), upper bracket (7-day ref period)
variable_name: unempldur_u
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
  max: 120
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
  condition: lstatus == 2
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - unemployment duration
  - months unemployed
  - upper bracket
  - duration of unemployment
  typical_section_names:
  - Labor status
  - Unemployment
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 7-day reference period, unempldur_u
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Labor status family, 7-day reference period. Upper bracket of unemployment duration in months.
---
## Definition

`unempldur_u` is a numeric/continuous variable recording the duration of unemployment in months (upper bracket), in the last 7 days. The variable is constructed for all unemployed persons (LSTATUS=2) and is missing otherwise.

## Conceptual intent

unempldur_u records the upper boundary of unemployment duration. If unemployment is recorded as a continuous variable, unempldur_l and unempldur_u take the same value. If the right bracket is open, unempldur_u is missing.

## Construction notes

If recorded continuously, records months of unemployment. If categorical, records the upper boundary of the bracket; if the right bracket is open, code as missing.

## Consistency checks

- If duration is continuous, unempldur_u == unempldur_l.
- If the upper bracket is open-ended, unempldur_u must be missing.
- Compare with unempldur_l: upper bracket must not be below the lower bracket.

## Escalation triggers

- An open-ended upper bracket is recorded as a value rather than missing.
- The survey does not make the bracket interpretation clear.

## Common mistakes

- Coding an open-ended bracket as a finite value.
- Setting unempldur_u below unempldur_l.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
