---
# ================================================================
# DECISION RULE — GMD Canonical Variable Schema v0.1
# ================================================================

rule_id: RULE-WLF-001
rule_name: "Methodological switch resolution and escalation gate"
scope: module
module_id: MOD-WLF
applies_to_variables:
  - VAR-welfare
  - VAR-consfood
  - VAR-conshousing
  - VAR-consdurables
  - VAR-conshealth
priority: 95
version: "0.1"
status: draft
authority: "GPID Team"
effective_from: "2026-07-01"
effective_to: null
---

## Plain language rule

The welfare aggregate is governed by methodological choices that move the
poverty number. Each such choice is a `methodological_switches` entry on the
variable record. A switch marked `escalate: true` must have its value set by a
GPID economist in the Harmonization Specification before the aggregate is
finalized. The agent may **propose** a value with justification, but must
**stop and escalate** — it must never apply a silent default to an escalating
switch. Switches with a safe default (`escalate: false`) may proceed, but the
value used must be recorded in the Harmonization Specification.

## Formal IF/THEN

```
FOR each switch S in the variable's methodological_switches:

  IF   S.escalate == true AND S has no value set by a human in the
       Harmonization Specification
  THEN the agent proposes S = <option> with a written justification
       AND sets the Harmonization Specification status to BLOCKED
       AND escalates to TTL
       AND does NOT finalize the aggregate
       (never apply S.default in this case, even if one exists)

  ELSE IF   S.escalate == false AND S has no value set
  THEN      apply S.default
            AND record "S = default (<value>)" in the Harmonization Specification

  ELSE  (S has a human-set value)
  THEN  use it AND record "S = <value>, set_by human" with justification
```

## Prohibitions

- Do not apply a default to any switch with `escalate: true`. An unset
  escalating switch blocks finalization.
- Do not finalize a welfare aggregate while any escalating switch is unset.
- Do not overwrite a human-set switch value.
- Do not record a switch value only in a do-file. Every methodological choice
  must appear in the Harmonization Specification, which is the audit record.
- Country-specific parameter values implied by a switch (price indices,
  equivalence constants) belong in `lookup-tables/`, never in `knowledge/`.

## Rationale

For an atomic variable, a wrong value fails an allowed-values check and is
caught. For the welfare aggregate, a wrong methodological choice — silently
including imputed rent, valuing durables at acquisition, choosing a valuation
price for own production — produces a defensible-looking number that is simply
wrong for poverty measurement, and nothing downstream flags it. Because the
error is invisible and load-bearing, the safe default is to surface the choice
to a human rather than guess. This is the aggregate analogue of the guidelines'
standing instruction never to guestimate.

## Test examples

| Situation | Action |
|---|---|
| `imputed_rent` unset in Harmonization Spec | Propose a method + justification; BLOCK; escalate to TTL |
| `own_production_valuation` unset, subsistence survey | Propose (e.g. market_local) + justification; BLOCK; escalate |
| `equivalence_scale` unset | Apply default `per_capita`; record it; proceed |
| `imputed_rent = user_cost` set by economist | Use it; record "set_by human" with justification |
| `durables_treatment` unset | Do NOT apply `use_value_flow` silently; propose it; BLOCK; escalate |

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-07-01 | 0.1     | Initial draft | GPID Team  |
