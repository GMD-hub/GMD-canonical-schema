---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-weight
canonical_label: "Household weights"
variable_name: weight
module_id: MOD-IDN
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because the household weighting coefficient is not available"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "weight"
    - "household weight"
    - "sampling weight"
    - "probability weight"
    - "wgt"
    - "hhweight"
  typical_section_names:
    - "Household identification"
    - "Sampling / Weights"
    - "Household questionnaire cover"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Lessons Learned and Challenges, household weighting coefficient"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "NON-NULL WEIGHT INVARIANT (documented here as provenance note, not a RULE): the household weighting coefficient cannot be missing. When weights are missing, analyze and document the reason first. If the missing weight is for non-regular household members (domestic workers, renters, etc.) per the country definition, do not assign any weight to these observations as they are usually excluded from analyses. Only after careful documentation may weights be revised. No numeric weight range is stated in the source; weights must be strictly positive (they are commonly fractional), so allowed_range is left null."
---

## Definition

`weight` is the household weighting coefficient used to expand sample
households to the survey population for analysis.

## Conceptual intent

`weight` provides the sampling weight required to produce population estimates
from the harmonized survey data. It supports weighted welfare and poverty
analysis, where unweighted estimates would be biased by the sample design.

## Construction notes

The household weighting coefficient cannot be missing (the Non-Null Weight
Invariant). All households in scope must receive a non-missing positive weight.

The first step when weights appear to be missing is to analyze and understand
the reason why weights are missing for a given observation. If the missing
weight is for non-regular household members (domestic workers, renters, etc.)
per the country definition, do not assign any weight to these observations, as
they are usually excluded from any analyses. Only after careful documentation
may weights be revised.

Record the weighting variable source and any adjustments in the do-file notes.

## Consistency checks

- No household in scope may have a missing `weight`.
- `weight` must be strictly positive.
- Weighted totals should approximate known survey population benchmarks.

## Escalation triggers

- Households in scope have missing weights and the reason cannot be clearly
  attributed to non-regular members or a documented exception.
- A revised weight is proposed without adequate documentation.

## Common mistakes

- Leaving `weight` missing without documenting the reason, violating the
  Non-Null Weight Invariant.
- Assigning weights to excluded non-regular household members.
- Using an unweighted analysis when population-representative weights are
  available.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
