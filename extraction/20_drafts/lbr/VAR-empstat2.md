---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-empstat2
canonical_label: Employment status, secondary job (7-day ref period)
variable_name: empstat_2
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
unit_of_analysis: individual
mapping_role: atomic
data_type: categorical
value_codes:
- value: 1
  label: Paid Employee
- value: 2
  label: Non-Paid Employee
- value: 3
  label: Employer
- value: 4
  label: Self-employed
- value: 5
  label: Other, workers not classifiable by status
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
- VAR-wagenc2
- VAR-wagetotal2
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - employment status
  - second job
  - secondary job
  - status in employment
  typical_section_names:
  - Employment
  - Secondary job
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    empstat_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Definitions from ILO Classification of Status in
    Employment; see primary empstat.
---
## Definition

`empstat_2` is a categorical variable recording the employment status of the secondary job with reference period of the last 7 days. Five categories after harmonization, identical to empstat: 1 = Paid Employee through 5 = Other workers not classifiable by status.

## Conceptual intent

empstat_2 classifies the status in employment of the secondary job, using the same definitions as the primary job.

## Construction notes

Construct for all individuals with a job (LSTATUS=1); missing otherwise. See empstat definitions.

## Consistency checks

- empstat_2 must be an integer in [1,5] where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The secondary job's status cannot be mapped to the five harmonized codes.

## Common mistakes

- Confusing the secondary job with the primary job.
- Leaving empstat_2 missing for individuals with a secondary job.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
