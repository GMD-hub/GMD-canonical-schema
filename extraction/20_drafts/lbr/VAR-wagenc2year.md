---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagenc2year
canonical_label: Last wage payment, secondary job, excl. bonuses (12-month ref period)
variable_name: wage_nc_2_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
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
- VAR-wagetotal2year
- VAR-twagencototalyear
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
  - wage
  - second job wage
  - 12 months
  typical_section_names:
  - Labor
  - Secondary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 12-month reference
    period, wage_nc_2_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Secondary job family, 12-month reference period. Last wage payment in local
    currency, excluding bonuses.
---
## Definition

`wage_nc_2_year` is a numeric/continuous variable recording the last wage payment in local currency of any individual (LSTATUS_YEAR=1 & EMPSTAT_YEAR=1) in its secondary occupation. The wage comes from the secondary job over the 12-month reference period.

## Conceptual intent

wage_nc_2_year captures the regular wage of the 12-month secondary job.

## Construction notes

Use gross wages when available. Non-paid employees (EMPSTAT_YEAR=2) should have wage = 0. Reference period recorded in unitwage_2_year.

## Consistency checks

- wage_nc_2_year should be non-missing only where lstatus_year == 1 and empstat_2_year == 1.
- Non-paid secondary employees should have wage == 0.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
