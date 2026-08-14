---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-thoursothers
canonical_label: Total hours of work in the last 7 days in other jobs excl. primary and secondary
variable_name: t_hours_others
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
- VAR-thourstotal
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
  - total hours
  - additional jobs
  typical_section_names:
  - Employment
  - Other employment
  - Hours
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Other Employment Earnings, 7-day reference
    period, t_hours_others
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Other employment earnings family, 7-day reference period. Excludes the main and secondary jobs.
    Annualized hours worked in all but the primary and secondary jobs.
---
## Definition

`t_hours_others` is a numeric/continuous variable recording the hours of work in the last 12 months in all jobs excluding the primary and secondary ones. Refers to all other employment earnings excluding the main and secondary jobs.

## Conceptual intent

t_hours_others captures hours from any tertiary and additional jobs so that total labor income is not understated.

## Construction notes

Annualized hours worked in all jobs other than the primary and secondary ones.

## Consistency checks

- t_hours_others must be non-negative.
- Should be consistent with the jobs not captured by the primary/secondary hours.

## Escalation triggers

- Hours for tertiary jobs are not collected in the survey.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
