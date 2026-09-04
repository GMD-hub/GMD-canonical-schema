---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-consrecreation
canonical_label: "Household recreation and culture consumption component"
variable_name: consrecreation
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
    label: "Cannot be harmonized — recreation module unusable"

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
    - component_id: recreation_services
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: recreation_goods
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: culture_goods
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "sum direct recreation and culture expenditures that reflect current use and services; quantity × unit price is not the default data structure for these categories"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "exclude recreation durables and capital-like goods from the current-use component"
    - "sum of included rows equals the recreation subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, pp. 35–40; non-durable recreation and culture items are included, while recreation durables are excluded."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "recreation"
    - "culture"
    - "books"
    - "movies"
    - "entertainment"
  typical_section_names:
    - "Recreation and culture"
    - "Leisure"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, pp. 35–40"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 includes non-durable recreation and cultural expenditures and excludes major recreation durables."
---

## Definition

`consrecreation` is the household's current-use recreation and culture
expenditure, including games, cultural services, and non-durable leisure
spending. It is a component of `VAR-welfare`.

## Conceptual intent

The category is included only for the ordinary goods and services that proxy
current consumption. Major recreation durables have a separate durable treatment
and should not be included here unless transformed into a service-flow concept.

## Construction notes

- Include recurring leisure and culture spending that reflects current use.
- Exclude obvious durable goods and large recreational acquisitions.
- Annualize to the common reference period before summing.

## Escalation triggers

- The survey mixes ordinary recreation spending with durable purchases without a
  clean split.
- A reported recreation item is clearly a stock acquisition rather than current
  household consumption.
