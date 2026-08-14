---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-twageothers
canonical_label: Annualized wage in all but primary and secondary jobs incl. bonuses (7-day)
variable_name: t_wage_others
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
- VAR-twagencothers
derives_to:
- VAR-twagencotal
- VAR-lincnc
- VAR-twagetotal
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - other jobs
  - total wage other jobs
  - annual income
  typical_section_names:
  - Employment
  - Other employment
  - Wages
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Other Employment Earnings, 7-day reference
    period, t_wage_others
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Other employment earnings family, 7-day reference period. Excludes the main and secondary jobs.
    Annualized wage (including tips/bonuses) in all but primary and secondary jobs.
---
## Definition

`t_wage_others` is a numeric/continuous variable recording the annualized wage in all jobs excluding the primary and secondary ones. This wage includes tips, bonuses, dwellings/clothes, and other payments.

## Conceptual intent

t_wage_others captures total (including compensation) wage from all tertiary and additional jobs.

## Construction notes

t_wage_others should equal t_wage_nc_others when there are no bonuses/tips. Annualization depends on available data; see the wage_total derivation formulae.

## Consistency checks

- t_wage_others must be >= t_wage_nc_others
- Should equal t_wage_nc_others when no bonuses/tips exist.

## Escalation triggers

- Wage data for tertiary jobs are insufficient to annualize.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
