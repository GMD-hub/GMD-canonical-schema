---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-lincnc
canonical_label: Total annual wage income in all jobs, excl. bonuses
variable_name: linc_nc
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
- VAR-twageothers
- VAR-twagetotal
- VAR-twagencotal
- VAR-twageothersyear
- VAR-twagetotalyear
- VAR-twagencototalyear
derives_to:
- VAR-laborincome
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - labor income
  - annual wage income
  - total wage income
  typical_section_names:
  - Labor
  - Total labor income
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Labor Income, linc_nc
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Cross-period variable. Total labor income is created based on either the 7-day or 12-month reference-period
    variables or a combination of both; harmonizers must ensure all jobs are included and none are double
    counted. Total annualized wage income excluding tips/bonuses.
---
## Definition

`linc_nc` is a numeric/continuous variable recording the total annualized wage income in all jobs including primary, secondary and others, regardless of their reference period, excluding tips, bonuses, and other payments. Aggregates wage income across jobs with different reference periods.

## Conceptual intent

linc_nc is the total annual non-compensation labor income, the basis for constructing laborincome.

## Construction notes

Use gross wages when available. Annualization depends on available data; see wage_total formulae.

## Consistency checks

- linc_nc must be non-negative.
- Should be consistent with t_wage_nc_total and t_wage_nc_total_year without double counting.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
