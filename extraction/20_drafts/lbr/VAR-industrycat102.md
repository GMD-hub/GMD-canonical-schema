---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat102
canonical_label: 1-digit industry classification, secondary job (7-day ref period)
variable_name: industrycat10_2
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
  label: Agriculture, Hunting, Fishing, etc.
- value: 2
  label: Mining
- value: 3
  label: Manufacturing
- value: 4
  label: Public Utility Services
- value: 5
  label: Construction
- value: 6
  label: Commerce
- value: 7
  label: Transport and Communications
- value: 8
  label: Financial and Business Services
- value: 9
  label: Public Administration
- value: 10
  label: Other Services, Unspecified
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
- name: ISIC Rev. 3.1/4.0 (International Standard Industrial Classification)
  url: https://unstats.un.org/unsd/classifications/Econ/ISIC
source_hints:
  question_keywords:
  - industry
  - second job industry
  - 1 digit industry
  typical_section_names:
  - Employment
  - Secondary job
  - Industry
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    industrycat10_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Based on ISIC Rev. 3.1/4.0.
---
## Definition

`industrycat10_2` is a categorical variable recording the 1-digit industry classification for the second job with reference period of the last 7 days. Ten categories after harmonization, based on the UN ISIC. Category 10 = Other Services, Unspecified.

## Conceptual intent

industrycat10_2 provides a comparable 1-digit industry classification for the secondary job.

## Construction notes

Can be recoded from industry_orig_2. If all 10 categories cannot be identified, set missing and create industrycat4_2.

## Consistency checks

- industrycat10_2 must be an integer in [1,10] where non-missing.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The secondary job's classification cannot be mapped to the 10 ISIC categories.

## Common mistakes

- Mapping unspecified secondary-job categories to a specific code instead of 10.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
