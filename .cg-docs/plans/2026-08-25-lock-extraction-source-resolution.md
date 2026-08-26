---
date: 2026-08-25
title: "Lock Extraction Source Resolution and Manifest Identity"
status: active
execution-report: ".cg-docs/work-reports/2026-08-26-lock-extraction-source-resolution.md"
scope: "Standard"
brainstorm: ".cg-docs/brainstorms/2026-08-03-extract-universal-non-welfare-schema.md"
language: "Python"
estimated-effort: "medium"
deviation-policy: "ask"
artifact-schema-version: 1
phases: 2
completed-phases: [1]
current-phase: 2
tags: [extraction, reproducibility, source-lock, manifest, pandoc, governance]
---

# Plan: Lock Extraction Source Resolution and Manifest Identity

## Objective

Make extraction source resolution reproducible and fail closed by validating the
exact GMD-guidelines repository revision, all governed source paths and bytes,
the GMD version, and the future Pandoc runtime. Implement generic validation and
tests before the human decision, but do not modify human-owned extraction
configuration or CI activation until a locatable GPID approval resolves every
decision item.

## Context

The extraction architecture already establishes a manifest-plus-resolver design
and pins `GMD-hub/GMD-guidelines` commit
`d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`. The current implementation is not
fully fail closed:

- `SourceFileEntry.sha256` is nullable and has no shape validator.
- `preflight.py` does not validate source hashes, exact `chapters/` paths, the
  required supporting Markdown source, or the installed Pandoc version.
- `source.py` hashes files with null expected values, omits supporting files,
  and does not prove that the checkout is at the manifest commit.
- `orchestrator.py` trusts that callers already verified source identity, while
  no production command or CI step invokes both preflight and source resolution.
- The protected manifest uses chapter paths without `chapters/`, has null source
  hashes and Pandoc version, has no supporting source, and declares
  `gmd_version: "1.0"` while all 267 extraction drafts declare `"3.0"`.
- `extraction-governance.v1.yaml` and draft governance Decision 4 also declare
  GMD version `"1.0"`; changing this governed constant requires explicit GPID
  approval rather than inference from draft counts.

Relevant prior knowledge:

- The source manifest must record an immutable commit, ordered files, scopes,
  SHA-256 values, parser contract, and governed versions. The resolver must fail
  for changed or unavailable source bytes. Source:
  `.cg-docs/brainstorms/2026-08-03-extract-universal-non-welfare-schema.md`.
- Chapter 8 scope is determined from its actual source path and is
  `welfare-excluded`; naming heuristics are insufficient. Source:
  `.cg-docs/solutions/testing-patterns/2026-08-03-welfare-boundary-content-based-detection.md`.
- Earlier review findings P0.1, P0.2, P1.4, P2.24, and P2.28 identify dead
  manifest-model validation, null-hash acceptance, and skipped success-path
  tests as reproducibility risks. Source:
  `.cg-docs/reviews/2026-08-03-extract-universal-non-welfare-schema-review.md`.

The `/cg-plan-review` critique on 2026-08-25 identified ten findings. This
revision resolves all of them by adding a mandatory source-gate command and CI
checkout, governance-version cross-validation, an exact parser contract,
immutable action pinning, a dedicated source-lock decision record, stable I/O
errors, ordered source enforcement, explicit environment setup, a test-complete
Phase 1, and a corrected manifest comment contract.

### Human Decision Proposal

Present the following as one indivisible GPID approval ballot. Approval must
cite a durable decision record; a conversation summary or roadmap status is not
sufficient.

| Item | Exact proposal | Current evidence/status |
|------|----------------|-------------------------|
| SL1 | Approve repository `https://github.com/GMD-hub/GMD-guidelines` at commit `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` and the eight governed files listed below. | Commit is established by the extraction brainstorm; file hashes supplied for seven valid SHA-256 values, with chapter 7 unresolved. |
| SL2 | Add `docs/GMD_household_survey_harmonization.md` to `supporting_files` with scope `supporting`; it is authoritative supporting canonical Markdown, not an independently inventoried chapter. | Path is named as authoritative in `AGENTS.md` and existing provenance. |
| SL3 | Set `gmd_version: "3.0"` in both protected extraction YAML files, narrowly superseding only the `gmd_version: "1.0"` value in `Extraction-Preflight-2026-08.md` Decision 4. | All 267 drafts declare `"3.0"`, but that consistency is evidence for a proposal, not approval. |
| SL4 | Pin the future parser runtime to Pandoc `3.1.12`; set manifest scalar `installation_method: "pandoc/actions/setup@86321b6dd4675f5014c611e05088e10d4939e09e"`; install it with that action commit (`v1`); require exact runtime agreement at preflight. The scalar records the approved CI installation mechanism and does not claim or verify how a local executable was installed. Treat the Pandoc version, scalar, and action commit as governed values. Do not claim this was the historical August runtime. | The annotated `v1` tag was independently resolved to the proposed commit on 2026-08-25; the version, method, and action commit still require GPID approval. |
| SL5 | Keep `chapters/chapter8-CONS.qmd` in the governed manifest with scope `welfare-excluded`; chapters 2-7 remain `included`. | Existing governance Decision 10 establishes the chapter 8 welfare boundary. |

Governed file proposal:

| Path | Scope | Proposed SHA-256 |
|------|-------|-----------------|
| `chapters/chapter2-IDN.qmd` | `included` | `5e25f7bc25031e102f8152feab8236c6384f1a3a438fcfb4e9d7b85f16da3e39` |
| `chapters/chapter3-GEO.qmd` | `included` | `850d635bb2cb36703e756d307e24cf33c94101e95c6ba5b9027fb44f1044e32e` |
| `chapters/chapter4-DEM.qmd` | `included` | `f091a0c110d931b911799618005a31dab9375794f68aca270653f9dc5d07acd0` |
| `chapters/chapter5-LMR.qmd` | `included` | `c46796103d86412daf8d38bd56fbe118e669aa319d7948822a3476239c6d0d40` |
| `chapters/chapter6-UTL.qmd` | `included` | `e8cb9818dd8c69317e7bb752d7afab9d6d3bc60c22526a72f751fe449bea1ba0` |
| `chapters/chapter7-DWL.qmd` | `included` | **BLOCKED: recompute from the pinned commit. The supplied value is 60 characters, not SHA-256.** |
| `chapters/chapter8-CONS.qmd` | `welfare-excluded` | `1fc00a05f15422d7217c41147df24dc76f82417f8fc3c725889ef97354946b31` |
| `docs/GMD_household_survey_harmonization.md` | `supporting` | `30cc0f581b5f0183a303357157379f419356619e4b2847b43da8445a97012136` |

Before presenting SL1 for approval, an authorized operator must recompute all
eight hashes from the named paths at the exact commit. Any mismatch replaces
the supplied evidence and blocks approval pending investigation; no value may
be padded, normalized, or inferred.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Require repository URL equality with `https://github.com/GMD-hub/GMD-guidelines` (no alternate host, repository, `.git`, or trailing-slash variant); require every included, supporting, and welfare-excluded file to have a 64-character lowercase hexadecimal SHA-256 value; require the repository revision to be an exact 40-character lowercase hexadecimal commit SHA-1. | User acceptance criteria; SL1; deterministic extraction contract |
| R2 | Enforce the exact ordered `source_files` sequence `chapters/chapter2-IDN.qmd` through `chapters/chapter8-CONS.qmd`, with chapters 2-7 `included` and chapter 8 `welfare-excluded`, followed by the exact singleton `supporting_files` sequence containing `docs/GMD_household_survey_harmonization.md` as `supporting`; reject omissions, extras, reorderings, duplicates, traversal, and scope mismatches. | User implementation requirements; governance Decision 10; ordered manifest contract |
| R3 | Validate manifest I/O and content through `SourceManifest`; translate non-file, read, decode, YAML, nonmapping, and Pydantic failures into stable chained `PreflightError`s. | Review P0.1/P2.24; plan review P2.3 |
| R4 | Define `ParserContract.tool` as `Literal["pandoc"]`, require nonblank `version` and `installation_method`, execute `[parser.tool, "--version"]` without a shell and with a timeout, and require an exact parsed runtime version. | User implementation requirements; SL4; plan review P1.3 |
| R5 | Load `extraction-governance.v1.yaml` during preflight; require nonblank and equal manifest/governance schema and GMD versions, and require the governance module source paths to equal the ordered included chapter 2-7 paths. | Objective; SL3; plan review P1.2 |
| R6 | Resolve both `source_files` and `supporting_files` in declared order; fail for absent, non-file, unreadable, unsafe, or hash-mismatched paths and for a checkout whose `HEAD` differs from the manifest commit. | User implementation requirements and acceptance criteria |
| R7 | Add one supported source-gate CLI that accepts manifest, governance, and checkout paths, invokes preflight then source resolution, and exits nonzero on either failure; invoke this command before extraction and in CI. | Acceptance criteria; plan review P1.1 |
| R8 | Add focused deterministic tests for every model, I/O, governance, parser-runtime, checkout, path, ordering, readability, hash, supporting-source, source-gate, and success class; make Phase 1 focused and full-suite green without protected-file changes. | User validation commands; review P1.4; plan review P2.5/P2.6 |
| R9 | Prepare an exact, unapplied diff for SL1-SL5 in a dedicated source-lock decision record and require a durable GPID approval before an authorized maintainer changes extraction configuration or CI. | Human Approval Gate; AGENTS.md; plan review P2.2 |
| R10 | After approval only, apply the approved decision/manifest/governance values, add the immutably pinned Pandoc setup and external GMD checkout to `.github/workflows/validate.yml`, run the source-gate command, and rerun focused/full tests. | User implementation requirements; plan review P1.1/P2.1 |

## Execution Prerequisites

Before implementation, verify `python3` is Python 3.10 or newer. If `.venv` is
absent, create the ignored local environment and install the existing locked
dependency ranges; do not add a dependency for this work:

```bash
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install --requirement requirements.txt
```

If `.venv` already exists, do not recreate it; verify its Python version and
install/synchronize `requirements.txt`. Inability to establish this environment
is a blocked-stop condition, not permission to substitute untracked tooling.

## Phase 1: Generic Fail-Closed Enforcement

### 1. Strengthen Manifest and Parser Identity Models

- **Requirements**: R1, R4
- **Files**: `schema/extraction/manifest.py`, `tests/extraction/test_manifest_models.py`
- **Details**: Make `SourceFileEntry.sha256` required and validate it against
  lowercase `[0-9a-f]{64}`. Tighten repository commit validation to exact
  lowercase `[0-9a-f]{40}` rather than silently normalizing uppercase or
  accepting a symbolic revision. Require exact repository URL equality with
  `https://github.com/GMD-hub/GMD-guidelines`; do not normalize alternate URL
  representations. Define `ParserContract.tool` as
  `Literal["pandoc"]`; add the exact field `installation_method: str`; validate
  `version` and `installation_method` as nonblank. This is the proposed
  future-runtime contract until SL4 is approved. Add nonblank validation for
  manifest governance version references. Extend `ResolvedSource` with an
  ordered `supporting_files: list[SourceFileEntry]` so both collections remain
  separately visible and verified. Keep Pydantic `extra="forbid"` behavior.
- **Test Scenarios**: happy path (complete lowercase identities); edge cases
  (uppercase, 63/65-character, non-hex hashes); error paths (wrong repository,
  trailing slash, `.git` suffix, null or omitted
  file hash, null/short/uppercase/symbolic commit, alternate parser tool, blank
  parser version, and missing/blank installation method).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_manifest_models.py -q`
- **Acceptance criteria**: No manifest model can represent an unpinned source
  file or malformed repository revision, and valid source/supporting entries
  round-trip without losing scope or hash.

### 2. Make Preflight Validate I/O, Ordering, Governance, and Runtime

- **Requirements**: R2, R3, R4, R5
- **Files**: `extraction_pipeline/preflight.py`, `tests/extraction/test_preflight.py`
- **Details**: Extend `run_preflight` to accept explicit `manifest_path` and
  `governance_path` inputs, with existing project paths as defaults. For each
  YAML file, reject a missing path, directory, read error, invalid UTF-8, YAML
  parse error, nonmapping root, or schema failure as a chained
  `PreflightError`; preserve the original exception as `__cause__`. Parse the
  manifest through `SourceManifest.model_validate` and retain a normalized-dict
  return contract for current callers. Enforce ordered list equality, not set
  equality: source entries must be chapters 2, 3, 4, 5, 6, 7, then 8 with the
  approved scopes, and supporting entries must be the single canonical Markdown
  path. Reject duplicates across both collections and paths that are absolute,
  contain `..`, or resolve outside the checkout contract. Cross-check nonblank
  `schema_version` and `gmd_version` for equality between manifest and
  governance config; require governance module `source_chapter` values, in
  module order, to equal included chapter 2-7 paths. Execute
  `[parser.tool, "--version"]` with `shell=False`, captured text, and a
  10-second timeout. Accept only first-line grammar
  `^pandoc ([0-9]+(?:\.[0-9]+){1,3})$`, then compare the captured version to the
  manifest exactly. Treat missing executable, timeout, nonzero exit, empty or
  malformed output, suffix drift, and version mismatch as blocking. Tests mock
  process and read boundaries rather than machine permissions/runtime.
- **Test Scenarios**: happy path (complete synthetic manifest and matching
  runtime and matching governance); edge cases (reordered chapter list, wrong
  directory, duplicate across source/supporting, wrong scope, extra source,
  blank governance values, governance module-path drift, parser suffix/patch
  drift); error paths (manifest/governance path is a directory, mocked read or
  decode failure, malformed YAML, nonmapping YAML, null/malformed hashes,
  missing supporting file, missing Pandoc, timeout, nonzero process, malformed
  output, wrong version).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_preflight.py -q`
- **Acceptance criteria**: The committed null manifest fails loudly, while a
  complete synthetic manifest passes only with ordered paths, matching
  governance identity, and an exact mocked Pandoc runtime.

### 3. Verify Checkout Revision and Every Governed Byte

- **Requirements**: R6
- **Files**: `extraction_pipeline/source.py`, `tests/extraction/test_source.py`
- **Details**: Build one ordered governed-entry stream from `source_files` and
  `supporting_files` without sorting or set conversion. Verify the local
  checkout's resolved `HEAD` equals the
  manifest commit before reading content. Reject missing roots, non-files,
  unreadable files, unsafe resolved paths/symlink escapes, and all hash
  mismatches with path-specific, chained `SourceResolutionError` messages. Remove the
  hash-only/null fallback and set `verified_sha256=True` only after all eight
  expected hashes match. Preserve source and supporting entries separately in
  `ResolvedSource`; assert the emitted collection order equals the manifest.
- **Test Scenarios**: happy path (synthetic checkout at expected commit with all
  eight matching bytes in manifest order); edge cases (supporting file present,
  nested chapter paths, symlink/path escape, preserved ordering); error paths
  (wrong `HEAD`, Git command failure,
  absent/non-file/unreadable source, absent supporting source, one mismatched
  hash).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_source.py -q`
- **Acceptance criteria**: A successful resolution proves commit identity and
  all eight expected byte hashes; no partial or hash-only result can be reported
  as verified.

### 4. Add the Mandatory Source-Gate Entry Point

- **Requirements**: R7
- **Files**: `extraction_pipeline/source_gate.py`,
  `tests/extraction/test_source_gate.py`, `extraction_pipeline/orchestrator.py`
  (caller-contract documentation only unless wiring requires a minimal code
  change)
- **Details**: Add the sole supported source-verification command:
  `.venv/bin/python -m extraction_pipeline.source_gate --manifest <path>
  --governance <path> --checkout <path>`. Parse arguments without optional
  implicit source discovery. Invoke `run_preflight(manifest_path,
  governance_path)` first and pass its validated manifest to `resolve_source`;
  generate one UTC ISO-8601 `resolved_at` timestamp (with `Z`) through an
  injectable clock and pass it as the resolver's required third argument. Do
  not expose volatile time as a CLI identity input. Never resolve bytes after
  failed preflight. Return exit code 0 only when the
  parser runtime, governance identity, checkout `HEAD`, and all eight hashes are
  verified; catch known preflight/source failures, log one actionable error, and
  return nonzero without a traceback by default. Document in `orchestrator.py`
  that callers must use this gate before item orchestration. CI and documented
  extraction execution must invoke this command; direct calls to the two helper
  functions remain test/library APIs, not the supported operational path.
- **Test Scenarios**: happy path (preflight then resolution called once in
  order with one injected UTC timestamp); edge case (explicit nondefault paths
  forwarded unchanged); error paths
  (argument error, preflight failure prevents resolver call, source failure,
  unexpected exception is not reported as success).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_source_gate.py -q`
- **Acceptance criteria**: One executable command proves all source identity
  layers and is the command used by CI; no operational path can claim source
  verification from preflight or hashing alone. At least one success test uses
  real `run_preflight` and `resolve_source` against temporary manifest,
  governance, and eight-file checkout fixtures while mocking only the Pandoc
  and Git process boundaries; helper-only mocks are insufficient.

### 5. Consolidate Focused Fixtures and Complete Phase 1 Regression Coverage

- **Requirements**: R8
- **Files**: `tests/extraction/test_manifest_models.py`,
  `tests/extraction/test_preflight.py`, `tests/extraction/test_source.py`,
  `tests/extraction/test_source_gate.py`,
  `tests/extraction/test_manifest.py` only where its legacy path/null assertions
  conflict with the new fail-closed contract
- **Details**: Use local pytest fixtures/builders for a complete manifest and
  eight-file checkout and matching governance config, extracting shared fixture
  code only if duplication is material. Replace tests that skip against null
  protected values with explicit
  failure assertions or complete synthetic success fixtures. Parameterize
  equivalent malformed-hash/path cases and keep process/filesystem failures
  deterministic across platforms.
- **Test Scenarios**: happy path (all focused suites pass); edge case (current
  protected manifest remains invalid before approval); error path (each failure
  class has a non-vacuous assertion on its blocking exception).
- **Tests**: `.venv/bin/python -m pytest tests/extraction/test_manifest_models.py -q`;
  `.venv/bin/python -m pytest tests/extraction/test_preflight.py -q`;
  `.venv/bin/python -m pytest tests/extraction/test_source.py -q`;
  `.venv/bin/python -m pytest tests/extraction/test_source_gate.py -q`;
  `.venv/bin/python -m pytest tests/ -q`
- **Acceptance criteria**: Every listed failure class and the complete success
  path are executed, no success assertion depends on a skip, and the full suite
  passes without changing protected configuration. Phase 1 is not complete or
  committable until all five commands are green and a path-only diff confirms
  no protected config, governance decision, or workflow file changed.

## Phase 2: Governed Decision and Conditional Activation

### 6. Present the Dedicated Source-Lock Decision and Exact Diff

- **Requirements**: R9
- **Files**: this plan plus approval/PR/work-report text only before approval;
  proposed governed targets are
  `governance/decisions/Extraction-Source-Lock-2026-08.md`,
  `extraction/config/source-manifest.v1.yaml`,
  `extraction/config/extraction-governance.v1.yaml`, and
  `.github/workflows/validate.yml`
- **Details**: Recompute all eight hashes from the pinned checkout, replace the
  blocked chapter 7 value, and present SL1-SL5 plus an exact unified diff. The
  dedicated decision record must begin as `status: draft`, identify GPID Team as
  authority, keep SL1-SL5 distinct from Decisions 1-11 in the older preflight
  record, include one locatable approval reference per ballot, and state that
  SL3 supersedes only the old GMD-version value. It may be marked approved only
  by an authorized maintainer after the cited decision. The
  manifest diff must add `chapters/` prefixes, the supporting Markdown entry,
  all hashes, the commit, approved GMD version, Pandoc version, and installation
  method with exact scalar
  `"pandoc/actions/setup@86321b6dd4675f5014c611e05088e10d4939e09e"`.
  The scalar records the approved CI mechanism, not local installation
  provenance. Correct the manifest header comment: approved hashes are independently
  recomputed at the approved commit and applied through the recorded decision;
  the resolver verifies and never generates approved identity values. The
  governance diff must align GMD version and ordered module source paths. The CI
  diff must use
  `pandoc/actions/setup@86321b6dd4675f5014c611e05088e10d4939e09e`
  with `version: "3.1.12"`, identify the commit as `v1` in a comment, check out
  GMD-guidelines at the exact source commit, and invoke the source-gate command.
  Any change to the action commit requires regeneration and reapproval. Do not
  apply governed hunks before a durable GPID approval references SL1-SL5.
- **Test Scenarios**: happy path (all ballot items approved with corrected hash
  evidence); edge case (approval changes one proposed value, requiring diff
  regeneration); error path (partial/verbal approval, malformed chapter 7 hash,
  hash mismatch, or historical-runtime inference request).
- **Tests**: static diff review plus independent `sha256` recomputation against
  commit `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`
- **Acceptance criteria**: The dedicated decision proposal and exact diff are
  reviewable and unapplied until all five source-lock decisions have locatable
  approval records; any unresolved item leaves
  the plan blocked after generic code/tests.

### 7. Apply Approved Configuration and CI Activation

- **Requirements**: R10
- **Files**: `governance/decisions/Extraction-Source-Lock-2026-08.md`,
  `extraction/config/source-manifest.v1.yaml`,
  `extraction/config/extraction-governance.v1.yaml`,
  `.github/workflows/validate.yml`
- **Details**: This step is human-gated. An authorized maintainer applies only
  the exact approved values, records the approval reference, installs Pandoc
  `3.1.12` in CI through the approved immutable action commit. Add a second
  `actions/checkout@v4` step with `repository: GMD-hub/GMD-guidelines`,
  `ref: d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`,
  `path: gmd-guidelines`, and `persist-credentials: false`. After Python
  dependencies and Pandoc are available, run:

  ```bash
  python3 -m extraction_pipeline.source_gate \
    --manifest extraction/config/source-manifest.v1.yaml \
    --governance extraction/config/extraction-governance.v1.yaml \
    --checkout gmd-guidelines
  ```

  This command must pass before extraction-related tests. If approval is
  unavailable, do not begin this step:
  retain the generic implementation and stop with the proposed diff.
- **Test Scenarios**: happy path (approved checkout and runtime pass preflight);
  edge case (CI installs a different patch version and fails); error path
  (manifest hash/path drift or absent approval prevents activation).
- **Tests**: all five focused/full pytest commands, the explicit source-gate
  command, and a CI workflow run against the approved checkout
- **Acceptance criteria**: Protected files exactly match the recorded decision,
  CI checks the approved future Pandoc runtime, the approved checkout resolves
  with all hashes verified, and focused/full tests pass.

## Testing Strategy

- Keep model tests pure and parameterized around exact digest shapes.
- Mock process boundaries for Pandoc, YAML I/O, and isolated Git failure cases; use a
  temporary Git checkout or a deterministic injected result for the successful
  checkout-revision path.
- Use `tmp_path` for all source trees and manifests; do not rewrite the
  protected manifest in tests.
- Assert both exception type and stable message fragment for every fail-closed
  branch, and assert exception chaining for wrapped I/O/parser failures.
- Exercise the source-gate CLI as the integration boundary; verify preflight
  failure prevents checkout resolution and every failure returns nonzero.
- Run focused suites first, then the full repository suite:

```bash
.venv/bin/python -m pytest tests/extraction/test_manifest_models.py -q
.venv/bin/python -m pytest tests/extraction/test_preflight.py -q
.venv/bin/python -m pytest tests/extraction/test_source.py -q
.venv/bin/python -m pytest tests/extraction/test_source_gate.py -q
.venv/bin/python -m pytest tests/ -q
```

- Before approval, explicitly verify that the source-gate command against
  `extraction/config/source-manifest.v1.yaml` fails because protected identity
  values/paths and governance paths are stale or missing. After approval, run
  the exact source-gate command against the approved local checkout and require
  matching manifest/governance versions, exact Pandoc, checkout `HEAD`, and all
  eight hashes.

## Documentation Checklist

- [ ] Record the durable GPID approval references for SL1-SL5 in
      `governance/decisions/Extraction-Source-Lock-2026-08.md`.
- [ ] State that Pandoc `3.1.12` is a future reproducible runtime, not evidence
      of the historical August runtime.
- [ ] Document all eight governed paths, scopes, hashes, and the repository
      commit in the approved manifest/decision record.
- [ ] Document chapter 8 as `welfare-excluded` and the rendered Markdown as
      supporting rather than inventory-bearing.
- [ ] Keep error messages actionable without suggesting that agents edit
      protected configuration without approval.
- [ ] Correct the manifest header to state that the resolver verifies approved
      hashes but never generates or applies them.
- [ ] Document the source-gate command as the supported operational entry point.

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Supplied chapter 7 digest is incomplete or another supplied digest mismatches the pinned bytes | High for chapter 7 | High | Recompute all eight from the exact commit; block approval and activation on any mismatch. |
| Pydantic validation changes break dict-based callers | Medium | Medium | Validate once in `load_manifest`, return a normalized dict for current consumers, and cover end-to-end preflight. |
| Runtime checks become machine-dependent | Medium | Medium | Mock Pandoc in unit tests; reserve real-runtime verification for approved CI/preflight. |
| Supporting files remain omitted from one resolver path | Medium | High | Build one combined ordered verification stream and assert separate source/supporting outputs. |
| Protected config is applied from an incomplete or informal approval | Low | High | Require the dedicated record to cover SL1-SL5 and compare the applied diff to the ballot. |
| GMD version `3.0` is inferred from drafts despite contrary draft governance | Medium | High | Treat draft consistency only as evidence; do not change either YAML until GPID explicitly supersedes Decision 4. |
| CI action/version method changes during approval | Low | Medium | Pin the action to `86321b6dd4675f5014c611e05088e10d4939e09e`; regenerate and reapprove if it changes. |
| Callers bypass source verification and invoke item orchestration directly | Medium | High | Make `source_gate` the sole supported operational entry point, document the orchestrator precondition, invoke it in CI, and integration-test call ordering. |
| Manifest and governance versions or module paths drift independently | Medium | High | Cross-validate both YAML documents during every preflight and source-gate run. |

## Out of Scope

- Inferring or reconstructing the historical August Pandoc runtime.
- Changing any of the 267 extraction drafts or their `gmd_version` values.
- Extracting additional variables or changing harmonization rules.
- Modifying approved artifacts under `knowledge/` or country-specific content.
- Refactoring unrelated extraction pipeline modules or adding dependencies.
- Immutably pinning pre-existing unrelated GitHub Actions; this plan pins the
  newly introduced Pandoc action and source revision only.
- Applying any protected configuration or workflow value without recorded GPID
  approval.

## Completion Contract

### Outcome

The supported source-gate command fails closed unless manifest and governance
versions/module paths, the local Git checkout, all eight governed files, and the
installed Pandoc runtime exactly match approved identities. Protected decision,
configuration, and CI activation changes occur only after durable GPID approval
resolves SL1-SL5 and the malformed chapter 7 digest.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|-------------------|------------------|----------|
| V1 | 1 | Manifest/parser models require the exact repository URL; reject null, uppercase, short, non-hex, blank, URL-variant, or alternate-tool identities; and preserve ordered source/supporting facts | `.venv/bin/python -m pytest tests/extraction/test_manifest_models.py -q` | yes |
| V2 | 1 | Preflight wraps manifest/governance I/O failures, enforces exact ordered paths/scopes, cross-validates versions/module paths, and rejects absent/wrong/malformed/timed-out Pandoc runtime | `.venv/bin/python -m pytest tests/extraction/test_preflight.py -q` | yes |
| V3 | 1 | Source resolution rejects absent, unreadable, unsafe, commit-mismatched, and byte-mismatched files; a synthetic checkout resolves all eight governed files in order | `.venv/bin/python -m pytest tests/extraction/test_source.py -q` | yes |
| V4 | 1 | The source-gate CLI invokes preflight before resolution, supplies one injectable UTC `resolved_at`, exits nonzero on either failure, and has a real-helper integration success proving complete identity | `.venv/bin/python -m pytest tests/extraction/test_source_gate.py -q` | yes |
| V5 | 1 | Phase 1 has no repository regressions and no protected-file changes | `.venv/bin/python -m pytest tests/ -q`; `git diff --name-only` | yes |
| V6 | 2 | Dedicated SL1-SL5 decision proposal and exact protected diffs include corrected chapter 7 evidence, manifest comment, immutable Pandoc action, and external checkout/source-gate CI steps | Approval ballot plus execution report/PR handoff diff | yes |
| V7 | 2 | Locatable GPID approval resolves SL1-SL5 before the dedicated decision, protected configuration, or CI is applied | `governance/decisions/Extraction-Source-Lock-2026-08.md` plus authorized maintainer diff | yes |
| V8 | final | Approved checkout passes the exact supported source-gate command in CI and all focused/full tests pass | `.github/workflows/validate.yml` run and source-gate output | yes |
| V9 | final | Final diff contains only generic source-lock code/tests and, only after V7, approved decision/config/Pandoc workflow changes | `git diff --name-only` and `git diff --check` | yes |

### Constraints

| ID | Phase | Constraint | Check |
|----|-------|------------|-------|
| C1 | 1 | Do not modify the dedicated governance decision, `extraction/config/*.yaml`, or `.github/workflows/validate.yml` before recorded GPID approval | Diff inspection before and after Phase 1 |
| C2 | final | Do not claim Pandoc `3.1.12` was the historical August runtime | Decision proposal and changed comments contain future-runtime wording only |
| C3 | 1 | Every governed path is exact, ordered, and traversal-safe; every file digest is lowercase SHA-256 | Model/preflight/source negative tests |
| C4 | 1 | Chapters 2-7 are included, chapter 8 is `welfare-excluded`, canonical Markdown is supporting, and manifest/governance versions/module paths agree | Synthetic preflight and source-gate tests |
| C5 | final | No approved CVS artifacts, extraction drafts, country parameters, or unrelated workflow behavior changes | Final path and diff review |

### Boundaries

- Allowed: `schema/extraction/manifest.py`,
  `extraction_pipeline/preflight.py`, `extraction_pipeline/source.py`,
  `extraction_pipeline/source_gate.py`, narrow orchestrator caller-contract
  documentation, focused extraction tests/fixtures, and an exact
  decision/config proposal.
- Conditionally allowed after approval:
  `extraction/config/source-manifest.v1.yaml`,
  `extraction/config/extraction-governance.v1.yaml`,
  `governance/decisions/Extraction-Source-Lock-2026-08.md`, and
  `.github/workflows/validate.yml`.
- Out of scope: changing extraction drafts, `knowledge/`, or country parameters;
  inferring historical runtime facts; extracting variables; or changing
  harmonization rules.

### Iteration Policy

1. Establish the documented Python environment, then implement generic
   fail-closed models, preflight, source resolution, and source-gate code without
   touching protected files.
2. Fix focused-test failures within the listed files and require all focused
   suites plus the full suite before Phase 1 completion.
3. Record the dedicated SL1-SL5 proposal, exact protected-file diff, and corrected chapter 7 digest
   evidence.
4. Under `deviation-policy: ask`, pause before any material scope or contract
   change.
5. Begin dedicated decision/config/CI activation only after locatable GPID
   approval resolves SL1-SL5.
6. If approval is unavailable, preserve Phase 1 results and stop blocked with
   the exact unapplied proposal.

### Blocked-Stop Conditions

- The complete 64-character chapter 7 SHA-256 cannot be independently
  established at the pinned commit or any supplied hash mismatches.
- `gmd_version`, supporting-file scope, chapter 8 scope, Pandoc version, or
  installation method remains unresolved.
- The local checkout cannot be proven to be exactly the approved commit.
- A request would infer the historical August Pandoc runtime.
- Any protected config or workflow change is requested without recorded GPID
  approval.
- Python 3.10+ and the `.venv` dependency environment cannot be established.
- The dedicated SL1-SL5 record is ambiguous, partially approved, or attempts to
  approve unrelated Decisions 1-11 by implication.
- The approved Pandoc action commit differs from
  `86321b6dd4675f5014c611e05088e10d4939e09e` without reapproval.
- The source-gate command is absent from CI or can report success without both
  preflight and source resolution passing.
- Required focused or full-suite verification remains failing after in-scope
  recovery.
