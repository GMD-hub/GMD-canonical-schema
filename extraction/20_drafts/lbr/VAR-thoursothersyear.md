---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-thoursothersyear
canonical_label: Total hours of work in the last 12 months in other jobs excl. primary and secondary
variable_name: t_hours_others_year
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
- VAR-thourstotalyear
- VAR-thoursannual
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - hours
  - other jobs
  - 12 months
  typical_section_names:
  - Labor
  - Other employment
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Other Employment, 12-month reference period,
    t_hours_others_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Other employment earnings family, 12-month reference period. Excludes primary
    and secondary jobs. Hours of work in all jobs excluding the primary and secondary ones.
---
## Definition

`t_hours_others_year` is a numeric/continuous variable recording the hours of work in the last 12 months in all jobs excluding the primary and secondary ones. Refers to all other employment earnings excluding the main and secondary jobs.

## Conceptual intent

t_hours_others_year captures hours from tertiary and additional jobs over 12 months.

## Construction notes

Annualized hours worked in all jobs other than the primary and secondary ones.

## Consistency checks

- t_hours_others_year must be non-negative.
- Cross-check against the sum of primary and secondary hours.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
