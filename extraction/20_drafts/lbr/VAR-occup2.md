---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-occup2
canonical_label: 1-digit occupation classification, secondary job (7-day ref period)
variable_name: occup_2
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
  label: Managers
- value: 2
  label: Professionals
- value: 3
  label: Technicians and associate professionals
- value: 4
  label: Clerical support workers
- value: 5
  label: Service and sales workers
- value: 6
  label: Skilled agricultural, forestry and fishery workers
- value: 7
  label: Craft and related trades workers
- value: 8
  label: Plant and machine operators, and assemblers
- value: 9
  label: Elementary occupations
- value: 10
  label: Armed forces occupations
- value: 99
  label: Other/unspecified
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
external_standards:
- name: ISCO-08 (International Standard Classification of Occupations)
  url: https://www.ilo.org/public/english/bureau/stat/isco/isco08/index.htm
source_hints:
  question_keywords:
  - occupation
  - second job occupation
  - 1 digit occupation
  typical_section_names:
  - Employment
  - Secondary job
  - Occupation
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    occup_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Based on ISCO-08.
---
## Definition

`occup_2` is a categorical variable recording the 1-digit occupation classification for the second job in the last 7 days. Eleven categories after harmonization, based on ISCO-08, identical to occup.

## Conceptual intent

occup_2 classifies the secondary job into the harmonized 1-digit occupation categories.

## Construction notes

Construct for all individuals with a job (LSTATUS=1); missing otherwise. Category 99 = Other/unspecified.

## Consistency checks

- occup_2 must be an integer in the harmonized set {1..10, 99} where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The secondary job's occupation cannot be mapped to ISCO-08 1-digit categories.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
