# Artifact Model

## Common file structure

Canonical artifacts are Markdown files with YAML front matter:

```markdown
---
artifact_id: EXAMPLE-ID
schema_version: "0.1"
status: draft
provenance:
  source_document: "authoritative source"
  human_reviewed: false
---

## Definition

Human-readable guidance follows here.
```

The front matter must begin at the first byte with `---` and end with a second
`---` delimiter. The parser requires the YAML document to be a mapping.

## Variable specifications

A variable specification describes one GMD output variable. Its structured
fields cover:

- identity: `variable_id`, name, label, module, GMD version, and schema version;
- behavior: tier, mapping role, unit of analysis, and data type;
- output contract: value codes or numeric range and extended missing codes;
- graph: `derived_from`, `derives_to`, and prerequisites;
- dependencies: decision rules, exceptions, and country parameter declarations;
- discovery: questionnaire keywords and common section names;
- provenance: source location, extraction method, review status, and notes.

The Markdown body normally adds a definition, conceptual intent, construction
notes, consistency checks, escalation triggers, common mistakes, and change
log. Keep one variable per file.

Mapping roles currently illustrated in the repository are:

| Role | Meaning |
|---|---|
| `atomic` | Map directly from raw survey evidence. |
| `derived` | Compute from other canonical variables. |
| `derived_preferred` | Prefer canonical derivation, with direct raw mapping as a documented fallback when allowed. |

## Decision rules

Rules separate reusable logic from variable descriptions. A rule identifies
its scope, module, applicable variables, priority, version, authority, status,
and validity. The body expresses plain language and formal IF/THEN behavior,
prohibitions, rationale, test examples, and history.

Variable files reference rules by ID. This avoids copying the same rule into
multiple variables and lets a reviewer inspect the controlling decision once.

## Parameter definitions

A universal parameter definition declares:

- a `PARAM-<MODULE>-<DESCRIPTIVE>` ID;
- whether it affects `construction` or `validation`;
- an `integer` or `mapping` value type and, for mappings, exact keys;
- variables to which it applies;
- a fallback policy and optional global default;
- provenance and review state.

Supported fallback policies are:

| Policy | Behavior when no valid country record exists |
|---|---|
| `use_global_default` | Use the required non-null universal default. |
| `skip_check` | Skip a validation check; valid only for validation parameters. |
| `block_and_escalate` | Stop the affected construction and request a decision. |
| `undecided` | Stop and escalate because governance has not selected a policy. |

## Country parameter records

A country parameter file identifies its country and contains zero or more
records. Each record references a registered parameter ID, supplies inclusive
`effective_from` and `effective_to` bounds, provides a value matching the
universal type contract, and records provenance. A null bound is open ended.

Overlapping windows for the same parameter and country are invalid because
they could select more than one value for the same survey year.

## Country exception records

Each exception uses an `EXC-<ISO3>-<NNN>` ID and contains:

- existing variable IDs in `applies_to_variables`;
- an inclusive validity window;
- natural-language `condition`, `action`, and `rationale` fields;
- source and approval provenance.

Exceptions are for country-specific conditional behavior that cannot be
expressed as a parameter value. They are not structural overrides.

## IDs and references

| Artifact | ID form | Example |
|---|---|---|
| Variable | `VAR-` + lowercase Stata name | `VAR-male` |
| Rule | `RULE-` + uppercase topic and sequence | `RULE-SEX-001` |
| Module | `MOD-` + uppercase module | `MOD-DEM` |
| Parameter | `PARAM-` + uppercase module and description | `PARAM-EDU-YEARS-BY-LEVEL` |
| Country | `CTY-` + uppercase ISO3 | `CTY-PER` |
| Country exception | `EXC-` + ISO3 and sequence | `EXC-PER-001` |

References must resolve to existing registered artifacts. Changes to
`derived_from` or `derives_to` always require human approval because they alter
the canonical dependency graph.
