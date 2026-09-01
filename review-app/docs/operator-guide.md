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

Descriptor schema 1.1 contains queue ID, the immutable initial source baseline,
creation actor/time, expected record count, a stable membership digest, and one
`approvals_enabled` Boolean. The digest uses queue ID, artifact ID, and source
artifact path. Per-record source commit, blob, content, actor, and enrollment
time are not membership inputs. New and migrated descriptors set approval to
`false`. Dashboard rows are derived from batched record reads. There is no
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
Strict descriptor 1.0 queues also remain readable. Both compatibility modes are
read-only. Migrate the queue before review writes.

The compatibility path preserves:

- queue ID and source revision
- source path, source Git blob SHA, and source content SHA-256
- enrolled and current reviewed-body SHA-256
- enrollment actor/time
- record state, assignments, assessment, blockers, and compact events
- record Git blob identity and protected branch history

## Migration

Migration is not available in the Shiny UI. An authenticated administrator
uses `tools/migrate-review-queue.R`, which invokes `migrate_review_queue()`.
The CLI requires an explicit target branch, expected old branch head, and actor.
It reads GitHub App credentials only from environment variables and builds the
adapter with the explicit target. It does not use
`REVIEW_APP_GH_REVIEW_BRANCH` as the migration target.

The migration input can be an approval-disabled production-v2 manifest/index or
a strict descriptor 1.0 queue. Before publication, the migrator:

1. Locks the current review-branch head and tree.
2. Validates the strict descriptor 1.0 fields, or the legacy immutable manifest
   fields and `approval_mode: disabled`.
3. Validates the legacy index against every record and record blob when present.
4. Validates every v2 record against its own immutable source commit and bytes.
5. Creates deterministic descriptor bytes from the existing records.
6. Confirms that no record, body, event history, or approved output is changed.

The one migration commit publishes descriptor 1.1 with
`approvals_enabled: false`. For production-v2, it removes
`queue-manifest.yml` and `queue-index.yml`. For descriptor 1.0, it replaces only
`queue-descriptor.yml`. It is forward-only and non-force. A moved branch ref or
any validation failure leaves the old branch head and control files unchanged.

### Wave 3 Staging

Before this command can run, `review-staging-wave3` must point exactly to
`8b5de18ae78f1dd5bb09511fd076c57e670f1db9`. Creating that staging branch and
running this command are separate operator actions after the CLI change is
merged, deployed from `main`, and authorized for staging.

```sh
Rscript review-app/tools/migrate-review-queue.R \
  --target-branch review-staging-wave3 \
  --expected-head 8b5de18ae78f1dd5bb09511fd076c57e670f1db9 \
  --actor acastanedaa
```

The command refuses a mismatched branch head before it reads or writes queue
content. On success, it prints deterministic JSON with the repository, target
branch, expected old head, migration commit, queue and source identities,
source format, record count, record-set digest, preserved-record-blob digest,
and `approvals_enabled: false`. The preserved-record-blob digest is SHA-256 over
the sorted, length-prefixed record path and Git blob SHA pairs. The evidence
does not include credentials, actor role data, or role-map contents.

Validate the migrated staging queue before any Posit Connect change. The
`review-staging-wave3` branch is staging data only. Never merge it into `main`
or `review-production`. Production migration is a separate later authorization
and is not authorized by this staging procedure.

Do not run migration against the production branch as part of development,
tests, review, or CI. Production migration is a later explicit operator action.

## Source Drift

Each v2 record stores the enrolled source revision, path, Git blob SHA,
full-content SHA-256, and exact enrolled-body SHA-256. The app displays the
enrolled source snapshot and checks the current source path separately.

Drift state is structured as `current`, `drifted`, or `unverifiable`, with a
stable reason code and expected/actual identity fields. Save and Submit operate
against the enrolled immutable snapshot when the current source is drifted or
unverifiable. Approval remains blocked on unresolved drift and is disabled by
descriptor policy.

An administrator can use the explicit Re-enroll source action for a non-approved
record. The action requires a reason and an immutable candidate commit. It
keeps the artifact ID, source path, queue membership, assignments, and blocker
references. It resets assessment data and reviewed body to the verified new
source. Draft stays Draft, In review becomes Needs revision, and Needs revision
stays Needs revision. A duplicate replay creates no commit or event.

An approved record must first use Reopen and retire output. Reopen requires an
administrator and a reason. It verifies the immutable enrolled source and exact
approved output, permits current source drift or temporary current-source read
failure, preserves the reviewed body, moves the record to Needs revision, and
deletes the active approved output in the same Git commit. A missing,
inconsistent, or concurrently changed approved output fails closed.

## Concurrency

Each action locks the selected record, descriptor, selected body, and selected
approved output when applicable. It does not lock or rewrite a global index.
An unrelated record commit can move the branch head without invalidating the
selected record. A same-record or descriptor change fails as stale. A ref race
can retry only after the selected dependencies are revalidated. Selected
record, body, approved-output, or source changes are terminal. Source-sensitive
writes create their Git objects, rerun the selected source check, and only then
perform the non-force ref update. A failed final check leaves the new Git
objects unreachable.

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
