---
date: 2026-09-03
title: "Direct GitHub App Review Queue Cutover"
category: "git-workflows"
language: "both"
tags: [github-app, posit-connect, queue-migration, production-cutover]
root-cause: "A one-time queue migration was wrapped in unnecessary workflow indirection that hid the actionable failure while the reviewed CLI already provided the required atomic and fail-closed controls."
severity: "P1"
plan: ".cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md"
related: [".cg-docs/work-reports/2026-08-26-complete-release-a-production-queue-cutover.md"]
---

# Direct GitHub App Review Queue Cutover

## Problem

The production queue needed one format-only migration from production-v2
controls to descriptor schema 1.1. A separate staging wave and a temporary
GitHub Actions workflow added credential setup, two failed runs, and generic
error output without changing any branch. The process became harder to operate
than the one-time migration required.

## Root Cause

The release process duplicated controls already enforced by the migration CLI:
explicit target and expected head, production authorization, immutable source
validation, administrator authorization, one atomic non-force commit, and
redacted evidence. The added workflow layer made credential diagnosis harder
without improving the queue mutation boundary.

## Solution

Use the reviewed CLI directly from a clean operator checkout after a separate
read-only credential and source preflight:

1. Validate the production baseline from a detached checkout.
2. Exchange the GitHub App credentials for a token without writing or printing
   the token.
3. Read and validate the expected branch head, controls, source snapshots, and
   all records.
4. Run the CLI once with the explicit production authorization and expected
   head.
5. Independently verify the new parent, App author, exact tree changes, record
   blob identities, descriptor, queue count, source identity, and path digest.
6. Switch only the Connect review-branch environment variable, restart, attest,
   and confirm the dashboard count.

For this cutover, the migration changed only the descriptor, manifest, and
index controls. All 267 record blobs remained identical and approval remained
disabled.

## Prevention

- Prefer the smallest existing reviewed operator path for a one-time action.
- Add reusable automation only when the operation will repeat.
- Test credential exchange separately before combining it with a write.
- Keep expected-head locking, immutable source checks, atomic non-force writes,
  redacted evidence, and rollback refs even when the procedure is simplified.
- Do not create synthetic production review content. Let the first genuine
  distinct-role review provide production smoke evidence.
- Remove temporary credentials and automation immediately after use.

## Related

- [Release A cutover report](../../work-reports/2026-08-26-complete-release-a-production-queue-cutover.md)
- [Release A cutover plan](../../plans/2026-08-25-complete-release-a-production-queue-cutover.md)
