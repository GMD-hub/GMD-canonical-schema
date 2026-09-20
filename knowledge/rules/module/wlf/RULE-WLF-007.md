---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-WLF-007
rule_name: "Outlier detection, treatment, and mandatory sensitivity analysis"
scope: module
module_id: MOD-WLF
applies_to_variables:
  - VAR-welfare
  - VAR-consfood
  - VAR-consalcoholtobacco
  - VAR-consclothing
  - VAR-conscommunications
  - VAR-consdurables
  - VAR-conseducation
  - VAR-consfurnishings
  - VAR-conshealth
  - VAR-conshotelsrestaurants
  - VAR-conshousing
  - VAR-consmiscellaneous
  - VAR-consrecreation
  - VAR-constransport
priority: 65
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-07-08"
effective_to: null

# Governs the `outlier_handling` switch (VAR-welfare). Detection is a standing
# convention (always performed, objectively and with robust statistics).
# Treatment is the switch: default `flag_only` (detect + report, no alteration)
# is the safe GMD default and does not escalate; any alteration (winsorize /
# trim / impute) is a deliberate spec choice and REQUIRES sensitivity analysis.
# Outlier is not a synonym for error, and treatment is context- and
# statistic-specific — there is no universal rule, by design.

---

## Plain language rule

An outlier is a value that appears to deviate markedly from the bulk of the
data. It is **not a synonym for error** — an extreme value may be a genuine
observation, a real error, or genuine-but-not-influential. So handling proceeds
in **two separate steps**: **detection** (what counts as extreme here) and
**treatment** (what, if anything, to do about it). There is no single best rule
for all cases, by design.

**Detection is always performed**, and prefers **objective, documentable rules**
over undocumentable eyeballing. Because income/expenditure distributions are not
Normal and because the mean and standard deviation are themselves pulled by the
very outliers being sought, detection uses a **normalizing transformation**
(e.g. log or Box-Cox) and **robust location/scale** statistics (median; IQR or
MAD) — e.g. a z-score / three-sigma rule applied to the normalized, robustified
distribution, or percentile/boxplot flags.

**Treatment is the `outlier_handling` switch.** The GMD default is **`flag_only`**
— detect and report, alter nothing — which is safe because it moves no number.
Any actual alteration (`winsorize`, `trim`, impute) is a deliberate choice set
in the Harmonization Spec and **requires sensitivity analysis** (ch. 8) as its
audit. Which statistic is at stake matters: **poverty** headcounts (with an
exogenous line) are insensitive to the top tail, while **inequality** and
distributional rankings are extremely sensitive in both tails.

Gross-error checks (misreported units, lumped item codes) are a given and feed
detection — e.g. the multimodality check on unit values in `RULE-WLF-002`.

## Formal IF/THEN

```
STEP 1 — DETECTION (standing convention, always run):
  normalize X (log / Box-Cox so it is approximately Normal)
  compute detection region with ROBUST location/scale (median, IQR/MAD), e.g.
    flag x where |z-score| > 3 on the normalized, robustified distribution
  (percentile or boxplot rules are acceptable objective alternatives)
  PREFER an objective, pre-declared rule over case-by-case visual judgment,
  because the rule must be documentable and comparable across surveys.

STEP 2 — TREATMENT (the outlier_handling switch, VAR-welfare):
  value = flag_only  (DEFAULT) → record flags; alter nothing; no escalation
  value = winsorize | trim | impute → alteration:
        apply as specified in the Harmonization Spec
        AND run SENSITIVITY ANALYSIS on the affected statistics (esp. inequality
            and any relative poverty line) — mandatory, not optional
        AND document detection rule + treatment + before/after impact
  value = none → take no action at all (neither flag nor treat); record it

STATISTIC AWARENESS:
  poverty (exogenous line)  → insensitive to top outliers
  inequality / dominance    → highly sensitive in both tails → treatment here
                              moves the number; sensitivity analysis is the audit
```

## Determinations produced (report, do not review)

- The detection rule and transformation used, and counts flagged per tail.
- For any treatment: the before/after value of the affected statistics
  (Gini/headcount) — i.e. the sensitivity result.

## Prohibitions

- Do **not** equate "outlier" with "error" and drop extremes indiscriminately —
  detection is not automatic rejection.
- Do **not** apply a treatment beyond `flag_only` without it being set in the
  Harmonization Spec AND accompanied by sensitivity analysis.
- Do **not** detect with non-robust mean/SD on the raw (non-normalized)
  distribution — the mean/SD are contaminated by the outliers themselves.
- Do **not** use undocumentable visual "looks off" judgment as the recorded
  rule — objective, pre-declared criteria are preferred for comparability.
- Do **not** treat outliers in a way that silently changes cross-survey or
  cross-region comparability without documenting it.

## Rationale

Extreme values are everywhere and cannot be wished away, but the reflex to
"clean" them is itself a source of bias: over-editing discards genuine
information and, worse, quietly breaks comparability of inequality estimates
across space and time — the dimension most sensitive to the tails. Separating
detection from treatment makes the reasoning transparent: the analyst can always
*see* the extremes (detection is not in question) while deciding case by case
whether *acting* on them is warranted for the statistic at hand. `flag_only` is
the safe default because it surfaces the extremes without moving any number;
once a treatment does move numbers, sensitivity analysis is the only honest way
to show how much — which is why MV22 makes it the mandatory companion to any
treatment, not an afterthought.

## Test examples

| Situation | Action |
|---|---|
| Consumption distribution has a long right tail | Detect with log-normalized robust z-score; default `flag_only`; report flags |
| Spec sets `outlier_handling = winsorize` at p99 | Winsorize; run + record Gini/headcount sensitivity; document rule |
| Unit-value distribution for an item is multimodal | Gross-error signal (units/lumped codes) via RULE-WLF-002; fix before treating |
| A top value is extreme but genuine, poverty is the only target | May leave as-is (poverty insensitive to top tail); record the reasoning |
| Analyst wants to eyeball-drop the top 10 households | Prohibited as an undocumented rule; use an objective criterion + sensitivity |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-07-08 | 0.1     | Initial draft from MV22 §7.3 (task-queue item 1) | GPID Team  |
