---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagetotal2year
canonical_label: Annualized total wage, secondary job (12-month ref period)
variable_name: wage_total_2_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
unit_of_analysis: individual
mapping_role: derived
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
derived_from:
- VAR-wagenc2year
- VAR-unitwage2year
- VAR-wmonths2year
- VAR-whours2year
derives_to:
- VAR-twageothersyear
- VAR-twagencototalyear
- VAR-twagetotalyear
- VAR-lincnc
- VAR-laborincome
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
- variable_id: VAR-empstat2year
  condition: empstat_2_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - annualized wage
  - second job total wage
  - 12 months
  typical_section_names:
  - Labor
  - Secondary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 12-month reference
    period, wage_total_2_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: '12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Secondary job family, 12-month reference period. Derived: annualized wage
    including bonuses, in-kind and other compensation.'
---
## Definition

`wage_total_2_year` is a numeric/continuous variable recording the annualized wage payment (regular wage plus bonuses, in-kind, compensation) for the secondary occupation in local currency. The wage comes from the secondary job and includes tips and other compensation.

## Conceptual intent

wage_total_2_year annualizes total wage of the 12-month secondary job over months actually worked.

## Construction notes

Derived from wage_nc_2_year, unitwage_2_year, wmonths_2_year, and whours_2_year using the wage_total formula. Do not assume full-year work.

## Consistency checks

- wage_total_2_year must be >= 0.
- Only non-missing for lstatus_year == 1 and empstat_2_year == 1.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
