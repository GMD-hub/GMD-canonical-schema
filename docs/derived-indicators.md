# Derived indicators: extending the CVS to the welfare aggregate

*This note proposes the smallest set of additions that let the existing CVS
hold a welfare/consumption aggregate. It is written to extend the current
schema, not fork it: every atomic/derived record stays valid unchanged, and
the new fields are used only by records with `mapping_role: aggregate`.*

## Why the existing record shape needs an extension

The current schema handles `atomic`, `derived`, and `derived_preferred`
variables — all resolved **within one row of one unit of analysis** (map or
recode a person-level or household-level value). The welfare aggregate is a
different kind of object:

- it is **assembled across units of analysis** — item-level diary/recall rows
  and person-level values roll up to one household number;
- it is governed by **methodological choices that move the poverty number**
  (imputed rent, durables treatment, own-production valuation, deflation,
  equivalence scale) — contestable decisions a researcher must own, not
  mapping rules;
- it has **no value domain to validate against** — a positive continuous
  number — so it is checked by reconciliation and by reproducing the known
  poverty rate, not by membership in a code list.

None of this fits `value_codes` + `derived_from` + a recode. Hence a fourth
`mapping_role` and four aggregate-only field blocks.

## The schema delta

**One new `mapping_role` value:** `aggregate` — computed by assembling
component variables across units of analysis under an explicit methodology.
(`schema/` Pydantic enum gains one member; the three existing roles are
unchanged.)

**Four aggregate-only blocks** (ignored by non-aggregate records):

| Block | What it holds | Why it can't reuse an existing field |
|---|---|---|
| `component_structure` | the components summed into the total, each with its native unit of analysis and roll-up key | `derived_from` gives identity but not assembly semantics or unit-of-analysis change |
| `methodological_switches` | the contestable, result-moving choices: id, options, default, `escalate` flag, what each governs | no existing field distinguishes a methodological choice from a mapping rule |
| `construction_pipeline` | the ordered normalization stages (unit standardization → recall annualization → assembly → deflation → equivalence scaling), each naming the lookup table and/or switch that governs it | construction prose alone isn't machine-checkable for order/dependencies |
| `reconciliation` | the aggregate validation: internal reconciliation, distributional sanity, external comparison to published figures | `consistency checks` prose exists but aggregates need structured, load-bearing checks |

Aggregate records declare their country parameters with the existing
`country_parameters: [PARAM-…]` field. The `PARAM-WLF-…` IDs they list are
**placeholders**: only some are genuine parameters — others are table lookups or
external data, split out in the extension asks below (Part A / Part B).

## How this respects AGENTS.md (universal / country / per-survey)

The extension deliberately reuses your three-way separation, so no
country-specific or per-survey content enters `knowledge/`:

- **Switch *definitions* are universal** → they live in the CVS record
  (`methodological_switches`): the *question*, the allowed *options*, the
  *default*, and whether it must escalate. This is stable GMD-wide.
- **Switch *values* are per-survey** → the chosen option for a given survey
  is recorded in Schema 3 (the Harmonization Specification), never here.
  This is the switch / switch-value split, and it is exactly your
  CVS / Harmonization-Spec split.
- **Parameters are country-specific** → genuine parameters (e.g. the
  equivalence-scale constants) are referenced by ID (`country_parameters:
  [PARAM-…]`); definitions live in `knowledge/parameters/` and per-country values
  in `country-parameters/`, like the existing `PARAM-EDU-YEARS-BY-LEVEL`. Country
  lookup *tables* and external data (price indices) need the Part B homes and
  are only placeholdered for now.

So the aggregate record stays universal and reviewable, and the parts that
vary by country or survey stay where AGENTS.md already requires them.

## Escalation is the point, not a footnote

For an atomic variable a wrong guess is visible (an out-of-range code fails
validation). For the welfare aggregate a wrong methodological choice is
**invisible and load-bearing**: silently including imputed rent, or valuing
durables at acquisition, produces a defensible-looking number that is simply
wrong for poverty. So any `methodological_switches` entry with
`escalate: true` and no human-set value in the Harmonization Spec **blocks
finalization** — the agent proposes and justifies, and waits for the TTL.
This is encoded as `RULE-WLF-001`.

## Artifacts in this proposal

**Variable records** (`knowledge/variables/wlf/`, all `mapping_role: aggregate`):

| File | Purpose |
|---|---|
| `VAR-welfare.md` | top-level welfare aggregate (worked example of `mapping_role: aggregate`; holds the methodological switches, construction pipeline, reconciliation) |
| `VAR-consfood.md` | food component — the deepest record; item-level quantity × price, unit standardization, own-production & ration valuation |
| `VAR-consalcoholtobacco.md` | alcohol, tobacco, narcotics component |
| `VAR-consclothing.md` | clothing and footwear component |
| `VAR-conshousing.md` | housing services component (`imputed_rent` switch) |
| `VAR-consfurnishings.md` | furnishings and household-equipment component |
| `VAR-conshealth.md` | health expenditure component (`health_lumpy` switch) |
| `VAR-constransport.md` | transport operations and services component |
| `VAR-conscommunications.md` | communications / information services component |
| `VAR-consrecreation.md` | recreation and culture component |
| `VAR-conseducation.md` | education expenditure component |
| `VAR-conshotelsrestaurants.md` | restaurants and accommodation component |
| `VAR-consmiscellaneous.md` | personal care / miscellaneous component |
| `VAR-consdurables.md` | durables component (`durables_treatment` switch) |

**Decision rules** (`knowledge/rules/module/wlf/`):

| File | Purpose |
|---|---|
| `RULE-WLF-001.md` | methodological-switch escalation gate |
| `RULE-WLF-002.md` | unit-value hierarchical cascade (own-produced / in-kind food pricing) |
| `RULE-WLF-003.md` | food-ration re-pricing ladder + official-price prohibition |
| `RULE-WLF-004.md` | reference period: short-recall preference, usual-month deprecation |
| `RULE-WLF-005.md` | zero-vs-missing distinction + item-nonresponse procedure |
| `RULE-WLF-006.md` | acquisition-as-proxy acceptance + bulk-purchase scrutiny |
| `RULE-WLF-007.md` | outlier detection, treatment, and mandatory sensitivity analysis |

**Parameter records** (`knowledge/parameters/`):

| File | Purpose |
|---|---|
| `PARAM-WLF-EQUIVALENCE-SCALE.md` | one **demonstration** parameter record — deliberately fails validation (float `value_schema`) to evidence the parameter `value_type` extension welfare needs, the parameter-side parallel of the `mapping_role: aggregate` records |

**Design note:** `docs/derived-indicators.md` (this file).

## Index additions (for `knowledge/index.md`)

```
## Variable specifications
| VAR-welfare                | Household welfare aggregate (consumption)                                | MOD-WLF | variables/wlf/VAR-welfare.md                | draft | 0.1 |
| VAR-consfood              | Household food consumption component                                    | MOD-WLF | variables/wlf/VAR-consfood.md              | draft | 0.1 |
| VAR-consalcoholtobacco    | Household alcohol and tobacco consumption component                     | MOD-WLF | variables/wlf/VAR-consalcoholtobacco.md    | draft | 0.1 |
| VAR-consclothing          | Household clothing and footwear consumption component                   | MOD-WLF | variables/wlf/VAR-consclothing.md          | draft | 0.1 |
| VAR-conshousing           | Household housing services consumption component                        | MOD-WLF | variables/wlf/VAR-conshousing.md           | draft | 0.1 |
| VAR-consfurnishings       | Household furnishings and household-equipment consumption component      | MOD-WLF | variables/wlf/VAR-consfurnishings.md       | draft | 0.1 |
| VAR-conshealth            | Household health expenditure component                                  | MOD-WLF | variables/wlf/VAR-conshealth.md            | draft | 0.1 |
| VAR-constransport         | Household transport consumption component                               | MOD-WLF | variables/wlf/VAR-constransport.md         | draft | 0.1 |
| VAR-conscommunications    | Household communications and information services consumption component  | MOD-WLF | variables/wlf/VAR-conscommunications.md    | draft | 0.1 |
| VAR-consrecreation        | Household recreation and culture consumption component                  | MOD-WLF | variables/wlf/VAR-consrecreation.md        | draft | 0.1 |
| VAR-conseducation         | Household education expenditure component                               | MOD-WLF | variables/wlf/VAR-conseducation.md         | draft | 0.1 |
| VAR-conshotelsrestaurants | Household hotels and restaurants consumption component                  | MOD-WLF | variables/wlf/VAR-conshotelsrestaurants.md | draft | 0.1 |
| VAR-consmiscellaneous     | Household miscellaneous goods and services consumption component         | MOD-WLF | variables/wlf/VAR-consmiscellaneous.md     | draft | 0.1 |
| VAR-consdurables          | Household durables consumption component                                | MOD-WLF | variables/wlf/VAR-consdurables.md          | draft | 0.1 |

## Decision rules
| RULE-WLF-001 | Methodological switch resolution and escalation gate                      | module | MOD-WLF | rules/module/wlf/RULE-WLF-001.md | draft | 0.1 |
| RULE-WLF-002 | Unit-value hierarchical cascade for pricing own-produced and in-kind food | module | MOD-WLF | rules/module/wlf/RULE-WLF-002.md | draft | 0.1 |
| RULE-WLF-003 | Food-ration re-pricing: preference ladder and official-price prohibition  | module | MOD-WLF | rules/module/wlf/RULE-WLF-003.md | draft | 0.1 |
| RULE-WLF-004 | Reference period: short-recall preference and usual-month deprecation     | module | MOD-WLF | rules/module/wlf/RULE-WLF-004.md | draft | 0.1 |
| RULE-WLF-005 | Zero-vs-missing distinction and item-nonresponse procedure                | module | MOD-WLF | rules/module/wlf/RULE-WLF-005.md | draft | 0.1 |
| RULE-WLF-006 | Acquisition-as-proxy acceptance and bulk-purchase scrutiny                | module | MOD-WLF | rules/module/wlf/RULE-WLF-006.md | draft | 0.1 |
| RULE-WLF-007 | Outlier detection, treatment, and mandatory sensitivity analysis          | module | MOD-WLF | rules/module/wlf/RULE-WLF-007.md | draft | 0.1 |
```

## Referenced external variables (owned by the main schema, not added here)

`VAR-welfare` intentionally references variables that belong to the broader GMD
schema and are **not** defined in this proposal. They are listed here so a
first-time reviewer does not read them as missing artifacts:

| Referenced ID | Where | Role | Disposition |
|---|---|---|---|
| `VAR-hhsize` | `prerequisites`, `construction_pipeline` (equivalence scaling) | household size for per-capita scaling | expected in the core schema (demographic) |
| `VAR-adulteq` | `prerequisites`, `construction_pipeline` | adult-equivalent scale, only if `equivalence_scale != per_capita` | to be defined when equivalence scales are added |

These are annotations only — none is required for the aggregate records to be
reviewed. When the reference-resolver runs, treat them as `allow_unresolved_draft`
(or stub them in the core schema), not as errors.

Of the `PARAM-WLF-…` IDs the welfare records mention, only
`PARAM-WLF-EQUIVALENCE-SCALE` is a genuine parameter and is declared in
`country_parameters` (with a record). The rest are **not parameters** — they are
the lookup table and external-data dependencies below, referenced only
descriptively in the construction pipeline until Part B gives them a home:

| Referenced ID | On | What it is | Where it belongs |
|---|---|---|---|
| `PARAM-WLF-EQUIVALENCE-SCALE` | `VAR-welfare` | α / θ scale constants (authored keys) | **parameter** — ask A2 (example drafted) |
| `PARAM-WLF-UNIT-CONVERSION` | `VAR-consfood` | local-unit → standard-unit table (data keys) | country lookup **table** — direction B1 |
| `PARAM-WLF-SPATIAL-PRICE-INDEX` | `VAR-welfare` | within-country price deflator | external data *or* recomputed — direction B2 |
| `PARAM-WLF-CPI-TEMPORAL` | `VAR-welfare` | official temporal price series | **external data** — direction B2 |

## Extension asks for the team

Two kinds, deliberately separated.

**Part A — concrete proposals, with worked examples in this PR.** Real artifacts
you can open, validate, and react to; each fails current validation on exactly
the proposed point, and nothing else.

- **A1 — `mapping_role: aggregate`** (+ the four aggregate blocks + a nullable
  `allowed_range.max`). *Worked example:* the 14 welfare variable records.
- **A2 — a float type in parameter `value_schema`.** *Worked example:*
  `PARAM-WLF-EQUIVALENCE-SCALE.md`, which validates cleanly except that α/θ need
  `number` rather than `integer` (proven: two `value_schema` errors).

**Part B — open directions, no example content yet.** These flag a need and a
rough shape only — we are *not* proposing fields. We don't yet know the right
sub-structure (for instance, how an external table should describe its source,
frequency, granularity, or join keys), so they are for discussion, not review.

- **B1 — a table / correspondence value_type** to finish the retired
  `lookup-tables/` → parameter migration. Test: *authored, enumerable keys* stay
  a parameter (today's `mapping`); *open, data-driven keys* need a table the
  current model can't express. General beyond welfare — unit conversion, and
  occupation / industry / education classifications. Open question: a
  `value_type: table`, or a distinct lookup category?
- **B2 — an external-data category** for country×time series that are *obtained
  and bound*, not authored — for example CPI and an adopted spatial price index.
  These are already `external_input` at the per-survey layer; the canonical
  schema has no parallel. Open question: what should declare an external-data
  dependency? Its descriptors are left deliberately unspecified.

## Remaining items

- **Variable-ID pattern (RESOLVED 2026-09-01).** Component IDs  satisfy `^VAR-[a-z][a-z0-9]*$`.
  However, if relaxed the pattern, it may improve readability for long names (i.e. `VAR-consalcoholtobacco`).
- **`source_coverage` (double-counting).** Deliberately left as an advisory
  check, not a hard constraint: "part of" is definitional, double-counting is
  a within-aggregate property, and the same flow legitimately appears in both
  consumption and income. See the note in `VAR-welfare.md`. Kept open until
  real data-shape examples inform it.
- **Whether switches should be externalized as their own files** (like rules)
  rather than inlined in the record. Inlined here for reviewability; easy to
  externalize later if reused across income and consumption aggregates.
