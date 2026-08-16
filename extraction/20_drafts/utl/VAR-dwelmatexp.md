---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-dwelmatexp
canonical_label: "Total annual consumption of materials for the maintenance and repair of the dwelling"
variable_name: dwelmat_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric_continuous

# --- Allowed output values ---
value_codes:
  null
allowed_range: null
# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"
  - code: ".o"
    label: "Other value not covered by harmonized codes"
# --- Derivation graph ---
derived_from:
  []
derives_to: []
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "COICOP 4.3.1"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Additional variables, dwelmat_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`dwelmat_exp` is a continuous variable that refers to total annual household expenditures on products and materials for maintenance and repair of the dwelling.

## Conceptual intent

It captures materials expenditure for minor maintenance and repair, following COICOP 4.3.1.

## Construction notes

Include paints and varnishes, renderings, wallpapers, windowpanes, plaster, cement, putty, etc. Exclude fitted carpets and linoleum (5.1.2), hand tools, door fittings, and lamp bulbs (5.5.2), brooms and cleaning products (5.6.1), and materials for major maintenance/repair or extension/conversion.

## Consistency checks

- Cross-check that `othhousingexp` equals `dwelmatexp` plus `dwelsvcexp`.
- Materials and services for repair may be combined in the survey.

## Escalation triggers

- Including major maintenance/repair or capital expenditure.

## Common mistakes

- Including cleaning products or hand tools in maintenance materials.
- Double counting when combined with `dwelsvcexp`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
