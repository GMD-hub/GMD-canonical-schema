---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.4
# ================================================================

parameter_id: PARAM-GEO-GMD-CROSSWALK
parameter_name: "Country geography crosswalk rows"
module_id: MOD-GEO
schema_version: "0.4"
status: draft
authority: "GPID Team"

kind: construction
value_type: table
value_schema: null
row_schema:
  country_entry_id: string
  survey_labels: string
  survey_variables: string
  gmd_subnatid1: string
  gmd_subnatid2: string
  gmd_subnatid3: string
  gmd_subnatid4: string
  is_rep_subnat1: boolean
  is_rep_subnat2: boolean
  is_rep_subnat3: boolean
  is_rep_subnat4: boolean
  representative_level: integer
  gmd_subnatidsurvey: string
  geo_year: string
  geo_source: string
  geo_level: string
  geo_idvar: string
  geo_id: string
  geo_nvar: string
  geo_name: string
  source_row: integer

applies_to_variables:
  - VAR-geocode
  - VAR-subnatid1prev
  - VAR-subnatid2prev
  - VAR-subnatid3prev
  - VAR-subnatid4prev
  - VAR-gauladm1code
  - VAR-gauladm2code

fallback_policy: block_and_escalate
global_default: null

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  extraction_method: manual
  extracted_on: "2026-09-18"
  human_reviewed: false
  reviewer: null
  notes: "v0.4 adds VAR-subnatid1prev through VAR-subnatid4prev and
          VAR-gauladm1code/VAR-gauladm2code to applies_to_variables (every
          GEO-family variable except VAR-psu and VAR-strata, which are
          sampling-design variables unrelated to geography resolution).
          subnatidN_prev is resolved from the prior effective-dated period
          of the same crosswalk when a country has 2+ PARAM-GEO-GMD-CROSSWALK
          records (documented boundary change) — verified 23 of 183
          countries have 2-3 periods. gaul_adm1_code/gaul_adm2_code reuse the
          matched row's geo_id directly when geo_source=GAUL, instead of a
          separate GAUL database lookup — verified against committed data
          (geo_idvar values ADM1_CODE/ADM2_CODE/gaul1_code/gaul2_code)."
---

## Definition

Defines row-level country geography crosswalk records that map survey labels
and source geography fields to GMD subnational identifiers and the survey-level
geography anchor.

## Parameter notes

- This parameter is row-based (`value_type: table`) because country source
  workbooks carry row-level crosswalk metadata.
- `survey_variables` stores one or more survey variables (`subnatid`,
  `subnatid1`, `subnatid2`, etc.) when rows are merged by geo identity.
- `survey_labels` stores one or more source label variants for the same
  geography identity.
- `gmd_subnatid1` to `gmd_subnatid4` are populated from `geo_code` according to
  the inferred representative level. `geo_code` itself is `VAR-geocode`'s
  resolved value (equal to `gmd_subnatidsurvey` on the matched row) — it is
  matched once against `survey_labels` and then fanned out, rather than each
  `subnatid` level independently re-matching survey text.
- `gmd_subnatidsurvey` stores the survey geography anchor used to align
  `VAR-subnatid1` to `VAR-subnatid4` across country implementations.
- `geo_year`, `geo_source`, `geo_level`, `geo_idvar`, `geo_id`, `geo_nvar`,
  and `geo_name` preserve source GEO metadata required for downstream
  crosswalking and diagnostics. When `geo_source` is `GAUL`, `geo_id` is the
  genuine GAUL numeric code for that row's level, and `VAR-gauladm1code`/
  `VAR-gauladm2code` reuse it directly instead of a separate GAUL database
  lookup.
- `representative_level` and `is_rep_subnat*` preserve representativeness flags
  by subnational level.
- `source_row` preserves traceability to the source workbook row used in
  extraction.
- A country with more than one effective-dated `PARAM-GEO-GMD-CROSSWALK`
  record (multiple `effective_from`/`effective_to` periods) has a documented
  administrative boundary change; `VAR-subnatid1prev` through
  `VAR-subnatid4prev` resolve from the immediately prior period's matched
  row rather than requiring a separate historical source.

## Fallback behavior

`block_and_escalate` is required when no valid country record exists.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-30 | 0.4 | Add VAR-subnatid1prev-4prev and VAR-gauladm1code/2code to applies_to_variables; document reuse of geo_id (GAUL) and prior effective-dated periods | GPID Team |
| 2026-09-30 | 0.3 | Add VAR-geocode to applies_to_variables; document geo_code as the single resolved code VAR-subnatid1-4 fan out from | GPID Team |
| 2026-09-18 | 0.2 | Add table contract for geography crosswalk extraction | GPID Team |
