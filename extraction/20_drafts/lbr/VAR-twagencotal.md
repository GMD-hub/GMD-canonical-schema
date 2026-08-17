---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-twagencotal
canonical_label: Annualized wage in all jobs excl. bonuses (7-day ref period)
variable_name: t_wage_nc_total
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
- VAR-wagenc
- VAR-wagenc2
- VAR-twagencothers
derives_to:
- VAR-lincnc
- VAR-laborincome
- VAR-twagetotal
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - total wage
  - wage all jobs
  - annual wage
  - total earnings
  typical_section_names:
  - Employment
  - Total earnings
  - Wages
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Employment Earnings, 7-day reference
    period, t_wage_nc_total
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Total employment earnings family, 7-day reference period. All jobs including primary, secondary
    and others. Total annualized wage income excluding tips/bonuses.
---
## Definition

`t_wage_nc_total` is a numeric/continuous variable recording the total annualized wage income in all jobs including primary, secondary and others, excluding tips, bonuses, and other payments. This is the total across all jobs.

## Conceptual intent

t_wage_nc_total aggregates the non-compensation annual wage across all jobs.

## Construction notes

Use gross wages when available and net only when gross is unavailable. Annualization depends on available data; see wage_total derivation formulae.

## Consistency checks

- t_wage_nc_total must be non-negative.
- Should equal wage_total + wage_total_2 + t_wage_nc_others where complete (net of compensation differences).

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
