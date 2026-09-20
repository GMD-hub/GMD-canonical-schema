---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-conshotelsrestaurants
canonical_label: "Household hotels and restaurants consumption component"
variable_name: conshotelsrestaurants
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: aggregate
data_type: numeric_continuous

value_codes: null
allowed_range:
  min: 0
  max: null

missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized — restaurants and lodging module unusable"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-welfare

country_parameters: []
prerequisites: []

# --- Aggregate: component structure ---
component_structure:
  operation: sum
  output_unit_of_analysis: household
  components:
    - component_id: restaurants_meals
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: hotel_lodging
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "collect restaurant meals, prepared food away from home, and lodging spending"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "keep ready-made meals out of the food aggregate when they are classified as meals away from home"
    - "sum of included rows equals the hotels and restaurants subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, p. 40; restaurants and accommodation services are included, while ready-made meals remain food."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "restaurants"
    - "hotels"
    - "meals away from home"
    - "lodging"
  typical_section_names:
    - "Restaurants and hotels"
    - "Accommodation"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, p. 40"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 includes restaurants and accommodation services in the nonfood aggregate, while ready-made meals are treated as food."
---

## Definition

`conshotelsrestaurants` is the household's spending on restaurants,
accommodation, and similar away-from-home lodging services. It is a component
of `VAR-welfare`.

## Conceptual intent

MV22 distinguishes prepared meals consumed away from home from food at home. The
former is part of the nonfood aggregate when it is a meal service, while in-home
or household-prepared food stays in the food component.

## Construction notes

- Include restaurant food spending and lodging or accommodation services.
- Keep ready-made meals separate from food-at-home consumption.
- Annualize periodic expenditures before household aggregation.

## Escalation triggers

- Survey data blur away-from-home meals with home food acquisition.
- The lodging or restaurant module is present but not classifiable into current
  consumption.
