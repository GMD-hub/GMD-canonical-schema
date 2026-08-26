# Work Report: Lock Extraction Source Resolution and Manifest Identity

## Plan Reference

`.cg-docs/plans/2026-08-25-lock-extraction-source-resolution.md`

## Active Deviation Policy

Stored policy: `ask`. No runtime override. The unrecognized token `pahses` was ignored; `ALL` indicates the requested cross-phase intent.

## Completed Steps and Phases

- Environment established with Python 3.14.4 and requirements synchronized.
- Plan artifact validation passed.
- Roadmap feature `lock-extraction-source-resolution` marked active.
- Phase 1 completed on 2026-08-26.

## Deviations

None.

## Accepted Exceptions

None.

## Evidence

| ID | Status | Evidence |
|----|--------|----------|
| V1 | passed | 28 tests passed in `tests/extraction/test_manifest_models.py` |
| V2 | passed | 41 tests passed in `tests/extraction/test_preflight.py` |
| V3 | passed | 8 tests passed in `tests/extraction/test_source.py` |
| V4 | passed | 8 tests passed in `tests/extraction/test_source_gate.py` |
| V5 | passed | Full suite: 318 passed, 1 skipped; `git diff --check` passed; no protected extraction config, governance decision, or workflow changed |
| V6 | passed | SL1-SL5 proposal and exact unapplied target changes recorded below; all eight hashes independently recomputed at the pinned commit |
| V7 | blocked | Durable GPID approval not found |
| V8 | blocked | Requires approved configuration and CI activation |
| V9 | pending | Final path and diff checks |

## Constraints Check

| ID | Status | Result |
|----|--------|--------|
| C1 | passed | Protected configuration and workflow files were excluded from Phase 1 edits. |
| C2 | active | Pandoc 3.1.12 is treated only as a proposed future runtime. |
| C3 | passed | Exact identity, ordering, traversal, and digest checks passed. |
| C4 | passed | Synthetic preflight and source-gate tests passed. |
| C5 | active | Approved CVS artifacts, drafts, and country parameters remain untouched. |

## Remaining Uncertainty

- SL1-SL5 lack a locatable durable GPID approval.
- All eight SHA-256 values were independently recomputed at the pinned commit; chapter 7 is recorded below with a complete digest.

## Phase 2 Source-Lock Proposal

Independent checkout: `https://github.com/GMD-hub/GMD-guidelines` at detached `HEAD` `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`.

| Ballot | Proposed decision |
|--------|-------------------|
| SL1 | Approve the repository, commit, and eight exact path/hash identities below. |
| SL2 | Approve `docs/GMD_household_survey_harmonization.md` as the singleton `supporting` source. |
| SL3 | Approve `gmd_version: "3.0"` in both protected extraction YAML files, superseding only Decision 4's GMD-version value. |
| SL4 | Approve future Pandoc runtime `3.1.12` and installation mechanism `pandoc/actions/setup@86321b6dd4675f5014c611e05088e10d4939e09e` (`v1`). This is not evidence of the historical August runtime. |
| SL5 | Approve chapters 2-7 as `included` and chapter 8 as `welfare-excluded`. |

| Path | Scope | Independently recomputed SHA-256 |
|------|-------|---------------------------------|
| `chapters/chapter2-IDN.qmd` | `included` | `5e25f7bc25031e102f8152feab8236c6384f1a3a438fcfb4e9d7b85f16da3e39` |
| `chapters/chapter3-GEO.qmd` | `included` | `850d635bb2cb36703e756d307e24cf33c94101e95c6ba5b9027fb44f1044e32e` |
| `chapters/chapter4-DEM.qmd` | `included` | `f091a0c110d931b911799618005a31dab9375794f68aca270653f9dc5d07acd0` |
| `chapters/chapter5-LMR.qmd` | `included` | `c46796103d86412daf8d38bd56fbe118e669aa319d7948822a3476239c6d0d40` |
| `chapters/chapter6-UTL.qmd` | `included` | `e8cb9818dd8c69317e7bb752d7afab9d6d3bc60c22526a72f751fe449bea1ba0` |
| `chapters/chapter7-DWL.qmd` | `included` | `3d881952d4ec0f21c88fd31101a0b0224681a19a7a1a7ec822f8bdab9d700743` |
| `chapters/chapter8-CONS.qmd` | `welfare-excluded` | `1fc00a05f15422d7217c41147df24dc76f82417f8fc3c725889ef97354946b31` |
| `docs/GMD_household_survey_harmonization.md` | `supporting` | `30cc0f581b5f0183a303357157379f419356619e4b2847b43da8445a97012136` |

### Exact Unapplied Target Changes

`governance/decisions/Extraction-Source-Lock-2026-08.md`:

- Create with `status: draft`, `authority: GPID Team`, separate SL1-SL5 sections, the identities above, and an empty locatable approval reference for each ballot item.
- State that SL3 supersedes only the `gmd_version` value in `Extraction-Preflight-2026-08.md` Decision 4.
- Change no status to approved until every approval reference is populated by an authorized maintainer.

`extraction/config/source-manifest.v1.yaml`:

```diff
-# Authority: governance/decisions/Extraction-Preflight-2026-08.md
+# Authority: governance/decisions/Extraction-Source-Lock-2026-08.md
-# Must be regenerated when a new guideline revision is approved for extraction.
-# Do not edit file hashes manually — they are set by the manifest resolver.
+# Approved hashes are independently recomputed at the approved commit and
+# applied through the recorded decision. The resolver verifies but never
+# generates or applies approved identity values.
-  commit_sha: null  # TODO: set by human after resolving the approved revision
-  # The brainstorm pinned commit d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
-  # but Phase 1 requires fresh resolution and approval.
+  commit_sha: "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1"
-  - path: "chapter2-IDN.qmd"
+  - path: "chapters/chapter2-IDN.qmd"
     scope: "included"
-    sha256: null
+    sha256: "5e25f7bc25031e102f8152feab8236c6384f1a3a438fcfb4e9d7b85f16da3e39"
-  - path: "chapter3-GEO.qmd"
+  - path: "chapters/chapter3-GEO.qmd"
     scope: "included"
-    sha256: null
+    sha256: "850d635bb2cb36703e756d307e24cf33c94101e95c6ba5b9027fb44f1044e32e"
-  - path: "chapter4-DEM.qmd"
+  - path: "chapters/chapter4-DEM.qmd"
     scope: "included"
-    sha256: null
+    sha256: "f091a0c110d931b911799618005a31dab9375794f68aca270653f9dc5d07acd0"
-  - path: "chapter5-LMR.qmd"
+  - path: "chapters/chapter5-LMR.qmd"
     scope: "included"
-    sha256: null
+    sha256: "c46796103d86412daf8d38bd56fbe118e669aa319d7948822a3476239c6d0d40"
-  - path: "chapter6-UTL.qmd"
+  - path: "chapters/chapter6-UTL.qmd"
     scope: "included"
-    sha256: null
+    sha256: "e8cb9818dd8c69317e7bb752d7afab9d6d3bc60c22526a72f751fe449bea1ba0"
-  - path: "chapter7-DWL.qmd"
+  - path: "chapters/chapter7-DWL.qmd"
     scope: "included"
-    sha256: null
+    sha256: "3d881952d4ec0f21c88fd31101a0b0224681a19a7a1a7ec822f8bdab9d700743"
-  - path: "chapter8-CONS.qmd"
+  - path: "chapters/chapter8-CONS.qmd"
     scope: "welfare-excluded"
-    sha256: null
+    sha256: "1fc00a05f15422d7217c41147df24dc76f82417f8fc3c725889ef97354946b31"
-supporting_files: []
+supporting_files:
+  - path: "docs/GMD_household_survey_harmonization.md"
+    scope: "supporting"
+    sha256: "30cc0f581b5f0183a303357157379f419356619e4b2847b43da8445a97012136"
-  gmd_version: "1.0"
+  gmd_version: "3.0"
-  version: null  # TODO: set by human after approving exact version and installation method
+  version: "3.1.12"
+  installation_method: "pandoc/actions/setup@86321b6dd4675f5014c611e05088e10d4939e09e"
```

`extraction/config/extraction-governance.v1.yaml`:

```diff
-gmd_version: "1.0"
+gmd_version: "3.0"
-    source_chapter: "chapter2-IDN.qmd"
+    source_chapter: "chapters/chapter2-IDN.qmd"
-    source_chapter: "chapter3-GEO.qmd"
+    source_chapter: "chapters/chapter3-GEO.qmd"
-    source_chapter: "chapter4-DEM.qmd"
+    source_chapter: "chapters/chapter4-DEM.qmd"
-    source_chapter: "chapter5-LMR.qmd"
+    source_chapter: "chapters/chapter5-LMR.qmd"
-    source_chapter: "chapter6-UTL.qmd"
+    source_chapter: "chapters/chapter6-UTL.qmd"
-    source_chapter: "chapter7-DWL.qmd"
+    source_chapter: "chapters/chapter7-DWL.qmd"
```

`.github/workflows/validate.yml`, immediately after the repository checkout and before extraction-related tests:

```diff
       - name: Check out repository
         uses: actions/checkout@v4
+
+      - name: Check out approved GMD guidelines source
+        uses: actions/checkout@v4
+        with:
+          repository: GMD-hub/GMD-guidelines
+          ref: d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
+          path: gmd-guidelines
+          persist-credentials: false
+
+      # Immutable commit for pandoc/actions/setup v1.
+      - name: Set up approved Pandoc runtime
+        uses: pandoc/actions/setup@86321b6dd4675f5014c611e05088e10d4939e09e
+        with:
+          version: "3.1.12"
@@
       - name: Install dependencies
         run: python3 -m pip install --requirement requirements.txt
+
+      - name: Verify approved extraction source identity
+        run: |
+          python3 -m extraction_pipeline.source_gate \
+            --manifest extraction/config/source-manifest.v1.yaml \
+            --governance extraction/config/extraction-governance.v1.yaml \
+            --checkout gmd-guidelines
```

## Final Status

Blocked at Phase 2 Step 7: durable GPID approval for SL1-SL5 is unavailable. Protected decision, configuration, and CI activation remain unapplied.
