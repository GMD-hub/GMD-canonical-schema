---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-socialsec
canonical_label: Social security (7-day ref period)
variable_name: socialsec
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
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - social security
  - pension
  - pension plan
  - social protection
  typical_section_names:
  - Employment
  - Primary job
  - Formality
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    socialsec
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Only constructed if there is an explicit social-security/pension
    question.
---
## Definition

`socialsec` is a categorical variable recording the social security status (YES/NO) of any individual with a job (LSTATUS=1). Two categories after harmonization: 0 = No, 1 = Yes.

## Conceptual intent

socialsec is a proxy for job formality, indicating whether the job provides pension plans or social security.

## Construction notes

This variable is only constructed if there is an explicit question about pension plans or social security. Missing otherwise.

## Consistency checks

- socialsec must be in {0,1} where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The survey conflates social security contributions with other payments.

## Common mistakes

- Inferring social security from contract or other proxies.
- Constructing socialsec without an explicit question.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
