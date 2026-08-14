---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-unitwage
canonical_label: Time unit of last wage payment, primary job (7-day ref period)
variable_name: unitwage
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
  label: Daily
- value: 2
  label: Weekly
- value: 3
  label: Every two weeks
- value: 4
  label: Every two months
- value: 5
  label: Monthly
- value: 6
  label: Quarterly
- value: 7
  label: Every six months
- value: 8
  label: Annually
- value: 9
  label: Hourly
- value: 10
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
derives_to:
- VAR-wagetotal
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
- variable_id: VAR-empstat
  condition: empstat == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - salary
  - payment period
  - how often paid
  - wage time unit
  typical_section_names:
  - Employment
  - Wages
  - Primary job
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    unitwage
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Time reference for wage_nc.
---
## Definition

`unitwage` is a categorical variable recording the time reference (time unit measurement) for the wage_nc variable. Acceptable values range from 1 = Daily through 10 = Other, including weekly, bi-weekly, monthly, quarterly, semi-annual, annual, and hourly.

## Conceptual intent

unitwage records the time unit of the last wage payment, which is required to annualize wages into wage_total and labor-income aggregates.

## Construction notes

Record the unit corresponding to the period over which the wage_nc payment applies. This value is essential for the wage_total annualization formula.

## Consistency checks

- unitwage must be an integer in [1,10].
- Should be non-missing wherever wage_nc is non-missing.

## Escalation triggers

- The survey does not clarify the payment period of the reported wage.

## Common mistakes

- Confusing bi-weekly (3, every two weeks) with semi-annual (7, every six months).
- Leaving unitwage missing while wage_nc is present.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
