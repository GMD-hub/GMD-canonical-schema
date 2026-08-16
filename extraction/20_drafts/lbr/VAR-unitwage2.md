---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-unitwage2
canonical_label: Time unit of last wage payment, secondary job (7-day ref period)
variable_name: unitwage_2
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
- VAR-wagetotal2
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
- variable_id: VAR-empstat2
  condition: empstat_2 == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - second job wage period
  - payment period
  typical_section_names:
  - Employment
  - Secondary job
  - Wages
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    unitwage_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Time reference for wage_nc_2.
---
## Definition

`unitwage_2` is a categorical variable recording the time reference (time unit measurement) for the wage_nc_2 variable. Ten categories after harmonization, identical to unitwage (1 = Daily through 10 = Other).

## Conceptual intent

unitwage_2 records the time unit of the secondary-job wage required for annualization.

## Construction notes

Record the unit corresponding to the period over which the secondary wage applies.

## Consistency checks

- unitwage_2 must be an integer in [1,10] where non-missing.

## Escalation triggers

- The secondary-job payment period is not reported.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
