---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-male
canonical_label: "Sex of household member"
variable_name: male
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Male"
  - value: 0
    label: "Female"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized — data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available — sex not collected in this survey"
  - code: ".o"
    label: "Other sex category not covered by harmonized codes"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country-specific requirements ---
requires_country_lookup: false
country_lookup_table: null

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules:
  - RULE-SEX-001
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "sex"
    - "gender"
    - "male"
    - "female"
  typical_section_names:
    - "Household roster"
    - "Household composition"
    - "Demographics"
    - "Individual characteristics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM) — Mapping and Description of Variables — male"
  extraction_method: manual
  extracted_on: "2026-06-25"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`male` is a binary dummy variable that records the biological sex of each
individual within a household. After harmonization it takes two values:
1 for male and 0 for female.

## Conceptual intent

`male` is the individual-level sex indicator used to support gender
disaggregation across all GMD modules and in downstream poverty and welfare
analysis. It is one of the most fundamental variables in the database and is
required for virtually every analytical output the GMD produces.

## Construction notes

Map the raw sex variable directly to the GMD binary codes. No imputation or
estimation of sex from other variables is permitted under any circumstances.

Numeric placeholder values that appear in the raw data — such as 98, 99,
or 9 — are not valid sex codes. They must be excluded and coded as `.a`.

When the raw survey contains categories beyond male and female — for example
"other," "non-binary," or "prefer not to say" — do not assign 1 or 0 to
those responses. Code them as `.o` and document the label, the raw code,
and its frequency in the do-file notes.

## Consistency checks

- No individual should have a standard missing value (`.`) for `male`. All
  cases must receive either a valid code (1 or 0) or an explicit extended
  missing code with a documented reason.
- Cross-check against `relationharm`: the household head and their spouse
  should typically have different values of `male`. Flag households where
  head and spouse share the same value for manual review.
- Cross-check the sample-level share of males and females. Shares that
  deviate sharply from 50/50 at the national level without a demographic
  explanation may signal a coding error.

## Escalation triggers

- The raw survey contains a sex category that is not clearly male or female
  and the questionnaire documentation does not clarify how to handle it.
- More than 2 percent of individual records result in `.o` or `.b` for `male`.
- The sample share of males is below 40 percent or above 60 percent with no
  apparent sampling explanation.

## Common mistakes

- Retaining numeric placeholder codes (98, 99, 9) as valid values instead of
  recoding them as `.a`.
- Coding "other" or ambiguous categories as 1 or 0 to avoid leaving missing
  values.
- Confusing biological sex (as recorded in the raw survey) with gender
  identity, which some newer surveys record as a separate variable.
- Using standard Stata missing (`.`) instead of the appropriate extended
  missing code, which prevents future harmonizers from understanding why the
  value is absent.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
