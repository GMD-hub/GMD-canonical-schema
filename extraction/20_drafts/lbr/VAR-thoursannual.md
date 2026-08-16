---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-thoursannual
canonical_label: Total hours worked in all jobs in the previous 12 months
variable_name: t_hours_annual
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
- VAR-whours
- VAR-whours2
- VAR-thoursothers
- VAR-thourstotal
- VAR-whoursyear
- VAR-whours2year
- VAR-thoursothersyear
- VAR-thourstotalyear
derives_to:
- VAR-lincnc
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - total hours
  - annual hours
  - hours all jobs
  typical_section_names:
  - Labor
  - Total labor income
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Labor Income, t_hours_annual
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Cross-period variable. Total labor income is created based on either the 7-day or 12-month reference-period
    variables or a combination of both; harmonizers must ensure all jobs are included and none are double
    counted.
---
## Definition

`t_hours_annual` is a numeric/continuous variable recording the annual number of hours worked in all jobs including primary, secondary and others, regardless of their reference period. Aggregates hours across jobs with different reference periods.

## Conceptual intent

t_hours_annual provides a single annual-hours measure across all jobs for the individual.

## Construction notes

Aggregate annual hours from all jobs regardless of whether they were reported on a 7-day or 12-month basis.

## Consistency checks

- t_hours_annual must be non-negative.
- Should reflect all jobs without double counting.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
