# The schema: fields and a first example

## Structure of every variable record

Each variable record has two parts in the same file.

**Structured fields** (top of the file): discrete facts about the variable
that the AI agent reads. These are validated automatically. A record with
a missing required field or an invalid value cannot be approved.

**Prose sections** (bottom of the file): nuanced guidance that the AI and
human reviewers both read. Includes the definition, step-by-step construction
notes, consistency checks, escalation triggers, and common mistakes.

## The fields

| Field | What it captures |
|---|---|
| Variable name and label | Stata name and official GMD label |
| Module | Which GMD module (DEM, EDU, GEO, IDN, LBR) |
| Tier | 1 = mandatory, 2 = recommended, 3 = optional |
| Mapping role | `atomic` (mapped directly from raw survey), `derived` (always computed from other GMD variables), `derived_preferred` (computed when possible, mapped directly as fallback) |
| Data type | Binary, ordered categorical, continuous integer, etc. |
| Allowed values | Complete list of valid output codes and labels |
| Missing value codes | Which extended missing codes apply and what each means |
| Derived from | Which GMD variables this one is computed from |
| Derives to | Which GMD variables are computed from this one |
| Country parameters | Registry IDs for parameters whose country coverage must be checked |
| Prerequisites | Other variables that must be evaluated first |
| Rules | References to the decision rule files that govern this variable |
| Source hints | Keywords and section names that help the AI find this concept in a raw questionnaire |

## Example: `male`

`male` is the simplest possible case: a binary atomic variable with one
decision rule.

**Key fields:**

| Field | Value |
|---|---|
| Tier | 1 (mandatory) |
| Mapping role | `atomic`, always mapped directly from the raw sex variable |
| Data type | Binary |
| Allowed values | 1 = Male, 0 = Female |
| Missing codes | `.a` not harmonized / `.b` cannot be harmonized / `.c` not collected / `.o` non-binary category |
| Derived from | none |
| Country parameters | none (`[]`) |
| Rules | RULE-SEX-001 |

**Construction guidance (from the prose section):**

Map the raw sex variable directly. Do not impute sex from any other variable.
Numeric placeholder codes (98, 99, 9) must be excluded and coded as `.a`.
When the raw survey has categories beyond male and female, for example
"other" or "non-binary", do not force those into 1 or 0. Use `.o` and
document the category in the do-file notes.

## Empty country parameter declaration

Variables that need no country parameter use this field in their YAML front
matter:

```yaml
# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []
```

The agent loads the country layer unconditionally. This declaration exists
only to detect missing required country records and apply registry fallback
policies.

**The accompanying rule file (RULE-SEX-001)** contains the explicit IF/THEN
logic the AI must follow: if the raw variable says male → set to 1, if female
→ set to 0, if placeholder code → set to `.a`, if non-binary → set to `.o`,
and so on. The rule also states what the AI is never allowed to do (impute,
drop individuals, force ambiguous categories into a binary value).
