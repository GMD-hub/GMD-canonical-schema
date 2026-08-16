---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-nlfreason
canonical_label: Reason not in the labor force (7-day ref period)
variable_name: nlfreason
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
  label: Student
- value: 2
  label: Housewife
- value: 3
  label: Retired
- value: 4
  label: Disabled
- value: 5
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
  condition: lstatus == 3
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - reason not in labor force
  - not working
  - not looking for work
  - student
  - housewife
  - retired
  - disabled
  typical_section_names:
  - Labor status
  - Not in labor force
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 7-day reference period, nlfreason
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Labor status family, 7-day reference period.
---
## Definition

`nlfreason` is a categorical variable recording the reason an individual was not in the labor force in the last 7 days. This variable is constructed for all those who are not presently employed and are not looking for work (LSTATUS=3) and is missing otherwise.

## Conceptual intent

nlfreason characterizes inactivity by its main reason, distinguishing students, homemakers, the retired, the disabled, and other inactive individuals. It is only defined for those not in the labor force.

## Construction notes

Five categories after harmonization: 1 = Student, 2 = Housewife, 3 = Retired, 4 = Disabled, 5 = Other. Construct only where LSTATUS=3; set missing for employed or unemployed individuals.

## Consistency checks

- nlfreason should only be non-missing where lstatus == 3.
- nlfreason must be an integer in [1,5] where non-missing.

## Escalation triggers

- A respondent reports an inactivity reason not covered by the five harmonized categories.
- lstatus is missing but nlfreason is present.

## Common mistakes

- Assigning nlfreason to unemployed or employed individuals.
- Mapping multiple raw inactivity reasons to a single code without documentation.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
