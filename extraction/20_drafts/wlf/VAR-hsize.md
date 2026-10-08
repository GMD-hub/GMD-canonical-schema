---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.2
# ================================================================

# --- Identity ---
variable_id: VAR-hsize
canonical_label: "Number of household members (household size)"
variable_name: hsize
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.2"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: integer

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 1
  max: 100

# --- Missing value codes ---
# Missing values are not allowed for hsize (see Definition): every household must
# carry a positive member count, so no extended-missing codes are declared.
missing_codes: []

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# The definition of a "regular member" is country-specific (a country-layer /
# methodology matter), but the count itself is a plain integer; no CVS parameter
# is declared here.
country_parameters: []

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "household size"
    - "number of household members"
    - "household members"
    - "regular members"
    - "residents"
    - "roster size"
  typical_section_names:
    - "Welfare"
    - "Household roster"
    - "Household composition"
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Welfare aggregates, hsize"
  extraction_method: manual
  extracted_on: "2026-09-21"
  human_reviewed: false
  reviewer: null
  notes: "Household-member count used as the
          per-capita denominator when a country prelude normalizes a household
          total into welfare; the regular-member definition is country-specific."
---

## Definition

`hsize` is the total number of residents (regular members) in the household,
excluding maids and servants. The definition of a regular member is
country-specific. Compare this variable with the number of persons counted in
Chapter 4 (DEM). Missing values are not allowed.

## Conceptual intent

`hsize` gives the household's member count on a consistent, country-defined
basis. It is the denominator a country prelude uses when normalizing a household
total into a per-capita welfare measure, and it is the reference against which
per-household demographic counts are checked. Because it underpins per-capita
welfare, every household must carry a valid, positive `hsize`.

## Construction notes

Record the count of regular resident members as defined by the survey, excluding
maids, servants, and other non-members. Apply the country's own definition of a
regular member (for example, minimum months of residence, or treatment of
absent members); document that definition where it is not obvious.

`hsize` may be taken directly from a household-size variable the survey provides,
or counted from the household roster after non-members are excluded. Either way
it must reconcile with the Chapter 4 (DEM) person roster for the same household.

## Consistency checks

- `hsize` must be present for every household — missing values are not allowed.
- `hsize` must be a positive integer (>= 1).
- `hsize` must equal the number of regular members counted for the household in
  the Chapter 4 (DEM) roster. Flag any household where the two disagree.
- When `hsize` is the per-capita denominator, `welfare * hsize` should
  reconstruct the household total the prelude started from (within rounding).

## Escalation triggers

- Any household has a missing, zero, or non-integer `hsize`.
- `hsize` disagrees with the Chapter 4 (DEM) roster count and the discrepancy
  cannot be explained by the exclusion of maids/servants or the country's
  regular-member rule.
- The survey does not document how regular membership is defined.

## Common mistakes

- Including relatives or other guests temporarily present, maids, servants, or other 
  non-members in the count.
- Using a raw roster row count without excluding non-regular members.
- Leaving `hsize` missing for households with incomplete rosters instead of
  escalating.
- Letting `hsize` diverge from the DEM person count without a documented reason.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-09-21 | 0.2     | Initial draft | GPID Team  |
