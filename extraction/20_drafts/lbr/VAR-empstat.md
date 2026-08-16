---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-empstat
canonical_label: Employment status, primary job (7-day ref period)
variable_name: empstat
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
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
- VAR-wagenc
- VAR-wagetotal
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
  - main job
  - paid employee
  - self employed
  - employer
  - status in employment
  typical_section_names:
  - Employment
  - Primary job
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    empstat
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Definitions from ILO Classification of Status in
    Employment.
---
## Definition

`empstat` is a categorical variable recording the main employment status in the last 7 days of any individual with a job (LSTATUS=1). Five categories after harmonization: 1 = Paid Employee, 2 = Non-Paid Employee, 3 = Employer, 4 = Self-employed, 5 = Other workers not classifiable by status.

## Conceptual intent

empstat classifies the status in employment of the primary (main) job, using ILO definitions with revisions for data availability. It is required to distinguish paid employees, contributing family workers, employers, and the self-employed and is a key input for labor income construction.

## Construction notes

Construct for all individuals with a job (LSTATUS=1); missing otherwise. Paid employees are those whose remuneration does not depend on the revenue of the unit; contributing family workers and all apprentices map to non-paid employee; employers have employees; self-employed own-account workers hire no permanent employees.

## Consistency checks

- EMPSTAT must be an integer in [1,5].
- If EMPSTAT is defined, LSTATUS must be 1 (employed).
- If LSTATUS == 1, EMPSTAT must not be missing.

## Escalation triggers

- The survey's status categories cannot be mapped cleanly to the five harmonized codes.
- Cooperative members are treated as paid employees per module guidance.

## Common mistakes

- Classifying contributing family workers as self-employed.
- Classifying an own-account worker with no employees as employer.
- Leaving EMPSTAT missing for employed individuals.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
