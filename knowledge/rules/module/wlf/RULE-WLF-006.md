---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-WLF-006
rule_name: "Acquisition-as-proxy acceptance and bulk-purchase scrutiny"
scope: module
module_id: MOD-WLF
applies_to_variables:
  - VAR-consfood
priority: 55
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-07-08"
effective_to: null

# Consumption is the target in principle, but the questionnaire almost always
# dictates the basis, so this is a convention + determination, not an escalating
# switch. Acquisition-based aggregates are ACCEPTED practice (not a deviation to
# justify). The only per-survey judgment — preferring consumption when a survey
# genuinely records both — is rare and clear-cut. The standing obligation when
# acquisition-based is to scrutinize bulk purchases via the outlier framework
# (RULE-WLF-007).

---

## Plain language rule

In principle the aggregate should hold food **consumed**, not food **acquired**
(the relevance criterion — welfare comes from eating food, not buying it). In
practice the questionnaire dictates: most surveys record acquisition (purchases)
for market food and consumption only for own-production/transfers, with no
overlap, and a large share record acquisition alone. **Acquisition-based food
aggregates are accepted practice** — using one is not a deviation requiring an
exception file.

When a survey genuinely records **both** amount acquired and amount consumed for
the same items (a small minority), **prefer consumption**. When it records only
acquisition, use it, record the basis, and apply the standing mitigation:
**scrutinize extreme values and large bulk purchases**, excluding or imputing
them where warranted, using the outlier detection-and-treatment framework
(`RULE-WLF-007`).

## Formal IF/THEN

```
DETERMINE the basis the survey provides, per item / module:

  IF   both "acquired" and "consumed" are recorded for the same items
  THEN use CONSUMED (relevance criterion); record basis = consumption.

  ELSE IF only acquisition is recorded
  THEN use ACQUISITION; record basis = acquisition (accepted proxy, no
       exception file required)
       AND apply bulk-purchase scrutiny:
         flag extreme food-expenditure / implied-quantity values and likely
         bulk purchases via RULE-WLF-007; exclude or impute where warranted;
         record each such action as a determination.

  ELSE (mixed across modules — e.g. acquisition for purchases, consumption for
        own-production)
  THEN use each module's available basis; record the mixed basis as a
       determination; the aggregate is acquisition-partly-based (typical case).
```

## Determinations produced (report, do not review)

- The basis actually used per module (consumption / acquisition / mixed).
- Bulk purchases or extreme acquisition values flagged, and whether each was
  kept, excluded, or imputed.

## Prohibitions

- Do **not** treat an acquisition-based aggregate as an error or write an
  exception file for it — it is accepted practice dictated by the instrument.
- Do **not** silently let large bulk purchases inflate an acquisition-based food
  aggregate — scrutinize them via the outlier framework.
- Do **not** choose acquisition when the survey genuinely offers a clean
  consumption measure for the same items — consumption wins on relevance.
- Do **not** attempt a stock-adjustment correction to convert acquisition into
  consumption unless the instrument supports it — the accepted mitigation is
  extreme-value scrutiny, not a synthetic conversion.

## Rationale

The theoretical target (consumption) and the practical datum (acquisition)
usually differ only modestly: most food is perishable and consumed at high
frequency, households smooth consumption, and stock-driven gaps tend to be
randomly distributed so population means of the two stay close (empirically a
few to ~14 percent on calories). The systematic residual risk is **bulk
purchasing** — a household stocking up in the recall window looks far richer than
it eats — which is concentrated, not random, and is exactly what the outlier
framework is built to catch. So MV22 ratifies the proxy while pinning the one
mitigation that matters, rather than pretending the analyst has a choice the
questionnaire has already made.

## Test examples

| Situation | Action |
|---|---|
| Survey records purchases only | Use acquisition; record basis; run bulk-purchase scrutiny — no exception file |
| Survey records both acquired and consumed for food items | Use consumed (relevance); record basis = consumption |
| Purchases as acquisition, own-production as consumption (no overlap) | Use each as given; record mixed basis (typical) |
| A household reports a huge one-off rice purchase in the recall window | Flag as likely bulk purchase via RULE-WLF-007; exclude/impute; record determination |
| Analyst tempted to file an exception because the aggregate is acquisition-based | Do not — acquisition is accepted; only document the basis |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-07-08 | 0.1     | Initial draft from MV22 §4.2.1 (task-queue item 1) | GPID Team  |
