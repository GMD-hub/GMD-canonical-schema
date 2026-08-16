---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-laborincome
canonical_label: Total annual individual labor income in all jobs, incl. bonuses
variable_name: laborincome
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
- VAR-lincnc
- VAR-wagetotal
- VAR-wagetotal2
- VAR-twagencotal
- VAR-twagetotal
- VAR-wagetotalyear
- VAR-wagetotal2year
- VAR-twagencototalyear
- VAR-twagetotalyear
derives_to: []
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - labor income
  - total labor income
  - annual labor income
  - income from work
  typical_section_names:
  - Labor
  - Total labor income
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Labor Income, laborincome
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Cross-period variable. Total labor income is created based on either the 7-day or 12-month reference-period
    variables or a combination of both; harmonizers must ensure all jobs are included and none are double
    counted. Total annualized individual labor income including tips and bonuses.
---
## Definition

`laborincome` is a numeric/continuous variable recording the total annualized individual labor income in all jobs including primary, secondary and others, regardless of their reference period, including tips, bonuses, and other payments. This variable should be used as the total annual labor income of an individual.

## Conceptual intent

laborincome is the umbrella total labor-income variable used in poverty and welfare analysis.

## Construction notes

Derived from the total (including compensation) wage aggregates across all jobs and reference periods. Ensure all jobs are included and none double counted.

## Consistency checks

- laborincome must be >= linc_nc.
- Should equal the compensation-inclusive total of all annualized job wages.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
