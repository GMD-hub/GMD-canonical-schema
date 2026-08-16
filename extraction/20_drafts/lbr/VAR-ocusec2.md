---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-ocusec2
canonical_label: Sector of activity, secondary job (7-day ref period)
variable_name: ocusec_2
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
  - second job sector
  - public
  - private
  - state owned
  typical_section_names:
  - Employment
  - Secondary job
  - Sector
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    ocusec_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period.
---
## Definition

`ocusec_2` is a categorical variable recording the sector of activity of the secondary job in the last 7 days. Four categories after harmonization, identical to ocusec.

## Conceptual intent

ocusec_2 classifies the sector of the secondary job.

## Construction notes

Construct for all individuals with a job (LSTATUS=1); missing otherwise. See ocusec definitions.

## Consistency checks

- ocusec_2 must be an integer in [1,4] where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The secondary job's sector cannot be distinguished as public vs state-owned.

## Common mistakes

- Using occupation (ISCO) or industry (ISIC) codes to infer sector.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
