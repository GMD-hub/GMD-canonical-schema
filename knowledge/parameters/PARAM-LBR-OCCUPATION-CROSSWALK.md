---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.3
# ================================================================

parameter_id: PARAM-LBR-OCCUPATION-CROSSWALK
parameter_name: "Country occupation classification crosswalk rows"
module_id: MOD-LBR
schema_version: "0.3"
status: draft
authority: "GPID Team"

kind: construction
value_type: table
value_schema: null
row_schema:
  country_entry_id: string
  national_classification: string
  national_code: string
  national_label_en: string
  national_label_local: string
  standard: string
  standard_code: string
  source_row: integer
  review_flags: array_of_string

applies_to_variables:
  - VAR-occup
  - VAR-occup2
  - VAR-occupyear
  - VAR-occup2year

fallback_policy: use_global_default
global_default: []

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-11-23"
  human_reviewed: false
  reviewer: null
  notes: "Draft, proposed, pending GPID Team review. New parameter, not in the guideline text:
          the variable records name ISCO as the basis of the harmonized occupation variables, so
          a national classification that differs has to be recoded to it, and this record gives
          that recoding a place in the country layer. Open points: the row fields (`standard` and `standard_code` are the same two fields in the
          industry and the occupation parameter), the `ISO3-<SEGMENT>-NN` segment of the entry ids,
          and whether an
          empty global default is the right way to say that most countries need no rows."
---

## Definition

Defines row-level country records that place the codes of a national occupation classification on
ISCO codes. The GMD codes follow from the ISCO code through the `VAR-occup`
anchors (`correspondence_output`).

## Parameter notes

- A country has rows only when its surveys code occupation in a national classification that is not
  ISCO. A survey whose codes are already ISCO codes needs no rows:
  they are placed by the `VAR-occup` anchors directly.
- Occupation is usually coded in the statistical office from the respondent's description of the
  work, so the codes in the data are the classification's own codes. A row is keyed by
  `national_code`; nothing links a questionnaire answer category to a row.
- A record lists every code of the classification, so that a code in the data with no row is
  known to be outside it: the column does not hold this classification, or not this version of
  it, and the target is not produced until that is resolved.
- `national_classification` names the classification and its version. A country whose
  classification changed has one record per version, each with the validity window of the
  survey years that use it.
- `standard` names the anchor of `VAR-occup` the row is placed under (`ISCO-08` or `ISCO-88`); the rows of
  one record may name different standards. `standard_code` is a code of that standard at the
  finest level the national code determines: a major group (`2`) or a finer group (`2330`).
- `national_label_local` is the classification's own label for the code. `national_label_en` is
  empty when the source gives none.
- A national code the source gives no ISCO code for, or one that spans several ISCO codes with
  different GMD codes and no coarser code in common, keeps its row with an empty `standard` and
  `standard_code`: its observations take `MISS-OTHER-CATEGORY`.

## Fallback behavior

`use_global_default` with an empty table: a country without rows has no national classification
to translate, and its surveys' codes are read as ISCO codes. A survey whose codes fit no
ISCO revision and whose country has no rows is escalated, not guessed.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-11-23 | 0.3 | Draft: new table parameter for national occupation classifications | GPID Team (proposed) |
