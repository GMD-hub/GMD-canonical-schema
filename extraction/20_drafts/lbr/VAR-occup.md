---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-occup
canonical_label: 1-digit occupation classification, primary job (7-day ref period)
variable_name: occup
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
  - 1 digit occupation
  - managers
  - professionals
  - occupation classification
  typical_section_names:
  - Employment
  - Primary job
  - Occupation
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    occup
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Based on ISCO-08.
---
## Definition

`occup` is a categorical variable recording the 1-digit occupation classification for the main job in the last 7 days. Eleven categories after harmonization, based on ISCO-08: 1 = Managers through 10 = Armed forces occupations, 99 = Other/unspecified.

## Conceptual intent

occup provides a comparable 1-digit occupation classification for the main job, supporting analysis of occupational structure and matching SDG earnings indicators by occupation.

## Construction notes

Most surveys collect detailed information and code it directly; no attempt is made to correct or check the original coding. Category 99 is used for other/unspecified occupations.

## Consistency checks

- OCCUP must be an integer in the harmonized set {1..10, 99} where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The survey's occupation coding cannot be mapped to the ISCO-08 1-digit categories.

## Common mistakes

- Mapping unspecified occupations to a specific category instead of 99.
- Leaving occup missing for employed individuals.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
