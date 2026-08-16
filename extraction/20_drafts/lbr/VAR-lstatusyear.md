---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-lstatusyear
canonical_label: Labor status (12-month ref period)
variable_name: lstatus_year
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
  label: Employed
- value: 2
  label: Unemployed
- value: 3
  label: Not-in-labor force
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
- VAR-nlfreasonyear
- VAR-unempldurlyear
- VAR-unemplduruyear
- VAR-empstatyear
- VAR-ocusecyear
- VAR-industryorigyear
- VAR-industrycat10year
- VAR-industrycat4year
- VAR-occuporigyear
- VAR-occupyear
- VAR-wagencyear
- VAR-unitwageyear
- VAR-whoursyear
- VAR-wmonthsyear
- VAR-wagetotalyear
- VAR-contractyear
- VAR-healthinsyear
- VAR-socialsecyear
- VAR-unionyear
- VAR-firmsizelyear
- VAR-firmsizeuyear
- VAR-empstat2year
- VAR-ocusec2year
- VAR-industryorig2year
- VAR-industrycat102year
- VAR-industrycat42year
- VAR-occuporig2year
- VAR-occup2year
- VAR-wagenc2year
- VAR-unitwage2year
- VAR-whours2year
- VAR-wmonths2year
- VAR-wagetotal2year
- VAR-firmsizel2year
- VAR-firmsizeu2year
- VAR-thoursothersyear
- VAR-twagencothersyear
- VAR-twageothersyear
- VAR-thourstotalyear
- VAR-twagencototalyear
- VAR-twagetotalyear
country_parameters: []
prerequisites:
- variable_id: VAR-minlaborageyear
  condition: age >= minlaborage_year
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - labor status
  - last 12 months
  - worked last year
  typical_section_names:
  - Labor
  - Labor status
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 12-month reference period,
    lstatus_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. See 7-day lstatus for definitions.
---
## Definition

`lstatus_year` is a categorical variable recording an individual's labor status in the last 12 months. Three categories after harmonization: 1 = Employed, 2 = Unemployed, 3 = Not-in-labor force.

## Conceptual intent

lstatus_year indicates labor status over the past 12 months. Note that the 12-month labor status primarily reflects whether the person worked during the last year, as many surveys cannot distinguish the unemployed from the out of the labor force over 12 months.

## Construction notes

The value must be missing for individuals below MINLABORAGE_YEAR. See the 7-day lstatus for category definitions.

## Consistency checks

- The 12-month status primarily reflects work over the past year; do not force an unemployed/out-of-labor-force split where the survey cannot support it.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
