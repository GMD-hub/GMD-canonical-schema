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
derived_from:
  - VAR-subnatidsurvey
derives_to:
  - VAR-gauladm1code
  - VAR-gauladm2code
  - VAR-subnatid1prev
  - VAR-subnatid2prev
  - VAR-subnatid3prev
  - VAR-subnatid4prev

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters:
  - PARAM-GEO-GMD-CROSSWALK

# --- Universe / skip condition ---
gates: []

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
      'ALB_2021_NUTS3_AL031') that PARAM-GEO-GMD-CROSSWALK rows carry in
      gmd_subnatidsurvey. Matched once from the survey's representative level
      (subnatidsurvey), then reused by the GAUL codes and the prior-boundary
      subnatid*_prev variables. It is NOT the source of subnatid1-4, which are
      survey-derived. Form verified against every committed
      PARAM-GEO-GMD-CROSSWALK record (144 countries, 2,195 unique non-empty
      values, 0 deviations)."
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

`geo_code` is the result of matching the survey's representative-level geography
(`subnatidsurvey`) against the stable country geography crosswalk. It is a
separate variable from the survey-derived identifiers: `subnatid1`-`subnatid4`
and `subnatidsurvey` are built directly from the survey data and do NOT depend
on this match. `geo_code` records the single matched crosswalk code once, and
that resolved match is reused by the GAUL codes (`gaul_adm1_code`,
`gaul_adm2_code`) and the prior-boundary identifiers (`subnatid1_prev`-
`subnatid4_prev`).

## Construction notes

Resolve `geo_code` from the survey's representative level (`subnatidsurvey`) —
the `subnatid{N}` level the survey is representative on. Match that
representative-level survey value against `PARAM-GEO-GMD-CROSSWALK` resolved
from the country layer for the survey's ISO3 code and survey ID year.
`survey_labels` holds one or more pipe-separated (`|`) label variants for the
same geography identity (accented/unaccented, cased, punctuation variants) —
normalize both the survey value and the stored variants (case-fold, trim,
collapse whitespace) before comparing.

On a match:
  geo_code = gmd_subnatidsurvey for the matched country_entry_id

Document the matched `country_entry_id` in the do-file notes.

`geo_code` does NOT supply `subnatid1`-`subnatid4`: those are built directly
from the survey data (the "code - label" string) and never from this crosswalk
match. The resolved match is instead reused downstream by `gaul_adm1_code`/
`gaul_adm2_code` (the GAUL `geo_id` when `geo_source=GAUL`) and by the
prior-boundary `subnatid*_prev` variables (via the prior effective-dated
crosswalk period).

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
- Treating `geo_code` as the source of `subnatid1`-`subnatid4`: those are
  survey-derived ("code - label") and independent of this crosswalk match.
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
