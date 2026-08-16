---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-twagetotalyear
canonical_label: Annualized total wage for all jobs (12-month ref period)
variable_name: t_wage_total_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
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
- VAR-twagencototalyear
derives_to:
- VAR-lincnc
- VAR-laborincome
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - total wage
  - total earnings
  - 12 months
  typical_section_names:
  - Labor
  - Total earnings
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Employment Earnings, 12-month reference
    period, t_wage_total_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Total employment earnings family, 12-month reference period. All jobs. Total
    annualized wage income including tips/bonuses for all jobs.
---
## Definition

`t_wage_total_year` is a numeric/continuous variable recording the total annualized wage income in all jobs including primary, secondary and others, including tips, bonuses, and other payments. This is the total across all jobs.

## Conceptual intent

t_wage_total_year aggregates the total (including compensation) annual wage across all jobs.

## Construction notes

t_wage_total_year equals t_wage_nc_total_year when there are no bonuses/tips.

## Consistency checks

- t_wage_total_year must be >= t_wage_nc_total_year.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
