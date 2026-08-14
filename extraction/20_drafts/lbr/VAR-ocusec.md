---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-ocusec
canonical_label: Sector of activity, primary job (7-day ref period)
variable_name: ocusec
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
  label: Public sector, Central Government, Army (including armed forces)
- value: 2
  label: Private, NGO
- value: 3
  label: State-owned
- value: 4
  label: Public or State-owned, but cannot distinguish
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
  - sector
  - public sector
  - private
  - state owned
  - government
  - employer type
  typical_section_names:
  - Employment
  - Primary job
  - Sector
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    ocusec
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period.
---
## Definition

`ocusec` is a categorical variable recording the sector of activity of the main job in the last 7 days. Four categories after harmonization: 1 = Public sector/Central Government/Army, 2 = Private/NGO, 3 = State-owned, 4 = Public or State-owned but cannot distinguish.

## Conceptual intent

ocusec classifies whether the main job is in the public sector, the private sector (including NGOs), or a state-owned enterprise, providing a proxy for formality and a key labor-market descriptor.

## Construction notes

Public sector is the part of the economy run by government. Private/NGO covers private-for-profit activity and non-governmental organizations. State-owned includes para-state firms and firms in which government control exceeds 50%. Choose category 4 when the questionnaire does not ask about state-owned enterprises separately.

## Consistency checks

- ocusec must be an integer in [1,4] where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The questionnaire combines categories in a way that cannot be mapped to the four harmonized codes.
- The survey conflates public and state-owned without a distinguishing question.

## Common mistakes

- Coding a state-owned enterprise as private because it is a firm.
- Using occupation (ISCO) or industry (ISIC) codes to infer sector (not permitted).

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
