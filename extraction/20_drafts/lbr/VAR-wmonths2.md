---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wmonths2
canonical_label: Months worked in the last 12 months, secondary job (7-day ref period)
variable_name: wmonths_2
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
  max: 12
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to:
- VAR-wagetotal2
- VAR-lincnc
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - months worked
  - second job months
  - months per year secondary
  typical_section_names:
  - Employment
  - Secondary job
  - Months
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    wmonths_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Months worked in the last 12 months for the secondary
    job.
---
## Definition

`wmonths_2` is a numeric/continuous variable recording the number of months worked in the last 12 months for the secondary job of any individual with a job (LSTATUS=1). The secondary job is the occupation in which the person dedicated less time than the primary job over the past week.

## Conceptual intent

wmonths_2 captures months of work in the secondary job over the past year for annualization.

## Construction notes

Record the number of months; do not assume full-year work.

## Consistency checks

- wmonths_2 must lie in [0,12].
- Should be non-missing only where lstatus == 1.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
