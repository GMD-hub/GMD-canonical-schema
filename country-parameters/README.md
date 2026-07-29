# Country Parameter Layer

This layer holds governed country-specific parameter values and country
exceptions. The Canonical Variable Schema under `knowledge/` remains strictly
universal. During harmonization, the effective canon is the union of the
universal CVS and the selected records for the survey country and period.
Both layers are canonical, version controlled, and governed.

## Organization and loading

Each ISO 3166-1 alpha-3 country code has one folder under `countries/`.
`parameters.md` contains parameter values and `exceptions.md` contains
conditional country exceptions. Records exist only when a country has an
actual supplied value or deviation. Absence is meaningful.

The agent loads both files for the survey ISO3 code on every run and for every
variable. Loading is unconditional. The agent then selects records whose
inclusive validity window contains the survey ID year. A null lower or upper
bound is open ended.

The survey ID year is the calendar year in which survey fieldwork began. A
survey beginning in December 2025 and ending in November 2026 uses 2025.
Welfare year is a different concept and is outside this layer.

## Bounded vocabulary

A country layer may contain only:

- Parameter value records for IDs defined in `knowledge/parameters/`.
- Country exception artifacts with condition and action statements.

It must never redefine value codes, definitions, data types, derivation
relationships, missing codes, or any other CVS structure. Validation rejects
files that exceed this scope. An exception may never redefine a variable's
value codes, data type, missing codes, or derivation graph. A proposed change
of that kind belongs in the universal CVS approval path.

Governance controls who may change a rule. The scope rule controls where each
kind of content is allowed to live, so approved changes are always filed in
the correct layer.

## Precedence and fallback

Within its allowed scope, a selected country record wins over a global default
because it is more specific. The universal CVS always wins on structure.
Resolution order is:

1. Use the country record valid for the survey ID year.
2. If none exists, read the parameter's `fallback_policy` in the universal
   registry.
3. Apply `use_global_default`, `skip_check`, or `block_and_escalate` exactly as
   defined by the registry model.
4. If the policy is `undecided`, stop and escalate. Never improvise a value.

Variables declare required parameter IDs in `country_parameters`. This is a
completeness check, not a routing instruction.

## Country exceptions

Exceptions express country-specific conditional logic that cannot be reduced
to a parameter value. They follow the same IF/THEN discipline as universal
rules through natural-language `condition` and `action` fields, scoped by
variable and validity window.

## Authoring and runtime bundles

Markdown plus YAML front matter is the authoring and governance format. Humans
author and approve these files. JSON is a derived build artifact for machine
consumption and is never hand edited. `build/compile_bundle.py` combines the
whole universal knowledge base with one selected country layer, validates it,
and records the source commit hash in the generated bundle.

## Country layer IDs

| Artifact | ID format | Example |
|---|---|---|
| Country layer | `CTY-` + uppercase ISO3 | `CTY-PER` |
| Country exception | `EXC-` + ISO3 + sequence | `EXC-PER-001` |
