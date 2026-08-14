---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-unempldurl
canonical_label: Unemployment duration (months), lower bracket (7-day ref period)
variable_name: unempldur_l
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
  - how long looking for work
  - duration of unemployment
  typical_section_names:
  - Labor status
  - Unemployment
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 7-day reference period, unempldur_l
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Labor status family, 7-day reference period. Lower bracket of unemployment duration in months.
---
## Definition

`unempldur_l` is a numeric/continuous variable recording the duration of unemployment in months (lower bracket), in the last 7 days. The variable is constructed for all unemployed persons (LSTATUS=2) and is missing otherwise.

## Conceptual intent

unempldur_l records the lower boundary of unemployment duration. It allows estimation of short- and long-term unemployment and supports the analysis of labor underutilization.

## Construction notes

If recorded continuously in the survey, records the number of months in unemployment. If categorical, records the lower boundary of the bracket. Missing values are allowed for everyone who is not unemployed.

## Consistency checks

- Should be non-missing only where lstatus == 2.
- If the survey records a bracket, the lower boundary must be <= the upper boundary (compare with unempldur_u).

## Escalation triggers

- The survey reports duration in units other than months (e.g. weeks) without conversion guidance.
- A categorical bracket has no defined lower boundary.

## Common mistakes

- Confusing the lower and upper brackets when the survey is categorical.
- Recording duration for non-unemployed individuals.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
