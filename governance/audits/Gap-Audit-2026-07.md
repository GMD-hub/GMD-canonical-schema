# Gap Audit, July 2026

| Field | Value |
|---|---|
| Record type | Repository gap audit |
| Record ID | AUDIT-2026-07 |
| Created | 2026-07-29 |
| Status | draft |
| Authority | GPID Team |
| Source branch | `gap-audit-2026-07` |
| Baseline | `main` at the start of the audit |
| Related decision record | [Open Decisions](../decisions/Open-Decisions.md) |

## Scope and method

This audit records the repository state found on 2026-07-29 before the Part B
changes on branch `gap-audit-2026-07`. Line references identified as baseline
refer to the `main` branch at the start of the audit. Each finding also records
the Part B disposition.

## A1. Continuous integration

**Gap exists.** The `.github/workflows/` directory existed, but it contained
only `.github/workflows/docs.yml`. That workflow triggers on a restricted push
at baseline line 4 and on pull requests at baseline line 13. Its path filters
cover wiki and documentation files, and it does not run
`validation/validate_country_layer.py`. No automated pull request check
validated the country layer or compiled runtime bundles.

**Part B disposition:** Added `.github/workflows/validate.yml` to run structural
validation, both PER smoke builds, and pytest on pushes and pull requests. The
workflow captures validator output and uploads it as the informational
`governance-reports` artifact without making report contents a separate failure
condition.

## A2. Code ownership

**Gap exists.** No `CODEOWNERS` file existed at the repository root, under
`.github/`, or under `docs/`. The governance page assigns `knowledge/` and
`country-parameters/` to human writers at
`wiki/Governance-and-Contributing.md:18-19` and lists approval requirements at
`wiki/Governance-and-Contributing.md:34-40`, but the baseline repository had no
technical ownership control. The documentation workflow does not enforce
semantic approval.

**Part B disposition:** Added `.github/CODEOWNERS` with the requested placeholder
team and documented that repository administrators must enable default-branch
protection and required code-owner review before the convention becomes a
technical control.

## A3. Exception precedence

**Gap exists.** Universal DEM rules use priorities 95, 90, and 80 at
`knowledge/rules/module/dem/RULE-EDU-001.md:15`,
`knowledge/rules/module/dem/RULE-SEX-001.md:12`,
`knowledge/rules/module/dem/RULE-EDU-002.md:12`, and
`knowledge/rules/module/dem/RULE-EDU-003.md:13`. The baseline
`CountryExceptionRecord` fields begin at `schema/country_exceptions.py:20`, and
its effective dates are at lines 25-26, but it has no ordering or priority
field. The country-layer documentation explains selection by year but does not
define whether a selected country exception runs before or after a universal
rule for the same variable.

**Part B disposition:** Did not add exception priority or choose an ordering.
Added an informational overlap report and recorded the decision request in
[Open Decisions](../decisions/Open-Decisions.md).

## A4. Exception window overlap

**Gap exists.** At baseline,
`validation/validate_country_layer.py:44-50` typed `windows_overlap` only for
`CountryParameterRecord`. Its only caller grouped country parameters and
reported overlapping parameter windows at baseline lines 108-122. Country
exception windows were individually checked for reversal by
`schema/country_exceptions.py:32-40`, but exception pairs were never compared.

**Part B disposition:** Generalized the overlap helper to effective-dated
parameter and exception records. Exceptions sharing a variable and an
overlapping window now appear in the informational `Overlapping exception
report`. Duplicate exception IDs and reversed windows are structural failures.

## A5. Strict models for universal artifacts

**Gap exists.** The baseline `schema/` directory contained `frontmatter.py`,
`parameter.py`, `country_parameters.py`, `country_exceptions.py`, and
`__init__.py`. Dedicated Pydantic models therefore covered universal parameter
definitions, country parameter files, and country exception files. At baseline,
`build/compile_bundle.py:26-27` defined `UniversalArtifact` as a generic mapping,
and baseline line 49 used it for variables, rules, and modules. As a practical
consequence, malformed variable, rule, or module front matter could pass bundle
compilation if it was valid YAML and did not violate the few separate reference
checks.

No undocumented front-matter fields were found in the three DEM variables or
four DEM rules. Strict modeling did reveal pre-existing unresolved references:
`knowledge/variables/dem/VAR-educat4.md:47-48,57` references `VAR-educat7`,
`VAR-educat5`, and `VAR-mineducatage`, while
`knowledge/variables/dem/VAR-educy.md:40-41,54,57` additionally references
`VAR-school`. None has a file or registry entry in `knowledge/index.md:10-14`.

**Part B disposition:** Added strict variable and rule models, forbidden unknown
fields, ID-pattern checks, a documented rule-priority range, reference checks,
and derivation-cycle detection. The compiler now uses those models; modules
remain generic because Part B requested no module model. Following explicit
user direction during implementation, unresolved references in draft variable
artifacts appear as governance warnings inside the validator output rather than
structural failures. This preserves the references without inventing governed
artifacts and allows draft bundles to compile. The GPID Team still must supply
and promote those artifacts or approve a relationship change before approval.

## A6. Documentation overlap

**Gap exists.** `docs/overview.md` duplicates the system purpose and
three-schema flow covered by `wiki/index.md` and `wiki/Architecture.md`.
`docs/the-schema.md` duplicates the variable field inventory and `VAR-male`
example covered by `wiki/Artifact-Model.md`. `docs/education-examples.md`
duplicates the education artifact examples and effective-country-input
explanation covered across `wiki/Artifact-Model.md` and
`wiki/Country-Parameter-Layer.md`.

Content unique to `docs/` includes the motivation based on inconsistent human
interpretation at `docs/overview.md:3-18`, the history of Laura's pilot at
`docs/overview.md:39-47`, a compact field-by-field `VAR-male` walkthrough at
`docs/the-schema.md:34-57`, and a single-page education derivation narrative at
`docs/education-examples.md:1-82`.

The baseline statement at `docs/the-schema.md:8-10` claimed every variable's
structured fields were validated automatically, while the baseline compiler
loaded variables as generic mappings. The education graph at
`docs/education-examples.md:67-82` also repeated `educat5` in a way that did not
accurately depict the declared relationships.

**Part B disposition:** Added the requested narrative-versus-operational purpose
statements, corrected the validation claim to match strict variable modeling,
and corrected the education graph without deleting narrative content.

## A7. Test coverage

**Gap exists.** No `tests/` directory existed at baseline. The only automated
test file was `validation/test_docs_site.py`, and the docs workflow runs it at
`.github/workflows/docs.yml:27`. The PER fixtures explicitly place one education
record at `country-parameters/countries/PER/parameters.md:15-16` and its
successor at line 30, while the exception ends in 1999 at
`country-parameters/countries/PER/exceptions.md:13-17`. No automated test
exercised the 1999-to-2000 boundary or exception expiry.

**Part B disposition:** Added pytest coverage for boundary-year selection,
expired exceptions, parameter overlap rejection, country-file scope rejection,
and bundle integrity using temporary paths where files are mutated.

## A8. Residual placeholders

**Gap exists.** `schema/.gitkeep` and `validation/.gitkeep` remained tracked
after those directories gained real Python files. Other tracked `.gitkeep`
files still preserve genuinely empty artifact or staging directories and are
not redundant. The empty `extraction/20_drafts/project-documentation/wiki/`
path is additional scaffolding, but Git does not track the empty directory and
this task does not assign it content. Historical log lines
`knowledge/log.md:34-41` also refer to an unavailable session summary and say
Pydantic models are not yet written; those statements are retained as history
rather than rewritten.

**Part B disposition:** Removed only `schema/.gitkeep` and
`validation/.gitkeep`. Retained placeholders in genuinely empty directories.

## Related records and implementation evidence

- [Governance Records](../README.md)
- [Open Decisions](../decisions/Open-Decisions.md)
- `wiki/Validation-and-Builds.md`
- `wiki/Governance-and-Contributing.md`
- `wiki/Repository-Map.md`
- `knowledge/log.md`
