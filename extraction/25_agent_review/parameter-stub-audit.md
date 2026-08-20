---
date: 2026-08-17
title: "Parameter stub audit"
scope: "agent-review"
---

# Parameter Stub Audit

Audit of the two parameter stubs in `knowledge/parameters/` after fixing the
runner to load the parameter registry. No files under `knowledge/` were created
or modified by this audit.

## Findings

| parameter_id | File | Issue | Recommended Human Action |
|---|---|---|---|
| `PARAM-DEM-MIN-MARRIAGE-AGE` | `knowledge/parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md` | `applies_to_variables: []` is stale — `VAR-marital` now declares this parameter. Prose ("No current variable spec declares it") and provenance notes ("marital status variable spec does not yet exist") are also now false. | Update `applies_to_variables` to `[VAR-marital]`. Update prose and provenance notes to reflect that `VAR-marital` now exists and declares this parameter. |
| `PARAM-EDU-YEARS-BY-LEVEL` | `knowledge/parameters/PARAM-EDU-YEARS-BY-LEVEL.md` | `applies_to_variables: [VAR-educy, VAR-educat4]` — `VAR-educy` declares it (correct); `VAR-educat4.md:54` has `country_parameters: []`, so `VAR-educat4` does NOT declare it. Real asymmetry, informational. | Review whether `VAR-educat4` should also declare this parameter, or remove `VAR-educat4` from the stub's `applies_to_variables` list. |

## Structural Validation

- Both stubs keep `fallback_policy: undecided` and `global_default: null` (no invented values).
- Both `parameter_id` values match their filenames and the `PARAM-<MODULE>-<DESCRIPTIVE>` pattern.
- Both stubs conform to `schema/parameter.py:ParameterDefinition`.
- No malformed parameter files were skipped during loading (the loader reported 0 skipped files).

## Constraints Respected

- No files under `knowledge/` were created or edited (AGENTS.md constraint).
- No `country-parameters/` files were created or edited.
