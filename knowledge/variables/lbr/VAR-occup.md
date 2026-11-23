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
  - MISS-OTHER-CATEGORY
derived_from: []
derives_to: []
correspondence_output:
- method: external_standard
  standard: "ISCO-08"
  level: occup
  map: {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 10, "01": 10, "02": 10, "03": 10, "11": 1, "12": 1, "13": 1, "14": 1, "21": 2, "22": 2, "23": 2, "24": 2, "25": 2, "26": 2, "31": 3, "32": 3, "33": 3, "34": 3, "35": 3, "41": 4, "42": 4, "43": 4, "44": 4, "51": 5, "52": 5, "53": 5, "54": 5, "61": 6, "62": 6, "63": 6, "71": 7, "72": 7, "73": 7, "74": 7, "75": 7, "81": 8, "82": 8, "83": 8, "91": 9, "92": 9, "93": 9, "94": 9, "95": 9, "96": 9}
- method: external_standard
  standard: "ISCO-88"
  level: occup
  map: {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 10, "01": 10, "11": 1, "12": 1, "13": 1, "21": 2, "22": 2, "23": 2, "24": 2, "31": 3, "32": 3, "33": 3, "34": 3, "41": 4, "42": 4, "51": 5, "52": 5, "61": 6, "62": 6, "71": 7, "72": 7, "73": 7, "74": 7, "81": 8, "82": 8, "83": 8, "91": 9, "92": 9, "93": 9}
country_parameters:
- PARAM-LBR-OCCUPATION-CROSSWALK
gates:
- variable_id: VAR-lstatus
  condition: VAR-lstatus == 1
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
  notes: >-
    Primary job family, 7-day reference period. Based on ISCO-08. Draft, proposed, pending GPID Team
    review: correspondence_output added. ISCO-08 major groups 1-9 carry the labels of codes 1-9 and
    major group 0 (Armed forces occupations) the label of code 10, so each major group is placed on
    the code of the same label; no source read states the placement in words. To confirm: the ISCO-88
    anchor places major groups digit for digit, as for ISCO-08, although the two versions assign some
    occupations to different major groups, so occup built from ISCO-88 codes is not strictly
    comparable with occup built from ISCO-08 codes. Code 99 has no ISCO major group. The sub-major groups of each anchor are the leading two digits of the
    unit groups in the ILO correspondence table ISCO-88 to ISCO-08 (corrtab88-08).
---
## Definition

`occup` is a categorical variable recording the 1-digit occupation classification for the main job in the last 7 days. Eleven categories after harmonization, based on ISCO-08: 1 = Managers through 10 = Armed forces occupations, 99 = Other/unspecified.

## Conceptual intent

occup provides a comparable 1-digit occupation classification for the main job, supporting analysis of occupational structure and matching SDG earnings indicators by occupation.

## Construction notes

Most surveys collect detailed information and code it directly; no attempt is made to correct or check the original coding. Category 99 is used for other/unspecified occupations.

The placement of ISCO major groups is the `correspondence_output` recipe of this record, one anchor per ISCO version. Each anchor holds the version's major groups (one digit) and its sub-major groups (two digits), every sub-major group on the code of its major group. A column of longer ISCO codes (a minor group, a unit group) is placed by its sub-major group, so a column whose leading two digits are not sub-major groups of the version is recognized as not holding that version's codes; a code that ends in zeros after its major group (`2000`: a professional, not further specified) is placed by the major group. A column of one-digit codes is placed by the major groups. A country that codes occupation in its own classification is placed from its `PARAM-LBR-OCCUPATION-CROSSWALK` record for the survey year.

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
| 2026-11-23 | 0.1 | Draft: add correspondence_output (ISCO-08 and ISCO-88 anchors) and PARAM-LBR-OCCUPATION-CROSSWALK | GPID Team (proposed) |
