---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-WLF-004
rule_name: "Reference period: short-recall preference and usual-month deprecation"
scope: module
module_id: MOD-WLF
applies_to_variables:
  - VAR-consfood
  - VAR-consalcoholtobacco
  - VAR-consclothing
  - VAR-conscommunications
  - VAR-conseducation
  - VAR-consfurnishings
  - VAR-conshealth
  - VAR-conshotelsrestaurants
  - VAR-conshousing
  - VAR-consmiscellaneous
  - VAR-consrecreation
  - VAR-constransport
priority: 55
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-07-08"
effective_to: null

# Reference-period guidance is stated for food (§4.2.2) but the principle
# generalizes to any recall-collected component. It is largely a convention +
# prohibition, not an escalating switch: the "usual month" recall is deprecated
# outright, and short recall is the standing preference. The only residual
# choice — picking among genuinely competing estimates — is now rare and, when
# live and material, is surfaced as a decision-log escalation rather than a
# standing switch.

---

## Plain language rule

Food (and any recall-collected component) is valued over a reference period and
scaled to annual terms. The **"usual month" recall approach is deprecated** —
experimental evidence finds it no better, often worse, and more burdensome than
simple short recall, and the standing methodological conclusion is that it should
not be used. **Prefer short recall** (7- or 14-day), relying on a survey design
that spreads fieldwork across the year and seasons (or revisits households in
different seasons) to handle seasonality.

Seasonality is a **design-side** remedy, not an analyst-side correction: where a
survey is single-season, no synthetic seasonal adjustment is invented — the
limitation is recorded as a determination.

Two competing estimates for the same items (the old two-recall LSMS design) are
now rare. Where they genuinely coexist, choose the estimate likely most accurate
for **annual consumption of each household** (not on average) — but never select
the usual-month estimate over a short-recall alternative.

## Formal IF/THEN

```
ANNUALIZE: every recall item value is scaled by 365 / recall_days (convention,
           §4.2; already staged in consfood.construction_pipeline).

REFERENCE-PERIOD SELECTION:

  IF   the survey offers a single recall period
  THEN use it; if it is a "usual month" instrument, record the determination
       "usual-month recall (deprecated) — only instrument available" and flag
       the known downward-bias risk. Do NOT fabricate a correction.

  ELSE IF two competing estimates exist for the same items
  THEN  IF one is short recall and the other is usual month
        THEN use the SHORT-RECALL estimate (usual month is prohibited as the
             choice when an alternative exists)
        ELSE choose the estimate likely most accurate for each household's
             ANNUAL consumption; if the choice is material and not clear-cut,
             raise it in the decision log (cannot_determine) and escalate
             per RULE-WLF-001's stop-and-escalate posture.

SEASONALITY:
  Single-season fieldwork ⇒ report as a determination; invent no adjustment.
```

## Determinations produced (report, do not review)

- The recall instrument(s) present and the recall window(s) in days.
- Whether the only instrument is a deprecated usual-month recall (bias flag).
- Whether fieldwork is single-season (seasonality caveat).

## Prohibitions

- Do **not** prefer or select a usual-month estimate when a short-recall
  alternative exists.
- Do **not** invent a seasonal-adjustment correction where the survey is
  single-season — seasonality is handled by design, and its absence is a
  reported limitation, not a gap to fill.
- Do **not** silently resolve a material competing-estimate choice — surface it.
- Do **not** mix recall windows across food sub-parts without annualizing each
  to a common annual basis first (see consfood construction pipeline;
  mixed-window mechanics are a script-harvest silence).

## Rationale

The usual-month design was meant to stretch the reference period to a year (to
beat seasonality) while keeping the recall short (to stay feasible). Experimental
work since the guidelines shows it fails on its own terms — it underestimates
food consumption relative to a supervised diary, carries the highest respondent
burden, and respondents tend to answer for the most recent rather than a "usual"
month, nullifying the seasonality advantage. Because the number moves and the
evidence is one-directional, this is a hard convention (a deprecation), not a
per-survey judgment. Seasonality is pushed back to survey design precisely
because no defensible analyst-side correction exists for a single-season sample.

## Test examples

| Situation | Action |
|---|---|
| Survey uses a 7-day food recall | Use it; annualize ×(365/7); no flag |
| Only instrument is a usual-month recall | Use it (no alternative), flag deprecated + downward-bias determination |
| Both 14-day and usual-month collected | Use the 14-day estimate; record usual-month as discarded per deprecation |
| Two short-recall estimates differ materially | Pick the one likelier accurate per household-year; if unclear, escalate via decision log |
| Fieldwork ran only in the harvest season | Record single-season determination; invent no seasonal correction |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-07-08 | 0.1     | Initial draft from MV22 §4.2.2 (task-queue item 1) | GPID Team  |
