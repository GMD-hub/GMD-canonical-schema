---
date: 2026-08-17
title: "Fix parameter-registry loading in the schema-compliance review runner"
status: done
scope: "Standard"
brainstorm: null
language: "Python"
estimated-effort: "small"
deviation-policy: "ask"
artifact-schema-version: 1
tags: [agent-review, schema-compliance, parameter-registry, review-runner, bugfix]
phases: 2
---

# Plan: Fix parameter-registry loading in the schema-compliance review runner

## Objective

Make `extraction_pipeline.review_agents.run_all_agents` load the universal
parameter registry from `knowledge/parameters/`, hard-stop if the registry is
missing or yields zero parameter IDs while drafts reference them, and pass the
known parameter IDs into the schema-compliance agent — so drafts declaring
`country_parameters` are validated against the real registry instead of an
always-empty set. This resolves the 4 `schema_compliance` errors currently
reported against `VAR-educy` and `VAR-marital`. It also reconciles the existing
test suite and answer key to the fixed behavior, and audits the two existing
parameter stubs for stale metadata (agents may not edit `knowledge/`).

> **Revision v2 (2026-08-17).** Incorporates `/cg-plan-review` findings:
> P2.1/P2.2/P2.4 (test suite + answer key encode the bug; tests/ treated as
> agent-editable per explicit user decision — C6), P2.3 (empty-registry hard
> stop — R5/V7), P3.1 (do not import `build/compile_bundle` — C7), P3.2
> (re-worded evidence), P3.3 (latent coupling noted, out of scope, tracked by
> roadmap idea `refresh-review-agent-test-and-doc-conventions`).

## Context

The agent review reports 4 `schema_compliance` errors — 2 each on `VAR-educy`
and `VAR-marital` — because their `country_parameters` references
(`PARAM-EDU-YEARS-BY-LEVEL`, `PARAM-DEM-MIN-MARRIAGE-AGE`) are flagged
"Parameter reference not in registry." Investigation shows the two parameter
stubs **already exist** in `knowledge/parameters/` with
`fallback_policy: undecided` (committed on `origin/main`, commit `ea190c8`,
dated 2026-07-28). They are well-formed and conform to
`schema/parameter.py:ParameterDefinition`.

The real defect is in the runner. `run_all_agents.run` builds `variable_ids`
and `rule_ids` from the drafts but never loads parameter IDs, then calls
`schema_check(path, variable_ids, rule_ids=rule_ids)` — the `parameter_ids`
argument is omitted, so inside `check_draft` it defaults to `None` and becomes
an empty `set()` (`schema_compliance.py:169-170`). Consequently:

- `schema_compliance._check_unresolved_parameter_refs` flags every
  `country_parameters` entry as "not in registry" (`schema_compliance.py:149-159`).
- `VariableDefinition.validate_references` raises "unknown parameter IDs"
  because the context's `parameter_ids` is empty
  (`schema/variable.py:151-152, 162-164`).

Exactly 2 drafts carry a non-empty `country_parameters` list referencing a
PARAM ID — `VAR-educy` (`dem/VAR-educy.md:50`, `PARAM-EDU-YEARS-BY-LEVEL`) and
`VAR-marital` (`dem/VAR-marital.md:51`, `PARAM-DEM-MIN-MARRIAGE-AGE`). All
other drafts declare `country_parameters: []`. So the bug currently surfaces
only on those two drafts.

This plan supersedes the original task framing ("register two parameter stubs
under `country-parameters/`"). That framing was based on a stale premise: the
stubs already exist, and `country-parameters/` is the wrong location for the
registry — per `country-parameters/README.md` and `build/compile_bundle.py:124`,
the parameter ID *registry* lives in `knowledge/parameters/`; the
`country-parameters/` folder holds country *values* only. Direction confirmed
with the user: "Runner fix + stub audit."

### Key files and locations

- `extraction_pipeline/review_agents/run_all_agents.py` — the buggy runner
  (`run` at line 68; missing parameter load; `schema_check` call at line 92).
- `extraction_pipeline/review_agents/schema_compliance.py` —
  `check_draft(path, variable_ids, parameter_ids=None, rule_ids=None)` at
  line 162; `_check_unresolved_parameter_refs` at line 149.
- `schema/variable.py` — `VariableDefinition.validate_references` (lines
  147-169) consumes context `parameter_ids`.
- `schema/parameter.py` — `ParameterDefinition` model (line 29); ID pattern
  `PARAM-<MODULE>-<DESCRIPTIVE>` (line 49).
- `schema/frontmatter.py` — `load_markdown` used by `helpers.load_draft`.
- `build/compile_bundle.py:48` — reference for the registry location
  (`ROOT / "knowledge" / "parameters"`); **do not import it** (see C7).
- `knowledge/parameters/PARAM-EDU-YEARS-BY-LEVEL.md` — stub, `applies_to_variables:
  [VAR-educy, VAR-educat4]`.
- `knowledge/parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md` — stub,
  `applies_to_variables: []` (stale: VAR-marital now declares it).
- `tests/review_agents/test_integration.py` — `all_findings` fixture (line 30)
  replicates the runner loop but omits `parameter_ids` (line 43);
  `test_runner_exit_code` (line 89) asserts `exit_code == 1`.
- `tests/review_agents/known_answer_key.yml` — 4 entries; 2 encode the
  parameter errors being removed (lines 4-8, 22-26).
- `tests/review_agents/test_schema_compliance.py` — `test_var_educy_parameter_error`
  (line 27) and `test_var_marital_parameter_error` (line 33) assert the error
  exists; `_findings_for` (line 18) passes no `parameter_ids`.

### Environment notes

- `.venv/bin/python` is NOT present in this worktree; it must be created or
  confirmed before the verification rerun (Constraint C5).
- `roadmap.json` exists at the repo root.
- The `.kilo/shared/artifact-view.contract.md` and
  `.kilo/shared/model-advisory.contract.md` files are absent in this worktree;
  the render/validate step is run via the `cg-render-artifact` CLI if available.

### Review context

This plan was challenged via `/cg-plan-review` (session `ses_fee13dc6effe9...`).
Findings: 0 P1, 4 P2 (all addressed in v2), 3 P3 (addressed or tracked).
Verified claims: all line citations are accurate; `parents[2]` is the correct
repo-root index from `extraction_pipeline/review_agents/`; the only production
caller of `schema_compliance.check_draft` is the runner; both stubs conform to
`ParameterDefinition`; `VAR-educat4.md:54` has `country_parameters: []` (a real
asymmetry with `PARAM-EDU-YEARS-BY-LEVEL`'s `applies_to_variables`); the marital
`TODO` is a `schema_compliance` **warning** (distinct from the 4 errors); the
marital `rules_caveats` stub **error** is what keeps the runner exit code at 1
after the fix (latent coupling — P3.3, out of scope).

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | The runner loads the set of valid `parameter_id` values from `knowledge/parameters/*.md` before running agents. | root cause analysis |
| R2 | `parameter_ids` is passed into `schema_check` and reaches the `VariableDefinition` validation context. | `schema_compliance.py:162-182`; `schema/variable.py:151-152` |
| R3 | After the fix, `VAR-educy` and `VAR-marital` each have 0 `schema_compliance` errors (the 4 errors are gone). | task constraint #4 |
| R4 | The two parameter stubs are audited; stale metadata (e.g. `applies_to_variables`, prose) is recorded for human escalation, not edited in place. | AGENTS.md (agents may not write `knowledge/`) |
| R5 | The runner hard-stops if the registry is missing or yields zero `parameter_ids` while ≥1 draft declares a non-empty `country_parameters` list — preventing silent false positives. | P2.3 (plan review) |
| R6 | The test suite and answer key are reconciled to the fixed behavior; `pytest tests/review_agents/` is green. | P2.1/P2.2/P2.4 (plan review) |

## Implementation Steps

## Phase 1: Core implementation

### 1. Load the parameter registry in the runner
- **Requirements**: R1, R5
- **Files**: `extraction_pipeline/review_agents/run_all_agents.py`; `extraction_pipeline/review_agents/helpers.py` for a shared `list_parameter_ids` loader
- **Details**:
  - Add a `list_parameter_ids(registry_dir: Path) -> set[str]` helper to
    `helpers.py`. It globs `*.md` under the registry dir, parses each with the
    shared `load_markdown` parser (same one `helpers.load_draft` uses), and
    collects each file's `parameter_id` frontmatter field into a `set[str]`.
  - **Mirror, do not import** (Constraint C7): `build/compile_bundle.load_parameter_artifacts`
    returns full artifact dicts (not `set[str]`), calls `model_validate` (raises
    on malformed — contradicting the skip-don't-crash policy), and couples to
    the build module. Replicate only the minimal glob + `load_markdown` +
    read `parameter_id` pattern.
  - Resolve the registry dir relative to the repo root, not the drafts dir:
    `Path(__file__).resolve().parents[2] / "knowledge" / "parameters"` (the
    correct index from `extraction_pipeline/review_agents/`; `build/` uses
    `parents[1]` because it sits one level shallower). Do not hardcode an
    absolute path.
  - Defensively handle a parse failure: if a parameter file's frontmatter
    fails to parse or lacks `parameter_id`, skip that file but record it for
    the audit (Iteration Policy 1). Do not crash the whole run on a single bad
    file.
  - In `run` (around the `variable_ids`/`rule_ids` construction, lines 78-87),
    call the loader and store the result as `parameter_ids`.
  - **Hard-stop (R5):** after loading, if `parameter_ids` is empty AND the
    collected drafts contain at least one non-empty `country_parameters` entry,
    the runner must stop with a clear message (e.g. print to stderr and return a
    nonzero exit) rather than proceed with an empty set. This closes the silent
    false-positive path where a wrong worktree / shallow clone produces empty
    `parameter_ids` and every `country_parameters` reference is re-flagged.
    A genuinely empty registry with no drafts referencing parameters may
    proceed (empty set is correct in that case).
- **Test Scenarios**:
  - happy path: `knowledge/parameters/` contains the 2 known stubs →
    `parameter_ids == {"PARAM-EDU-YEARS-BY-LEVEL", "PARAM-DEM-MIN-MARRIAGE-AGE"}`.
  - edge case (registry empty, no draft references params) → proceeds with
    empty set, no crash.
  - error path (registry empty/missing, but a draft references params) →
    runner hard-stops with a clear message (the false-positive guard).
  - error path (one malformed file) → skipped, reported; other IDs load.
- **Tests**: unit test `list_parameter_ids` returns the two known IDs from the
  real registry; empty dir yields an empty set without raising; a malformed
  file is skipped not fatal.
- **Acceptance criteria**: `parameter_ids` is non-empty and contains both PARAM
  IDs when run against the current repo; the loader does not raise on the
  current registry; the hard-stop fires when the registry is empty but drafts
  reference params.

### 2. Pass parameter_ids into schema compliance
- **Requirements**: R2
- **Files**: `extraction_pipeline/review_agents/run_all_agents.py`
- **Details**:
  - Update the `schema_check` call at line 92 from
    `schema_check(path, variable_ids, rule_ids=rule_ids)` to
    `schema_check(path, variable_ids, parameter_ids=parameter_ids, rule_ids=rule_ids)`.
  - Confirm `check_draft` forwards `parameter_ids` into both
    `_check_unresolved_parameter_refs(data, parameter_ids)` (already does,
    line 182) and the `VariableDefinition.model_validate` context
    `parameter_ids` key (already does, lines 70-76). No change expected in
    `schema_compliance.py` — only the call site was wrong.
  - Do not change the `allow_unresolved_draft` flag behavior; parameters must
    remain resolved (unlike the `derived_from` draft allowance).
- **Test Scenarios**:
  - happy path: VAR-educy passes `_check_unresolved_parameter_refs` and
    `VariableDefinition` validation because `PARAM-EDU-YEARS-BY-LEVEL` is in
    `parameter_ids`.
  - edge case: a draft referencing a genuinely unknown PARAM still errors
    (regression guard for the check itself).
  - error path: none new.
- **Tests**: extend the schema-compliance unit test (see Step 5 for the
  reconciliation pattern).
- **Acceptance criteria**: the `schema_check` call site passes
  `parameter_ids`; no other call site of `check_draft` is affected.

## Phase 2: Reconcile tests, run, and audit

### 3. Run the review agents and confirm the 4 errors are gone
- **Requirements**: R3
- **Files**: `extraction/25_agent_review/VAR-educy.schema_compliance.yml`, `extraction/25_agent_review/VAR-marital.schema_compliance.yml`, `extraction/25_agent_review/SUMMARY.md` (all regenerated, not hand-edited)
- **Details**:
  - Ensure `.venv` exists (create with `uv venv` / `python -m venv .venv` and
    install dependencies per repo conventions if missing — Constraint C5).
  - Run `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents`
    (module invocation per corrections.md; do NOT use a file path).
  - Read the regenerated `VAR-educy.schema_compliance.yml` and
    `VAR-marital.schema_compliance.yml`. Confirm `summary.errors == 0` for both.
  - The `VAR-marital` body warning "Placeholder text detected: TODO on line 13"
    is a known calibration-fixture defect (Constraint C4) and is NOT one of the
    4 errors; it must remain and is out of scope.
  - Sanity-check `SUMMARY.md`: no NEW errors appeared on previously-passing
    drafts (only educy/marital use `country_parameters`, so none expected).
    If new errors appear, stop (Blocked-Stop Condition).
- **Test Scenarios**:
  - happy path: both files show `errors: 0` for the parameter findings; the
    two "Parameter reference not in registry" and two "unknown parameter IDs"
    findings are gone.
  - edge case: `SUMMARY.md` total errors dropped by exactly 4 vs. the prior
    run; no other draft's error count increased.
- **Tests**: the verification run itself is the test; assert via reading the
  YAML `summary` blocks.
- **Acceptance criteria**: `grep -c "Parameter reference not in registry"
  extraction/25_agent_review/*.yml` returns 0; both educy and marital
  schema_compliance files report `errors: 0`.

### 4. Audit the two parameter stubs and document escalation items
- **Requirements**: R4
- **Files**: write `extraction/25_agent_review/parameter-stub-audit.md` (or `.yml`); read-only `knowledge/parameters/PARAM-EDU-YEARS-BY-LEVEL.md` and `knowledge/parameters/PARAM-DEM-MIN-MARRIAGE-AGE.md`
- **Details**:
  - Audit each stub against `schema/parameter.py:ParameterDefinition` and the
    drafts that declare it. Record findings; do NOT edit `knowledge/`.
  - Known issues to confirm and document:
    - `PARAM-DEM-MIN-MARRIAGE-AGE.md`: `applies_to_variables: []` is stale —
      `VAR-marital` now declares it. Prose ("No current variable spec declares
      it") and provenance notes ("marital status variable spec does not yet
      exist") are also now false. Flag for human update.
    - `PARAM-EDU-YEARS-BY-LEVEL.md`: `applies_to_variables: [VAR-educy,
      VAR-educat4]` — VAR-educy declares it ✓; `VAR-educat4.md:54` has
      `country_parameters: []`, so VAR-educat4 does NOT declare it — a real
      asymmetry, flagged for human review (informational).
    - Confirm both stubs keep `fallback_policy: undecided` and `global_default:
      null` (Constraint C3) — no invented values.
  - Cross-check each `parameter_id` matches its filename and the
    `PARAM-<MODULE>-<DESCRIPTIVE>` pattern; if any mismatch, that is a
    Blocked-Stop Condition (registry integrity → escalate).
  - Also record in the audit any malformed parameter file the loader skipped
    in Step 1 (Iteration Policy 1).
  - The audit artifact goes under `extraction/25_agent_review/` (agent-writable
    per AGENTS.md). Use a clear filename and a short table of
    parameter_id → issue → recommended human action.
- **Test Scenarios**:
  - happy path: audit file lists the stale `applies_to_variables`/prose for
    PARAM-DEM-MIN-MARRIAGE-AGE and confirms the educat4 asymmetry for
    PARAM-EDU-YEARS-BY-LEVEL.
  - edge case: a stub is structurally invalid against `ParameterDefinition`
    → recorded as a Blocked-Stop escalation item, not auto-fixed.
- **Tests**: human review of the audit artifact; no automated assertion beyond
  "file exists and references both PARAM IDs."
- **Acceptance criteria**: audit artifact exists under
  `extraction/25_agent_review/`, references both parameter IDs, and states
  explicitly that no `knowledge/` files were modified.

### 5. Reconcile the test suite and answer key to the fixed behavior
- **Requirements**: R6
- **Files**: `tests/review_agents/test_integration.py`, `tests/review_agents/known_answer_key.yml`, `tests/review_agents/test_schema_compliance.py`
- **Details** (per C6, `tests/` is agent-editable code for this plan):
  - **`test_integration.py` `all_findings` fixture (line 30-47):** mirror the
    fixed runner. Load `parameter_ids` from `knowledge/parameters/` the same
    way the runner now does (reuse `list_parameter_ids`), then pass
    `parameter_ids=parameter_ids` in the `schema_check(...)` call (line 43).
    This makes the integration test exercise the fixed path, not the old buggy
    one.
  - **`known_answer_key.yml`:** remove the two parameter-error entries that the
    fix eliminates (the `VAR-educy` / `country_parameters` / `error` /
    `PARAM-EDU-YEARS-BY-LEVEL` entry at lines 4-8, and the `VAR-marital` /
    `country_parameters` / `error` / `PARAM-DEM-MIN-MARRIAGE-AGE` entry at
    lines 22-26). Leave the other two entries (educat7 TODO warning, marital
    rules_caveats stub error) intact — those remain valid.
  - **`test_schema_compliance.py`:** adopt the P2.2 path-(a) pattern — leave
    `_findings_for` (line 18) WITHOUT `parameter_ids`, so the two existing
    tests `test_var_educy_parameter_error` and `test_var_marital_parameter_error`
    become the **regression guard for the "unloaded → error" case** (rename or
    re-comment them to make this intent explicit, e.g.
    `test_var_educy_parameter_error_when_registry_unloaded`). Then add a NEW
    test that passes the known `parameter_ids` and asserts ZERO parameter
    findings for both VAR-educy and VAR-marital. Do NOT rewrite the existing
    tests to assert zero errors — that would delete the regression guard.
  - **`test_runner_exit_code` (line 89-91):** keep asserting `exit_code == 1`
    (still valid — the marital `rules_caveats` stub error keeps the runner at
    exit 1). Add a comment that this assertion is sustained by the unrelated
    marital stub defect, and that fixing that fixture later requires updating
    it (P3.3; tracked by roadmap idea).
- **Test Scenarios**:
  - happy path: `pytest tests/review_agents/` is green after reconciliation.
  - edge case: the unloaded-registry unit tests still pass (error present when
    no `parameter_ids`); the new loaded test passes (no error when
    `parameter_ids` populated).
- **Tests**: `.venv/bin/python -m pytest tests/review_agents/` (V6).
- **Acceptance criteria**: `pytest tests/review_agents/` exits 0; the suite
  exercises the fixed path via the reconciled `all_findings` fixture.

## Testing Strategy

- **Unit**: `list_parameter_ids` returns the expected ID set from the real
  registry and handles empty/malformed inputs. Schema-compliance: known PARAM
  (with `parameter_ids`) → no finding; unknown PARAM (or unloaded) → error
  (regression guard, both directions).
- **Integration**: the reconciled `all_findings` fixture exercises the fixed
  runner path; `test_all_key_entries_matched` passes against the trimmed answer
  key; full runner rerun produces 0 parameter errors on educy/marital and no
  regressions elsewhere.
- **Manual/verification surface**: read the regenerated YAML `summary` blocks
  and `SUMMARY.md`; confirm `git status` shows no `knowledge/` or
  `country-parameters/` edits.
- Run the existing review-agent test suite first to establish a baseline; the
  repo's test command is `.venv/bin/python -m pytest tests/review_agents/`.

## Documentation Checklist

- [ ] Audit artifact (`extraction/25_agent_review/parameter-stub-audit.*`)
      documents the stale `applies_to_variables` and prose in
      `PARAM-DEM-MIN-MARRIAGE-AGE.md` for human escalation.
- [ ] `list_parameter_ids` helper has a docstring.
- [ ] No README or `country-parameters/README.md` changes required (the README
      is already correct: registry lives in `knowledge/parameters/`).
- [ ] Optional: a one-line note in the runner docstring that parameter IDs are
      loaded from `knowledge/parameters/`.
- [ ] A comment on `test_runner_exit_code` noting it is sustained by the
      unrelated marital stub defect (P3.3).

## Risks & Mitigations

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| 1 | Importing `build/compile_bundle` couples the review-agent path to the build module and has the wrong contract | Medium | Medium | C7: mirror the minimal glob+`load_markdown`+read pattern in `helpers.py`; do not import `build/`. |
| 2 | Resolving the registry dir relative to `__file__` breaks if the package is installed/relocated | Low | Medium | Resolve relative to repo root via `Path(__file__).resolve().parents[2]`; add a test pinning the expected path. |
| 3 | The rerun surfaces NEW errors on previously-passing drafts (unexpected parameter-related regressions) | Low | High | Only educy/marital declare `country_parameters`, so this is unlikely; if it happens, stop per Blocked-Stop Conditions and investigate before proceeding. |
| 4 | A maintainer "fixes" the stubs by editing `knowledge/` from this agent session | Low | High | Constraint C2 + AGENTS.md; `git status` check (V5) guards it; audit step explicitly escalates instead. |
| 5 | `.venv` is missing in this worktree, blocking the verification rerun | High (confirmed) | Medium | Constraint C5: create/confirm venv before V3/V6; document the exact command. |
| 6 | The marital `TODO` body warning is mistaken for one of the 4 errors | Low | Low | Constraint C4 explicitly excludes it; it is a known calibration-fixture defect and remains. |
| 7 | An empty/missing registry silently re-introduces the false positives (wrong worktree / shallow clone) | Medium | High | R5/V7: the runner hard-stops when the registry is empty but drafts reference params, instead of proceeding with an empty set. |
| 8 | Test reconciliation over-adjusts (e.g. rewrites the unloaded-case tests instead of keeping them as a regression guard) | Low | Medium | Step 5 mandates path-(a): keep `_findings_for` unloaded, add a separate loaded test; do not delete the regression guard. |
| 9 | `test_runner_exit_code` breaks later if the marital stub defect is fixed, with no warning | Low | Low | Step 5 adds a comment; cleanup tracked by roadmap idea `refresh-review-agent-test-and-doc-conventions`. |

## Out of Scope

- Populating real parameter values for any country.
- Editing any file under `knowledge/` (including the two stubs) — escalate to human.
- Fixing the `VAR-marital` body `TODO` (calibration fixture, known defect).
- Creating country-value records under `country-parameters/countries/`.
- Redesigning the parameter registry or the `country-parameters/` layer.
- Building/promoting any draft toward `knowledge/`.
- Refreshing the stale `.cg-docs/solutions/testing-patterns/2026-08-15-pydantic-rule-ids-context.md` note and decoupling `test_runner_exit_code` from the marital stub defect — tracked by roadmap idea `refresh-review-agent-test-and-doc-conventions`.
- The broader agent-review / review-app workstream (separate sessions).

## Completion Contract

### Outcome

The review-agent runner loads `parameter_ids` from `knowledge/parameters/`,
hard-stops on an empty/missing registry that would cause false positives, and
passes them into schema compliance, so `VAR-educy` and `VAR-marital` report 0
`schema_compliance` errors (down from 4); the test suite and answer key are
reconciled to the fixed behavior (pytest green); and the two existing stubs are
audited with stale-metadata items recorded for human escalation — with no files
created or edited under `knowledge/` or `country-parameters/`.

### Verification Surface

| ID | Evidence Required | Command/Artifact | Phase | Required |
|----|-------------------|------------------|-------|----------|
| V1 | Runner loads `parameter_ids` from `knowledge/parameters/` | `grep` / code review of `run_all_agents.py` loader | 1 | yes |
| V2 | `parameter_ids` passed into `schema_check` (reaches `VariableDefinition` context) | code review of the `schema_check(...)` call site | 1 | yes |
| V7 | Empty-registry hard-stop present (missing-dir stop + empty-set-while-drafts-reference-params stop) | code review of `run()` | 1 | yes |
| V3 | 0 `schema_compliance` errors for VAR-educy & VAR-marital (4 → 0) | `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents`; read `VAR-educy.schema_compliance.yml` + `VAR-marital.schema_compliance.yml` `summary.errors` | 2 | yes |
| V4 | Stub-audit findings recorded (stale `applies_to_variables`/prose flagged; no `knowledge/` edits) | `extraction/25_agent_review/parameter-stub-audit.*` | 2 | yes |
| V6 | `pytest tests/review_agents/` green after reconciliation | `.venv/bin/python -m pytest tests/review_agents/` | 2 | yes |
| V5 | No new/edited files under `knowledge/` or `country-parameters/` | `git status -- knowledge/ country-parameters/` (empty) | final | yes |

### Constraints

| ID | Constraint | Check |
|----|------------|-------|
| C1 | Runner invoked via module form | `.venv/bin/python -m extraction_pipeline.review_agents.run_all_agents` |
| C2 | No agent writes to `knowledge/` (AGENTS.md) | `git status` shows no `knowledge/` changes |
| C3 | `fallback_policy` stays `undecided`; no invented parameter values | stub files unchanged (V5) |
| C4 | The marital body `TODO` warning (line 13) is a known fixture defect, not one of the 4 errors; it remains | not counted in V3 |
| C5 | `.venv` must exist before V3/V6 | create/confirm venv if missing |
| C6 | `tests/` is agent-editable code per explicit user decision (AGENTS.md's write table covers content artifacts, not test code); agent reconciles tests directly and verifies pytest green | V6 |
| C7 | Mirror the glob+`load_markdown`+read pattern; do NOT import `build/compile_bundle` | code review |

### Boundaries

- **Allowed**: edit `extraction_pipeline/review_agents/{run_all_agents,helpers}.py`;
  edit `tests/review_agents/{test_integration,test_schema_compliance}.py` +
  `known_answer_key.yml` (per C6); write audit findings to
  `extraction/25_agent_review/`; re-run the runner (regenerates findings YAML +
  `SUMMARY.md`); add/extend tests under `tests/review_agents/`; run pytest.
- **Out of scope**: populate real parameter values; edit `knowledge/` stubs
  (escalate instead); fix the marital `TODO`; create country-value records under
  `country-parameters/countries/`; refresh the stale `.cg-docs/solutions` note
  and decouple `test_runner_exit_code` (tracked by roadmap idea); broad
  parameter-registry redesign.

### Iteration Policy

1. If the loader hits a registry file that fails to parse, extract
   `parameter_id` defensively (skip, don't crash) and report the parse issue in
   the audit artifact.
2. If the re-run surfaces NEW errors in drafts that previously passed (none
   expected — only educy/marital use `country_parameters`), stop and
   investigate before proceeding.
3. If the stub audit finds a stub is malformed in a way that blocks validation
   (e.g., bad `parameter_id` not matching its filename or the `PARAM-` pattern),
   escalate to human immediately — do not edit `knowledge/`.
4. A pytest failure after reconciliation that isn't explained by the parameter
   fix → stop and investigate before adjusting tests further.

### Blocked-Stop Conditions

- `knowledge/parameters/` dir is missing at run time (configuration error).
- Registry yields zero `parameter_ids` while ≥1 draft declares a non-empty
  `country_parameters` list (silent false-positive guard — R5).
- A parameter file's `parameter_id` doesn't match its filename or the
  `PARAM-<MODULE>-<DESCRIPTIVE>` pattern (registry integrity → escalate).
- The re-run produces errors in previously-passing drafts (regression).
- Post-reconciliation pytest failures not explained by the fix → investigate.
