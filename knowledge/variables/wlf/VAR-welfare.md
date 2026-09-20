---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate  (schema extension — see docs/derived-indicators.md)
# ================================================================

# --- Identity ---
variable_id: VAR-welfare
canonical_label: "Household welfare aggregate (consumption)"
variable_name: welfare
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household          # unit of the OUTPUT
mapping_role: aggregate              # NEW ROLE: assembled across units of analysis
data_type: numeric_continuous

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 0                             # strictly positive after construction; 0 only degenerate
  max: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized — required components missing and no
            usable pre-computed aggregate available"

# --- Derivation graph ---
# Components summed into the total. Assembly semantics are in
# component_structure below; this lists identity only, per schema convention.
derived_from:
  # VAR-consfood is DEFERRED (temporary, 2026-08-31): the welfare aggregate does
  #   NOT depend on food for now (harder variable, resumed later). Kept here as an
  #   identity member; assembly is suppressed via include: deferred below. See the
  #   "Temporary scope" note. Reversible: restore include: always to re-activate.
  - VAR-consfood
  - VAR-consalcoholtobacco
  - VAR-consclothing
  - VAR-conshousing
  - VAR-consfurnishings
  - VAR-conshealth
  - VAR-constransport
  - VAR-conscommunications
  - VAR-consrecreation
  - VAR-conseducation
  - VAR-conshotelsrestaurants
  - VAR-consmiscellaneous
  - VAR-consdurables
derives_to: []

# --- Country parameter declarations ---
# Only the genuine parameter is declared here. The price indices (external data)
# and unit conversion (a lookup table) that construction also needs have no home
# in the current model — see docs/derived-indicators.md, Part B; they appear only
# descriptively in construction_pipeline, not as country_parameters.
country_parameters:
  - PARAM-WLF-EQUIVALENCE-SCALE      # only if equivalence_scale != per_capita

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-hhsize
    condition: "Household size must be defined before per-capita scaling."
  - variable_id: VAR-adulteq
    condition: "Required only if the equivalence_scale switch is not per_capita."
  - variable_id: VAR-consfood
    condition: "DEFERRED (temporary, 2026-08-31): food is NOT required for the
                current partial build. All OTHER in-scope component variables must
                be constructed (or explicitly marked absent) before the aggregate
                is assembled; food re-enters this prerequisite when its deferral
                is lifted."

# --- Aggregate: component structure (NEW BLOCK) ---
component_structure:
  operation: sum
  output_unit_of_analysis: household
  derived_units:
    - per_capita                     # welfare / hhsize  — the poverty welfare
    - per_adult_equivalent           # welfare / adulteq — if equivalence_scale set
  components:
    - component_id: VAR-consfood
      native_unit_of_analysis: item          # diary/recall rows
      roll_up_key: hhid
      include: deferred                       # TEMPORARY (2026-08-31): food paused
      deferral:
        status: temporary
        since: "2026-08-31"
        reason: "Food purchases + in-kind are the hardest components; deferred so
                 the full process runs on the rest of welfare first. Reversible."
        consequence: "Assembled welfare is PARTIAL (food-excluded), not
                      poverty-valid; poverty-reproduction divergence is expected
                      and recorded as a determination, not a failure."
    - component_id: VAR-consalcoholtobacco
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-consclothing
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-conshousing
      native_unit_of_analysis: household
      roll_up_key: hhid
      include: governed_by_switch      # imputed_rent may set to exclude
      governed_by: imputed_rent
    - component_id: VAR-consfurnishings
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-conshealth
      native_unit_of_analysis: household
      roll_up_key: hhid
      include: governed_by_switch
      governed_by: health_lumpy
    - component_id: VAR-constransport
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-conscommunications
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-consrecreation
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-conseducation
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-conshotelsrestaurants
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-consmiscellaneous
      native_unit_of_analysis: item
      roll_up_key: hhid
      include: always
    - component_id: VAR-consdurables
      native_unit_of_analysis: household
      roll_up_key: hhid
      include: governed_by_switch
      governed_by: durables_treatment

# --- Aggregate: methodological switches (NEW BLOCK) ---
# Universal DEFINITIONS only. The chosen value per survey is recorded in the
# Harmonization Specification (Schema 3), never here. escalate: true means an
# unset value BLOCKS finalization (see RULE-WLF-001).
methodological_switches:
  - switch_id: imputed_rent
    question: "How is the consumption flow from owner-occupied / rent-free housing valued?"
    options: [self_assessed, hedonic_regression, user_cost, exclude]
    default: null
    escalate: true
    governs: [VAR-conshousing]
    consequence: "Inclusion raises mean welfare and reshapes the lower tail; method affects cross-survey comparability."
  - switch_id: durables_treatment
    question: "Durables as acquisition expenditure, or as imputed use-value (flow of services)?"
    options: [use_value_flow, acquisition, exclude]
    default: use_value_flow
    escalate: true
    governs: [VAR-consdurables]
    consequence: "acquisition injects lumpiness; use_value_flow needs stock, age, depreciation, real interest assumptions."
  - switch_id: own_production_valuation
    question: "At what prices are own-produced / in-kind items valued?"
    # Stated preference order (MV22 §4.2.4, pp.30-33): self-reported valuations
    # are generally preferable to purchase unit values (market_local via the
    # RULE-WLF-002 cascade, broadening to market_national); farm-gate is a
    # theoretical ideal, effectively never constructible, so demoted to last.
    # Survey circumstances may reverse this (esp. where non-purchased food
    # dominates -> more care + sensitivity analysis); default is a PROPOSAL only
    # (escalate: true still routes the choice to a human per RULE-WLF-001).
    options: [self_reported_value, market_local, market_national, farmgate]
    default: self_reported_value
    escalate: true
    governs: [VAR-consfood]
    consequence: "Shifts the welfare of agricultural / subsistence households materially."
  - switch_id: ration_valuation
    question: "At what price are free / subsidized food rations re-priced?"
    # Preference-ordered ladder (MV22 §4.2.5); official/subsidized price is
    # PROHIBITED and deliberately absent from the option set (see RULE-WLF-003).
    options: [secondary_market_unit_value, market_substitute_price, self_reported_wtp, expert_judgment]
    default: null
    escalate: true
    governs: [VAR-consfood]
    consequence: "Understating rations biases both welfare LEVELS and household RANKINGS (unless the ration is universal)."
  - switch_id: health_lumpy
    question: "How are large, infrequent health expenditures treated?"
    options: [include_full, smooth, winsorize, exclude_catastrophic]
    default: null
    escalate: true
    governs: [VAR-conshealth]
    consequence: "Catastrophic spending can dominate a household total and is conceptually ambiguous as welfare."
  - switch_id: spatial_deflation
    question: "Adjust nominal values for within-country price differences?"
    options: [none, regional_price_index, urban_rural, temporal_only]
    default: null
    escalate: true
    governs: [__pipeline__]
    consequence: "Changes the ranking of households across regions; drives who is counted poor."
  - switch_id: equivalence_scale
    question: "How is the household total converted to a per-person welfare measure?"
    options: [per_capita, oecd_modified, oecd_original, theta_parametric]
    default: per_capita
    escalate: false
    governs: [__pipeline__]
    consequence: "Safe GMD default is per_capita; record the choice regardless."
  - switch_id: outlier_handling
    question: "Treatment of implausible component values / unit-price outliers?"
    options: [flag_only, winsorize, trim, none]
    default: flag_only
    escalate: false
    governs: [__all_components__]

# --- Aggregate: construction pipeline (NEW BLOCK) ---
# Ordered. Each stage names the lookup and/or switch that governs it.
construction_pipeline:
  - stage: unit_standardization
    scope: item-level quantity components
    requires_lookup: PARAM-WLF-UNIT-CONVERSION
  - stage: recall_annualization
    scope: every component with a recall/diary period
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum components to household via roll_up_key"
  - stage: spatial_temporal_deflation
    governed_by: [spatial_deflation]
    requires_lookup: [PARAM-WLF-SPATIAL-PRICE-INDEX, PARAM-WLF-CPI-TEMPORAL]
  - stage: equivalence_scaling
    governed_by: [equivalence_scale]
    requires: [VAR-hhsize, VAR-adulteq]

# --- Aggregate: reconciliation / validation (NEW BLOCK) ---
reconciliation:
  internal:
    - "grand total == sum of component subtotals (no omission or double-count)"
    - "every household has a strictly positive, non-null welfare"
    - "where the survey also reports a total expenditure, |assembled − reported| within tolerance"
  distributional:
    - "food share (Engel) within a context-plausible band"
    - "no implausible zero/negative totals; flag unit-price outliers"
    - "per-capita distribution free of spikes that signal unit-conversion errors"
  external:
    - "reproduce the published poverty headcount within tolerance (LOAD-BEARING;
       while consfood is DEFERRED this WILL diverge — recorded as a determination,
       not a failure)"
    - "mean/median welfare vs national accounts or prior survey round"

# --- Cross-references ---
rules:
  - RULE-WLF-001            # methodological switch escalation gate
  - RULE-WLF-005            # zero-vs-missing distinction + item-nonresponse procedure (module-wide)
  - RULE-WLF-007            # outlier detect/treat/sensitivity (governs the outlier_handling switch)
  # Note: earlier a RULE-WLF-002 placeholder ("assembly & normalization order")
  # was listed here; that intent is covered by the construction_pipeline block.
  # Per the CLOSED task queue, RULE-WLF-002..007 are the six MV22-derived rules;
  # the food-specific ones (002 cascade, 003 rations, 004 recall, 006 acquisition)
  # live on VAR-consfood.
exceptions: []
external_standards:
  - name: "Mancini, Giulia & Vecchi, Giovanni (2022), On the Construction of a Consumption Aggregate for Inequality and Poverty Analysis, Washington, D.C.: World Bank Group — PRIMARY authority (MV22), successor to Deaton & Zaidi (2002). Key sections: §4.1 four criteria; §4.2 food (§4.2.1 acquisition, §4.2.2 recall, §4.2.4 own-production/unit-values, §4.2.5 rations); §7.2 missing/zero; §7.3 outliers; ch.8 sensitivity"
    url: "http://documents.worldbank.org/curated/en/099225003092220001"   # extracted text at extraction/sources/mancini-vecchi-2022.txt
  - name: "Deaton & Zaidi (2002), Guidelines for Constructing Consumption Aggregates — superseded canon, retained for lineage"
    url: "https://openknowledge.worldbank.org/handle/10986/14101"

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "expenditure"
    - "consumption"
    - "how much did your household spend"
    - "food consumed"
    - "own production"
    - "rent"
    - "imputed rent"
    - "diary"
  typical_section_names:
    - "Consumption"
    - "Expenditure"
    - "Household budget"
    - "Food diary"
    - "Non-food expenditure"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "TBD — welfare / consumption aggregate section (confirm with GPID Team)"
  extraction_method: manual
  extracted_on: "2026-07-01"
  human_reviewed: false
  reviewer: null
  notes: "PROPOSAL / schema extension. Introduces mapping_role: aggregate and
          the component_structure, methodological_switches, construction_pipeline,
          and reconciliation blocks (see docs/derived-indicators.md). Module code
          MOD-WLF, component variable names, and lookup-table IDs are placeholders
          pending alignment with GMD conventions and the guidelines source document.
          Per AGENTS.md, source document wins on any conflict."
---

## Definition

`welfare` is the household consumption aggregate used as the welfare proxy for
poverty and distributional analysis: total real consumption over a standard
annual reference period, assembled from component modules under a documented
methodology, then expressed per capita (or per adult equivalent). It is never a
single survey question; it is constructed.

## Conceptual intent

The aggregate exists to make households comparable in real welfare terms across
surveys and countries. Its value depends not only on what the survey collected
but on a small set of **methodological choices** that a GPID economist must own
— because those choices, not the raw data, decide where the poverty line falls
relative to the distribution. The schema's job is to make every such choice
explicit and reviewable rather than buried in a do-file.

## Temporary scope — food deferred (2026-08-31)

For now the welfare aggregate is assembled **without `VAR-consfood`**. Food
purchases and in-kind are the hardest components and get dedicated attention
later; deferring them lets the full process (spec-fill → validate → derive →
reconcile) be exercised on the breadth of the remaining components first. The
deferral is **temporary and reversible** — food's component record stands
unchanged; it is simply not assembled while `include: deferred`.

Consequences while food is deferred:

- The result is a **partial (food-excluded) welfare**, useful for process and
  coverage testing but **not poverty-valid** (food is the largest component).
- The load-bearing poverty-reproduction check is **retained but expected to
  diverge**; that divergence is recorded as a **determination**, not treated as
  a failure or an escalation.
- At the hspec level the deferral needs no new field: food is simply absent from
  `component_scope`; a component in `derived_from` but not in scope is deferred
  (a view). Lifting the deferral = adding food back to scope and restoring
  `include: always` here.

## Construction notes

**Path 0 (preferred when available): use a pre-computed aggregate that meets the
GMD definition.** If the survey (or the country poverty team) already provides a
consumption aggregate constructed to a standard consistent with GMD, validate it
against the reconciliation checks and use it directly, documenting its source and
the methodological choices it embodies. This mirrors `derived_preferred`: assemble
from components only when a valid aggregate is not already available.

**Path 1: assemble from components.** Construct each component variable
(`VAR-consfood`, …), then run `construction_pipeline` in order:

1. **Unit standardization** — convert item quantities to standard units via
   `PARAM-WLF-UNIT-CONVERSION` before any value is computed from quantity × price.
2. **Recall annualization** — scale each component to an annual figure using its
   recall/diary period.
3. **Component assembly** — sum components to the household via `hhid`. Include
   switch-governed components (`conshousing`, `consdurables`, `conshealth`)
   only according to their methodological switch.
4. **Spatial / temporal deflation** — apply within-country and survey-period
   deflation per the `spatial_deflation` switch and the price-index lookups.
5. **Equivalence scaling** — divide by `hhsize` (per_capita, the GMD default) or
   by `adulteq` if a different `equivalence_scale` is set.

**Methodological switches gate the construction.** Every switch with
`escalate: true` must have a value set by a human in the Harmonization
Specification before finalization. The agent proposes a value with justification
and **stops** — it never applies a silent default to imputed rent, durables,
own-production valuation, health treatment, or spatial deflation. See
`RULE-WLF-001`.

## Consistency checks

Run the `reconciliation` block. The **external comparison — reproducing the
published poverty headcount within tolerance — is load-bearing**: it is the only
check that can confirm a number that has no value domain. Internal reconciliation
catches omission and double-counting; it is **blind to misclassification** (an
item filed under the wrong component still sums correctly), so a clean total is
not evidence the components are clean.

## Escalation triggers

- Any `escalate: true` switch is unset in the Harmonization Spec.
- A required component cannot be constructed and no valid pre-computed aggregate
  is available → `welfare = .b`, escalate to TTL.
- The reproduced poverty headcount departs from the published figure beyond
  tolerance. (Suspended while `consfood` is deferred — the food-excluded
  partial is expected to diverge; the gap is recorded as a determination.)
- A required country parameter (price index, unit conversion) does not yet exist
  for the country — as with `PARAM-EDU-YEARS-BY-LEVEL`, this blocks the
  affected path until the value is supplied.

## Common mistakes

- **Silently including imputed rent, or valuing durables at acquisition.** These
  move the poverty number and must be explicit human choices, not defaults.
- **Skipping deflation** — comparing nominal welfare across regions or time.
- **Confusing per_capita and per_adult_equivalent** — record which scale was used.
- **Double-counting own production.** Own-produced food belongs in the
  consumption aggregate; it *also* legitimately appears in an income aggregate.
  That cross-aggregate overlap is correct — it is not double-counting. Counting
  it twice *within* consumption is.
- **Trusting a clean grand total** as proof the components are correctly
  classified. It is not (see Consistency checks).

## Note on source_coverage (advisory, deliberately not a hard check)

Whether the components partition the survey's expenditure space without overlap
is worth flagging but is **not** enforced as a constraint: "part of" is a
definitional choice, and overlap detection depends on data shape (in a
long-format expenditure file two components may share one value column,
separated only by a category filter). Treat any detected overlap as a warning to
review, not an error. Left open pending real examples.

## Change log

| Date       | Version | Change                          | Authority  |
|------------|---------|---------------------------------|------------|
| 2026-07-01 | 0.1     | Initial draft (schema extension proposal) | GPID Team  |
| 2026-08-31 | 0.1     | Temporarily defer consfood (include: deferred); welfare is a food-excluded partial for the full-process breadth test; poverty divergence recorded as a determination | Zurab |
