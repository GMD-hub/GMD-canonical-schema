---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-twagencototalyear
canonical_label: Annualized wage in all jobs excl. bonuses (12-month ref period)
variable_name: t_wage_nc_total_year
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
- VAR-wagencyear
- VAR-wagenc2year
- VAR-twagencothersyear
derives_to:
- VAR-lincnc
- VAR-laborincome
- VAR-twagetotalyear
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - total wage
  - wage all jobs
  - 12 months
  typical_section_names:
  - Labor
  - Total earnings
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Employment Earnings, 12-month reference
    period, t_wage_nc_total_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Total employment earnings family, 12-month reference period. All jobs. Total
    annualized wage income excluding tips/bonuses.
---
## Definition

`t_wage_nc_total_year` is a numeric/continuous variable recording the total annualized wage income in all jobs including primary, secondary and others, excluding tips, bonuses, and other payments. This is the total across all jobs.

## Conceptual intent

t_wage_nc_total_year aggregates the non-compensation annual wage across all jobs.

## Construction notes

Use gross wages when available. Annualization depends on available data; see wage_total formulae.

## Consistency checks

- t_wage_nc_total_year must be non-negative.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
