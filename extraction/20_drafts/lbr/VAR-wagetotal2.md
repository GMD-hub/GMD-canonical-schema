---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagetotal2
canonical_label: Annualized total wage, secondary job (7-day ref period)
variable_name: wage_total_2
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
- VAR-wagenc2
- VAR-unitwage2
- VAR-wmonths2
- VAR-whours2
derives_to:
- VAR-twageothers
- VAR-twagencotal
- VAR-twagetotal
- VAR-lincnc
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
- variable_id: VAR-empstat2
  condition: empstat_2 == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - annualized wage
  - secondary wage total
  - total wage second job
  typical_section_names:
  - Employment
  - Secondary job
  - Wages
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    wage_total_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 'Secondary job family, 7-day reference period. Derived: annualized wage including bonuses, in-kind
    and other compensation.'
---
## Definition

`wage_total_2` is a numeric/continuous variable recording the annualized wage payment (regular wage plus bonuses, in-kind, compensation, etc.) in local currency of any individual (LSTATUS=1 & EMPSTAT=1) in its secondary occupation. The wage comes from the secondary job and includes tips and other compensation.

## Conceptual intent

wage_total_2 annualizes total wage of the secondary job over months actually worked.

## Construction notes

Derived from wage_nc_2, unitwage_2, whours_2, and wmonths_2 using the wage_total formula. wage_total_2 equals wage_nc_2 when there are no bonuses/tips. Do not assume full-year work.

## Consistency checks

- wage_total_2 must be >= 0.
- Only non-missing for lstatus == 1 and empstat_2 == 1.

## Escalation triggers

- Secondary-job wage components are incomplete for annualization.

## Common mistakes

- Assuming full-year work for the secondary job.
- Applying the wrong unitwage conversion.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
