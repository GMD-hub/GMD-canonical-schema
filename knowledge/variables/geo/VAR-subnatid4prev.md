---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-subnatid4prev
canonical_label: "Subnational ID previous - lowest level"
variable_name: subnatid4_prev
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
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
    label: "Information not available because the subnational classification has not changed since the previous survey"

# --- Derivation graph ---
derived_from: []
derives_to: []

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
    - "previous village"
    - "previous locality"
    - "administrative change"
    - "split"
    - "boundary change"
    - "subnational"
  typical_section_names:
    - "Geography"
    - "Identification"
    - "Administrative boundaries"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, subnatid4_prev"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "country_parameters updated 2026-09-30 to declare
      PARAM-GEO-GMD-CROSSWALK: countries with more than one effective-dated
      crosswalk record capture a documented boundary change; the prior
      period's matched row supplies subnatid4_prev."
---

## Definition

`subnatid4_prev` is a country-specific categorical string variable that is coded
as missing unless the classification used for `subnatid4` has changed since the
previous survey. When the classification has changed, it records the `subnatid4`
code used in the previous survey.

## Conceptual intent

`subnatid4_prev` maintains temporal consistency in lowest-level subnational
identifiers, allowing analysts to track splits and administrative changes across
surveys.

## Construction notes

`subnatid4_prev` is coded as missing unless the lowest-level classification
changed since the previous survey. Where a change occurred (e.g., a village
redefinition), the previous survey's code is recorded for all affected
households.

**Reusing the geography crosswalk.** Resolve `PARAM-GEO-GMD-CROSSWALK` from
the country layer for the survey's ISO3 code. If the country has more than
one effective-dated record, match the household's area against the period
containing the survey ID year to obtain `subnatid4`, then match the same
geography against the immediately prior period to obtain `subnatid4_prev`
from that record's `gmd_subnatid4`. If the country's crosswalk has only one
effective-dated record, `subnatid4_prev` remains coded as missing.

`value_codes` is intentionally null because the previous values depend on the
country's administrative history and the country parameter layer. Load the
country parameters and exceptions valid for the survey's ID year and the
relevant previous survey. Values follow the same "code - name" string convention
as `subnatid4`.

## Consistency checks

- `subnatid4_prev` must be a string variable.
- When populated, its value must be a valid fourth-level code from the previous
  survey's classification.
- When resolved from the crosswalk, the prior-period record's `effective_to`
  must immediately precede the current period's `effective_from`.
- Affected households' previous codes must be consistent with the documented
  administrative change.
- No household may carry a standard missing (`.`) where a classification change
  occurred.

## Escalation triggers

- Administrative boundaries changed but the previous classification cannot be
  determined from documentation.
- The previous codes cannot be reconciled with the current `subnatid4` mapping
  for affected households.
- The country's crosswalk has multiple periods but the prior period's
  geography cannot be matched to the current period's geography.

## Common mistakes

- Populating `subnatid4_prev` even when the classification did not change.
- Using current codes instead of the previous survey's codes when recording a
  change.
- Fabricating previous codes instead of using the documented historical
  classification.
- Assuming every country has a prior period in the crosswalk; most have only
  one effective-dated record, so `subnatid4_prev` is missing by default.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
| 2026-09-30 | 0.2     | Resolve subnatid4_prev from the prior effective-dated period of PARAM-GEO-GMD-CROSSWALK when the country has boundary-change history | GPID Team |
