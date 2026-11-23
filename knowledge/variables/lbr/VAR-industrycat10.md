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
  - MISS-OTHER-CATEGORY
derived_from: []
derives_to:
- VAR-industrycat4
correspondence_output:
- method: external_standard
  standard: "ISIC-4"
  level: industrycat10
  map: {
    "A": 1, "01": 1, "02": 1, "03": 1,
    "B": 2, "05": 2, "06": 2, "07": 2, "08": 2, "09": 2,
    "C": 3, "10": 3, "11": 3, "12": 3, "13": 3, "14": 3, "15": 3, "16": 3, "17": 3, "18": 3, "19": 3, "20": 3, "21": 3, "22": 3, "23": 3, "24": 3, "25": 3, "26": 3, "27": 3, "28": 3, "29": 3, "30": 3, "31": 3, "32": 3, "33": 3,
    "D": 4, "35": 4,
    "E": 4, "36": 4, "37": 4, "38": 4, "39": 4,
    "F": 5, "41": 5, "42": 5, "43": 5,
    "G": 6, "45": 6, "46": 6, "47": 6,
    "H": 7, "49": 7, "50": 7, "51": 7, "52": 7, "53": 7,
    "I": 6, "55": 6, "56": 6,
    "J": 7, "58": 7, "59": 7, "60": 7, "61": 7, "62": 7, "63": 7,
    "K": 8, "64": 8, "65": 8, "66": 8,
    "L": 8, "68": 8,
    "M": 8, "69": 8, "70": 8, "71": 8, "72": 8, "73": 8, "74": 8, "75": 8,
    "N": 8, "77": 8, "78": 8, "79": 8, "80": 8, "81": 8, "82": 8,
    "O": 9, "84": 9,
    "P": 10, "85": 10,
    "Q": 10, "86": 10, "87": 10, "88": 10,
    "R": 10, "90": 10, "91": 10, "92": 10, "93": 10,
    "S": 10, "94": 10, "95": 10, "96": 10,
    "T": 10, "97": 10, "98": 10,
    "U": 10, "99": 10
  }
- method: external_standard
  standard: "ISIC-3.1"
  level: industrycat10
  map: {
    "A": 1, "01": 1, "02": 1,
    "B": 1, "05": 1,
    "C": 2, "10": 2, "11": 2, "12": 2, "13": 2, "14": 2,
    "D": 3, "15": 3, "16": 3, "17": 3, "18": 3, "19": 3, "20": 3, "21": 3, "22": 3, "23": 3, "24": 3, "25": 3, "26": 3, "27": 3, "28": 3, "29": 3, "30": 3, "31": 3, "32": 3, "33": 3, "34": 3, "35": 3, "36": 3, "37": 3,
    "E": 4, "40": 4, "41": 4,
    "F": 5, "45": 5,
    "G": 6, "50": 6, "51": 6, "52": 6,
    "H": 6, "55": 6,
    "I": 7, "60": 7, "61": 7, "62": 7, "63": 7, "64": 7,
    "J": 8, "65": 8, "66": 8, "67": 8,
    "K": 8, "70": 8, "71": 8, "72": 8, "73": 8, "74": 8,
    "L": 9, "75": 9,
    "M": 10, "80": 10,
    "N": 10, "85": 10,
    "O": 10, "90": 10, "91": 10, "92": 10, "93": 10,
    "P": 10, "95": 10, "96": 10, "97": 10,
    "Q": 10, "99": 10
  }
country_parameters:
- PARAM-LBR-INDUSTRY-CROSSWALK
gates:
- variable_id: VAR-lstatus
  condition: VAR-lstatus == 1
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
  notes: >-
    Primary job family, 7-day reference period. Based on ISIC Rev. 3.1/4.0. Draft, proposed, pending
    GPID Team review: correspondence_output added. The placement of ISIC sections and divisions is
    taken from the GLD manual (worldbank/gld, Support/A - Guides and Documentation/GLD Manual
    Files/Labor.md, Table 5 'Overview of coding of industrycat based on different ISIC revisions'),
    which defines the same variable with the same ten categories; the GMD guideline text this record
    was extracted from names ISIC but does not write the placement out. To confirm: (1) accommodation
    and food service (Rev. 4 section I, divisions 55-56; Rev. 3.1 section H, division 55) is 6
    Commerce in that table, while a legacy ECA GMD file places divisions 55-56 in 10; (2) the table
    names division 95 for Rev. 3.1 section P, and divisions 96-97, which Rev. 3.1 has in the same
    section, are placed with it; (3) NACE Rev. 2 is taken to have the sections and divisions of ISIC
    Rev. 4, and NACE Rev. 1.1 those of ISIC Rev. 3.1; (4) ISIC Rev. 2, which the table also covers, is
    not drafted.
---
## Definition

`industrycat10` is a categorical variable recording the 1-digit industry classification in the last 7 days for the main job. Ten categories after harmonization, based on the UN International Standard Industrial Classification (ISIC) revision 3.1/4.0.

## Conceptual intent

industrycat10 provides a comparable 1-digit industry classification for the main job, enabling cross-country industry analysis.

## Construction notes

Can be recoded from INDUSTRY_ORIG. Carefully check the economic activity classification and its revision used by the survey (ISIC vs NACE). Category 10 is also used for unspecified categories. If all 10 categories cannot be identified, set this variable missing and create INDUSTRYCAT4 instead.

The placement of ISIC Rev. 4 and ISIC Rev. 3.1 sections and divisions in the ten categories is the `correspondence_output` recipe of this record, one anchor per revision: the codes in a survey are those of the revision it was coded in, and the same letter or number means different activities in different revisions. A group or class code (three or four digits) is placed by its division, the first two digits. A NACE Rev. 2 code is placed under the ISIC Rev. 4 anchor and a NACE Rev. 1.1 code under the ISIC Rev. 3.1 anchor, by its division. A country whose classification is neither ISIC nor NACE is placed through its `PARAM-LBR-INDUSTRY-CROSSWALK` rows.

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
| 2026-11-23 | 0.1 | Draft: add correspondence_output (ISIC Rev. 4 and Rev. 3.1 anchors), derives_to VAR-industrycat4 and PARAM-LBR-INDUSTRY-CROSSWALK | GPID Team (proposed) |
