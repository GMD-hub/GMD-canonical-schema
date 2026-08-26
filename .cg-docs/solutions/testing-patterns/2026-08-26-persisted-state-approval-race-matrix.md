---
date: 2026-08-26
title: "Make persisted state the sole approval authority and classify publication races"
category: "testing-patterns"
language: "R"
tags: [approval-gate, optimistic-locking, atomic-write, race-testing, fail-closed]
root-cause: "Approval code can be bypassed or publish stale decisions when it evaluates caller-held records and treats all optimistic-lock failures as equivalent retryable races."
severity: "P1"
plan: ".cg-docs/plans/2026-08-25-human-review-rubric-approval-gate.md"
related: [".cg-docs/solutions/data-quality/2026-08-26-source-bound-validator-attestations.md", ".cg-docs/solutions/testing-patterns/2026-08-10-golem-module-testserver-capture.md"]
---

# Persisted-State Approval and Publication Race Matrix

## Problem

An approval API received an in-memory review record that had originally been
loaded by the UI. If approval eligibility, transition construction, artifact
paths, or serialization used that caller object, a mutated or stale caller
could bypass the persisted assessment and blocker state even when the UI hid
the approval control correctly.

Atomic Git writes also exposed several distinct races: selected manifest,
index, record, body, approved destination, source branch, and review ref. A
generic retry could accidentally reuse a previously built transition after a
selected input changed, or publish approval after the source changed between
preflight and the final ref update.

## Root Cause

The action boundary mixed two responsibilities for the caller record: expected
loaded identity and authoritative write data. It also modeled optimistic-lock
failure as one broad class instead of distinguishing stale selected inputs,
source drift, and unrelated review-ref movement. Retrying without discarding
derived state turns optimistic locking into stale-state replay.

## Solution

Use the caller record only as an expected identity. Reread all persisted
controls and require canonical equality before using the persisted record as
the sole base for authorization, eligibility, transition, paths, events, queue
updates, and serialization:

```r
controls <- read_controls(adapter, expected_manifest, expected_index)
persisted <- controls$record

if (!identical(record_to_yaml(caller), record_to_yaml(persisted))) {
  stop(stale_write_error("caller record differs from persisted review record"))
}

updated <- transition(persisted, action, actor, role)
```

Carry expected identities for every selected path into the atomic write. For
approval, run a narrow pre-publication hook after creating Git objects but
immediately before updating the review ref. Reread the source head/path there;
if the head, blob, or content digest differs, abort and leave created objects
unreachable.

Classify races explicitly:

| Race | Retry | Required outcome |
|---|---|---|
| Manifest, index, record, body, or destination changed | No | Deny; publish nothing |
| Source changed before publication | No | Return source drift; publish nothing |
| Unrelated review ref moved | Once | Reread, rebuild, and recheck everything |
| Review ref moved again | No | Deny; publish nothing |

On the one permitted retry, discard every previously derived record, event,
change set, and pre-publication result. The retry succeeds only from a complete
fresh read and rebuild.

Test the public server action directly, not only UI visibility. The focused
matrix should mutate each lock boundary independently and assert both the
specific denial class and zero reachable ref publications. Also test a
caller-mutated assessment/assignment/state and verify that unsaved UI inputs
never become approval authority.

## Prevention

- Define every API input as either expected identity, human-owned payload, or
  server-owned authority; never let one field serve multiple trust roles.
- Keep machine evidence, bindings, actors, timestamps, and snapshot digests out
  of client payloads.
- Require loaded manifest and index blob identities at write boundaries.
- Make selected-path races terminal; retry only a proven unrelated ref race.
- Rebuild all derived state on retry and cap retries explicitly.
- Add a pre-publication check for authorities stored on a different mutable ref.
- Assert no publication and no selected-path updates for every rejected race.

## Related

- [Source-bound validator attestations](../data-quality/2026-08-26-source-bound-validator-attestations.md)
- [Golem module server testing](2026-08-10-golem-module-testserver-capture.md)
- [Human review rubric approval-gate plan](../../plans/2026-08-25-human-review-rubric-approval-gate.md)
