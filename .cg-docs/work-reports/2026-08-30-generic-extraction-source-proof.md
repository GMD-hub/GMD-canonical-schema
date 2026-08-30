# Work Report: Generic Extraction Source Proof

## Scope

This branch implements Task B1A only. It provides reusable source-proof
engineering without selecting or activating GMD source policy.

The implementation:

- validates generic HTTPS repository identities;
- requires lowercase 40-character Git SHA-1 commit and blob identities;
- requires lowercase 64-character SHA-256 content identities;
- validates canonical repository-relative paths, generic scope identifiers,
  and path uniqueness;
- reads regular-file bytes from blobs at an explicit Git commit, not from the
  mutable worktree;
- rejects traversal, missing objects, non-regular entries, Git symlinks, and
  Git replacement-object overrides;
- returns a typed `ResolvedSource` proof with repository, commit, paths,
  scopes, blob identities, content hashes, parser identity, governance
  identities, and the exact verified bytes; and
- re-verifies that proof against the complete manifest and Git object graph
  inside orchestration before it can enter `SOURCE_VERIFIED`;
- validates citations from proof bytes, binds evidence and strict candidates
  to a deterministic proof digest, and derives G3-G5 from those records; and
- derives all generated paths from the manifest's generic `run_root` policy
  field and enforces both output-root and allowlist containment.

## Generic Code And Governed Policy

Reusable Python code validates identity shapes and proof consistency. It does
not select a repository, chapter list, source hashes, parser version, or
inclusion and exclusion decisions. Those exact values remain the responsibility
of versioned policy data. The generic output `run_root` is also selected in
versioned policy data; reusable code does not embed a run-directory name.

Task B1.1 remains a human source-policy gate. This branch does not claim B1.1
approval and does not claim approval of SL1-SL5. After the human decision, a
second policy-activation PR will apply the approved values and activate the
protected source policy.

## Relationship To PR #16

PR #16 was inspected as read-only source material. Its branch was not modified,
rebased, pushed, or closed.

This replacement preserves only the useful generic engineering intent from
PR #16: strict identity validation, source hashing, safe path handling, and a
typed resolution result. It replaces the mutable-checkout gate with immutable
Git-object reads and passes the resulting proof into orchestration. It also
restores the model and hashing tests that PR #16 removed.

This branch does not preserve PR #16 policy constants, proposed GMD values,
protected configuration changes, roadmap state, active-state changes, or old
execution evidence. The new PR supersedes only PR #16's generic engineering
portion. PR #16 must remain open until the replacement PR exists and this
preserved-work mapping is available in that PR.

## Protected Boundaries

This work does not modify:

- `extraction/config/`;
- `.github/workflows/validate.yml`;
- `review-app/` runtime or approval behavior;
- `.cg-docs/active-state/current.json`;
- `roadmap.json`;
- approved `knowledge/` artifacts; or
- country parameters.

## Verification

Only results produced on this branch are recorded here.

- Focused source-proof validation: 155 passed, 1 skipped because the protected
  manifest still has human-gated null policy values.
- Full Python validation: 343 passed, 2 policy-gated skips.
- Full review-app `devtools::test(reporter = "summary")`: passed after the
  local package was installed into the restored `renv` library for the app
  smoke process.
- Review-app `R CMD check --no-manual`: tests passed; the existing package
  produced 1 missing-documentation warning and 2 package-metadata or hidden-file
  notes. No review-app file changed in this branch.
- `git diff --check`: passed.
