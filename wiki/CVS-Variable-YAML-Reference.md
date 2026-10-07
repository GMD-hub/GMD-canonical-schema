# CVS Variable YAML Reference

This page describes the current YAML front matter for one variable record. The
field contract comes from [`schema/variable.py`][schema], not from the examples.
The current model uses `gates: list[Gate]`; the former `prerequisites` key is
not accepted. Gate fields describe applicability, not a general list of inputs
to compute first.
The examples show current usage, not new rules. A change to a
field's name, type, validation, or meaning requires an update to this reference
in the same PR. The Python field-coverage test checks names, not the accuracy
of these human-written explanations.

## Reading a variable file

[`schema/frontmatter.py`][frontmatter] requires `---` followed by a newline at
the start of the file, a closing `---` delimiter on its own line,
and a YAML mapping between them. It returns that mapping and the Markdown body
separately. `VariableDefinition` validates the mapping, forbids unknown keys at
all model levels, and checks references against the supplied validation context.
Reference sets default to empty when context is absent; this does not disable
reference checks.
The Markdown body is not a `VariableDefinition` field: it holds definition,
construction notes, checks, escalation triggers, and change history. Agents
must read the relevant rules and prose as well as the structured fields; the
YAML alone is not a complete harmonization algorithm. See
[`VAR-educy`][educy] for both parts.

**Eligibility is exact:** Foundry and other harmonization agents may use only
canonical variable records under `knowledge/` with `status: approved`. They
must ignore every other status and all review records, review branches, and
staging folders, even if those records say `approved`. This is the operating
rule in [`AGENTS.md`][agents]. The model accepts only `draft` or `approved`, and
requires an approved record to have
`provenance.human_reviewed: true` and a non-blank reviewer. Model validation
does **not** check the file's location or perform human promotion. The current
[`knowledge/variables/dem/VAR-male.md`][male] is still `draft`, so its location
alone does not make it eligible.

## How to read the tables

`R` means the key must be present; `O` means the key may be omitted. `N` means
YAML `null` is accepted; `no` means it is not. All keys are `R` except
`provenance.reviewer`, which is `O` and defaults to `null`. A required nullable
key must still appear. `[]` means an empty list, not an absent or null field;
for list fields it means no declared entries of that kind. List items and
nested objects are not nullable. `int`, `str`, and `list` below are Pydantic
types: except for `provenance.human_reviewed` (`StrictBool`), the model does not
require strict input types. Do not treat coercion as a documented coding rule.
For example, a numeric string can be accepted for an `int`, but a code such as
`INC` cannot. A YAML string must be quoted when YAML would otherwise read it as
a number or date, as in `schema_version: "0.2"` and the extraction date in the
[welfare draft][welfare].
Unless a row says otherwise, strings have no enforced vocabulary, format,
length, or non-blank check; integers have no enforced bounds; lists have no
minimum size or uniqueness check. Each row gives the field's purpose and its
use by a downstream agent. **Code** identifies model checks; **Docs** identifies
documented practice that the model does not enforce.

## Top-level fields

<!-- variable-field-paths:start -->
| Field path | Type; presence/null | Purpose, checks, and downstream use |
|---|---|---|
| `variable_id` | `str`; R/no | Canonical variable ID. **Code:** `VAR-` then a lowercase letter and zero or more lowercase letters or digits. Agent uses it to identify the output and resolve dependencies. [Example][male]. |
| `canonical_label` | `str`; R/no | Human-readable output label; no label format check. Agent uses it to identify the concept in reports. [Example][male]. |
| `variable_name` | `str`; R/no | Output variable name (documented as the Stata name); no code check that it matches `variable_id`. Agent uses it to name the output column. [`VAR-tvcable` uses `tv_cable`][tvcable]. |
| `module_id` | `str`; R/no | Module identifier. **Code:** `MOD-` then an uppercase letter and zero or more uppercase letters, digits, or hyphens; no directory or registry lookup here. Agent uses it to group the output with its module. [GEO example][urban]; [WLF example][welfare]. |
| `gmd_version` | `str`; R/no | GMD specification version; no format or version check. Agent uses it to track the applicable GMD version. [Example][male]. |
| `schema_version` | `str`; R/no | Record schema version; no compatibility or format check in this model. Agent uses it to track the record format. [Version 0.1][male]; [version 0.2][welfare]. |
| `status` | `Literal["draft", "approved"]`; R/no | Approval state. **Code:** approved requires reviewed provenance; draft requires unreviewed provenance. **Docs:** only `approved` records under `knowledge/` are eligible for harmonization. Agent must apply the exact eligibility rule above. [Draft example][male]. |
| `tier` | `int`; R/no | Priority tier. **Docs:** 1 mandatory, 2 recommended, 3 optional in [schema narrative][narrative]; **Code:** does not limit it to these values. Agent uses it to prioritize coverage, not to infer construction logic. [Tier 2 example][w30m]. |
| `unit_of_analysis` | `str`; R/no | Output observation unit, such as `individual` or `household`; no enum. Agent uses it to select the proper survey unit. [Household example][weight]. |
| `mapping_role` | `Literal["atomic", "derived", "derived_preferred"]`; R/no | Mapping strategy. **Docs:** atomic maps from raw data; derived is computed; derived_preferred prefers derivation with a documented direct fallback. **Code:** checks only the literal, not consistency with dependencies. Agent reads rules and prose before choosing a path; [the welfare draft][welfare] uses this role for passthrough, an open question below. [Derivation example][educy]. |
| `data_type` | `str`; R/no | Output data kind, e.g. `binary`, `categorical_ordered`, `numeric_continuous`, `integer`, or `string`; no enum or consistency check against codes/range. Agent uses it to interpret the output contract. [Categorical example][educat7]; [string example][welfaretype]. |
| `value_codes` | `list[ValueCode] \| None`; R/N | Declared discrete output codes and labels; `null` means no discrete code list declared, `[]` means a declared but empty list. Neither means unrestricted output. **Code:** no mutual-exclusion or completeness check with `allowed_range`. Agent checks the declared codes and reads rules and prose for mapping. [Integer codes][male]; [string codes only in Markdown][welfaretype]. |
| `allowed_range` | `AllowedRange \| None`; R/N | Declared output bounds, stored as integers; this does not require integer observations. `null` means no bounds declared, not that every value is valid. **Code:** when present, `min <= max`; no check against `value_codes` or `data_type`. Agent uses it for output checks. [Continuous welfare with integer bounds][welfare]; [null with numeric weights][weight]. |
| `missing_codes` | `list[MissingCode]`; R/no | Declared missing codes and meanings; `[]` means none declared, not a general ban on missing data. No enforced code set, uniqueness, or cross-check against output codes. Agent uses these labels when assigning missing values under the rules. [Codes][male]; [`hsize` has a prose no-missing rule and `[]`][hsize]. |
| `derived_from` | `list[str]`; R/no | Upstream variable IDs; `[]` means no declared derivation inputs. **Code:** each ID matches the variable ID pattern; references must exist in validation context unless unresolved draft references are allowed; graph cycles are checked by the separate graph validator. Agent inspects these inputs and their rules. [Example][educy]. |
| `derives_to` | `list[str]`; R/no | Downstream variable IDs; `[]` means no declared outputs that derive from this variable. **Code:** same ID and reference checks as `derived_from`; no inverse-edge check. Agent uses it to find dependent outputs. [Example][educat7]. |
| `country_parameters` | `list[str]`; R/no | Parameter registry IDs needed by the variable; `[]` means none declared, **not** permission to skip country-layer loading. **Code:** each matches `PARAM-` plus uppercase module, hyphen, and uppercase/digit/hyphen suffix; references must exist in validation context. Agent loads the country layer for every variable and resolves declared parameters with registry fallback rules. [Example][educy]. |
| `gates` | `list[Gate]`; R/no | Universe / skip conditions that determine where this output applies; `[]` means no gates declared, not that all construction inputs are available. **Code:** each `variable_id` must resolve in validation context unless unresolved draft references are allowed; condition text is not parsed or executed. **Docs:** the condition must hold for the output to apply. Agent reads the condition with the rules and prose for out-of-universe handling. [Example][tvcable]. |
| `rules` | `list[str]`; R/no | Governing decision-rule IDs; `[]` means none linked, not that no guidance exists. **Code:** each matches `RULE-` plus uppercase letter followed by uppercase letters/digits/hyphens; references must exist in validation context. Agent reads linked rules before harmonizing. [Example][male]. |
| `exceptions` | `list[str]`; R/no | Exception references; `[]` means none declared. **Code:** no ID format or existence check here. Agent checks applicable exceptions in the loaded country layer and does not treat an ID alone as permission to apply one. [Empty list][male]; [`EXC-PER-001` reference][welfare]. |
| `external_standards` | `list[ExternalStandard]`; R/no | Named external reference sources; `[]` means none declared. No URL validity or availability check. Agent may consult the stated standard with the controlling rules, not treat it as a replacement for them. [ISCED example][educy]; [PIP example][welfare]. |
| `source_hints` | `SourceHints`; R/no | Search clues for raw survey evidence; must contain both lists below. Agent uses them to locate candidate questionnaire items, not as proof of a mapping. [Example][male]. |
| `provenance` | `VariableProvenance`; R/no | Source and review record; must contain its required keys below. Agent uses it to trace authority and enforce review state. [Example][educy]. |

## Nested fields

The `[]` meaning for each nested list is the same as above: no declared entries.
When the parent list is empty or nullable parent is `null`, its child paths
do not occur in that record. The parent type still defines the child contract.

| Field path | Type; presence/null | Purpose, checks, and downstream use |
|---|---|---|
| `value_codes.value` | `int`; R/no per item | Discrete output code; no uniqueness or range check. Non-numeric strings such as `INC` are rejected in this field. Agent uses the number in output mappings; string code sets currently need the prose. [Integer example][male]; [string classifier with null parent][welfaretype]. |
| `value_codes.label` | `str`; R/no per item | Meaning of that output code; no non-blank check. Agent uses it to interpret output codes. [Example][male]. |
| `allowed_range.min` | `int`; R/no when range present | Inclusive lower bound by documented usage; **Code:** only checks `min <= max`. Agent uses it to check outputs. [Example][educy]. |
| `allowed_range.max` | `int`; R/no when range present | Inclusive upper bound by documented usage; **Code:** only checks `max >= min`. Agent uses it to check outputs. [Example][educy]. |
| `missing_codes.code` | `str`; R/no per item | Missing value token such as `.a`; no pattern or uniqueness check, and no type-specific representation check. Agent uses the declared token where applicable; its representation for a string output is an open question below. [Numeric example][male]; [string example][welfareothertype]. |
| `missing_codes.label` | `str`; R/no per item | Reason for that missing token; no controlled vocabulary. Agent uses it to distinguish missing cases. [Example][male]. |
| `gates.variable_id` | `str`; R/no per item | Variable used in the applicability gate; **Code:** variable ID pattern and contextual existence check (draft exception as above). Agent resolves it to assess the gate, not to declare a derivation edge. [Example: `VAR-tv`][tvcable]. |
| `gates.condition` | `str`; R/no per item | Applicability condition, e.g. `VAR-tv == 1`; no expression parser, non-blank check, token resolution, or semantic check. Drafts use `VAR-` and `PARAM-` IDs in condition strings, but this is current usage, not an enforced grammar. Agent reads it with rules and construction notes rather than executing it as code. [Example][tvcable]; [education draft][educy-draft]. |
| `external_standards.name` | `str`; R/no per item | Name of cited standard; no non-blank check. Agent identifies the relevant source. [Example][educy]. |
| `external_standards.url` | `str`; R/no per item | Address of cited standard; no URL scheme or reachability check. Agent can locate the cited source. [Example][educy]. |
| `source_hints.question_keywords` | `list[str]`; R/no | Candidate question terms; `[]` means no terms supplied. No keyword quality check. Agent uses them for discovery only. [Example][male]. |
| `source_hints.typical_section_names` | `list[str]`; R/no | Candidate questionnaire sections; `[]` means none supplied. No section registry check. Agent uses them for discovery only. [Example][male]. |
| `provenance.source_document` | `str`; R/no | Name of source document; no source identity or file existence check in this model. Agent traces the underlying authority. [Example][male]. |
| `provenance.source_section` | `str`; R/no | Location within the source; no locator validation. Agent verifies the stated basis for the record. [Example][male]. |
| `provenance.extraction_method` | `str`; R/no | How the record was extracted, e.g. `manual`; no enum. Agent understands how the draft was made. [Example][male]. |
| `provenance.extracted_on` | `str`; R/no | Extraction date as text; no date format or chronology check. Agent tracks when extraction occurred. [Example][male]. |
| `provenance.human_reviewed` | `StrictBool`; R/no | Whether a human reviewed the record; only actual YAML booleans accepted. **Code:** true requires a non-blank reviewer and `approved` status; false requires a null reviewer and `draft` status. Agent checks review state, but still applies the location-and-status eligibility rule. [Example][male]. |
| `provenance.reviewer` | `str \| None`; O/N; defaults `null` | Human reviewer identity; null means no reviewer. **Code:** must be non-blank if reviewed, null if unreviewed; no identity format check. Agent traces approval evidence. [Example][male]. |
| `provenance.notes` | `str \| None`; R/N | Source or review caveats; null means no note supplied. No content check. Agent reads it for gaps and conflicts, not as a substitute for a rule. [Example with caveat][educy]. |
<!-- variable-field-paths:end -->

## Cross-field and governance limits

**Code:** `AllowedRange` rejects `min > max`. A variable rejects status and
review-state conflicts. It rejects unknown parameter
and rule IDs and unknown variable IDs in `derived_from`, `derives_to`, and
`gates.variable_id`, based on context sets (empty if omitted). Unknown variable
IDs can pass only for drafts when
`allow_unresolved_draft` is true. The separate
`validate_acyclic_derivation_graph` function checks cycles in `derived_from`
for the variables passed to it. The model does not validate that `derives_to`
mirrors `derived_from`, that `value_codes` and `allowed_range` are exclusive,
or that a range matches a data type. Whether a caller supplies full reference
sets and runs the graph check depends on the validation workflow. Gate edges
are not part of that derivation-cycle check. IDs mentioned only in a
`gates.condition` string are not resolved or checked against `country_parameters`
by `VariableDefinition`.

The model validates the record's metadata, not survey observations. It does not
check output values against codes or ranges, apply gates, prohibit missing
observations, or perform a welfare calculation.

**Docs and governance:** [`AGENTS.md`][agents] requires country-layer
loading for every run and every variable; `country_parameters: []` does not
change that duty. Edits to `derived_from` and `derives_to` need human approval.
Source conflicts must go in `provenance.notes` and be escalated. These are
operating rules, not extra Pydantic validators.

## Current welfare examples

The nine WLF files are extraction drafts, not eligible harmonization inputs.
They illustrate field usage and the limits of YAML-only interpretation:

| Case | Real drafts | What the reference reader must distinguish |
|---|---|---|
| String output codes in prose | [`welfaretype`][welfaretype], [`welfareothertype`][welfareothertype], [`welfshprtype`][welfshprtype] | Each declares `data_type: string`, `value_codes: null`, and `allowed_range: null`. The Markdown body lists `INC`, `CONS`, and `EXP`. Null YAML fields do not remove that prose contract; `ValueCode.value` currently cannot store these strings. |
| No missing observations | [`hsize`][hsize] | Declares `missing_codes: []` and a range of 1 to 100. The separate prose forbids missing values and requires a positive integer. That prohibition does not follow from `[]` alone. |
| Passthrough, not reconstruction | [`welfare`][welfare], [`welfarenom`][welfarenom], [`welfaredef`][welfaredef], [`welfareother`][welfareother] | These drafts use `derived_preferred` with empty derivation lists, but the body limits the variable to a country-provided final aggregate. The model permits the combination; the mapping-role narrative does not explain it. Do not infer a construction algorithm from the role. |
| Conditional reuse described in prose | [`welfshprosperity`][welfshprosperity] | Uses `derived_from: []` and `gates: []`, but construction notes allow reuse of `welfare` only when the documented concepts match. Empty lists do not make all prose conditions disappear. |

## Open documentation questions

- Should `variable_name` be checked against the suffix of `variable_id`, and
  should `module_id` match the containing directory? [`VAR-tvcable`][tvcable]
  uses `variable_name: tv_cable`; the ID pattern does not allow that underscore.
  `VariableDefinition` does not check either relationship.
- What exact vocabulary should `data_type`, `unit_of_analysis`, `tier`, and
  `provenance.extraction_method` use? The narrative lists examples or tier
  meanings, but the model accepts broader values.
- Must an output have codes, a range, or both? The model allows both to be
  null, as in [`VAR-weight`][weight], and does not validate whether numeric
  weights are positive.
- What does a nonempty universal `exceptions` list reference, and how is it
  resolved alongside country exceptions? [The welfare draft][welfare] references
  the country-specific `EXC-PER-001`, while `AGENTS.md` requires universal CVS
  content. The model checks neither the list's format nor its targets. Does the
  ID serve as a discovery hint, or is another declaration required?
- Are `derived_from` entries ordered instructions? `VAR-educy` documents a
  preference order, but the model treats them as a graph set for validation;
  precedence is not a general field contract.
- What grammar and reference declarations should gate conditions use? The
  [canonical `VAR-educy`][educy] uses `age >= mineducatage`; the
  [extraction draft][educy-draft] uses
  `VAR-age >= PARAM-EDU-MIN-EDUCATION-AGE`. The latter parameter is not registered
  in `knowledge/parameters/` or declared in that draft's `country_parameters`.
  The model checks only `gates.variable_id`, not the IDs within the condition.
- How should multiple gates combine, and which missing code applies when a
  gate fails or cannot be assessed? The model defines no such behavior. Read
  each variable's rules and prose; do not assume a general AND/OR or missing
  code convention.
- How should `derived_preferred` describe passthrough-only welfare aggregates?
  The [schema narrative][narrative] describes computation with a direct fallback,
  but [the welfare draft][welfare] forbids reconstruction and declares no
  derivation inputs. The model checks neither that meaning nor its relation
  to the derivation graph.
- Should string classifiers have structured value codes in a future schema?
  The three classifiers above put `INC`, `CONS`, and `EXP` in Markdown because
  `ValueCode.value` is integer-only. Their definitions say "three-letter string",
  although `CONS` has four letters. No string length rule is enforced by the
  model; this wording needs a human documentation decision.
- How are `.a` and `.b` represented for string outputs? The
  [alternative classifier][welfareothertype] declares these missing codes and
  instructs `.a` when its aggregate is absent, but does not specify whether
  these are literal strings or an abstract missing convention.
- Does tier 1 require an output column even when its value is missing?
  [`welfareother`][welfareother] has `tier: 1` but calls the secondary aggregate
  optional and uses `.a` when none exists. The narrative says tier 1 is
  mandatory; it does not distinguish column presence from usable observations.
- What supports the upper range bounds of 100 for [`hsize`][hsize] and
  1000000000 for the continuous welfare drafts? Their prose gives lower bounds
  but does not explain these upper bounds. The model validates their ordering,
  not their source basis.

[schema]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/schema/variable.py
[frontmatter]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/schema/frontmatter.py
[agents]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/AGENTS.md#harmonization-eligibility
[narrative]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/docs/the-schema.md#the-fields
[male]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/knowledge/variables/dem/VAR-male.md
[educy]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/knowledge/variables/dem/VAR-educy.md
[educy-draft]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/dem/VAR-educy.md
[urban]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/geo/VAR-urban.md
[weight]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/idn/VAR-weight.md
[educat7]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/dem/VAR-educat7.md
[w30m]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/utl/VAR-w30m.md
[tvcable]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/dwl/VAR-tvcable.md
[welfare]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfare.md
[hsize]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-hsize.md
[welfaretype]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfaretype.md
[welfareothertype]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfareothertype.md
[welfshprtype]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfshprtype.md
[welfarenom]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfarenom.md
[welfaredef]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfaredef.md
[welfareother]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfareother.md
[welfshprosperity]: https://github.com/GMD-hub/GMD-canonical-schema/blob/main/extraction/20_drafts/wlf/VAR-welfshprosperity.md
