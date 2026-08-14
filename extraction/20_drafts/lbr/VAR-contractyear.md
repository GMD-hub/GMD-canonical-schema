---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-contractyear
canonical_label: Contract (12-month ref period)
variable_name: contract_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
data_type: binary
value_codes:
- value: 0
  label: 'No'
- value: 1
  label: 'Yes'
allowed_range: null
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
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - contract
  - formal contract
  - 12 months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    contract_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Primary job family, 12-month reference period. Only constructed if there
    is an explicit contract question.
---
## Definition

`contract_year` is a categorical variable recording the contract status (YES/NO) of any individual with a job (LSTATUS_YEAR=1). Two categories after harmonization: 0 = No, 1 = Yes.

## Conceptual intent

contract_year is a formality proxy for the 12-month primary job.

## Construction notes

Only constructed if there is an explicit contract question. Missing otherwise.

## Consistency checks

- contract_year must be in {0,1} where non-missing.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
