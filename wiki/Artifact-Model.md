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

!!! example "Example: reading a variable specification"
  The current draft `VAR-educy` is `derived_preferred`. That label alone is
  not an algorithm. Its `derived_from`, prerequisites, rules, and country
  parameter declarations must be read together to understand the permitted
  paths and required evidence. This is why a variable file is a contract
  with references, not a standalone recipe.

## Decision rules

Rules separate reusable logic from variable descriptions. A rule identifies
its scope, module, applicable variables, priority, version, authority, status,
and validity. The body expresses plain language and formal IF/THEN behavior,
prohibitions, rationale, test examples, and history.

Variable files reference rules by ID. This avoids copying the same rule into
multiple variables and lets a reviewer inspect the controlling decision once.

!!! example "Example: one rule, multiple consumers"
  If an age restriction applies to several education outputs, those variable
  files can reference one registered rule such as `RULE-EDU-001`. A later
  proposal to change the condition is reviewed once in the rule; copying the
  IF/THEN text into every variable would create competing versions.

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

!!! example "Example: a missing construction input"
  `PARAM-EDU-YEARS-BY-LEVEL` is a construction parameter whose current draft
  fallback is `undecided`. In a hypothetical run with no valid country
  record, the consumer stops the affected construction path and escalates.
  It must not average neighboring countries or silently reuse an expired
  value.

## Country parameter records

A country parameter file identifies its country and contains zero or more
records. Each record references a registered parameter ID, supplies inclusive
`effective_from` and `effective_to` bounds, provides a value matching the
universal type contract, and records provenance. A null bound is open ended.

The file may also declare an optional `focal_point` for the person who should
be consulted about coverage gaps for that country. It defaults to null and is
governance metadata, not a country value or runtime selection input. The
coverage gap report displays it so reviewers know whom to consult.

Overlapping windows for the same parameter and country are invalid because
they could select more than one value for the same survey year.

For example, windows `1990–2000` and `2000–2010` overlap in 2000 because both
bounds are inclusive. A non-overlapping successor would begin in 2001.

## Country exception records

Each exception uses an `EXC-<ISO3>-<NNN>` ID and contains:

- existing variable IDs in `applies_to_variables`;
- an inclusive validity window;
- natural-language `condition`, `action`, and `rationale` fields;
- source and approval provenance.

Exceptions are for country-specific conditional behavior that cannot be
expressed as a parameter value. They are not structural overrides.

!!! example "Parameter or exception?"
  A mapping such as `{primary: 6, lower_secondary: 3,
  upper_secondary: 3}` has a stable universal shape and belongs in a
  parameter record. A sourced instruction that applies only when a specific
  legacy questionnaire code is present is conditional behavior and may
  require an exception. The [Country Parameter Layer](Country-Parameter-Layer.md#parameters-versus-exceptions)
  shows a fully hypothetical exception record.

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

## Suggested reading

- **To see how these records combine at runtime:** return to
  [Architecture and Data Flow](Architecture.md).
- **To resolve effective-dated values and exceptions:** continue to the
  [Country Parameter Layer](Country-Parameter-Layer.md).
- **To propose a new or changed record:** follow the
  [Artifact Lifecycle](Artifact-Lifecycle.md).

## All wiki pages

[Home](index.md) | [Learning Paths](Learning-Paths.md) |
[Architecture](Architecture.md) | [Repository Map](Repository-Map.md) |
[Artifact Model](Artifact-Model.md) |
[Country Parameter Layer](Country-Parameter-Layer.md) |
[Artifact Lifecycle](Artifact-Lifecycle.md) |
[Validation and Builds](Validation-and-Builds.md) |
[Governance and Contributing](Governance-and-Contributing.md) |
[Glossary](Glossary.md)
