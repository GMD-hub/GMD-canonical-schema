# Education examples: `educat4` and `educy`

These two variables illustrate the more complex cases in the schema.

## `educat4` — a variable with a derivation hierarchy

`educat4` records highest education in four categories (no education /
primary / secondary / tertiary). Unlike `male`, it is not always mapped
directly from the raw survey.

**Key fields:**

| Field | Value |
|---|---|
| Tier | 1 (mandatory — must be generated for every survey) |
| Mapping role | `derived_preferred` |
| Derived from | `educat7` (preferred), `educat5` (fallback) |
| Country lookup | not required |
| Rules | RULE-EDU-001 (age restriction), RULE-EDU-002 (derivation order) |

**What `derived_preferred` means here:**

The AI must first attempt to compute `educat4` from `educat7` using this
exact recode: `recode educat7 (1=1) (2 3=2) (4 5=3) (6 7=4), gen(educat4)`.
If `educat7` cannot be built for this survey, the AI falls back to `educat5`.
Only if neither can be built does the AI map directly from the raw survey
categories — and in that case it must flag this departure in the harmonization
record and escalate to the TTL.

**The age restriction (RULE-EDU-001):**
All individuals below `mineducatage` receive a specific missing code (`.c`),
not standard missing. This rule applies to `educat7`, `educat5`, `educat4`,
and `primarycomp` consistently. One rule file, referenced by four variables.

## `educy` — continuous variable with a country lookup table

`educy` records years of education completed. It is continuous (not
categorical) and requires a country-specific conversion table that maps
grade levels to years of schooling.

**Key fields:**

| Field | Value |
|---|---|
| Tier | 1 (mandatory) |
| Mapping role | `derived_preferred` |
| Derived from | `educat7`, `educat5`, or `educat4` (depending on what is available) |
| Country lookup | required — `education_years_by_country_v1` |
| Prerequisites | `mineducatage` (age restriction), `school` (enrollment status) |
| Rules | RULE-EDU-001 (age restriction), RULE-EDU-003 (construction logic) |

**Construction logic (from RULE-EDU-003):**

The AI follows three paths in order. Path 1: if the survey directly records
years of education, use that. Path 2: if the survey records grade level, use
the country lookup table to convert grades to years. Path 3: if only
categorical education information is available, use the highest available
categorical variable plus the country lookup table. Enrolled individuals use
current grade minus one; non-enrolled use highest completed grade. Repeated
grades count once.

**An open gap:** The country lookup table (`education_years_by_country_v1`)
does not yet exist. It needs to be built before `educy` can be reliably
harmonized via paths 2 and 3. Building this table is a separate workstream.

## The education derivation graph

```
raw survey data
      │
      ▼
educat7  (atomic) ──────────────────────────────────┐
      │                                               │
      ├──► educat5  (derived_preferred) ─────────────┤
      │         │                                     │
      │         └──► educat4  (derived_preferred)     │
      │               educat5  (derived_preferred)    │
      │               primarycomp                     │
      │                                               ▼
      └──────────────────────────────────────►  educy (derived_preferred)
                                               + country lookup table
```

`educat7` is the root. Everything else in the education module flows from it.
