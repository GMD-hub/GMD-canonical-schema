---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-WLF-EQUIVALENCE-SCALE
parameter_name: "Adult-equivalence scale constants (alpha, theta)"
module_id: MOD-WLF
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
# DEMONSTRATION ARTIFACT (fails validation on purpose — see the "Why this record
# does not validate yet" section). The ONLY non-conformance is value_schema:
# alpha/theta are floats, but the current model allows dict[str, Literal["integer"]].
kind: construction
value_type: mapping
value_schema:
  alpha: number          # weight of a child relative to an adult (0..1) — FLOAT
  theta: number          # economies-of-scale elasticity (0..1)            — FLOAT

# --- Where it is used ---
applies_to_variables:
  - VAR-welfare

# --- Behavior when no country record exists ---
fallback_policy: undecided
global_default: null

# --- Provenance ---
provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  extraction_method: manual
  extracted_on: "2026-09-01"
  human_reviewed: false
  reviewer: null
  notes: "DEMONSTRATION. Deliberately non-conforming, the parameter-side parallel
          of the mapping_role: aggregate variable records: value_schema uses the
          float type `number`, which the current ParameterDefinition rejects
          (integer only). Shows the value_type extension welfare needs. MV22 §6,
          eq. 6.1 ES = (A + alpha*K)^theta."
---

## Definition

Defines the two constants of the parametric adult-equivalence scale used when
converting the household consumption total to a per-adult-equivalent welfare
measure: `alpha`, the weight given to a child relative to an adult, and `theta`,
the degree of economies of scale within the household. Under MV22 (§6, eq. 6.1)
the scale is `ES = (A + alpha * K)^theta`, where `A` is the number of adults and
`K` the number of children.

## Why this is country specific

The defensible values of `alpha` and `theta` reflect country- and context-
specific consumption patterns and household-composition norms. The universal
definition and value shape stay stable, while each governed country record
supplies the applicable constants for a validity window. Per capita
(`alpha = 1`, `theta = 1`) remains the GMD default, so this parameter is
consulted only when the `equivalence_scale` switch selects a non-per-capita
scale.

## How the agent uses it

The agent always loads the folder matching the survey ISO3 code, selects the one
record whose inclusive validity window contains the survey ID year (the calendar
year in which fieldwork began), and applies the constants in the
equivalence-scaling stage of `VAR-welfare`'s construction pipeline.

## Why this record does not validate yet (the point)

This file is intentionally non-conforming — the parameter-side counterpart of the
`mapping_role: aggregate` variable records that already fail against the current
variable model. Its `value_schema` declares `alpha` and `theta` as `number`
(floating point), but `ParameterDefinition.value_schema` is typed
`dict[str, Literal["integer"]]`, so validation fails on `value_schema`.

The failure is the message. Welfare's country parameters are inherently
fractional — equivalence-scale `alpha`/`theta` in `0..1`, unit-conversion factors,
spatial/temporal price indices — so the parameter model needs a
float `number` value type (and, for unit conversion and price indices, an
open-keyed float *table* rather than a fixed small mapping). Until that extension
lands, the `PARAM-WLF-…` records are declared by ID on the variable specs
(`country_parameters`) but cannot be created validly. This one file makes that
need concrete.

## Fallback behavior

The fallback policy is not yet decided. Until the GPID Team selects one, the
validator flags this parameter and harmonization must stop when a valid country
record is missing. Candidate policies mirror those on `PARAM-EDU-YEARS-BY-LEVEL`
(`use_global_default`, `block_and_escalate`, or an approved coverage
requirement); `skip_check` is not a candidate because this is a construction
parameter.

## Data sources for populating values

MV22 §6 (equivalence scales) is the primary methodological source; the
OECD-modified and OECD-original scales supply reference `alpha`/`theta` values.
Every country value requires human verification before use.

## Change log

| Date | Version | Change | Authority |
|---|---|---|---|
| 2026-09-01 | 0.1 | Initial draft — demonstration of the parameter value_type need | GPID Team |
