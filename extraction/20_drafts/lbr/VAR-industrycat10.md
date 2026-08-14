---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat10
canonical_label: 1-digit industry classification, primary job (7-day ref period)
variable_name: industrycat10
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
  - economic activity
  - 1 digit industry
  - sector
  typical_section_names:
  - Employment
  - Primary job
  - Industry
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    industrycat10
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Based on ISIC Rev. 3.1/4.0.
---
## Definition

`industrycat10` is a categorical variable recording the 1-digit industry classification in the last 7 days for the main job. Ten categories after harmonization, based on the UN International Standard Industrial Classification (ISIC) revision 3.1/4.0.

## Conceptual intent

industrycat10 provides a comparable 1-digit industry classification for the main job, enabling cross-country industry analysis.

## Construction notes

Can be recoded from INDUSTRY_ORIG. Carefully check the economic activity classification and its revision used by the survey (ISIC vs NACE). Category 10 is also used for unspecified categories. If all 10 categories cannot be identified, set this variable missing and create INDUSTRYCAT4 instead.

## Consistency checks

- INDUSTRYCAT10 must be an integer in [1,10].
- INDUSTRYCAT4 must not conflict with the 10-category classification (see chapter mismatch check).

## Escalation triggers

- The survey classification cannot be mapped to the 10 ISIC-based categories.
- The revision used by the survey is ambiguous.

## Common mistakes

- Mapping an unspecified category to something other than 10.
- Creating industrycat10 when fewer than 10 categories can be reliably identified.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
