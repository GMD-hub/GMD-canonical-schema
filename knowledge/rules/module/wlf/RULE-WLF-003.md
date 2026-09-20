---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-WLF-003
rule_name: "Food-ration re-pricing: preference ladder and official-price prohibition"
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

# This rule governs the `ration_valuation` methodological switch (VAR-welfare).
# The rung of the ladder is a switch (escalate: true) because rung viability
# requires human judgment (substitute closeness, self-report trust) and the
# choice moves the poverty number. The agent runs the ladder, PROPOSES the
# highest viable rung, and escalates per RULE-WLF-001. This rule also carries a
# hard, non-escalable prohibition: official/subsidized ration prices are never
# used. Once a rung selecting a unit-value concept is chosen, the geographic
# imputation still follows the cascade in RULE-WLF-002.

---

## Plain language rule

Food rations — food quotas given free or at a mandated below-market price — are
an in-kind transfer whose recorded (paid or subsidized) value understates the
welfare the household actually derives. They must be **re-priced** at a value
representing the benefit of consuming them, in accordance with the valuation
criterion, and added to `consfood`. Never leave a free ration at zero, and
never value a ration at its official/subsidized price.

The price concept is chosen from a **five-rung preference ladder**, in order:

1. **Secondary-market unit value** — median unit value from resales of the
   ration item, *conditional on* a secondary market existing and enough recorded
   resale transactions.
2. **Market price of a close substitute** — the market price of a
   market-traded variety close enough to the ration item.
3. **Self-reported willingness-to-pay** — the household's stated amount it would
   pay for a ration-equivalent item on the market, where the questionnaire asks.
4. **Expert judgment** — last resort (e.g. national median of prices reported by
   local ration agents, akin to a price survey).

Below all four sits a **prohibited** route — official/subsidized prices — which
is not a rung and is never selected.

The chosen rung is the `ration_valuation` switch (`escalate: true`). The agent
proposes the **highest viable rung** with justification and escalates via
`RULE-WLF-001`; it does not silently apply one.

## Formal IF/THEN

```
PRECONDITION: the food module contains ration items to be valued.

# Assess viability of each rung top-down; PROPOSE the highest viable rung.

  RUNG 1  secondary_market_unit_value
          VIABLE iff a secondary/resale market exists
                 AND recorded resale transactions are numerous enough to
                     compute a reliable unit value (determination: transaction
                     count; thin ⇒ not viable — cf. Iraq, <2% report rice resale)
          If chosen, price = median unit value of resales, imputed by the
          RULE-WLF-002 geographic cascade.

  RUNG 2  market_substitute_price
          VIABLE iff a market-traded item is a close enough substitute for the
          ration item (judgment: quality/kind gap small)

  RUNG 3  self_reported_wtp
          VIABLE iff the questionnaire elicits ration-equivalent WTP
          (caution: thin secondary markets ⇒ high nonresponse + inaccurate
          answers; weigh reliability)

  RUNG 4  expert_judgment                              # last resort
          e.g. national median of ration-agent-reported prices

  FORBIDDEN  official_subsidized_price
          NEVER used, at any rung, even if convenient — it suppresses the
          ration's value. Not part of the switch's option set.

THEN  propose ration_valuation = <highest viable rung> + justification
      AND escalate per RULE-WLF-001 (BLOCK finalization until a human sets it)
```

## Determinations produced (report, do not review)

- Whether a secondary market for ration items exists, and its recorded resale
  **transaction count** (the objective gate on rung 1).
- Item-nonresponse rate on any WTP question (bears on rung 3 reliability).
- The rung actually proposed, and why higher rungs were judged not viable.

## Prohibitions

- Do **not** value rations at official or subsidized prices — the explicitly
  non-advisable route. It is not a selectable rung.
- Do **not** leave a free ration recorded at zero, or a subsidized ration at the
  amount paid — both understate welfare and (unless the ration is universal)
  corrupt household rankings.
- Do **not** silently pick a rung. The rung is an escalating switch; propose and
  escalate per `RULE-WLF-001`.
- Do **not** skip to a lower rung to avoid work when a higher rung is viable; the
  ladder is preference-ordered.
- Country-specific ration bundles, substitute mappings, and ration-agent price
  tables belong in `lookup-tables/`, never in `knowledge/`.

## Rationale

Leaving a ration at its paid value makes two errors. First the **level** is
wrong: a household lifted past the food poverty line by a free ration shows no
improvement, because the recorded value is zero. Second the **ranking** is
wrong: two households eating an identical diet — one via ration, one via market
purchase — are not ranked equally well-off, and the ration household looks
poorer. Official prices fail for the same reason in reverse: being subsidized,
they artificially suppress the ration's welfare value. The ladder exists because
the ideal price (a thick secondary market) is often unavailable, so the analyst
descends to progressively more approximate but still defensible proxies — a
choice that moves the poverty number and therefore escalates.

## Test examples

| Situation | Action |
|---|---|
| Thick secondary resale market, many transactions | Propose `secondary_market_unit_value`; price via RULE-WLF-002 cascade; escalate |
| Iraq-type case: <2% resell the main ration item | Rung 1 not viable; assess substitute (rung 2), else propose `expert_judgment` (national median of ration-agent prices); escalate |
| Ration rice ≈ a market rice variety | Propose `market_substitute_price` with the substitute named; escalate |
| WTP question present but secondary market thin | Flag likely nonresponse/inaccuracy; use rung 3 only if higher rungs fail; escalate |
| Analyst tempted to use the subsidized shop price | Prohibited — reject; drop to the ladder |
| Free ration left at value 0 in raw data | Defect — re-price via the ladder; never keep the zero |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-07-08 | 0.1     | Initial draft from MV22 §4.2.5 (task-queue item 1) | GPID Team  |
