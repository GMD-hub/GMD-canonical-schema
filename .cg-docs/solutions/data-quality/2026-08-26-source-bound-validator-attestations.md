---
date: 2026-08-26
title: "Bind validation attestations to source bytes and the complete validator context"
category: "data-quality"
language: "both"
tags: [attestation, provenance, pydantic, git-identity, reproducibility]
root-cause: "A validation result is not trustworthy when it identifies only the reviewed artifact and omits the validator code, registry inputs, and deterministic generation context that produced the result."
severity: "P1"
plan: ".cg-docs/plans/2026-08-25-human-review-rubric-approval-gate.md"
related: [".cg-docs/solutions/testing-patterns/2026-08-26-persisted-state-approval-race-matrix.md", ".cg-docs/solutions/testing-patterns/2026-08-15-pydantic-rule-ids-context.md"]
---

# Bind Validation Attestations to Source Bytes and Validator Context

## Problem

The human-review approval gate needed to consume automated Pydantic results
without trusting a mutable branch, an aggregate agent summary, or evidence that
merely named an artifact. A source-only digest was insufficient: the same
source bytes can validate differently after validator code, rule registries,
parameter registries, validation options, or package versions change.

Historical review records added a second constraint. Their enrolled source
commit can predate a newly introduced attestation artifact, so requiring the
attestation to exist in the historical source commit would make unchanged
enrolled artifacts unverifiable.

## Root Cause

Validation provenance was initially treated as descriptive metadata rather
than an executable trust boundary. Artifact identity alone cannot prove which
validator and context produced a result, while resolving evidence through a
mutable branch permits evidence to change between validation and consumption.
Conflating the source commit with the evidence commit also prevents newer
evidence from attesting unchanged historical source bytes.

## Solution

Compile a dedicated, deterministic attestation and lock source authority and
evidence authority independently:

1. Require `SOURCE_DATE_EPOCH`; never use wall-clock time in generated output.
2. Record every artifact's path, Git blob SHA-1, content SHA-256, and explicit
   Pydantic result.
3. Record a sorted, exact manifest of every validation input: compiler code,
   schema code, drafts, rule registry, and parameter registry.
4. Digest the canonical path/blob/content manifest and include package versions
   and validation options.
5. Resolve the attestation at an immutable evidence commit. Match the selected
   entry to the record's enrolled source path/blob/content identities rather
   than requiring the evidence artifact in the historical source commit.
6. At runtime, recompute the filtered path set and verify every Git blob and
   content digest before trusting the stored result.

The compiler's core identity shape is:

```python
manifest_identity = "".join(
    f"{item['path']}|{item['git_blob_sha']}|{item['content_sha256']}\n"
    for item in manifest
).encode()

attestation = {
    "generated_at": generated_at_from_source_date_epoch,
    "context_manifest_sha256": hashlib.sha256(manifest_identity).hexdigest(),
    "context_manifest": manifest,
    "artifacts": source_bound_results,
}
```

The consumer must reject missing, extra, reordered, or changed context inputs,
then require exact equality for the selected artifact:

```r
identical(entry$source_path, record$source_artifact_path) &&
  identical(entry$source_git_blob_sha, record$source_artifact_blob_sha) &&
  identical(entry$source_content_sha256, record$source_content_sha256)
```

Keep broad agent-review findings as informational provenance unless governance
explicitly activates them. A dedicated schema attestation is the authority for
the schema gate; an aggregate `summary.passed` value is not.

## Prevention

- Treat validator code and lookup registries as inputs to validation, not as
  deployment details.
- Store both Git object identity and content SHA-256 at trust boundaries.
- Generate evidence deterministically and test byte-identical output for equal
  inputs and epoch.
- Verify exact manifest set equality so newly added validator inputs cannot be
  silently omitted.
- Separate immutable source enrollment from immutable evidence publication when
  evidence may be introduced after enrollment.
- Test tampered source entries, changed context blobs, extra matched paths,
  malformed timestamps, missing evidence, and historical-source compatibility.

## Related

- [Persisted-state approval and race matrix](../testing-patterns/2026-08-26-persisted-state-approval-race-matrix.md)
- [Pydantic registry context requirements](../testing-patterns/2026-08-15-pydantic-rule-ids-context.md)
- [Human review rubric approval-gate plan](../../plans/2026-08-25-human-review-rubric-approval-gate.md)
