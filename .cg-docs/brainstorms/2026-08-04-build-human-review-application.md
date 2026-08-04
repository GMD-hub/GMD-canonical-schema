---
date: 2026-08-04
title: "Build the Human Review Application"
status: decided
scope: "Deep"
chosen-approach: "Git-backed Shiny review application with per-artifact audit records"
tags: [human-review, shiny, posit-connect, github, audit, markdown, governance]
---

<!-- Valid status values: decided, in-progress, abandoned -->

# Build the Human Review Application

## Context

The completed extraction milestone produces governed CVS drafts with YAML front matter for machine-validated identity, values, derivation, and provenance, plus a human-readable Markdown body for descriptions, rules prose, and caveats.

GPID reviewers need a private application that lets them browse these drafts by module, inspect the extracted YAML and source evidence, enrich only the Markdown body, and record a complete review history before downstream reconciliation and canonical promotion.

The application will be deployed privately on Posit Connect. No managed database is currently available. GitHub must therefore provide the MVP's durable content, review state, and audit storage. Posit Connect supplies authenticated user identity and secure configuration for the application's GitHub credentials; it is not the authoritative review-state database.

This design respects the governed lifecycle:

```text
source/context -> extraction/20_drafts -> human review -> extraction/40_approved -> knowledge
```

The app performs the human-review stages only. It must not alter canonical YAML or automatically promote content into `knowledge/`. The existing `AGENTS.md` restriction that `extraction/30_review/` and `extraction/40_approved/` are human-owned remains in force: application writes occur only in response to an authenticated human action and are traceable to that person.

## Requirements

- Deploy a private Shiny for Python application to Posit Connect.
- Use Connect authentication as the user-identity source; do not add a second login layer.
- Map authenticated identities explicitly to the roles `reviewer`, `approver`, and `administrator`; never infer roles from email naming conventions.
- Let reviewers browse artifacts organized and filtered by module, review state, assignment, and action required.
- Show extracted YAML front matter and guideline evidence/citations as read-only context alongside the editable Markdown body.
- Allow edits to the Markdown body only. Preserve YAML front matter exactly and reject structural alterations or invalid full-artifact serialization.
- Support a plain Markdown textarea and rendered preview as the MVP editing experience. Rich-text/Quarto editing is deferred.
- Persist work-in-progress with save-draft and transition a submitted artifact for GPID review.
- Let GPID approvers request revision or mark an artifact approved in the app.
- Record reviewer identity, role, review round, timestamps, state transitions, source Git SHA, body SHA-256, and optional notes in an auditable history.
- Detect concurrent edits through optimistic locking; never silently overwrite a newer remote revision.
- Use a GitHub App or dedicated bot identity, configured through Posit Connect secrets/environment variables, rather than reviewer personal access tokens.
- Keep pull-request, branch-protection, outbound-notification, automatic YAML reconciliation, database provisioning, real-time collaboration, and automatic promotion to `knowledge/` out of scope for this iteration.

## Decisions From Clarification

1. GPID approvers can mark artifacts approved in the application; approval is not merely an external GitHub activity.
2. Permissions are role-based:
   - **Reviewer:** edit Markdown, save a draft, and submit for GPID review.
   - **GPID approver:** request revision or approve an artifact.
   - **Administrator:** assign artifacts, reopen artifacts, and maintain the repository-managed role mapping.
3. The review state machine includes a revision loop:

   ```text
   draft -> in-review -> approved
                  |-> needs-revision -> in-review
   ```

   `draft -> in-review` and `needs-revision -> in-review` are reviewer submit transitions. `in-review -> needs-revision` and `in-review -> approved` are approver transitions. Reopening an approved artifact is administrator-only and must emit an explicit audit event; its target state is `needs-revision`.
4. The app uses GitHub as the MVP persistence backend because a managed PostgreSQL service is not currently available. A storage interface must keep a future database migration possible without redesigning the UI or workflow.
5. State is stored in per-artifact review files rather than a single mutable manifest. This limits merge conflicts for concurrent reviewers. The dashboard derives its view by scanning/indexing these files; an aggregate index is a future performance optimization, not a source of truth.
6. The app reads source drafts and writes review outputs to a dedicated protected review branch. The default branch remains canonical source context until a separate reconciliation and promotion workflow acts.
7. On approval, the app writes the full approved artifact, retaining its exact YAML and approved Markdown body, to `extraction/40_approved/` on the review branch. The review working copy and immutable history remain under `extraction/30_review/`.
8. SHA-256 is the content-hash algorithm. Use the repository's existing deterministic hashing helper where it meets this contract.
9. Connect persistent application storage can be used only for disposable cache or temporary operational state, never as the authoritative audit ledger.
10. The MVP gives reviewers a dashboard/work queue. External notifications are deferred.

## Review Record Format

Each artifact has an adjacent per-artifact review record, for example `extraction/30_review/VAR-male.review.yml`. It holds current state and an append-only event history:

```yaml
artifact_id: VAR-male
source_artifact_path: extraction/20_drafts/variables/dem/VAR-male.md
state: in-review
review_round: 2
assigned_to:
  - reviewer@example.org
current_content_sha256: "<sha256-of-markdown-body>"
source_commit: "<git-commit-or-blob-sha>"
events:
  - event_id: "<uuid>"
    action: submitted
    from_state: draft
    to_state: in-review
    actor: reviewer@example.org
    actor_role: reviewer
    occurred_at: "2026-08-04T14:00:00Z"
    source_blob_sha: "<github-blob-sha>"
    body_sha256: "<sha256-of-markdown-body>"
    note: null
```

Every save also creates an event and a versioned review working copy. Transition records are append-only: state corrections happen through new events rather than mutation of prior history.

## Approaches Considered

### Approach 1: Git-backed Shiny application with per-artifact audit records

The application reads CVS drafts from GitHub and writes Markdown-only working copies, per-artifact review records, and approved staging copies to a protected review branch through a GitHub App.

**Pros**

- Requires no database provisioning.
- Keeps reviewed content, audit records, and repository history together.
- Uses atomic multi-file Git commits for a save, submit, revision request, or approval whenever the GitHub API supports the complete tree update.
- Per-artifact records minimize cross-reviewer write conflicts.
- Directly supports the existing staging lifecycle and later reconciliation.

**Cons**

- Dashboard queries require repository scanning/indexing rather than database queries.
- Concurrent editing relies on optimistic conflict handling rather than locks.
- Git commits are less convenient than database tables for reporting at scale.
- Partial write failures require explicit recovery and operator visibility.

**Effort:** Large.

**Recommended:** Yes. It provides the necessary governed workflow without blocking on unavailable infrastructure, while allowing a later storage backend replacement.

### Approach 2: Posit Connect persistent application storage

Persist review state, audit events, and edited bodies in an application-managed directory on Posit Connect, while using GitHub only as read-only source context.

**Pros**

- Simple prototype implementation.
- Avoids GitHub write integration initially.

**Cons**

- Does not make review history naturally version-controlled or independently recoverable.
- Reliability across application restarts, redeployments, backups, and multiple processes depends on Connect infrastructure details.
- Adds a later migration before reviewed Markdown can enter the governed Git lifecycle.
- Does not satisfy the operational need for durable GitHub access and traceable review writes.

**Effort:** Medium initially; high when migration and governance gaps are included.

**Recommended:** No. It is appropriate only for disposable cache or temporary operational state.

### Approach 3: Dedicated PostgreSQL-backed application

Store roles, assignments, events, versions, and concurrency controls in managed PostgreSQL; use GitHub for source/approved artifact files.

**Pros**

- Strong transactional audit queries, assignments, and row-level locking.
- Better scaling for dashboards, notifications, and reporting.
- Cleaner operational state model for a multi-reviewer application.

**Cons**

- The required managed database is not currently available.
- Increases infrastructure, credential, backup, migration, and support work.
- Still requires GitHub integration for governed Markdown outputs.

**Effort:** Large.

**Recommended:** Later. Keep a repository interface so this can become the state backend when institutional infrastructure is available.

## Decision

Build **Approach 1: a Git-backed Shiny for Python application with per-artifact audit records**.

The application will use Posit Connect authentication and deployment controls, a repository-managed role map, and a minimally scoped GitHub App. It will operate on a dedicated protected review branch. GitHub will be the durable MVP store for reviewed Markdown bodies, review records, and versions; Connect will safely provide user identity and secrets but will not replace transactional storage.

The UI will provide a dashboard, module navigation, side-by-side read-only YAML and evidence panels, a Markdown textarea with preview, an audit timeline, and state-appropriate actions. Server-side authorization and validation govern all writes; hiding controls in the UI is not a security mechanism.

Each user action loads and retains the remote blob SHA and body SHA-256. Before writing, the app compares the current remote SHA to the loaded SHA. A mismatch rejects the stale write, preserves unsaved entered text for user recovery, and requires reload/merge guidance. The app must not overwrite a newer revision.

For any logical operation that changes multiple files—working artifact, review record, and, when approved, approved artifact—the GitHub adapter should create one atomic commit with all tree changes. If an API or network failure leaves an operation incomplete, the app must fail loudly, report the affected paths and commit status, and provide an operator recovery path; it must not claim a successful transition.

## Devil's Advocate

1. **Problem validation:** The need is established by the completed extraction pipeline: humans must enrich and approve source-grounded Markdown before any downstream reconciliation can occur. Manual file editing would provide no reliable queue, transition control, or consistent audit evidence.
2. **Simplicity check:** A shared Markdown editor plus GitHub commits is simpler, but it cannot safely restrict YAML edits, present review context, apply role gates, manage a reviewer queue, or prevent silent concurrent overwrites. The proposed app is the smallest solution that satisfies those governance controls.
3. **Effort-value check:** The full application is a large effort. The MVP should intentionally stop at plain Markdown editing, Git-backed work queues, optimistic locking, and no notifications. That delivers most review value while deferring rich text, real-time collaboration, and database-backed reporting.
4. **Charter alignment:** The approach aligns with the charter's current focus on a private Posit Connect review app and the constraint that humans own review, approval, and promotion. It does not allow agents to edit `knowledge/`, change artifact YAML, or bypass human decisions.

## Next Steps

1. Create an implementation plan that first inspects the current front-matter loader, hashing utilities, extraction staging structure, validation patterns, and dependency configuration.
2. Define Pydantic models and strict transition/authorization functions for the review record, events, assignments, and role map.
3. Specify exact paths and versioning conventions for review working copies, state files, and approved copies without changing the existing draft source.
4. Implement a GitHub App adapter with authenticated reads, atomic commit writes, remote-SHA checks, deterministic hashing, and explicit partial-failure errors.
5. Build the Shiny for Python application as an isolated deployable package with dashboard, artifact detail, read-only context panels, Markdown editor/preview, timeline, and role-gated actions.
6. Add unit tests for parsing, front-matter immutability, validation, state transitions, authorization, content hashes, review rounds, stale saves, and recovery errors. Add integration tests against a test GitHub repository or dedicated test branch.
7. Produce a Posit Connect operator guide covering private access/groups, Connect identity fields, GitHub App credentials, repository/review-branch configuration, deployment, monitoring, and incident recovery.
8. Validate the MVP with a representative calibration sample before scaling to all extracted artifacts.
