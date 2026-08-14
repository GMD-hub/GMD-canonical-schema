---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-njobs
canonical_label: Total number of jobs
variable_name: njobs
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
  max: 100
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to:
- VAR-thoursannual
- VAR-lincnc
- VAR-laborincome
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - number of jobs
  - total jobs
  - multiple jobs
  - how many jobs
  typical_section_names:
  - Labor
  - Total labor income
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Total Labor Income, njobs
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Cross-period variable. Total labor income is created based on either the 7-day or 12-month reference-period
    variables or a combination of both; harmonizers must ensure all jobs are included and none are double
    counted.
---
## Definition

`njobs` is a numeric/continuous variable recording the total number of jobs. Do not put missing values for people below working age, the unemployed, or people out of the labor force.

## Conceptual intent

njobs counts the total number of jobs held, supporting the study of multiple-job-holding.

## Construction notes

Count all jobs. Do not code missing for those below working age, unemployed, or out of the labor force.

## Consistency checks

- njobs must be a non-negative integer.
- Unemployed and out-of-labor-force individuals may have njobs == 0.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
