---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat42
canonical_label: 4-category industry classification, secondary job (7-day ref period)
variable_name: industrycat4_2
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
  - second job
  - broad economic activity
  typical_section_names:
  - Employment
  - Secondary job
  - Industry
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    industrycat4_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Broad Economic Activities.
---
## Definition

`industrycat4_2` is a categorical variable recording the 1-digit industry classification for Broad Economic Activities for the second job in the last 7 days. Four categories after harmonization: 1 = Agriculture, 2 = Industry, 3 = Services, 4 = Other.

## Conceptual intent

industrycat4_2 aggregates secondary-job industry into four broad categories.

## Construction notes

Either created directly from the data or created from industrycat10_2.

## Consistency checks

- industrycat4_2 must be an integer in [1,4] where non-missing.
- Must not conflict with industrycat10_2.

## Escalation triggers

- Aggregation between industrycat4_2 and industrycat10_2 mismatches.

## Common mistakes

- Aggregating industrycat10_2 into industrycat4_2 incorrectly.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
