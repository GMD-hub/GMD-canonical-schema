---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-conseducation
canonical_label: "Household education expenditure component"
variable_name: conseducation
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
    label: "Cannot be harmonized — education module unusable"

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
    - component_id: education_tuition
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: education_other_costs
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "collect education-related expenditures that are current consumption and not capital accumulation"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "education spending is included despite the life-cycle concern; keep the category coherent with MV22"
    - "sum of included rows equals the education subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, pp. 38–40; education expenditure is included in the consumption aggregate."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "education"
    - "school"
    - "tuition"
    - "fees"
  typical_section_names:
    - "Education"
    - "School expenditure"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, pp. 38–40"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 explicitly recommends including education expenditure in the consumption aggregate even though it is partly investment-like."
---

## Definition

`conseducation` is the household's education expenditure component, capturing
school fees and other direct education costs arising during the reference
period. It is a component of `VAR-welfare`.

## Conceptual intent

MV22 rejects the view that education should be excluded purely because it is
partly investment-like. While some overlap with long-term human capital exists,
the recommended practice is to treat education spending as part of current
consumption for welfare measurement.

## Construction notes

- Include direct tuition and school-related outlays that reflect current
  household consumption.
- Keep the treatment aligned with the survey's education module and reference
  period.
- Annualize as needed before aggregation.

## Escalation triggers

- The module contains spending that is not clearly part of current consumption.
- Education expenditure is reported but cannot be reconciled to the household's
  current-period welfare concept.
