---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate  (a component is itself an aggregate — the recursion)
# ================================================================

# --- Identity ---
variable_id: VAR-consfood
canonical_label: "Household food consumption component"
variable_name: consfood
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household          # OUTPUT unit
mapping_role: aggregate              # assembled from item-level rows to household
data_type: numeric_continuous

value_codes: null
allowed_range:
  min: 0
  max: null

missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized — food module present but unusable"

# --- Derivation graph ---
# A leaf-level aggregate: assembled from RAW survey items, not from other GMD
# variables. derived_from is therefore empty; the raw item source is described
# in component_structure and source_hints.
derived_from: []
derives_to:
  - VAR-welfare

country_parameters: []              # unit conversion is a lookup TABLE (design note Part B1), not a parameter — no model home yet

prerequisites: []

# --- Aggregate: component structure (NEW BLOCK) ---
# Three sub-parts, each an item-level source with its own value path. This is
# where the diary / quantity x price mechanics live.
component_structure:
  operation: sum
  output_unit_of_analysis: household
  components:
    - component_id: food_purchased
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value | quantity_x_price   # whichever the survey provides
      include: always
    - component_id: food_ownproduced
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: quantity_x_price                  # usually no direct value
      include: always
      governed_by: own_production_valuation          # price source is the switch
    - component_id: food_inkind
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: quantity_x_price
      include: always
      governed_by: own_production_valuation
      # In-kind from households / charities / private transfers / payment in kind.
      # EXCLUDES subsidized government ration programs -> those go to food_ration
      # (a distinct switch); keeping them separate avoids double-counting.
    - component_id: food_ration
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: quantity_x_price                  # re-priced; recorded/subsidized outlay understates welfare
      include: when_present                         # only countries with ration programs populate this
      governed_by: ration_valuation                 # five-rung ladder, RULE-WLF-003 (NOT own_production_valuation)
      # Identified at the item level by acquisition_mode (canonical item table);
      # official/subsidized price is prohibited as a valuation source.

# --- Aggregate: construction pipeline (NEW BLOCK) ---
construction_pipeline:
  - stage: unit_standardization
    scope: quantity-based item rows
    requires_lookup: PARAM-WLF-UNIT-CONVERSION
  - stage: value_computation
    rule: "if value_path == quantity_x_price: value = standardized_quantity * unit_price"
  - stage: recall_annualization
    scope: all food item rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation (NEW BLOCK) ---
reconciliation:
  internal:
    - "no negative item values; unit prices within plausible per-unit bands"
    - "purchased + own-produced + in-kind + ration reconcile to any reported food total"
    - "ration items counted in food_ration only, never also in food_inkind (no double-count)"
  distributional:
    - "implied unit prices not extreme vs local norms (flag unit-conversion errors)"

# --- Cross-references ---
rules:
  - RULE-WLF-001            # methodological switch escalation gate (own_production_valuation)
  - RULE-WLF-002            # unit-value cascade: prices own-produced/in-kind food once the switch picks a unit-value concept
  - RULE-WLF-003            # food-ration re-pricing ladder + official-price prohibition (ration_valuation switch)
  - RULE-WLF-004            # reference period: short-recall preference, usual-month deprecation
  - RULE-WLF-005            # zero-vs-missing distinction + item-nonresponse procedure (module-wide)
  - RULE-WLF-006            # acquisition-as-proxy acceptance + bulk-purchase scrutiny
  - RULE-WLF-007            # outlier detect/treat/sensitivity (module-wide; governs outlier_handling)
exceptions: []
external_standards:
  - name: "Mancini, Giulia & Vecchi, Giovanni (2022), On the Construction of a Consumption Aggregate for Inequality and Poverty Analysis, Washington, D.C.: World Bank Group — PRIMARY authority (MV22). Food sections: §4.2.1 acquisition vs consumption (pp.26-27); §4.2.2 recall / usual-month deprecation (pp.27-28); §4.2.3 food away from home; §4.2.4 own-production & unit-value cascade eq.4.1 (pp.30-32); §4.2.5 rations (pp.33-34); §7.2 zero-vs-missing (pp.98-101); §7.3 outliers (pp.101-106)"
    url: "http://documents.worldbank.org/curated/en/099225003092220001"   # extracted text at extraction/sources/mancini-vecchi-2022.txt

source_hints:
  question_keywords:
    - "food expenditure"
    - "food consumed"
    - "quantity"
    - "unit"
    - "price paid"
    - "own production"
    - "food received as gift"
    - "food diary"
  typical_section_names:
    - "Food"
    - "Food diary"
    - "Consumption — food"

provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "TBD — consumption / food module (confirm with GPID Team)"
  extraction_method: manual
  extracted_on: "2026-07-01"
  human_reviewed: false
  reviewer: null
  notes: "PROPOSAL. Demonstrates the recursion (a welfare component is itself an
          aggregate record) and the item-level quantity x price mechanics. Names
          are placeholders pending GMD alignment."
---

## Definition

`consfood` is the household's total food consumption over the reference period:
food purchased, food produced by the household and consumed, and food received
in kind — each valued, standardized to annual terms, and summed to the household.
It is a component of `VAR-welfare`.

## Conceptual intent

Food is the largest and most measurement-sensitive part of the consumption
aggregate in poor households, and the part most often collected as item-level
diary or recall data rather than a single value. Getting its unit handling and
own-production valuation right is what makes the Engel share plausible and the
welfare ranking of subsistence households correct.

## Construction notes

**Value path depends on what the survey gives you.** Some surveys record a food
*value* per item directly (`direct_value`); many record *quantity* and *unit*
(and sometimes price), requiring `quantity_x_price`. Detect which per item.

**Unit standardization first.** Convert local units (bunch, tin, plate, heap) to
standard units via `PARAM-WLF-UNIT-CONVERSION` *before* computing value from quantity.
A wrong conversion is the most common source of implausible welfare.

**Own-produced and in-kind food need a price.** They rarely carry a value, so
they are valued at a price whose source is the `own_production_valuation`
methodological switch. Stated preference order (MV22 §4.2.4): self-reported
valuation ≻ market unit values (local, via the RULE-WLF-002 cascade, broadening
to national) ≻ farm-gate (a theoretical ideal, effectively never constructible).
That switch has `escalate: true` — do not pick a valuation silently; propose
(default `self_reported_value`) and escalate per `RULE-WLF-001`.

**Government food rations are valued separately.** Rations are a *type* of
in-kind transfer, but MV22 (§4.2.5) gives them their own valuation ladder, so
they are a distinct component (`food_ration`) governed by the separate
`ration_valuation` switch (secondary-market unit value / close-substitute market
price / self-reported WTP / expert judgment; official-subsidized price is
prohibited) per `RULE-WLF-003`. Keep them out of `food_inkind` to avoid
double-counting. Countries without a ration program simply leave `food_ration`
empty — the split gives ration countries the granularity without burdening the
rest.

**Annualize, then assemble.** Scale each item to annual terms by its recall
period, then sum all food rows to the household via `hhid`.

## Consistency checks

Run the `reconciliation` block. Flag implied unit prices that are extreme
relative to local norms — these almost always indicate a unit-conversion error
rather than a genuine outlier.

## Escalation triggers

- `own_production_valuation` is unset in the Harmonization Spec.
- `ration_valuation` is unset in the Harmonization Spec and ration items are
  present (`food_ration` non-empty).
- Local units appear that are not in `PARAM-WLF-UNIT-CONVERSION` and cannot be resolved.
- Food module present but neither value nor quantity is usable → `.b`.

## Common mistakes

- Computing value from quantity **before** standardizing units.
- Valuing own production at a price source different from the one the switch
  specifies, or picking one silently.
- Forgetting to annualize, or mixing recall periods across food sub-parts.

## Change log

| Date       | Version | Change                          | Authority  |
|------------|---------|---------------------------------|------------|
| 2026-07-01 | 0.1     | Initial draft (schema extension proposal) | GPID Team  |
