---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-minlaborageyear
canonical_label: Labor module application age (12-month ref period)
variable_name: minlaborage_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric_continuous
value_codes: null
allowed_range:
  min: 0
  max: 120
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to: []
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - minimum working age
  - labor module age
  - 12 months
  typical_section_names:
  - Labor
  - Labor status
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 12-month reference period,
    minlaborage_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period.
---
## Definition

`minlaborage_year` is a numeric/continuous variable recording the lowest age for which the labor module is implemented in the survey in the 12-month reference period. The lower age cutoff varies from country to country.

## Conceptual intent

minlaborage_year defines the population to which the 12-month labor module applies.

## Construction notes

Record the country-specific minimum working age for the 12-month module.

## Consistency checks

- MINLABORAGE_YEAR must be an integer and should not be higher than 20.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
