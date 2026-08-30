# GMD Human Review Application Operator Guide

This guide covers the protected Git-backed review queue. It does not authorize
a production migration or a Posit Connect configuration change.

## Architecture

The application uses Connect identity for authentication and the repository
role map for server-side authorization. GitHub App installation tokens perform
repository reads and writes. Source artifacts are read from the configured
default branch. Review records, reviewed bodies, and approved outputs are
stored on the configured protected review branch.

The authoritative queue state consists of:

- `extraction/30_review/queue-descriptor.yml`
- `extraction/30_review/<artifact_id>.review.yml`
- optional `extraction/30_review/<artifact_id>.body.md`
- approved outputs under `extraction/40_approved/`
- protected Git commit history

The descriptor contains only schema version, queue ID, source revision,
creation actor/time, expected record count, and the immutable record-set
digest. Dashboard rows are derived from batched record reads. There is no
authoritative mutable queue index or global index lock.

## Authentication

Connect must provide an authenticated identity. The role map resolves that
identity to `reviewer`, `approver`, or `administrator`. UI visibility is not an
authorization boundary. The server checks every action again.

The GitHub App requires repository Contents read/write permission and Metadata
read permission. Store these values in Connect secret configuration:

```text
GITHUB_APP_ID
GITHUB_APP_INSTALLATION_ID
GITHUB_APP_PRIVATE_KEY
REVIEW_APP_GH_OWNER
REVIEW_APP_GH_REPO
REVIEW_APP_GH_DEFAULT_BRANCH
REVIEW_APP_GH_REVIEW_BRANCH
```

Queue source revision is an immutable descriptor field supplied explicitly to
the operator initializer. It is not a runtime environment setting.

## Branch Protection

The review data branch must block force pushes and deletion. Permit governed
direct writes only for the GitHub App and named administrators. Never merge the
review data branch into `main`. A logical action must create one commit with the
current branch head as its only parent and update the ref with `force = false`.

The preserved `review` calibration branch is read-only. Do not initialize,
migrate, repair, or write records on that branch.

## Initialization

Initialization is not available in the Shiny UI. An authenticated
administrator invokes `initialize_review_queue()` from an operator-controlled
R session with:

- the configured GitHub adapter
- authenticated actor identity present as an administrator in the configured
  repository role map
- an explicit lowercase 40-character source revision
- a queue ID
- an independent expected record count and source path-set digest

The initializer rejects every non-placeholder path under
`extraction/30_review/` or `extraction/40_approved/`. This includes review
records, body files, event files, queue controls, and approved outputs. It then
validates the source tree and source blobs, creates source-bound v2 records and
the descriptor, and publishes one non-force atomic commit.

Do not use the production review branch to test initialization. Use an
in-memory adapter, a fixture, or a temporary repository.

## Compatibility

The application temporarily reads an existing production-v2
`queue-manifest.yml`. It adapts only the immutable queue identity fields. The
old `queue-index.yml` is ignored by dashboard reads and review actions.
This compatibility mode is read-only. Migrate the queue before review writes.

The compatibility path preserves:

- queue ID and source revision
- source path, source Git blob SHA, and source content SHA-256
- enrolled and current reviewed-body SHA-256
- enrollment actor/time
- record state, assignments, assessment, blockers, and compact events
- record Git blob identity and protected branch history

## Migration

Migration is not available in the Shiny UI. An authenticated administrator
invokes `migrate_review_queue()` only after the compatible application code is
deployed and verified.

Before publication, the migrator:

1. Locks the current review-branch head and tree.
2. Validates the legacy immutable manifest fields.
3. Validates the legacy index against every record and record blob.
4. Validates all v2 source and record identities.
5. Creates deterministic descriptor bytes from the existing records.
6. Confirms that no record, body, event history, or approved output is changed.

The one migration commit adds `queue-descriptor.yml` and removes
`queue-manifest.yml` and `queue-index.yml`. It is forward-only and non-force.
A moved branch ref causes migration to fail without publication.

Do not run migration against the production branch as part of development,
tests, review, or CI. Production migration is a later explicit operator action.

## Source Drift

Each v2 record stores the enrolled source revision, path, Git blob SHA,
full-content SHA-256, and exact enrolled-body SHA-256. The app displays the
enrolled source snapshot and checks the current source path separately.

Drift state is structured as `current`, `drifted`, or `unverifiable`, with a
stable reason code and expected/actual identity fields. Every non-current state
blocks save, submit, revision, assignment, approval, and reopen. Approval
remains unavailable until Task D installs the complete human rubric gate. V2
reopen remains unavailable until Task E installs approved-output retirement
and source-revision lifecycle rules.

Full source-revision retirement, re-enrollment, and reopen behavior remain a
later sequential change.

## Concurrency

Each action locks the selected record, descriptor, selected body, and selected
approved output when applicable. It does not lock or rewrite a global index.
An unrelated record commit can move the branch head without invalidating the
selected record. A same-record or descriptor change fails as stale. A ref race
can retry only after the selected dependencies are revalidated.

## Validation

Run the read-only validator from a checked-out queue tree:

```sh
Rscript review-app/tools/validate-production-queue.R \
  --repo "$PWD" \
  --expected-source <source-sha1> \
  --expected-count <record-count> \
  --expected-path-digest <source-path-set-sha256>
```

The validator supports the simplified descriptor and the temporary
production-v2 control. It validates the descriptor denominator and digest,
record identities, enrolled source bytes, and persisted reviewed-body hashes.

## Rollback

Application-code rollback uses the normal Git-backed Connect deployment path.
Data rollback is forward-only: create a new restoring commit after diagnosis;
never reset, rebase, or force-push protected history.

For the established safe read-only rollback, configure the app to read the
preserved `review` branch and restart the Connect content. This exposes the
legacy calibration records without permitting writes. Leave the versioned
queue branch intact for diagnosis.
