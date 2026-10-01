---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-geocode
canonical_label: "Resolved geography crosswalk code"
variable_name: geo_code
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: derived_preferred
data_type: string

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Survey area text could not be matched to any country_entry_id in
            PARAM-GEO-GMD-CROSSWALK for the survey ISO3 code and survey ID year"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-subnatid1
  - VAR-subnatid2
  - VAR-subnatid3
  - VAR-subnatid4
  - VAR-subnatidsurvey

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters:
  - PARAM-GEO-GMD-CROSSWALK

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "area"
    - "region"
    - "province"
    - "district"
    - "commune"
    - "sampling area"
  typical_section_names:
    - "Identification"
    - "Geography"
    - "Sampling design"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), country geography crosswalk resolution"
  extraction_method: manual
  extracted_on: "2026-09-30"
  human_reviewed: false
  reviewer: null
  notes: "New variable: captures the single resolved crosswalk code (e.g.
      'ALB_2021_NUTS3_AL031') that PARAM-GEO-GMD-CROSSWALK rows already carry
      in gmd_subnatidsurvey, so it can be matched and recorded once before
      being fanned out to VAR-subnatid1 through VAR-subnatid4."
---

## Definition

`geo_code` is the resolved geography crosswalk code for a household's survey
area, matched from the raw survey area/region text against
`PARAM-GEO-GMD-CROSSWALK` for the survey's ISO3 code and survey ID year. It
takes the form `<ISO3>_<geo_year>_<geo_source><geo_level>_<geo_id>`, e.g.
`ALB_2021_NUTS3_AL031`. Only the first three segments (ISO3, geo_year,
`geo_source`+`geo_level`) have fixed shape; `geo_id` is the remainder of the
string and may itself contain further underscores or dots (e.g. GADM's
composite codes such as `COD_2022_GADM1_COD.10_1`, where `geo_id` is
`COD.10_1`). Verified against every committed `PARAM-GEO-GMD-CROSSWALK`
record (144 countries, 2,195 unique non-empty values): 0 values deviate from
this form once `geo_id` is treated as the full remainder rather than a
single token.

## Conceptual intent

`geo_code` is the single matched-row output that the subnational identifier
family (`subnatid1`-`subnatid4`, `subnatidsurvey`) is fanned out from. Instead
of each of those variables independently re-matching survey text, `geo_code`
performs the match once and records the crosswalk row's resolved code, which
is then assigned to whichever `subnatid` levels the row declares as
representative (`is_rep_subnat1`-`is_rep_subnat4`, `representative_level`).

## Construction notes

Match the individual's/household's reported survey area text against the
`survey_labels` field of each row in `PARAM-GEO-GMD-CROSSWALK` resolved from
the country layer for the survey's ISO3 code and survey ID year.
`survey_labels` holds one or more pipe-separated (`|`) label variants for the
same geography identity (accented/unaccented, cased, punctuation variants) —
normalize both the survey response and the stored variants (case-fold, trim,
collapse whitespace) before comparing. Scope the match to rows whose
`survey_variables` field includes the raw survey variable being harmonized
(e.g. `subnatid`, `subnatid1`).

On a match:
  geo_code = gmd_subnatidsurvey for the matched country_entry_id

Document the matched `country_entry_id` in the do-file notes.

**Relationship to subnatid1-4.** Once `geo_code` is resolved, the matched
row's `gmd_subnatid1` through `gmd_subnatid4` and `is_rep_subnat1` through
`is_rep_subnat4` supply the fan-out values for those variables directly —
they must not be independently re-matched against survey text.

## Consistency checks

- `geo_code` must match `<ISO3>_<geo_year>_<geo_source><geo_level>_<geo_id>`,
  where only the first three segments are fixed-shape (3-letter ISO3, 4-digit
  year, source+level token); `geo_id` is everything remaining and may itself
  contain `_` or `.` (e.g. GADM composite codes). Do not parse `geo_code` by
  splitting on every underscore.
- Every non-missing `geo_code` must correspond to exactly one
  `country_entry_id` in the country's `PARAM-GEO-GMD-CROSSWALK`.
- Cross-check that the matched row's `geo_year` is consistent with the
  survey ID year (flag large mismatches for review).
- Some crosswalk rows are legitimately unpopulated placeholders (blank
  `geo_source`, `geo_level`, and all `gmd_subnatid*`/`gmd_subnatidsurvey`
  fields) — these must resolve to `.c`, not an empty-string `geo_code`.

## Escalation triggers

- No `PARAM-GEO-GMD-CROSSWALK` record is valid for the survey's ISO3 code and
  survey ID year. Apply the registry's `block_and_escalate` fallback policy.
- The survey area text does not match any `survey_labels` entry for the
  resolved country/year. Do not guestimate a geography code from a partial
  or fuzzy match beyond normalized exact matching.
- The survey area text matches more than one `country_entry_id` ambiguously
  (e.g. duplicate `survey_labels` across rows after normalization).

## Common mistakes

- Matching against raw, non-normalized survey label text (case/accent/
  whitespace differences causing false misses).
- Re-deriving `subnatid1`-`subnatid4` independently instead of reusing the
  same matched row's `gmd_subnatid1`-`gmd_subnatid4` values.
- Using a crosswalk record from the wrong ISO3 code or survey ID year.
- Splitting `geo_code` into segments on every underscore — `geo_id` (the
  final segment) can itself contain underscores or dots and must be treated
  as the remainder after the third underscore, not re-split further.
- Treating a blank/placeholder crosswalk row (no `geo_source`/`geo_level`
  populated) as a match instead of escalating.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-30 | 0.1     | Initial draft | GPID Team  |
