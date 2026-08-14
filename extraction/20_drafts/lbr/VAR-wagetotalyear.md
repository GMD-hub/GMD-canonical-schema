---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagetotalyear
canonical_label: Annualized total wage, primary job (12-month ref period)
variable_name: wage_total_year
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
- VAR-unitwageyear
- VAR-wmonthsyear
- VAR-whoursyear
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
- variable_id: VAR-empstatyear
  condition: empstat_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - annualized wage
  - total wage
  - 12 months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    wage_total_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: '12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Primary job family, 12-month reference period. Derived: annualized wage
    including bonuses, in-kind and other compensation.'
---
## Definition

`wage_total_year` is a numeric/continuous variable recording the annualized wage payment (regular wage plus bonuses, in-kind, compensation) for the primary occupation in local currency. The wage comes from the main job and includes tips, bonuses, in-kind, and other payments.

## Conceptual intent

wage_total_year annualizes total wage of the 12-month primary job over months actually worked.

## Construction notes

Derived from wage_nc_year, unitwage_year, whours_year, and wmonths_year using the wage_total formula. Do not assume full-year work. Use gross wages when available.

## Consistency checks

- wage_total_year must be >= 0.
- Only non-missing for lstatus_year == 1 and empstat_year == 1.

## Escalation triggers

- Wage components are incomplete for annualization.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
