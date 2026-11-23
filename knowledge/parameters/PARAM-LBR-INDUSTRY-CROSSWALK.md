---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.3
# ================================================================

parameter_id: PARAM-LBR-INDUSTRY-CROSSWALK
parameter_name: "Country industry classification crosswalk rows"
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
  - VAR-industrycat10
  - VAR-industrycat102
  - VAR-industrycat10year
  - VAR-industrycat102year
  - VAR-industrycat4
  - VAR-industrycat42
  - VAR-industrycat4year
  - VAR-industrycat42year

fallback_policy: use_global_default
global_default: []

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-11-23"
  human_reviewed: false
  reviewer: null
  notes: "Draft, proposed, pending GPID Team review. New parameter, not in the guideline text:
          the variable records name ISIC as the basis of the harmonized industry variables, so
          a national classification that differs has to be recoded to it, and this record gives
          that recoding a place in the country layer. Open points: the row fields (`standard` and `standard_code` are the same two fields in the
          industry and the occupation parameter), the `ISO3-<SEGMENT>-NN` segment of the entry ids,
          and whether an
          empty global default is the right way to say that most countries need no rows."
---

## Definition

Defines row-level country records that place the codes of a national industry classification on
ISIC codes. The GMD codes follow from the ISIC code through the `VAR-industrycat10`
anchors (`correspondence_output`).

## Parameter notes

- A country has rows only when its surveys code industry in a national classification that is not
  ISIC or NACE. A survey whose codes are already ISIC codes needs no rows:
  they are placed by the `VAR-industrycat10` anchors directly.
- Industry is usually coded in the statistical office from the respondent's description of the
  work, so the codes in the data are the classification's own codes. A row is keyed by
  `national_code`; nothing links a questionnaire answer category to a row.
- A record lists every code of the classification, so that a code in the data with no row is
  known to be outside it: the column does not hold this classification, or not this version of
  it, and the target is not produced until that is resolved.
- `national_classification` names the classification and its version. A country whose
  classification changed has one record per version, each with the validity window of the
  survey years that use it.
- `standard` names the anchor of `VAR-industrycat10` the row is placed under (`ISIC-4` or `ISIC-3.1`); the rows of
  one record may name different standards. `standard_code` is a code of that standard at the
  finest level the national code determines: a division (`47`) or, when the national code is coarser, a section (`G`).
- `national_label_local` is the classification's own label for the code. `national_label_en` is
  empty when the source gives none.
- A national code the source gives no ISIC code for, or one that spans several ISIC codes with
  different GMD codes and no coarser code in common, keeps its row with an empty `standard` and
  `standard_code`: its observations take `MISS-OTHER-CATEGORY`.

## Fallback behavior

`use_global_default` with an empty table: a country without rows has no national classification
to translate, and its surveys' codes are read as ISIC codes. A survey whose codes fit no
ISIC revision and whose country has no rows is escalated, not guessed.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-11-23 | 0.3 | Draft: new table parameter for national industry classifications | GPID Team (proposed) |
