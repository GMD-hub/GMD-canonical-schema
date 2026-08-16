---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-lstatus
canonical_label: Labor status (7-day ref period)
variable_name: lstatus
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
- VAR-nlfreason
- VAR-unempldurl
- VAR-unemplduru
- VAR-empstat
- VAR-ocusec
- VAR-industryorig
- VAR-industrycat10
- VAR-industrycat4
- VAR-occuporig
- VAR-occup
- VAR-wagenc
- VAR-unitwage
- VAR-whours
- VAR-wmonths
- VAR-wagetotal
- VAR-contract
- VAR-healthins
- VAR-socialsec
- VAR-union
- VAR-firmsizel
- VAR-firmsizeu
- VAR-empstat2
- VAR-ocusec2
- VAR-industryorig2
- VAR-industrycat102
- VAR-industrycat42
- VAR-occuporig2
- VAR-occup2
- VAR-wagenc2
- VAR-unitwage2
- VAR-whours2
- VAR-wmonths2
- VAR-wagetotal2
- VAR-firmsizel2
- VAR-firmsizeu2
- VAR-thoursothers
- VAR-twagencothers
- VAR-twageothers
- VAR-thourstotal
- VAR-twagencotal
- VAR-twagetotal
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: age >= minlaborage
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - labor status
  - employment status
  - worked
  - looking for work
  - last 7 days
  - reference week
  typical_section_names:
  - Labor status
  - Employment
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 7-day reference period, lstatus
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Chapter source file is chapter5-LMR.qmd, where 'LMR' is the module-code alias for LBR; references
    resolve to MOD-LBR (Labor).
---
## Definition

`lstatus` is a categorical variable recording an individual's labor status in the last 7 days. Three categories are used after harmonization: 1 = Employed, 2 = Unemployed, 3 = Not-in-labor force.

## Conceptual intent

lstatus is the central labor-force-status indicator of the 7-day reference period and drives virtually all other labor variables. Employed is anyone who worked at least 1 hour in the last 7 days or had a job but did not work; unemployed is not working but actively seeking (or waiting to start) a job; not-in-labor force is not working and not seeking.

## Construction notes

The value must be missing for individuals below the minimum working age (MINLABORAGE). Employed includes formal, informal, paid, and unpaid work for a minimum of 1 hour. The pre-2013 ILO employment definition is retained for comparability; own-production and unpaid labor that the 2013 ILO resolution would reclassify are treated using the traditional definition.

## Consistency checks

- LSTATUS must be an integer in the range [1,3]. Flag `lstatus < 1 | lstatus > 3 | mod(lstatus,1) != 0`.
- If LSTATUS is employed, the employment type (EMPSTAT) must be defined: flag `lstatus == 1 & empstat missing`.
- If an employment type is defined, labor status must be employed: flag `empstat <= 5 & lstatus != 1`.

## Escalation triggers

- The survey uses a post-2013 ILO employment definition that conflicts with the harmonized pre-2013 definition.
- A large share of working-age records has missing lstatus.
- The questionnaire does not clearly distinguish unemployed from not-in-labor force.

## Common mistakes

- Coding unemployed or not-in-labor force as employed.
- Leaving lstatus missing for individuals above the minimum working age.
- Applying labor variables to individuals below MINLABORAGE.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
