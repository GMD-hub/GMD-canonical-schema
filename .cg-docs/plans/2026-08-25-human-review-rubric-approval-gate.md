---
date: 2026-08-25
title: "Implement Human Review Rubric and Approval Gate"
status: active
scope: "Deep"
brainstorm: ".cg-docs/brainstorms/2026-08-07-calibrate-human-review.md"
language: "both"
estimated-effort: "large"
deviation-policy: "ask"
artifact-schema-version: 1
phases: 3
tags: [human-review, rubric, approval-gate, shiny, r, python, optimistic-locking, governance, testing]
---

# Plan: Implement Human Review Rubric and Approval Gate

## Objective

Extend v2 review records with a complete, auditable human-assessment snapshot
and enforce the finalized two-layer promotion rubric at the server boundary.
Approvals must remain globally disabled, but the app and direct action API must
be ready to deny every approval whose persisted assessment, blocker state,
source binding, or queue controls are incomplete, failing, or stale.

## Context

The finalized rubric in `.cg-docs/calibration/review-rubric.md` requires a
passing automated Layer 1 result, one `pass` or noted `revise` rating for each
of seven Markdown sections, and no unresolved `block` or `major` content error.
Agent-review findings are explicitly reserved as a future gate, so this task
records their identity and disposition without making them approval-eligible
criteria.

Release A already provides strict v2 record parsing, a production queue
manifest and index, source binding, role-gated actions, atomic review-branch
writes, and optimistic locking. The current assessment scaffold is not yet
sufficient for this rubric:

- `review-app/R/models.R` stores only status/evidence pairs for Layer 1 and
  agent review, permits partial Layer 2 coverage, requires notes for `revise`
  but not `fail`, and does not bind an assessment to the reviewed body/source.
- `review-app/R/queue_manifest.R` considers any non-empty Layer 2 list and an
  agent-review `pass` eligible, rather than requiring the exact seven sections
  and treating agent review as provenance-only.
- `review-app/R/actions.R` rereads the v2 controls but evaluates the caller's
  in-memory record during approval. A caller-mutated assessment must never be
  able to bypass the persisted record.
- `review-app/R/mod_detail.R` displays approval only when the current helper
  returns true, but has no assessment form or persistence action. UI hiding is
  not an authorization or approval boundary.

Existing persisted v2 scaffold records are a concrete compatibility concern.
They must remain readable as explicitly incomplete and ineligible; they must
not be silently treated as complete or require a bulk production migration.
The selected compatibility policy is a lazy deterministic migration: the exact
Release A scaffold normalizes to the expanded pending shape on read and is
serialized on the next authorized v2 write of any kind. This behavior must be
explicit in tests and audit diffs.

No new runtime package is expected. The implementation should reuse `yaml`,
`shiny`, the GitHub adapter, source binding, canonical serialization, and
`testthat` already declared by `review-app/DESCRIPTION`. A build-time Python
compiler produces a dedicated source-byte-bound Pydantic attestation using the
repository's existing Pydantic/PyYAML stack. The Shiny process consumes that
immutable YAML through a separately locked evidence commit/blob and never
invokes Python. Existing records do not need their historical `source_commit`
to contain the new artifact; their enrolled source bytes must match an entry in
the evidence artifact.

### Brain Findings Applied

1. Preserve the existing Git-backed state machine and atomic action path rather
   than introducing separate assessment storage. Source:
   `.cg-docs/plans/2026-08-04-build-human-review-application.md`.
2. Keep agent-review findings non-gating until a later governed enablement.
   Source: `.cg-docs/plans/2026-08-07-calibrate-human-review.md` and
   `.cg-docs/calibration/review-rubric.md`.
3. Exercise Golem modules with namespaced inputs and verify installed-package
   behavior with `R CMD check`. Source:
   `.cg-docs/solutions/testing-patterns/2026-08-10-golem-module-testserver-capture.md`.

### Plan Review Findings Resolved

The `/cg-plan-review` pass on 2026-08-25 returned five P1 and three P2
findings. This revision resolves all eight:

| Finding | Resolution |
|---------|------------|
| P1.1 undefined trusted evidence boundary | Step 1 names immutable evidence paths, identities, validators, human-owned payload fields, and fail-closed behavior. |
| P1.2 incomplete source lock | The assessment binding now includes `source_commit`; Step 7 defines a pre-publication default-branch head/path/blob/content check. |
| P1.3 caller record remains write base | Step 7 makes the reread persisted record the sole transition, event, path, and serialization base. |
| P1.4 caller-controlled legacy read-only flag | Steps 5 and 9 require the public action boundary to derive routing from the adapter and reject legacy records without a caller override. |
| P1.5 unrunnable verification commands | Step 10 fixes `devtools::test("review-app")`, adds `.venv` preflight, and cleans generated R check artifacts. |
| P2.1 Layer 1 not enforced at submission | Step 3 adds a server-side submission gate that persists machine evidence atomically. |
| P2.2 incomplete race matrix | Steps 7-8 add body, approved-destination, and review-ref races to manifest/index/record/source races. |
| P2.3 implicit scaffold migration | Context, Step 2, and tests adopt and verify lazy expansion on every authorized v2 write. |

The verification review then identified one remaining P1 and two P2 details;
this revision also resolves them:

| Finding | Resolution |
|---------|------------|
| Verification P1.1 aggregate schema-compliance evidence is stale/overbroad | Step 1 adds a dedicated Pydantic-only attestation with source path/blob/content and validation-context identities; aggregate agent `summary.passed` is never a Layer 1 gate. |
| Verification P2.1 retry/no-publication contradiction | Step 7 distinguishes one recoverable unrelated ref retry from non-retryable selected-path and source races; Step 8 tests each outcome. |
| Verification P2.2 Python timestamp incompatibility | Steps 1-2 define a strict evidence-specific RFC 3339 parser that accepts fractional seconds and offsets while preserving the original value. |

The final verification pass raised three additional consistency issues, also
resolved here:

| Finding | Resolution |
|---------|------------|
| Final P1.1 historical enrolled commits cannot contain a new attestation | Step 1 resolves a separately locked `evidence_commit` and binds it into the assessment; existing records match by enrolled source bytes and need Task E only when source bytes changed. |
| Final P1.2 validator/context digests were stored but not consumed | Step 1 requires an exact ordered path-to-Git-blob manifest and runtime comparison against the evidence commit tree, including missing/extra inputs. |
| Final P2.1 timestamp broke deterministic output | The compiler derives `generated_at` from required `SOURCE_DATE_EPOCH`; equal inputs and epoch produce byte-identical YAML. |

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Persist a versioned v2 assessment containing server-generated Layer 1 result, validator identity, immutable evidence identity, and timestamp. | Invocation requirement 1; rubric Layer 1 |
| R2 | Persist exactly one entry for each of the seven required Markdown sections, with rating `pass`, `revise`, or `fail`; require a non-empty note for every `revise` and `fail`. | Invocation requirements 1-2; rubric lines 40-58 |
| R3 | Persist an approver-attested content-error snapshot whose digest, actor, and timestamp are server-generated and whose items carry severity, status, and evidence; unresolved `block`/`major` items deny approval. | Invocation requirements 1 and 5; rubric lines 63-71 |
| R4 | Read immutable per-artifact agent-review evidence at the locked evidence commit and persist its server-computed snapshot identity and disposition, without activating it as an approval criterion. | Invocation requirement 1; rubric lines 73-74 |
| R5 | Bind an assessment to enrolled `source_commit`/source blob/content, the exact persisted Markdown body, and separate evidence commit/attestation/context identities; missing, partial, malformed, or stale assessments are never eligible. | Invocation requirements 2, 5, and 6; final review P1.1/P1.2 |
| R6 | Display assessment evidence and section ratings to reviewers and approvers; allow only approvers to edit/persist ratings, notes, and content-error attestations; keep YAML front matter and machine evidence read-only. | Invocation requirements 3-4 |
| R7 | Preserve role boundaries: reviewers save/edit/submit, approvers assess/request revision/approve, and administrators manage queue controls. | Invocation requirement 4 |
| R8 | Make `queue_approval_eligible()` implement the finalized rubric, dependency/blocker checks, assessment binding, and fail-closed validation. | Invocation requirement 5 |
| R9 | At approval, reread and optimistic-lock manifest, index, persisted record, reviewed body, approved destination, review ref, and source; use only reread persisted data as the transition/write base. | Invocation requirement 6; plan review P1.2/P1.3/P2.2 |
| R10 | Preserve legacy `review` branch records as read-only at the exported server action boundary without a caller-controlled override. | Invocation requirement 7; plan review P1.4 |
| R11 | Keep `approval_mode: disabled`, leave `RUBRIC_GATE_PENDING` open, and make no production queue or approved-record writes during development/tests. | Invocation requirement 8; acceptance criteria |
| R12 | Add the requested happy-path, validation, role, direct-call, legacy, and concurrency tests in a focused approval-gate test file. | Invocation Tests section |
| R13 | Preserve existing blocker, source-drift, front-matter, and atomic-write protections and pass the full R/Python verification surface. | Acceptance criteria; merge dependency |
| R14 | Leave Task E reopen/re-enrollment changes for a branch rebased from this task after merge. | Merge dependency |
| R15 | Enforce Layer 1 server-side before `submitted`; a failing or unverifiable structural result cannot enter `in-review`. | Finalized rubric lines 11-36; plan review P2.1 |
| R16 | Restrict assessment action input to human-owned ratings, notes, and content-error entries; construct binding, evidence, actor, timestamps, and snapshot digests server-side. | Plan review P1.1 |
| R17 | Generate and consume a dedicated Pydantic-only attestation through a separately locked evidence commit/blob, bound to source path/blob/content and an exact validator/registry path-to-blob manifest; do not gate on aggregate agent-review summaries. | Verification and final review P1.1/P1.2 |
| R18 | Parse upstream Python timestamps with strict RFC 3339 fractional-second/offset support while retaining strict canonical UTC timestamps for server-stamped fields. | Verification review P2.2 |
| R19 | Permit one recoverable unrelated review-ref retry only after fully rereading/rebuilding/rechecking; selected-path/control and source-prepublish races are non-retryable and publish nothing. | Verification review P2.1 |
| R20 | Produce byte-identical attestation YAML for identical repository inputs and `SOURCE_DATE_EPOCH`; no wall-clock value enters the artifact. | Final review P2.1 |

## Implementation Steps

## Phase 1: Assessment Contract and Eligibility

### 1. Build the Pydantic Attestation and Lock Evidence Authorities

- **Requirements**: R1, R3, R4, R5, R15, R16, R17, R18, R20
- **Files**: `extraction_pipeline/review_agents/layer1_attestations.py`,
  `tests/review_agents/test_layer1_attestations.py`,
  `extraction/25_agent_review/evidence/layer1-attestations.v1.yml`,
  `review-app/R/assessment.R` (new focused domain helper),
  `review-app/R/github_adapter.R`, `review-app/R/source_binding.R`
- **Details**:
  - Add a deterministic Python compiler for the aggregate artifact
    `extraction/25_agent_review/evidence/layer1-attestations.v1.yml`. The
    subdirectory prevents the existing root-level stale-findings purge from
    deleting it.
  - Validate each of the 267 source front matters with
    `schema.variable.VariableDefinition` only, using the same explicit
    `allow_unresolved_draft`, variable-ID, rule-ID, and parameter-ID context as
    the authoritative extraction validator. Do not fold heading, placeholder,
    heuristic, warning, or other agent-review results into this Pydantic result.
  - Store artifact schema version, validator ID, validator/code SHA-256,
    normalized validation options, deterministic digests of variable/rule/
    parameter context, generation timestamp, and one entry per artifact with
    source path, Git blob SHA-1, source content SHA-256, explicit
    `pydantic_result: pass|fail`, and failure details when applicable.
  - Make validator/context identity executable rather than descriptive. Store a
    sorted exact path-to-Git-blob manifest covering the compiler, all
    `schema/**/*.py` validator code, all 267 draft inputs, and every matched
    `knowledge/rules/**/*.md` and `knowledge/parameters/*.md` registry input,
    plus Pydantic/PyYAML versions. Derive context digests from this canonical
    manifest.
  - Validate complete 267/path/module coverage before writing. Generate through
    a temporary file plus atomic replacement; tests write only to temp paths.
    This task may commit the aggregate evidence artifact but must not generate
    or modify queue records or close `RUBRIC_GATE_PENDING`.
  - Require `SOURCE_DATE_EPOCH` as compiler input and derive `generated_at`
    deterministically from it. Reject missing/invalid epochs; never call the
    wall clock. Two runs with identical repository inputs and epoch must be
    byte-identical.
  - At submission, resolve the current default-branch head as a separate
    `evidence_commit`, read the aggregate attestation at that commit, and store
    evidence commit/blob/content identities in the assessment. Existing records
    need not contain the artifact in their historical `source_commit`.
  - Verify the attestation blob and recompute the exact filtered input path set
    and Git blob identities from the evidence commit tree. Reject any missing,
    extra, or changed validator/schema/rule/parameter/draft input before
    trusting context digests or results.
  - Select exactly one artifact entry and require its path/blob/content equality
    with the record's enrolled source identities plus explicit
    `pydantic_result: pass`. Never use
    `<artifact>.schema_compliance.yml` or aggregate `summary.passed` as Layer 1
    authority.
  - Pair that attestation with an R-owned runtime validator
    (`reviewapp-layer1-v1`) over the exact persisted review body and enrolled
    front matter: YAML parses, front matter is byte-preserved, all seven
    headings occur exactly once, and every section exceeds both one sentence
    and 50 non-whitespace characters. Either component failing makes Layer 1
    `fail`; missing/unverifiable upstream evidence makes it `pending` and
    submission-ineligible.
  - Define non-gating agent-review provenance separately as all expected
    per-artifact
    `schema_compliance`, `source_grounding`, `rules_caveats`, and
    `consistency_derivation` blobs available at `evidence_commit`, plus
    the queue manifest's `agent_review.identity`/digest. Compute disposition as
    `clear`, `findings-present`, or `unavailable` from verified files. It is
    displayed but remains non-gating.
  - Define content errors as an approver-owned human attestation. The client may
    submit only items (`id`, `severity`, `status`, `evidence_ref`); the server
    validates them and generates canonical snapshot SHA-256, `captured_by`, and
    UTC `captured_at`. An empty item list is valid only as an explicit signed
    attestation; a missing snapshot is incomplete.
  - Whitelist the `assessed` action payload to section ratings/notes and
    content-error items. Reject caller-supplied Layer 1 results, source/body
    bindings, evidence identities, agent disposition, actor, timestamps, and
    snapshot digests; construct those fields from reread server state.
  - Keep evidence readers injectable and path-scoped so tests use in-memory
    GitHub fixtures and production never invokes local Python, the filesystem,
    or network services other than the existing repository adapter.
  - Add an evidence-specific strict RFC 3339 parser accepting UTC `Z` or
    `+00:00`/other numeric offsets and optional fractional seconds, matching
    current Python output. Preserve the original evidence timestamp in its
    identity and canonicalize any server-stamped derivative to whole-second UTC
    `Z`; do not relax the existing app-event timestamp validator.
- **Test Scenarios**: byte-identical compiler output with fixed
  `SOURCE_DATE_EPOCH`; missing/invalid epoch; 267 coverage; historical record
  consuming a newer evidence commit with matching source bytes; source
  path/blob/content mismatch; Pydantic pass/fail; schema/rule/parameter blob
  change or extra matched path with unchanged source; wrong entry;
  tampered/missing attestation; existing fractional `+00:00` timestamp;
  malformed timestamp; explicit empty content-error attestation; machine-field
  injection; missing agent files yield non-gating `unavailable`.
- **Tests**:
  - `.venv/bin/python -m pytest tests/review_agents/test_layer1_attestations.py -q`
  - evidence authority and payload-whitelist cases in
    `review-app/tests/testthat/test-approval-gate.R`
- **Acceptance criteria**: every machine-owned field is reproducible from an
  immutable evidence commit whose attestation, source entry, validator code,
  and registry context are all Git-identity verified; aggregate agent findings
  remain non-gating, and every human-owned field is attributable to an
  authorized approver.

### 2. Define the Expanded Assessment Model and Lazy Migration

- **Requirements**: R1, R2, R3, R4, R5, R16, R18
- **Files**: `review-app/R/models.R`; `review-app/NAMESPACE` only if a new
  public constructor/validator is intentionally exported
- **Details**:
  - Add an assessment schema/version marker while keeping
    `record_schema_version: "2.0"`.
  - Store a binding with enrolled `source_commit`,
    `source_artifact_blob_sha`, `source_content_sha256`, `body_sha256`, separate
    `evidence_commit`, attestation Git blob/content digests, and validated
    context-manifest digest; validate SHA-1/SHA-256 formats.
  - Store Layer 1 `result` (`pending|pass|fail`), validator ID, immutable
    evidence reference/digests, and check timestamp.
  - Preserve the original upstream RFC 3339 timestamp and store a separately
    canonicalized UTC value when needed; app-generated assessment/event times
    continue to use the existing whole-second `...Z` format.
  - Materialize all seven canonical section entries in order with nullable
    pending `rating` and `note`; complete values are `pass|revise|fail` and
    notes are mandatory for `revise` and `fail`.
  - Store the server-stamped content-error snapshot and the server-computed
    agent-review snapshot/disposition described in Step 1.
  - Store assessment attestation actor/time separately from machine evidence;
    both remain `NULL` until an approver saves the assessment.
  - Align content-error enums with calibration:
    `block|major|minor|info` and `open|resolved|escalated`; `open` and
    `escalated` are unresolved.
  - Recognize only the exact Release A assessment scaffold, normalize it to the
    expanded pending shape, and serialize that shape on the next authorized v2
    write of any action. This is the selected lazy migration policy; no bulk or
    production migration command is added.
  - Reject unknown fields/enums, duplicate/unknown/missing sections in a
    complete assessment, invalid timestamps/digests, and inconsistent pending
    combinations. Preserve deterministic `canonical_yaml()` round trips.
- **Test Scenarios**: expanded pending and complete round trips; exact scaffold
  normalization; unrelated `saved`/`submitted` action emits expanded pending
  form; unknown/duplicate/malformed input; no inferred pass.
- **Tests**: model and compatibility cases in `test-approval-gate.R`.
- **Acceptance criteria**: old v2 records remain readable and explicitly
  ineligible, and every subsequent authorized write has one deterministic
  expanded representation.

### 3. Enforce and Persist Layer 1 Before Submission

- **Requirements**: R1, R4, R5, R7, R9, R13, R15, R16
- **Files**: `review-app/R/actions.R`, `review-app/R/assessment.R`,
  `review-app/R/source_binding.R`, `review-app/R/state_machine.R`
- **Details**:
  - For `submitted`, reread manifest, index, record, persisted body, and source
    first; resolve/verify the separate evidence commit and run the Step 1 Layer
    1 builder from those values, never caller data.
  - Deny submission before any write when YAML/front matter/sections/stub checks
    fail or the locked evidence-commit Pydantic evidence is missing, malformed,
    or failing. Absence from the historical `source_commit` is expected and is
    not a failure when enrolled path/blob/content match the evidence entry.
    Return a specific structural/evidence reason.
  - On success, persist a fresh assessment bound to source commit/blob/content
    and body digest plus evidence commit/attestation/context identities, with
    Layer 1 and agent-review snapshots populated and all human ratings/content
    errors pending, in the same atomic record/index write as the `submitted`
    transition.
  - Existing records whose enrolled source bytes still match an attestation
    entry can submit without re-enrollment even though their historical source
    commit predates the attestation. If source bytes no longer match, fail as
    source drift and leave re-enrollment to Task E.
  - On `needs-revision -> submitted`, replace the current assessment with that
    fresh pending snapshot. Prior ratings remain in Git history; they cannot be
    carried forward to different body bytes.
  - Preserve reviewer authorization, state-machine semantics, body companion
    locking, source drift checks, event sequencing, and no-write failure paths.
- **Test Scenarios**: valid submission; missing/failing Pydantic evidence;
  missing/duplicate/stub section; front-matter mismatch; resubmission resets
  human fields; failure leaves state/record/index/ref unchanged.
- **Tests**: submission-gate cases in `test-approval-gate.R`.
- **Acceptance criteria**: no v2 artifact can enter `in-review` unless current
  persisted content has a passing, server-generated Layer 1 snapshot.

### 4. Replace Permissive Approval Eligibility with the Exact Rubric

- **Requirements**: R2, R3, R4, R5, R8, R11, R13
- **Files**: `review-app/R/queue_manifest.R`, `review-app/R/models.R`,
  `review-app/R/assessment.R`
- **Details**:
  - Keep syntactically valid pending assessments but return `FALSE` for every
    incomplete, malformed, or binding-mismatched state.
  - Require current Layer 1 `pass` with complete immutable evidence and binding
    equality for source commit/blob/content, persisted body digest, evidence
    commit/attestation, and validator-context manifest.
  - Require the exact seven sections once each. Permit only `pass` or noted
    `revise`; deny every `fail` even when it has a note.
  - Require an explicit server-stamped content-error snapshot and deny
    unresolved `block`/`major` items. Minor/info items remain context.
  - Exclude agent-review disposition from the active rubric predicate, while
    retaining Release A's manifest dependency availability check.
  - Preserve `approval_mode`, global/artifact blockers, strict manifest/record
    validation, `RUBRIC_GATE_PENDING`, and default disabled state. Tests may use
    isolated enabled/closed fixtures only to reach lower predicates.
- **Test Scenarios**: all-pass; revise-with-note; revise without note; fail with
  or without note; missing/failing Layer 1; stale binding; exact section set;
  absent content snapshot; unresolved/resolved major; adverse agent disposition
  remains non-gating.
- **Tests**: eligibility matrix in `test-approval-gate.R` and retained
  `test-production-queue.R` assertions.
- **Acceptance criteria**: eligibility exactly implements the finalized active
  rubric without changing production enablement controls.

## Phase 2: Role-Gated Persistence and Assessment UI

### 5. Persist Human Assessment Through the Existing Atomic Action Path

- **Requirements**: R3, R5, R7, R9, R10, R11, R13, R16
- **Files**: `review-app/R/authorization.R`, `review-app/R/state_machine.R`,
  `review-app/R/actions.R`, `review-app/R/models.R`,
  `review-app/R/assessment.R`
- **Details**:
  - Add non-transitioning action `assessed`, authorized only for `approver`, and
    extend event validation/`record_action()` without changing transitions.
  - Accept only Step 1's human payload. Start from the reread persisted record,
    verify current Layer 1/body/source and immutable evidence-commit identities,
    server-stamp content errors and attestation actor/time, refresh non-gating
    agent provenance from that evidence commit, and replace assessment.
  - Persist record and queue-index row through one
    `adapter_write_with_recovery()` transaction; add no assessment sidecar or
    direct write path.
  - Require expected manifest/index/record/body identities. Any concurrent
    change returns stale-write recovery and no reachable ref update.
  - Keep request-revision and approval separate. Approval consumes only a
    previously saved current assessment; unsaved form data never enters it.
  - Remove the caller-controlled `legacy_read_only` trust decision from the
    exported action boundary. Derive legacy routing from the adapter/record;
    `perform_action()` must unconditionally reject legacy records served from
    the preserved `review` branch. Pure legacy state-machine tests may use pure
    functions, not an exported write bypass.
- **Test Scenarios**: valid assessment save; reviewer/administrator denied;
  machine-field injection denied; stale controls denied; no state transition;
  direct legacy write without a read-only flag denied.
- **Tests**: direct action tests in `test-approval-gate.R`.
- **Acceptance criteria**: assessment writes are attributable, server-built,
  role-gated, optimistic-locked, atomic, and unavailable to legacy records.

### 6. Add the Reviewer/Approver Assessment Workspace

- **Requirements**: R1, R2, R3, R4, R6, R7, R10, R16
- **Files**: `review-app/R/mod_detail.R`, `review-app/R/ui_components.R`,
  `review-app/inst/app/www/custom.css` if existing classes cannot express the
  assessment layout
- **Details**:
  - Add an assessment panel alongside the Markdown workspace without moving or
    exposing the raw YAML front matter as an editable input.
  - Display Layer 1 result, validator/evidence identity, timestamp, assessment
    content/source binding status, content-error snapshot/items, and
    agent-review snapshot/disposition.
  - Render all seven sections in canonical order. Approvers receive rating and
    per-section note controls plus a compact structured content-error editor;
    reviewers receive the persisted assessment read-only while retaining their
    Markdown editor/save/submit controls.
  - Keep Layer 1, all bindings, validator/agent identities, snapshot digests,
    actor, and timestamps read-only and absent from the action payload.
  - Show inline validation for missing ratings and required `revise`/`fail`
    notes. Keep fail ratings saveable so approvers can persist evidence and
    request revision, but never approval-eligible.
  - Add an explicit Save assessment action. Track assessment dirtiness
    separately from Markdown dirtiness, and prevent approval from using unsaved
    assessment inputs.
  - On stale-write recovery, retain local rating/note inputs, display the
    recovery message, and require reload/reconciliation before retry.
  - In `legacy_read_only` mode, display any available historical context but
    render no assessment inputs or write controls.
  - Use accessible fieldsets/legends, labels, status text, and mobile behavior
    consistent with the existing app rather than introducing a new visual
    system.
- **Test Scenarios**: approver sees editable seven-section form; reviewer sees
  ratings/notes read-only; YAML remains code-only/read-only; required-note
  feedback; dirty assessment hides/disables approval; legacy has no write
  controls.
- **Tests**: `shiny::testServer()` or pure UI-helper assertions in
  `test-approval-gate.R`, using namespaced inputs and captured module returns
  where module behavior is exercised.
- **Acceptance criteria**: structured assessment is visible to both workflow
  roles, editable only by approvers, and persisted only through the authorized
  v2 action path.

### 7. Make Persisted State the Sole Approval and Write Authority

- **Requirements**: R5, R7, R8, R9, R11, R13, R16, R19
- **Files**: `review-app/R/actions.R`, `review-app/R/mod_detail.R`,
  `review-app/R/source_binding.R`, `review-app/R/recovery.R`
- **Details**:
  - Reorder the approval path so it rereads manifest, index, and record first,
    then checks source binding and persisted reviewed body using that reread
    record.
  - Make `controls$record` the sole base for artifact/path selection, state
    transition, event append, assignments/blocker refs, body identity, queue-row
    update, and YAML serialization. Treat caller `rec` only as expected loaded
    identity and reject canonical mismatch; never merge caller fields.
  - Compare the caller's expected record/index/manifest identities with current
    blobs and compare the selected index row with the persisted record path,
    state, source path, and record blob.
  - Bind approval to the reread body's SHA-256 and source commit/blob/content
    hashes plus evidence commit/attestation/context identities, and require all
    identities to equal the persisted assessment binding.
  - Fetch the attestation and validator/context path manifest by the assessment's
    immutable `evidence_commit`, not by mutable branch name, and repeat the Step
    1 identity checks before eligibility.
  - At action load, capture the current default-branch head and verify the
    source path blob/content still matches the enrolled source commit binding.
  - Extend the atomic adapter with a narrow `pre_publish_check` hook executed
    after blob/tree/commit object creation and immediately before PATCHing the
    review ref. The approval hook rereads the default-branch head and source
    path; it requires the observed head, path blob, Git blob bytes, and content
    SHA-256 to match the approval preflight. A mismatch aborts before ref
    publication; any created Git objects remain unreachable.
  - Carry manifest, index, persisted record, body companion, destination
    approved blob, and review head through expected-blob/ref preconditions.
  - Define retry classes explicitly:
    - a selected manifest/index/record/body/destination path change is
      non-retryable stale state and publishes nothing;
    - a source pre-publish mismatch is non-retryable `source_drift` and
      publishes nothing;
    - an unrelated review-ref race may retry once only when selected paths are
      unchanged. Discard every previously built `updated` record/event/changes
      object, reread all controls/body/source/evidence, rebuild from the latest
      persisted record, and rerun `pre_publish_check` before one eventual
      publication. A second ref race returns failure without publication.
  - Keep UI approval visibility as convenience only. The direct
    `perform_action(..., action = "approved")` path must execute authorization,
    persisted eligibility, blockers, drift, immutable front matter, and all
    optimistic-lock checks independently.
  - Produce specific denial reasons for disabled approval, blockers, incomplete
    rubric, stale assessment binding, and source drift without leaking secrets.
- **Test Scenarios**: direct ineligible call; caller-mutated assessment,
  assignments, blocker refs, state, and events; stale assessment body/source;
  source changes before pre-publish; manifest/index/record/body-companion/
  approved-destination races publish nothing; unrelated review-ref race retries
  from fully reread state and publishes once; second ref race publishes nothing;
  valid fixture writes only from the reread persisted base.
- **Tests**: adapter-double race and direct-call cases in
  `test-approval-gate.R`.
- **Acceptance criteria**: no caller or UI state can authorize approval; only a
  current, persisted, fully eligible snapshot can reach the write transaction.

## Phase 3: Focused and Full Verification

### 8. Build the Focused Approval-Gate Test Matrix

- **Requirements**: R1, R2, R3, R5, R7, R8, R9, R10, R11, R12, R13, R15, R16, R17, R18, R19, R20
- **Files**: `review-app/tests/testthat/test-approval-gate.R`; existing helper
  or queue tests only when a shared public fixture must be adjusted
- **Details**:
  - Create self-contained valid assessment, enabled/closed manifest, v2 record,
    index, source, body, and GitHub adapter fixtures. Keep the production
    defaults disabled/open; lower-level eligible fixtures must be local copies.
  - Cover every requested case as an explicit behavioral test:
    - valid all-pass assessment;
    - revise without note;
    - any fail rating;
    - Layer 1 missing/failing;
    - open major/block content error;
    - stale assessment/source/manifest/index races;
    - unknown section/rating;
    - reviewer attempting an approver action;
    - direct `perform_action()` approval while ineligible;
    - direct legacy write without a caller flag remains read-only.
  - Add high-value complements discovered from the current implementation:
    exact seven-section coverage, fail-with-note still ineligible, identified
    empty content-error snapshot, caller-mutated assessment bypass attempt,
    agent disposition non-gating, machine-field injection rejection,
    submission Layer 1 enforcement, lazy scaffold migration, persisted-record
    write base, historical-record/newer-evidence-commit compatibility,
    validator/context tree drift, fixed-epoch byte determinism, and
    assessment-save audit/atomicity.
  - Add distinct races for manifest, index, record, body companion, source
    pre-publication check, existing approved destination, and review ref.
    Selected-path and source races assert no reachable publication. The
    unrelated review-ref test asserts a full reread/rebuild/recheck and exactly
    one eventual publication; a repeated ref race asserts no publication.
  - Assert rejected paths do not update adapter refs, records, index rows, body
    companions, or approved artifacts.
  - Avoid ambient filesystem state, live GitHub/Connect calls, and production
    queue reads. Use `withr` cleanup and package-safe fixture access.
- **Test Scenarios**: happy path, all named edge cases, authorization errors,
  stale writes at each lock boundary, and no-write assertions.
- **Tests**:
  `Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-approval-gate.R")'`.
- **Acceptance criteria**: the focused file passes and each requested denial is
  proven at the server boundary, not only through UI visibility.

### 9. Verify UI, Legacy Routing, and Existing Queue Protections

- **Requirements**: R6, R7, R9, R10, R13, R15, R16
- **Files**: `review-app/tests/testthat/test-approval-gate.R`,
  `review-app/tests/testthat/test-production-queue.R`, and existing tests only
  where public behavior has intentionally changed
- **Details**:
  - Exercise role-specific UI rendering and namespaced assessment inputs using
    the established Golem testing pattern.
  - Confirm reviewers retain save/submit and cannot assess/approve; approvers
    can assess/request revision and see approval only for persisted eligibility;
    administrators retain queue actions and cannot impersonate reviewer or
    approver write actions.
  - Retain Release A tests for disabled approval, stable blocker IDs, immutable
    source identity, front-matter preservation, source drift, atomic writes,
    and legacy read-only routing.
  - Replace tests that rely on `legacy_read_only = TRUE` with direct assertions
    that trusted adapter routing rejects legacy writes even when no flag is
    supplied. Keep pure legacy transition coverage separate from persistence.
  - Keep tests valid under installed-package namespace semantics; do not rely
    on `load_all()` exposing undeclared helpers.
- **Test Scenarios**: all three roles, stale UI data, legacy mode, direct action
  bypass, package namespace loading.
- **Tests**: focused file followed by
  `Rscript -e 'devtools::test("review-app")'`.
- **Acceptance criteria**: UI behavior mirrors server authorization without
  weakening any existing queue/source/write regression test.

### 10. Run Full Verification and Audit Non-Mutation

- **Requirements**: R11, R12, R13, R14
- **Files**: implementation files above plus the dedicated generated
  `extraction/25_agent_review/evidence/layer1-attestations.v1.yml`; no queue or
  approved records
- **Details**:
  - Preflight the Python environment in this worktree. If
    `.venv/bin/python` is absent, create `.venv` with the verified system
    `python3` and install `requirements.txt`; then retain the user-required
    `.venv/bin/python` test command.
  - Run the exact focused, full R, package build/check, and Python commands from
    the invocation in that order.
  - Generate the dedicated attestation with the implemented module, validate
    its 267 source-bound entries, and inspect that its only output is the
    declared evidence artifact. Do not run the general review-agent runner or
    rewrite existing per-agent findings.
  - Derive `SOURCE_DATE_EPOCH` reproducibly from the latest committed change to
    the attested draft/schema/rule/parameter inputs. The compiler must fail if
    the variable is absent instead of falling back to wall-clock time.
  - Inspect `git status --short -- extraction/30_review extraction/40_approved`
    after tests. The only repository entries there remain their existing
    `.gitkeep` files with no changes or new records.
  - Inspect the code diff to confirm `approval_mode` still defaults to
    `disabled`, `RUBRIC_GATE_PENDING` remains in the open blocker set, and no
    production queue/bootstrap command was executed.
  - Confirm no new dependency was added unless separately approved under the
    `ask` deviation policy.
  - After recording package-check evidence, delete only the generated
    `reviewapp_0.1.0.tar.gz` and `reviewapp.Rcheck/` artifacts so handoff does
    not include build output.
  - Record Task E as a downstream merge/rebase dependency; do not implement its
    reopen/re-enrollment changes here. Existing records do not re-enroll solely
    to discover the separate evidence commit; Task E is required when enrolled
    source bytes changed or its own reopen/re-enrollment conditions apply.
- **Test Scenarios**: focused behavior, complete R regression, installed package
  check, cross-language regression, protected-directory cleanliness.
- **Tests**:
  - `test -x .venv/bin/python || python3 -m venv .venv`
  - `.venv/bin/python -m pip install -r requirements.txt`
  - `.venv/bin/python -m pytest tests/review_agents/test_layer1_attestations.py -q`
  - `SOURCE_DATE_EPOCH="$(git log -1 --format=%ct -- extraction/20_drafts schema knowledge/rules knowledge/parameters)" .venv/bin/python -m extraction_pipeline.review_agents.layer1_attestations --output extraction/25_agent_review/evidence/layer1-attestations.v1.yml`
  - `Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-approval-gate.R")'`
  - `Rscript -e 'devtools::test("review-app")'`
  - `R CMD build review-app && R CMD check --no-manual reviewapp_0.1.0.tar.gz`
  - `.venv/bin/python -m pytest tests/ -q`
  - `git status --short -- extraction/30_review extraction/40_approved`
- **Cleanup**: after evidence capture, remove generated
  `reviewapp_0.1.0.tar.gz` and `reviewapp.Rcheck/`; never remove source or
  user-created files.
- **Acceptance criteria**: every required command exits successfully, protected
  review/approved directories are clean, production controls are unchanged,
  and the branch is ready for review before Task E rebases.

## Testing Strategy

- Use `testthat` edition 3 and a dedicated `test-approval-gate.R` file as the
  executable acceptance contract.
- Test evidence parsing/identity, lazy scaffold normalization, assessment
  validation/completeness/binding, and Layer 1 body checks separately from
  adapter/action behavior so failures identify the layer at fault.
- Use an in-memory GitHub adapter double for manifest, index, record, body,
  locked evidence-commit evidence, source, approved destination, and ref races. Cover
  every declared precondition separately and assert both denial and absence of
  reachable writes.
- Test the Python Pydantic attestation compiler independently for source-byte
  binding, validator/context digests, deterministic ordering, complete corpus
  coverage, explicit failures, and atomic output.
- Test the public `perform_action()` boundary directly for authorization and
  submission, assessment persistence, legacy rejection, persisted-record write
  base, and approval eligibility. UI tests supplement but never replace server
  tests.
- Drive Golem module inputs with namespaced IDs and avoid bare unexported
  helpers in tests so `R CMD check` exercises the same behavior.
- Preflight/create the worktree-local `.venv`, run the focused file during
  implementation, then `devtools::test("review-app")`, package build/check, and
  the user-required `.venv/bin/python` suite before completion.
- Do not execute queue bootstrap, production adapters, live GitHub calls, or
  Posit Connect operations.

## Documentation Checklist

- [ ] Roxygen comments describe the expanded assessment constructor/validator,
      evidence authority, submission gate, eligibility semantics, pre-publish
      hook, and new public assessment action API.
- [ ] `NAMESPACE` is regenerated or updated only when public exports change.
- [ ] The Python attestation schema and CLI document every identity/digest and
      state that aggregate agent summaries are not Layer 1 authority.
- [ ] UI labels explain that YAML is read-only, Layer 1 evidence is automated,
      ratings/content-error attestations must be saved, and agent review is
      informational in this release.
- [ ] Error messages distinguish incomplete rubric, blockers, stale assessment,
      and source drift without exposing credentials or raw tokens.
- [ ] Existing rubric and production queue documents remain unchanged; this
      task implements their contract rather than revising governance.
- [ ] Downstream handoff notes state that Task E must rebase/branch after this
      task merges because it modifies overlapping app files.

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Existing v2 scaffold records fail strict parsing before an approver can assess them. | Medium | High | Recognize only the exact old scaffold, normalize it to explicit pending/ineligible state, and serialize the expanded form deterministically on the next authorized v2 write of any action. |
| A caller mutates `rec$assessment` in memory and bypasses the persisted record. | High in adversarial calls | Critical | Reread the record and evaluate only `controls$record`; add a direct bypass regression test. |
| Repository-committed validator evidence is missing, stale, or does not match the enrolled artifact. | Medium | Critical | Resolve a separate immutable evidence commit, compile a Pydantic-only attestation with source and exact context path/blob identities, verify every identity, block submission when unavailable, and test tampering. |
| Existing records predate the attestation artifact. | High | High | Resolve attestation by separate evidence commit and match enrolled source bytes; require Task E re-enrollment only when source bytes changed, not merely because evidence was introduced later. |
| Source changes on its separate branch between validation and review-branch ref update. | Low | Critical | Bind `source_commit`/blob/content, capture the observed source head, run a pre-publish source hook immediately before review-ref PATCH, and simulate the race. |
| An empty or absent content-error list is mistaken for proof of zero blockers. | Medium | High | Require snapshot identity/timestamp even for zero items; absence remains incomplete and ineligible. |
| Agent-review disposition accidentally becomes an active gate, contradicting the rubric. | Medium | Medium | Keep it out of the active predicate and add an explicit non-gating test; future activation requires a separate governed task. |
| Approver UI shows eligibility from unsaved ratings or stale content. | Medium | High | Track assessment dirtiness separately, evaluate only persisted reread records, and disable/hide approval until a saved current assessment is eligible. |
| Assessment persistence creates a second non-atomic write path. | Low | Critical | Reuse `perform_action()` and `adapter_write_with_recovery()` for record/index updates and audit events. |
| Lazy scaffold expansion causes unexpected diffs during unrelated actions. | Medium | Medium | Document expansion-on-any-write as the selected policy and assert deterministic unrelated-action output. |
| Module tests pass under `load_all()` but fail under installed-package semantics. | Medium | Medium | Use namespaced inputs, avoid undeclared helpers, and require package build plus `R CMD check`. |
| Tests or fixtures mutate production review/approved paths. | Low | Critical | Use in-memory adapters and temporary paths; verify protected directory status after all suites. |
| An unrelated review-ref retry reuses a previously built record or skips the source hook. | Low | Critical | Classify retries explicitly, discard all derived changes, fully reread/rebuild, rerun pre-publish validation, and test one-success/second-failure outcomes. |

## Out of Scope

- Enabling `approval_mode` or writing an approval-enablement audit.
- Closing, removing, or changing `RUBRIC_GATE_PENDING` or any other production
  blocker.
- Bootstrapping, migrating, or editing production queue records during
  development or tests.
- Making agent-review results an active promotion gate.
- Regenerating or changing existing per-agent findings schema/content. The only
  new review-evidence output is the dedicated Layer 1 attestation declared in
  Step 1.
- Changing the finalized calibration rubric or content-error taxonomy.
- Task E reopen/re-enrollment safety and assessment reset policy for a new
  enrollment generation. This task only specifies when source-byte mismatch
  requires that downstream path.
- Tasks B/C source-lock or inventory-ledger implementation.
- Changes to `knowledge/`, `country-parameters/`, approved artifacts, or rule
  logic.
- Posit Connect deployment, live operator calibration, or production approval.

## Completion Contract

### Outcome

V2 review records persist a strict, content-bound assessment covering automated
Layer 1 evidence, all seven Layer 2 ratings and required notes, content-error
evidence, and agent-review provenance. Server-side submission rejects failing or
unverifiable Layer 1 content, and both the Shiny workflow and direct server calls
deny approval unless all reread persisted controls and write preconditions are
current and eligible.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|-------------------|------------------|----------|
| V1 | 1 | Fixed-epoch byte-deterministic Pydantic attestation, separate evidence-commit/context-tree verification, historical-record compatibility, evidence timestamp parsing, lazy schema migration, Layer 1 submission gate, and exact rubric matrix pass | `.venv/bin/python -m pytest tests/review_agents/test_layer1_attestations.py -q`; `Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-approval-gate.R")'` | yes |
| V2 | 2 | Role-specific UI persists only human-owned ratings/notes/content errors; server constructs machine fields; legacy and unauthorized writes are denied | `Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-approval-gate.R")'` | yes |
| V3 | 3 | Approval uses the reread record as write base; selected-path/source races publish nothing; one unrelated review-ref race fully rereads/rebuilds/rechecks and publishes once; a repeated ref race publishes nothing | `Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-approval-gate.R")'` | yes |
| V4 | final | Full R regression suite passes against the package path | `Rscript -e 'devtools::test("review-app")'` | yes |
| V5 | final | Installed-package semantics and package checks pass | `R CMD build review-app && R CMD check --no-manual reviewapp_0.1.0.tar.gz` | yes |
| V6 | final | Worktree-local Python environment exists and schema/extraction/review-agent regressions remain green | `test -x .venv/bin/python || python3 -m venv .venv`; `.venv/bin/python -m pip install -r requirements.txt`; `.venv/bin/python -m pytest tests/ -q` | yes |
| V7 | final | Development and tests leave production queue/approved records untouched and retain disabled approval/open rubric blocker defaults | `git status --short -- extraction/30_review extraction/40_approved` plus focused manifest assertions | yes |

### Constraints

| ID | Phase | Constraint | Check |
|----|-------|------------|-------|
| C1 | 1 | Machine Layer 1 evidence comes only from the dedicated Pydantic attestation at a locked evidence commit with exact source/context tree identities; aggregate agent review remains provenance-only | Fixed-epoch compiler, historical-record, source/context-tree tampering, timestamp, and adverse-agent tests |
| C2 | 2 | Reviewers edit/save/submit; approvers assess/request revision/approve; administrators retain queue controls; legacy writes are always rejected | Authorization, payload-whitelist, and direct legacy-call tests |
| C3 | 3 | UI/caller state never substitutes for reread persisted state, server authorization, source pre-publish validation, or write locks | Mutated-record direct calls plus non-retryable and recoverable race tests |
| C4 | final | `approval_mode` remains `disabled`; `RUBRIC_GATE_PENDING` remains open | Manifest fixture/default assertions and diff review |
| C5 | final | Legacy `review` branch records remain read-only | Legacy routing/action regression test |
| C6 | final | No production queue records or approved artifacts are written by development/tests | Git status check and hermetic adapter fixtures |
| C7 | final | No new runtime dependency is introduced solely for assessment handling | `DESCRIPTION`, build, and check evidence |

### Boundaries

- Allowed: dedicated Python Pydantic-attestation compiler/artifact/tests, v2
  assessment models/validators, locked evidence-commit readers, Layer 1
  submission gate, human content-error attestation, role-mapped assessment
  persistence, queue eligibility/approval handling, narrow pre-publish source
  hook, detail-module UI, supporting styles/helpers, focused R tests, and
  generated namespace updates only if required.
- Out of scope: enabling approvals, closing `RUBRIC_GATE_PENDING`, changing
  production queue state, writing queue records, Task E reopen/re-enrollment
  behavior, Tasks B/C contracts, changing the finalized rubric, modifying
  `knowledge/` or country parameters, and making agent review an active gate.

### Iteration Policy

1. Implement and prove evidence authority, lazy migration, and the fail-closed
   submission/assessment contracts before wiring UI.
2. Persist assessment through the same v2 atomic action path; do not add a
   separate write mechanism.
3. Bind transitions, serialization, and eligibility to the reread persisted
   record and exact source/body identities, never caller-mutated data.
4. Run the focused file after each phase, then full R, package-check, and Python
   verification.
5. Under deviation policy `ask`, stop before changing schemas, dependencies,
   role semantics, or production controls beyond this contract.

### Blocked-Stop Conditions

- Layer 1 evidence cannot be tied to an existing, verifiable
  evidence commit with source-byte-bound validator/context identities without
  inventing provenance.
- Completion would require enabling approvals, closing blockers, changing
  production queue records, or writing to protected human/canonical artifacts.
- A required race or role test cannot be made hermetic and would contact
  production services.
- Any required verification remains failing after task-scoped recovery.
- Task E or another concurrent change creates a direct conflict in the same app
  files that cannot be reconciled without altering scope.
- A protected boundary must be crossed, a required deviation under `ask` lacks
  approval, or the execution report cannot be durably maintained.
