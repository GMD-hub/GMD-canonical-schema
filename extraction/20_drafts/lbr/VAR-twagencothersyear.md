---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-twagencothersyear
canonical_label: Annualized wage in all but primary and secondary jobs excl. bonuses (12-month)
variable_name: t_wage_nc_others_year
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
derived_from: []
derives_to:
- VAR-twagencototalyear
- VAR-lincnc
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - other jobs
  - 12 months
  typical_section_names:
  - Labor
  - Other employment
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Other Employment, 12-month reference period,
    t_wage_nc_others_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Other employment earnings family, 12-month reference period. Excludes primary
    and secondary jobs. Annualized wage (excluding tips/bonuses) in all but primary and secondary jobs.
---
## Definition

`t_wage_nc_others_year` is a numeric/continuous variable recording the annual wage in all jobs excluding the primary and secondary ones, excluding tips, bonuses, and other payments. Refers to all other employment earnings excluding the main and secondary jobs.

## Conceptual intent

t_wage_nc_others_year captures the non-compensation wage from all tertiary jobs over 12 months.

## Construction notes

Use gross wages when available. Annualization depends on available data; see wage_total derivation formulae.

## Consistency checks

- t_wage_nc_others_year must be non-negative.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
