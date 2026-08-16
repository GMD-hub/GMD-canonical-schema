---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat4
canonical_label: 4-category industry classification, primary job (7-day ref period)
variable_name: industrycat4
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
  label: Agriculture
- value: 2
  label: Industry
- value: 3
  label: Services
- value: 4
  label: Other
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
  - industry
  - economic activity
  - broad economic activity
  - agriculture industry services
  typical_section_names:
  - Employment
  - Primary job
  - Industry
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    industrycat4
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Broad Economic Activities.
---
## Definition

`industrycat4` is a categorical variable recording the 1-digit industry classification for Broad Economic Activities for the main job in the last 7 days. Four categories after harmonization: 1 = Agriculture, 2 = Industry, 3 = Services, 4 = Other.

## Conceptual intent

industrycat4 aggregates industry into four broad economic activities, used when the 10-category classification is not available and as a coarser harmonized industry indicator.

## Construction notes

Either created directly from the data (if a 10-category industry classification does not exist) or created from INDUSTRYCAT10.

## Consistency checks

- INDUSTRYCAT4 must be an integer in [1,4].
- There must be no mismatch between industrycat4 and industrycat10 (e.g. industrycat4==1 requires industrycat10==1).

## Escalation triggers

- The mapping between the survey classification and the four broad categories is unclear.

## Common mistakes

- Aggregation errors between industrycat4 and industrycat10.
- Creating industrycat4 when only industrycat10 is available without recoding.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
