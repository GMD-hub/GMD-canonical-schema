# Education examples: `educat4` and `educy`

> **Purpose:** `docs/` holds narrative background explaining why the design is
> what it is, written to be read once. `wiki/` holds operational reference
> documentation describing how the system currently behaves and is maintained
> continuously.

These two variables illustrate the more complex cases in the schema.

## `educat4`: a variable with a derivation hierarchy

`educat4` records highest education in four categories (no education /
primary / secondary / tertiary). Unlike `male`, it is not always mapped
directly from the raw survey.

**Key fields:**

| Field | Value |
|---|---|
| Tier | 1 (mandatory; must be generated for every survey) |
| Mapping role | `derived_preferred` |
| Derived from | `educat7` (preferred), `educat5` (fallback) |
| Country parameters | none (`[]`) |
| Rules | RULE-EDU-001 (age restriction), RULE-EDU-002 (derivation order) |

**What `derived_preferred` means here:**

The AI must first attempt to compute `educat4` from `educat7` using this
exact recode: `recode educat7 (1=1) (2 3=2) (4 5=3) (6 7=4), gen(educat4)`.
If `educat7` cannot be built for this survey, the AI falls back to `educat5`.
Only if neither can be built does the AI map directly from the raw survey
categories. In that case it must flag this departure in the harmonization
record and escalate to the TTL.

**The age restriction (RULE-EDU-001):**
All individuals below `mineducatage` receive a specific missing code (`.c`),
not standard missing. This rule applies to `educat7`, `educat5`, `educat4`,
and `primarycomp` consistently. One rule file, referenced by four variables.

## `educy`: continuous variable with a country parameter

`educy` records years of education completed. It is continuous (not
categorical) and declares a country-specific construction parameter that maps
education levels to years of schooling.

**Key fields:**

| Field | Value |
|---|---|
| Tier | 1 (mandatory) |
| Mapping role | `derived_preferred` |
| Derived from | `educat7`, `educat5`, or `educat4` (depending on what is available) |
| Country parameters | `PARAM-EDU-YEARS-BY-LEVEL` |
| Prerequisites | `mineducatage` (age restriction), `school` (enrollment status) |
| Rules | RULE-EDU-001 (age restriction), RULE-EDU-003 (construction logic) |

**Construction logic (from RULE-EDU-003):**

The AI follows three paths in order. Path 1: if the survey directly records
years of education, use that. Path 2: if the survey records grade level, use
the country parameter selected by ISO3 code and survey ID year to convert
grades to years. Path 3: if only
categorical education information is available, use the highest available
categorical variable plus the selected country parameter. Enrolled individuals use
current grade minus one; non-enrolled use highest completed grade. Repeated
grades count once.

**An open gap:** `PARAM-EDU-YEARS-BY-LEVEL` has an undecided fallback policy,
and most country folders have no supplied values. Paths 2 and 3 must stop and
escalate when no valid country record exists.

## The education derivation graph

```
raw survey data
      │
      ▼
educat7 (referenced source) ───────┬──────────────► educy
      │                           │
      ├──► educat4 ───────────────┘
      │
      └──► educat5 (referenced source) ───────────► educat4 and educy

educat4 and educy also depend on documented prerequisites.
Country construction paths for educy require the declared country parameter.
```

The current repository does not yet contain artifacts for `educat7`,
`educat5`, `mineducatage`, or `school`, even though the available variable
specifications reference them. Strict validation therefore reports those
references until the GPID Team supplies and promotes the governed artifacts or
approves a relationship change.
