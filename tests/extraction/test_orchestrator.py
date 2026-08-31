"""Tests for the extraction orchestrator — Phase 4 Step 9."""

import copy
import hashlib
from pathlib import Path

import pytest

from extraction_pipeline.orchestrator import (
    OrchestrationError,
    initialize_run,
    run_item_pipeline,
)
from extraction_pipeline.evidence import collect_evidence, validate_citation
from extraction_pipeline.preflight import PROJECT_ROOT
from extraction_pipeline.source import resolve_source
from extraction_pipeline.state import ExtractionState, ItemState
from schema.extraction.manifest import ResolvedSource, SourceManifest


@pytest.fixture
def pipeline_source(
    source_repository: dict[str, object],
) -> tuple[Path, SourceManifest, ResolvedSource, dict, dict]:
    root = source_repository["root"]
    manifest_data = source_repository["manifest"]
    assert isinstance(root, Path)
    assert isinstance(manifest_data, dict)
    manifest = SourceManifest.model_validate(manifest_data)
    proof = resolve_source(root, manifest, "2026-08-30T12:00:00Z")
    evidence = collect_evidence(
        proof,
        {
            "inventory_id": "INV-001",
            "source_path": "docs/source.md",
            "citations": [
                {
                    "citation_id": "CIT-001",
                    "source_path": "docs/source.md",
                    "excerpt": "immutable source bytes",
                    "expected_excerpt_sha256": hashlib.sha256(
                        b"immutable source bytes"
                    ).hexdigest(),
                }
            ],
        },
    )
    candidate = {
        "inventory_id": "INV-001",
        "source_proof_sha256": proof.proof_sha256(),
        "module_code": "FIXTURE",
        "variable_name": "fixture_variable",
        "canonical_label": "Fixture variable",
        "tier": "1",
        "value_codes": [],
        "allowed_range": {},
        "missing_codes": [],
        "field_classifications": {"canonical_label": "source-explicit"},
        "evidence_ids": {
            field: ["CIT-001"]
            for field in (
                "canonical_label",
                "tier",
                "value_codes",
                "allowed_range",
                "missing_codes",
            )
        },
        "blocking_issue_ids": [],
    }
    return root, manifest, proof, evidence, candidate


class TestInitializeRun:
    def test_initializes_all_items_queued(self) -> None:
        run_state = initialize_run("exec-001", ["INV-001", "INV-002"])
        assert run_state.execution_id == "exec-001"
        assert len(run_state.items) == 2
        assert run_state.items["INV-001"].state == ExtractionState.QUEUED
        assert run_state.items["INV-002"].state == ExtractionState.QUEUED

    def test_empty_inventory(self) -> None:
        run_state = initialize_run("exec-001", [])
        assert run_state.items == {}


class TestRunItemPipeline:
    _ALL_GATES_PASS = {
        "g6_all_sections_present": True,
        "g8_targets_exist": True,
        "g8_no_cycles": True,
        "g8_no_duplicate_ids": True,
        "g9_leakage_report": {"leaked": False, "leaked_ids": [], "detector_version": "v1-content"},
    }

    def test_canonical_path(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        """An item with all gates passed and no blocking issues reaches CANONICAL."""
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.CANONICAL
        assert result.canonical_path is not None
        assert result.canonical_path.startswith(
            str(PROJECT_ROOT / "extraction" / "20_drafts" / "runs")
        )

    def test_blocked_path_on_critic_rejection(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        """A critic rejection must lead to BLOCKED state."""
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="rejected",
            gate_results=self._ALL_GATES_PASS,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_blocked_path_on_blocking_issues(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        """An item with blocking issues must reach BLOCKED even if gates pass."""
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(
            inventory_id="INV-001",
            state=ExtractionState.QUEUED,
            issue_ids=["ISSUE-001"],
        )
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_blocked_path_on_gate_failure(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        """A gate failure must lead to BLOCKED state."""
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        gates = dict(self._ALL_GATES_PASS)
        gates["g6_all_sections_present"] = False
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=gates,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_blocked_path_on_welfare_leakage(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        """Welfare leakage (G9 fail) must lead to BLOCKED state."""
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        gates = dict(self._ALL_GATES_PASS)
        gates["g9_leakage_report"] = {
            "leaked": True,
            "leaked_ids": ["INV-001"],
            "detector_version": "v1-content",
        }
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=gates,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_missing_source_proof_fails_before_state_transition(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root, manifest, _, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        with pytest.raises(OrchestrationError, match="proof is required"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=None,
                _evidence_packet=evidence,
                _candidate=candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )
        assert item.state == ExtractionState.QUEUED

    def test_serialized_source_proof_is_consumed(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root, manifest, original, evidence, candidate = pipeline_source
        proof = ResolvedSource.model_validate_json(original.model_dump_json())
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.CANONICAL

    def test_forged_proof_cannot_enter_source_verified(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root, manifest, proof, evidence, candidate = pipeline_source
        forged_data = proof.model_dump()
        forged_data["repository"] = {
            "url": proof.repository.url,
            "commit_sha": "a" * 40,
        }
        forged = ResolvedSource.model_validate(forged_data)
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        with pytest.raises(OrchestrationError, match="trusted source policy"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=forged,
                _evidence_packet=evidence,
                _candidate=candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )
        assert item.state == ExtractionState.QUEUED

    def test_changed_worktree_does_not_change_evidence_or_orchestration(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root, manifest, proof, _, candidate = pipeline_source
        (root / "docs/source.md").write_bytes(b"mutable worktree bytes\n")
        committed_result = validate_citation(
            proof,
            "docs/source.md",
            "immutable source bytes",
        )
        mutable_result = validate_citation(
            proof,
            "docs/source.md",
            "mutable worktree bytes",
        )
        assert committed_result.valid
        assert not mutable_result.valid
        evidence = collect_evidence(
            proof,
            {
                "inventory_id": "INV-001",
                "source_path": "docs/source.md",
                "citations": [
                    {
                        "citation_id": "CIT-001",
                        "source_path": "docs/source.md",
                        "excerpt": "immutable source bytes",
                        "expected_excerpt_sha256": hashlib.sha256(
                            b"immutable source bytes"
                        ).hexdigest(),
                    }
                ],
            },
        )
        assert proof.get_bytes("docs/source.md") == b"immutable source bytes\n"
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.CANONICAL

    def test_evidence_and_candidate_must_bind_to_proof(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        changed_evidence = dict(evidence, source_sha256="a" * 64)
        with pytest.raises(OrchestrationError, match="source_sha256"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=proof,
                _evidence_packet=changed_evidence,
                _candidate=candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )

        forged_evidence = copy.deepcopy(evidence)
        forged_evidence["citations"][0].update(
            {
                "excerpt": "forged but internally consistent excerpt",
                "excerpt_sha256": hashlib.sha256(
                    b"forged but internally consistent excerpt"
                ).hexdigest(),
            }
        )
        with pytest.raises(OrchestrationError, match="proof bytes"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=proof,
                _evidence_packet=forged_evidence,
                _candidate=candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )

        changed_candidate = dict(candidate)
        changed_candidate["evidence_ids"] = {
            "canonical_label": ["CIT-UNKNOWN"]
        }
        with pytest.raises(OrchestrationError, match="validated proof-backed"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=proof,
                _evidence_packet=evidence,
                _candidate=changed_candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )

        changed_candidate = dict(candidate, source_proof_sha256="b" * 64)
        with pytest.raises(OrchestrationError, match="source_proof_sha256"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=proof,
                _evidence_packet=evidence,
                _candidate=changed_candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )

        unknown_field_candidate = copy.deepcopy(candidate)
        unknown_field_candidate["evidence_ids"]["not_a_candidate_field"] = [
            "CIT-001"
        ]
        with pytest.raises(OrchestrationError, match="unknown candidate fields"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=proof,
                _evidence_packet=evidence,
                _candidate=unknown_field_candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="exec-001",
            )

        missing_field_evidence = copy.deepcopy(candidate)
        missing_field_evidence["evidence_ids"].pop("tier")
        caller_override = dict(
            self._ALL_GATES_PASS,
            g5_all_required_present=True,
            g5_no_governance_blocked=True,
        )
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=missing_field_evidence,
            critic_disposition="accepted",
            gate_results=caller_override,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_execution_id_traversal_fails_before_state_transition(
        self,
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root, manifest, proof, evidence, candidate = pipeline_source
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        with pytest.raises(OrchestrationError, match="safe path component"):
            run_item_pipeline(
                item=item,
                source_repository=root,
                source_manifest=manifest,
                resolved_source=proof,
                _evidence_packet=evidence,
                _candidate=candidate,
                critic_disposition="accepted",
                gate_results=self._ALL_GATES_PASS,
                execution_id="../../knowledge",
            )
        assert item.state == ExtractionState.QUEUED

    def test_nondefault_policy_run_root_controls_all_generated_paths(
        self,
        source_repository: dict[str, object],
        pipeline_source: tuple[Path, SourceManifest, ResolvedSource, dict, dict],
    ) -> None:
        root = source_repository["root"]
        manifest_data = copy.deepcopy(source_repository["manifest"])
        assert isinstance(root, Path)
        assert isinstance(manifest_data, dict)
        manifest_data["output"]["run_root"] = (
            "extraction/20_drafts/custom-runs/"
        )
        manifest_data["output"]["allowlist"] = [
            "extraction/20_drafts/custom-runs/"
        ]
        manifest = SourceManifest.model_validate(manifest_data)
        proof = resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        evidence = collect_evidence(
            proof,
            {
                "inventory_id": "INV-001",
                "source_path": "docs/source.md",
                "citations": [
                    {
                        "citation_id": "CIT-001",
                        "source_path": "docs/source.md",
                        "excerpt": "immutable source bytes",
                        "expected_excerpt_sha256": hashlib.sha256(
                            b"immutable source bytes"
                        ).hexdigest(),
                    }
                ],
            },
        )
        candidate = copy.deepcopy(pipeline_source[4])
        candidate["source_proof_sha256"] = proof.proof_sha256()
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            source_repository=root,
            source_manifest=manifest,
            resolved_source=proof,
            _evidence_packet=evidence,
            _candidate=candidate,
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            execution_id="exec-001",
        )
        expected_root = str(
            PROJECT_ROOT / "extraction" / "20_drafts" / "custom-runs"
        )
        generated_paths = [
            result.evidence_json_path,
            result.candidate_json_path,
            result.critic_json_path,
            result.gate_json_path,
            result.canonical_path,
        ]
        assert all(
            path is not None and path.startswith(expected_root)
            for path in generated_paths
        )
