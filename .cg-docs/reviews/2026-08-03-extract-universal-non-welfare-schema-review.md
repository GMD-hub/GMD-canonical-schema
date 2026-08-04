---
date: 2026-08-03
depth: standard
type: standard
plan: .cg-docs/plans/2026-08-03-extract-universal-non-welfare-schema.md
findings:
  P0.1: fixed
  P0.2: fixed
  P0.3: fixed
  P0.4: fixed
  P0.5: fixed
  P1.1: fixed
  P1.2: fixed
  P1.3: fixed
  P1.4: fixed
  P1.5: fixed
  P2.1: fixed
  P2.2: fixed
  P2.3: fixed
  P2.4: fixed
  P2.5: fixed
  P2.6: fixed
  P2.7: fixed
  P2.8: fixed
  P2.9: fixed
  P2.10: fixed
  P2.11: fixed
  P2.12: fixed
  P2.13: fixed
  P2.14: fixed
  P2.15: fixed
  P2.16: fixed
  P2.17: fixed
  P2.18: fixed
  P2.19: fixed
  P2.20: fixed
  P2.21: fixed
  P2.22: fixed
  P2.23: fixed
  P2.24: fixed
  P2.25: fixed
  P2.26: fixed
  P2.27: fixed
  P2.28: fixed
  P2.29: fixed
  P3.1: fixed
  P3.2: fixed
  P3.3: fixed
  P3.4: fixed
  P3.5: fixed
  P3.6: fixed
  P3.7: fixed
  P3.8: fixed
  P3.9: fixed
  P3.10: fixed
  P3.11: fixed
---

## Review Report

**Review mode**: standard (data-risk signals noted: extraction pipeline, reproducibility-sensitive, survey harmonization, welfare boundary)
**Files reviewed**: ~40 new files (Python pipeline, Pydantic models, tests, config, agent/skill docs, governance record, plan/roadmap status)
**Findings**: 50 (P0: 5, P1: 5, P2: 29, P3: 11)
**Autofix**: 15 safe_auto fixes applied (tests pass: 176 passed, 2 skipped)

> Auto-routing note: the diff matches `data-risk` triggers (`**/extract*.{R,py}`, `**/pipeline*.{R,py}`, reproducibility-sensitive scripts). The user explicitly requested `standard`, so the explicit route is kept and data-risk signals are noted in review focus. Mandatory emphasis applied to `@cg-data-quality`, `@cg-reproducibility`, and `@cg-testing`.

### ⚠️ Incomplete Reviews
- `@cg-version-control` did not produce usable output. Consider re-running `/cg-review` with a higher model tier, or invoke `@cg-version-control` directly.

### P0 — BLOCKING (immediate remediation required)

- **[P0.1]** [cg-reproducibility] `extraction/config/source-manifest.v1.yaml:8` — `commit_sha: null` with TODO; preflight does not enforce non-null
  **Why**: The charter requires "deterministic Python orchestration" and AGENTS.md requires a "pinned source commit." `preflight.py` validates `parser_contract.version` is non-null but no check validates `repository.commit_sha`. With `commit_sha: null`, two runs against different checkout states produce different content with no gate catching it — the pipeline is not deterministic.
  **Fix**: Add a `check_repository_pin(manifest)` preflight step that raises `PreflightError` when `repository.commit_sha` is null or not 40-hex. Also validate the manifest against `SourceManifest` (the Pydantic model) in preflight so null `commit_sha`/`sha256`/`version` are caught loudly at the gate.
  **Tag**: [manual]

- **[P0.2]** [cg-reproducibility] `extraction_pipeline/source.py:55-67` — null expected hashes are hashed but never verified; `verified_sha256=True` set anyway
  **Why**: `verify_source_hashes` skips verification when `entry.get("sha256")` is `None`. With the shipped manifest (all `sha256: null`), G0 receives `hashes_verified=True` even though no hash was compared against an expected value. A tampered or drifted source file passes the source gate — silent data-integrity loss.
  **Fix**: Distinguish "verified against expected" from "hashed only." Either require non-null `sha256` in the manifest before G0 can pass, or set `verified_sha256=False` when any expected hash was null.
  **Tag**: [manual]

- **[P0.3]** [cg-data-quality] `schema/extraction/candidate.py:18-46` — `ExtractionCandidate` has no validator linking null fields to `blocking_issue_ids`
  **Why**: `field-classification.v1.yaml` defines class `unresolved` as "Store null in candidate; block canonical emission." The model has many `Optional` fields and `blocking_issue_ids: list[str]`, but no `model_validator` ensures that when a required field is `None`, a blocking issue is recorded. A candidate with `canonical_label=None` and `blocking_issue_ids=[]` validates cleanly — incomplete candidates can be canonicalized.
  **Fix**: Add a `@model_validator(mode="after")` that requires either the field is non-null or `blocking_issue_ids` is non-empty for each required `source-explicit` field.
  **Tag**: [manual]

- **[P0.4]** [cg-data-quality] `extraction_pipeline/reports.py:62-67` — `check_no_welfare_leakage` is too narrow to enforce the welfare boundary
  **Why**: The detector does a substring match on the inventory ID for `"CONS"`. Per Decision 10, welfare content also includes cross-references to chapter 8 and aggregate consumption references. An inventory ID `INV-UTL-014` whose candidate cites `chapter8-CONS.qmd` passes the check. The check also produces false positives (any ID containing "CONS" as a substring).
  **Fix**: Replace the ID-substring heuristic with a content-based check: inspect each candidate's `evidence_ids` → `Citation.source_path`; flag leakage if any citation points to `chapter8-CONS.qmd`.
  **Tag**: [manual]

- **[P0.5]** [cg-data-quality] `extraction_pipeline/gates.py:139-147` — `g9_welfare_gate` receives a bare `bool`; detector wiring is unverified
  **Why**: `g9_welfare_gate(no_leakage: bool)` trusts its caller. There is no guarantee that `no_leakage` was produced by `check_no_welfare_leakage`. A caller can pass `True` without ever running detection. Combined with P0.4, the welfare gate is effectively a no-op.
  **Fix**: Change the gate signature to accept the detector's structured output, or have `g9_welfare_gate` call the detector itself given the candidate set.
  **Tag**: [manual]

### P1 — CRITICAL (must fix before merge)

- **[P1.1]** [cg-testing] `tests/extraction/test_governance.py:113` — `test_preflight_blocks_on_missing_approval` has no assertion *(vacuous test)*
  **Why**: The function body is `if not decision_file.exists(): pass` with no `assert` in either branch. The test passes vacuously whether the decision file exists or not.
  **Fix**: Either assert the contract against the real validator, or `pytest.fail`/`pytest.skip` with a reason.
  **Tag**: [manual] — *Not autofixed: requires deciding the intended contract.*

- **[P1.2]** [cg-testing] `extraction_pipeline/agents.py:79` — `validate_agent_output` ignores `_schema_version`
  **Why**: The parameter `_schema_version` is never used. The fail-loudly contract requires schema-version mismatches to be caught, yet an `AgentResponse` with any `agent_version` is accepted. No test verifies a version mismatch raises.
  **Fix**: Either implement the version check and add `test_version_mismatch_raises`, or rename the parameter and add a `# TODO` plus a skipped test documenting the gap.
  **Tag**: [manual]

- **[P1.3]** [cg-testing] `schema/extraction/candidate.py:38` — `confidence_scores` not range-constrained
  **Why**: The docstring says `field -> 0.0-1.0` but the field is typed `dict[str, float]` with no `Field(ge=0.0, le=1.0)`. A candidate with `confidence_scores={"age": 5.0}` validates successfully. Same issue in `agents.py:18` (`AgentResponse.confidence`).
  **Fix**: Add a `@field_validator` checking `0.0 <= v <= 1.0`, and add `test_confidence_out_of_range_raises`.
  **Tag**: [manual]

- **[P1.4]** [cg-testing] `tests/extraction/test_preflight.py:62` — `test_run_preflight_passes` permanently skipped in CI
  **Why**: The committed manifest has `parser_contract.version: null`, so this test hits `pytest.skip` on every CI run. The "preflight passes" path is never exercised.
  **Fix**: Add a `test_run_preflight_passes_with_synthetic_manifest` that writes a complete manifest (with non-null version) to `tmp_path` and calls `pf.run_preflight` end-to-end.
  **Tag**: [manual]

- **[P1.5]** [cg-documentation] `schema/extraction/run.py:11-17` vs `governance/decisions/Extraction-Preflight-2026-08.md:128-132` — `ModuleDefinition` model omits the `provenance` field required by Decision 9
  **Why**: Decision 9 states the model should have `provenance`. The implemented model has only 5 fields and uses `extra="forbid"`, so any attempt to supply `provenance` would be rejected — code and governance decision are in direct conflict.
  **Fix**: Either add `provenance` to `ModuleDefinition` to match Decision 9, or amend Decision 9 to drop `provenance`. Mark as a TODO in the decision record's "Pending Human Authorization" list.
  **Tag**: [manual]

### P2 — IMPORTANT (should fix)

- **[P2.1]** [cg-code-quality] `extraction_pipeline/agents.py:71` — Docstring typo: "agract" → **FIXED** (corrected to "against the AgentResponse schema")
  **Tag**: [safe_auto] ✅

- **[P2.2]** [cg-code-quality] `extraction_pipeline/agents.py:13-21` — `AgentResponse`/`CriticResponse` use untyped `dict`/`list[dict]` fields
  **Why**: Bare `dict` defeats type-checking. Should use `dict[str, Any]`.
  **Fix**: Use `dict[str, Any]` for `fields`/`confidence`/`citations`, and `list[dict[str, Any]]` for `blocking_issues`/`findings`.
  **Tag**: [manual]

- **[P2.3]** [cg-code-quality] `extraction_pipeline/agents.py:13-21` — `AgentResponse`/`CriticResponse` lack `extra="forbid"` → **FIXED** (added `model_config = ConfigDict(extra="forbid")`)
  **Tag**: [safe_auto] ✅

- **[P2.4]** [cg-code-quality] `extraction_pipeline/agents.py:73-83` — `validate_agent_output` catches bare `Exception`
  **Why**: Catches `KeyboardInterrupt`/`SystemExit` indirectly and obscures non-validation errors.
  **Fix**: Catch `pydantic.ValidationError` (and `TypeError`) explicitly; re-raise others.
  **Tag**: [manual]

- **[P2.5]** [cg-code-quality] `extraction_pipeline/evidence.py:1-4` — Module docstring says "Phase 5/6" but spans two phases with no step number
  **Fix**: Update to `"""Evidence pipeline — Phase 5 Step 13 / Phase 6 Step 14. Citation validation, evidence collection, and canonical Markdown emission."""`
  **Tag**: [manual]

- **[P2.6]** [cg-code-quality] `extraction_pipeline/evidence.py:9-30` — `validate_citation` returns ad-hoc `dict` instead of a typed pydantic model
  **Why**: Untyped return forces every caller to know the shape; contradicts the strict-model pattern.
  **Fix**: Define a `CitationValidation` pydantic model in `schema/extraction/evidence.py` and return it.
  **Tag**: [manual]

- **[P2.7]** [cg-code-quality] `extraction_pipeline/evidence.py:33-34` — `collect_evidence` is a near-no-op passthrough with unused `_source_dir`
  **Why**: Shipping a stub that silently returns unverified input violates fail-loudly.
  **Fix**: Either implement citation collection against `_source_dir`, or raise `NotImplementedError`.
  **Tag**: [manual]

- **[P2.8]** [cg-code-quality] `extraction_pipeline/evidence.py:74-110` — `canonicalize_to_markdown` uses silent `""` defaults for required frontmatter fields
  **Why**: Emitting `variable_id: ''` into a canonical draft is silent data corruption at the output boundary.
  **Fix**: Raise a `ValueError` when any required field is missing, rather than defaulting to empty string.
  **Tag**: [manual]

- **[P2.9]** [cg-code-quality] `extraction_pipeline/gates.py:19-152` — Every gate method repeats the identical `passed = ...; return GateReport(...)` pattern 11 times (DRY violation)
  **Fix**: Extract a helper `_emit(gate, passed, ok_msg, fail_msg) -> GateReport`.
  **Tag**: [manual]

- **[P2.10]** [cg-code-quality] `extraction_pipeline/preflight.py:60-72` — Required-chapter set hardcoded inside function body, duplicating the manifest
  **Fix**: Drive from a config key or extract to a module-level `REQUIRED_CHAPTERS` constant. *(Comment added noting it's a defensive cross-check.)*
  **Tag**: [manual]

- **[P2.11]** [cg-code-quality] `extraction_pipeline/reports.py:18` — `build_completeness_report` returns untyped `dict`
  **Fix**: Define a `CompletenessReport` pydantic model in `schema/extraction/run.py`.
  **Tag**: [manual]

- **[P2.12]** [cg-code-quality] `extraction_pipeline/reports.py:51-70` — `compare_runs` reads every file into memory before comparing
  **Fix**: Compare file-set keys first, then stream-compare with early-exit.
  **Tag**: [manual]

- **[P2.13]** [cg-code-quality] `extraction_pipeline/reports.py:51` — `compare_runs` excludes `"run-ledger"` via substring, not precise path check
  **Why**: A content file named `run-ledger-notes.md` would be silently skipped.
  **Fix**: Match the exact ledger filename.
  **Tag**: [manual]

- **[P2.14]** [cg-code-quality] `extraction_pipeline/state.py:42-48` — `ItemState.issue_ids: list[str] = []` mutable default → **FIXED** (changed to `Field(default_factory=list)`)
  **Tag**: [safe_auto] ✅

- **[P2.15]** [cg-code-quality] `extraction_pipeline/writers.py:30-38` — `atomic_write_json` `.tmp` suffix bug for multi-suffix paths → **FIXED** (now uses `path.parent / (path.name + ".tmp")`)
  **Tag**: [safe_auto] ✅

- **[P2.16]** [cg-code-quality] `extraction_pipeline/*.py` — No module uses `loguru`; pipeline emits no structured logs
  **Why**: Project convention mandates `loguru` for all logging. Side-effecting modules (`preflight`, `source`, `writers`, `state`) warrant structured logging for auditability.
  **Fix**: Add a `loguru` logger to side-effecting modules and emit `logger.bind(execution_id=...)` events at hash-verify, write, and transition boundaries.
  **Tag**: [manual]

- **[P2.17]** [cg-code-quality] `extraction_pipeline/evidence.py` & `pandoc_ast.py` — Line-bound recovery logic duplicated across modules
  **Fix**: Have `evidence.validate_citation` call `pandoc_ast.recover_line_bounds`.
  **Tag**: [manual]

- **[P2.18]** [cg-reproducibility] `extraction_pipeline/writers.py:23` — `atomic_write_json` omits `sort_keys=True`
  **Why**: Key order depends on construction order; two semantically-equal outputs with different key order fail `compare_runs` or pass falsely. `default=str` is also a silent coercion.
  **Fix**: Add `sort_keys=True` to `json.dumps`. Remove `default=str` or replace with an explicit serializer that raises on unsupported types.
  **Tag**: [manual]

- **[P2.19]** [cg-reproducibility] `extraction_pipeline/state.py:73` — `save_run_state` uses `model_dump_json(indent=2)` without sorted keys; `run-state.json` not excluded from `compare_runs`
  **Fix**: Exclude `run-state.json` from `compare_runs` alongside `run-ledger` (it is orchestration state, not content).
  **Tag**: [manual]

- **[P2.20]** [cg-reproducibility] `extraction_pipeline/reports.py:62-78` — `compare_runs` excludes only `"run-ledger"`; volatile `extracted_on` in canonical Markdown body
  **Why**: `evidence.py:canonicalize_to_markdown` writes `**Extracted on**` into content that `compare_runs` compares. If `extracted_on` is a run timestamp, two runs at different times fail G10.
  **Fix**: (1) Exclude volatile-metadata files from `compare_runs`. (2) Move `extracted_on` to the run ledger only, per Decision 7.
  **Tag**: [manual]

- **[P2.21]** [cg-reproducibility] `extraction_pipeline/pandoc_ast.py:43` — `generate_node_id` truncates SHA-256 to 16 hex chars (64 bits)
  **Why**: Birthday-collision probability ~1% at ~6×10⁸ IDs. Low risk today but a latent hazard for graph integrity.
  **Fix**: Use the full 64-char SHA-256 digest, or add a collision check that fails loudly.
  **Tag**: [advisory]

- **[P2.22]** [cg-reproducibility] `requirements.txt` — dependencies use range constraints, not pinned versions; no lockfile
  **Why**: `pydantic>=2.0,<3.0` etc. are range constraints. Two `pip install` runs at different times resolve different transitive versions, affecting byte-identical output.
  **Fix**: Generate and commit a lockfile (`uv lock` → `uv.lock`, or `pip freeze > requirements.lock`). Pin `pydantic` and `PyYAML` to exact versions.
  **Tag**: [manual]

- **[P2.23]** [cg-architecture] `extraction_pipeline/__init__.py:9` — Missing orchestrator module
  **Why**: The package docstring advertises a "State machine orchestrator," but no module ties the 6 phases together. Each phase is independently callable but there is no single entry point.
  **Fix**: Add `extraction_pipeline/orchestrator.py` that drives the per-item state machine through the phases.
  **Tag**: [manual]

- **[P2.24]** [cg-architecture] `extraction_pipeline/preflight.py` vs `schema/extraction/manifest.py` — Manifest loaded as `dict`, not validated against `SourceManifest`
  **Why**: The rich validators in `manifest.py` (HTTPS enforcement, 40-hex commit_sha, scope literal) are dead code in the pipeline path. `preflight.py` re-implements validation inline that duplicates `SourceFileEntry.scope`'s `Literal`.
  **Fix**: Have `load_manifest()` return `SourceManifest` via `SourceManifest.model_validate(yaml.safe_load(...))`.
  **Tag**: [manual]

- **[P2.25]** [cg-architecture] `extraction_pipeline/agents.py:53-95` — `FakeExtractor`/`FakeCritic` test doubles live in production code
  **Fix**: Move to `tests/extraction/fakes.py`. Define a `Protocol`/`ABC` for real adapters.
  **Tag**: [manual]

- **[P2.26]** [cg-architecture] `extraction_pipeline/evidence.py:11,64` — `validate_citation` and `collect_evidence` return untyped `dict` instead of schema models
  **Fix**: Define a `CitationValidation` model and return `EvidencePacket` from `collect_evidence`.
  **Tag**: [manual]

- **[P2.27]** [cg-architecture] `extraction_pipeline/preflight.py:55-62` — Required-chapter list hardcoded, duplicating `extraction-governance.v1.yaml`
  **Fix**: Load the module registry from `extraction-governance.v1.yaml` and derive `required` from `source_chapter` fields.
  **Tag**: [manual]

- **[P2.28]** [cg-data-quality] `extraction_pipeline/source.py:44-66` — `verified_sha256=True` set even when no expected hash was verified
  **Fix**: Split into `hashed: bool` and `verified_against_manifest: bool`, or require `sha256` non-null before allowing `verified_sha256=True`.
  **Tag**: [manual]

- **[P2.29]** [cg-data-quality] `extraction_pipeline/agents.py:8-26` — `AgentResponse.fields` and `confidence` are untyped/unbounded
  **Why**: `confidence: dict[str, float]` does not validate values are in `[0.0, 1.0]`. Invalid confidence values silently propagate.
  **Fix**: Add `field_validator("confidence")` asserting `0.0 <= v <= 1.0`.
  **Tag**: [manual]

### P3 — MINOR (nice to have)

- **[P3.1]** [cg-code-quality] `extraction_pipeline/gates.py:14-17` — `GateRunner.__init__` is an empty `pass` → **FIXED** (removed)
  **Tag**: [safe_auto] ✅

- **[P3.2]** [cg-code-quality] `extraction_pipeline/hashing.py:11-19` — `hash_file` uses `open()` instead of `path.open()` → **FIXED** (changed to `path.open("rb")`)
  **Tag**: [safe_auto] ✅

- **[P3.3]** [cg-code-quality] `extraction_pipeline/pandoc_ast.py:30-31` — Long single-line list comprehension → **FIXED** (broken across lines)
  **Tag**: [safe_auto] ✅

- **[P3.4]** [cg-code-quality] `schema/extraction/run.py:33` — `GateReport.affected_items: list[str] = []` mutable default → **FIXED** (changed to `Field(default_factory=list)`)
  **Tag**: [safe_auto] ✅

- **[P3.5]** [cg-code-quality] `extraction_pipeline/agents.py:38-58` — `FakeExtractor`/`FakeCritic` live in production module rather than test fixtures
  **Fix**: Move to `tests/extraction/conftest.py` or `tests/extraction/fakes.py`.
  **Tag**: [manual]

- **[P3.6]** [cg-code-quality] `extraction_pipeline/source.py:42-58` — `verify_source_hashes` bypasses streaming hasher → **FIXED** (now calls `hash_file(file_path)`)
  **Tag**: [safe_auto] ✅

- **[P3.7]** [cg-performance] `extraction_pipeline/evidence.py:18` — source file re-read and re-decoded on every citation
  **Fix**: Introduce a small caller that groups citations by `source_path` and caches the decoded string for the duration of a run.
  **Tag**: [manual]

- **[P3.8]** [cg-documentation] `extraction/config/source-manifest.v1.yaml:26-27` — `chapter5-LMR.qmd` missing `sha256: null` → **FIXED** (added)
  **Tag**: [safe_auto] ✅

- **[P3.9]** [cg-documentation] `extraction/skills/modules/dem.md` — no "Expected Variables" section, unlike sibling module docs → **FIXED** (added)
  **Tag**: [safe_auto] ✅

- **[P3.10]** [cg-documentation] `extraction/skills/universal-extraction.md:9` — stray space "VAR- ID" → **FIXED** (corrected to "VAR-id")
  **Tag**: [safe_auto] ✅

- **[P3.11]** [cg-documentation] `README.md` and `knowledge/index.md` — no reference to the new `extraction_pipeline/` package
  **Fix**: Add a row to the README Repository map table and a brief entry in `wiki/Repository-Map.md`.
  **Tag**: [manual]

### ✅ Passed
- `@cg-performance`: No P0/P1 issues. Three safe_auto micro-optimizations applied (P2.1, P2.2, P3.3 in performance agent's numbering — double-scan fix, streaming hasher, line-break). Pipeline is well-suited to its scale.
- `@cg-architecture`: Package separation clean, dependency direction correct (no circular deps), AGENTS.md write boundaries respected, all modules independently testable.

### Test improvements applied (safe_auto)
- Strengthened single-assertion contract tests in `test_contracts.py`, `test_agents.py`, `test_evidence.py` (now assert all supplied fields round-trip)
- Added `test_run_ledger_excluded_from_comparison`, `test_missing_reference_dir_returns_false`, `test_missing_current_dir_returns_false`, `test_different_file_sets_return_false` to `test_completeness.py`
- Added parametrized `test_invalid_transition_raises` (5 cases) to `test_state.py`
- Added `test_missing_governance_raises`, `test_empty_governance_raises`, `test_non_mapping_yaml_raises`, parametrized `test_missing_each_required_key_raises` to `test_preflight.py`
- Converted `BASE_MANIFEST` usages to `copy.deepcopy` via `_base_manifest()` helper in `test_preflight.py`
- Fixed vacuous `test_digest_is_reproducible` and `test_preflight_rejects_branch_names` in `test_manifest.py`
- Added `test_source_path_is_directory_raises` to `test_source.py`
- Added `test_resolve_output_path_empty_filename` and fixed `test_no_partial_write_on_error` (macOS-safe) in `test_writers.py`
- Added `TestResolvedSource` and `TestRunModels` extra-forbid tests to `test_manifest_models.py`
- Added `test_hash_match` and `test_multiline_excerpt_bounds` to `test_evidence.py`
- Added `test_collect_missing_keys_default` to `test_evidence.py`

### Model Advisory Handoff

For the transition to fix triage, the review capability profile suggests:
- **Strong option**: A high-reasoning model (e.g., GPT-4-class or Claude Sonnet/Opus class) for the P0/P1 findings, which involve reproducibility-core logic, welfare-boundary enforcement, and governance decisions requiring careful judgment.
- **Economical option**: A mid-tier model is sufficient for the P2/P3 `manual` findings (typing improvements, DRY refactors, docstring updates) since they are well-specified with clear fixes.
- **Rationale**: The P0 findings (source pinning, welfare leakage, candidate validation) touch data-integrity and reproducibility contracts where errors are costly. The P2/P3 findings are mechanical and low-risk. Availability differs by platform; the user makes the final selection.
