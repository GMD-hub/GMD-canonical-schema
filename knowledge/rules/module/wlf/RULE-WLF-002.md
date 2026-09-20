---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-WLF-002
rule_name: "Unit-value hierarchical cascade for pricing own-produced and in-kind food"
scope: module
module_id: MOD-WLF
applies_to_variables:
  - VAR-consfood
priority: 60
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-07-08"
effective_to: null

# This rule is a construction PROCEDURE (a convention), not a methodological
# switch. It is invoked only when the own_production_valuation switch
# (VAR-welfare) resolves to a unit-value-based option (market_local /
# market_national). It is never itself escalated; the cell-count fallback it
# fires is a determination (reported, not reviewed). See RULE-WLF-001 for the
# switch that selects the price CONCEPT; this rule fixes the price VALUE once a
# unit-value concept has been chosen.

---

## Plain language rule

Own-produced and in-kind food carry no market price, so their value must be
imputed from the price of the same item purchased on the market. When the
`own_production_valuation` switch has resolved to a unit-value-based option, the
price used is the **median unit value** of that item, computed over the
narrowest geographic cell that contains enough purchase transactions, and only
otherwise broadened. Unit value = amount paid ÷ quantity purchased. Use the
**median, not the mean** (robust to outliers). Start at the household's own
cluster (PSU); if that cell has fewer than the transaction threshold (~50), move
up one administrative level — subregion, then region, then national — stopping
at the first level whose cell meets the threshold. National is the guaranteed
terminal fallback.

This is a deterministic algorithm. The agent runs it; it is not a choice to
escalate. Each fallback that fires (a cell below threshold) is a **determination**
to record, not a decision to review.

## Formal IF/THEN

```
GIVEN: target household h, food item j, own-produced or in-kind quantity to price
PRECONDITION: own_production_valuation ∈ {market_local, market_national}
              (if == self_reported_value, this rule does NOT apply — use the
               respondent's stated valuation instead; see Prohibitions)

DEFINE uv(purchase) = amount_paid / quantity_purchased   # per purchase transaction
DEFINE threshold T = 50                                   # named parameter (convention)

# Cascade — first level whose cell has ≥ T transactions wins (eq. 4.1):

  IF   count(purchase transactions of j in h's PSU) >= T
  THEN price_hj = median( uv(purchase) | j, PSU(h) )

  ELSE IF count(... in h's subregion) >= T
  THEN price_hj = median( uv(purchase) | j, subregion(h) )

  ELSE IF count(... in h's region) >= T
  THEN price_hj = median( uv(purchase) | j, region(h) )

  ELSE
  THEN price_hj = median( uv(purchase) | j, national )    # terminal fallback

value_hj = standardized_quantity_hj * price_hj
```

The number of subnational levels is survey-dependent (eq. 4.1 illustrates three:
PSU / subregion / region). Use whatever "fine → coarse" administrative hierarchy
the dataset provides; national is always the last resort.

## Parameters

| Parameter | Default | Nature | Note |
|---|---|---|---|
| Transaction threshold `T` | 50 | convention (named) | MV22 says "some 50 or more"; adjustable per survey as a documented deviation, not an escalated switch |
| Central tendency | median | fixed | median, not mean — robustness to outliers is the stated reason |
| Geographic hierarchy | PSU → subregion → region → national | survey-shaped | use the finest units available; national is the terminal fallback |

## Determinations produced (report, do not review)

- The administrative **level at which each item's cell cleared the threshold**
  (e.g. "figs priced at subregion level; PSU cell had 12 transactions").
- Items that fell through **all the way to national** — a coverage signal.
- Cells that are thin even nationally (< T at national) — surface as a data
  determination; the national median is still used but flagged.

## Quality diagnostic (from the same section)

Plot the distribution of computed unit values, within clusters or regions, per
item. A unimodal, low-variance shape is reassuring. High variance signals
quality heterogeneity or outliers; **multimodality signals gross errors** —
misreported units of measurement (e.g. eggs in units vs. dozens, rice in kg vs.
bags) or distinct foods lumped under one item code. This feeds the `consfood`
`reconciliation.distributional` check: implied unit prices extreme vs. local
norms almost always mean a unit-conversion error, not a genuine outlier.

## Prohibitions

- Do not use the **mean** unit value; use the median.
- Do not skip levels or pick a level to hit a "nicer" price. The first level
  clearing the threshold wins, deterministically.
- Do not apply this cascade when `own_production_valuation` resolved to
  `self_reported_value` — self-reported valuations are added directly and, per
  MV22, are generally preferable where available (see the pending re-ordering of
  the switch options). Nor when it resolved to `farmgate` (a theoretical ideal
  MV22 treats as impractical; if ever selected it is its own procedure, not this
  one).
- Do not treat a fallback to a coarser level as an escalation or a switch. It is
  a determination — record it and proceed.
- Do not silence a below-threshold-at-national cell; use the national median but
  flag the thin coverage.
- Country-specific administrative-level definitions and any per-survey override
  of `T` are recorded per survey (Harmonization Spec / lookup-tables), never in
  `knowledge/`.

## Rationale

Foods a household consumes are best approximated by market transactions in its
vicinity, where similar-quality items trade — hence start narrow. But narrow
cells are thin and noisy, and thin cells produce wild imputed prices (the well
water valued at the price of a nearby Perrier bottle; the fallen mango valued at
capital-city supermarket prices). The threshold trades locality against
stability: stay local while the cell is dense enough to trust, broaden only when
it is not. The median guards each cell against its own outliers. Because every
step is mechanical and every fallback is logged, the imputation is reproducible
and auditable — which is exactly why it is a convention the agent executes, not a
choice a human must originate.

## Test examples

| Situation | Action |
|---|---|
| `own_production_valuation = market_local`, figs, PSU has 80 fig purchases | Price at PSU median unit value; record "level = PSU" |
| Same, PSU has 12 purchases, subregion has 140 | Fall through to subregion median; record determination "PSU cell < 50 → subregion" |
| Same, item never purchased below national level | Use national median; flag "national fallback" as a coverage determination |
| Item purchases show a bimodal unit-value distribution | Flag likely unit-of-measurement / lumped-code error before pricing; route to reconciliation |
| `own_production_valuation = self_reported_value` | This rule does not fire; add the household's stated valuation directly |
| `own_production_valuation` unset | Cascade cannot run; `RULE-WLF-001` blocks and escalates the switch first |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-07-08 | 0.1     | Initial draft from MV22 §4.2.4 eq. 4.1 (task-queue item 1) | GPID Team  |
