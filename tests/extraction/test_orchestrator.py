"""Tests for the extraction orchestrator — Phase 4 Step 9."""

from pathlib import Path

import pytest

from extraction_pipeline.orchestrator import initialize_run, run_item_pipeline
from extraction_pipeline.state import ExtractionState, ItemState


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
        "g3_evidence_collected": True,
        "g3_all_citations_valid": True,
        "g4_excerpt_hash_match": True,
        "g4_line_bounds_recovered": True,
        "g5_all_required_present": True,
        "g5_no_governance_blocked": True,
        "g6_all_sections_present": True,
        "g8_targets_exist": True,
        "g8_no_cycles": True,
        "g8_no_duplicate_ids": True,
        "g9_leakage_report": {"leaked": False, "leaked_ids": [], "detector_version": "v1-content"},
    }

    def test_canonical_path(self, tmp_path: Path) -> None:
        """An item with all gates passed and no blocking issues reaches CANONICAL."""
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            _source_dir=tmp_path,
            _evidence_packet={},
            _candidate={},
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            output_root=tmp_path,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.CANONICAL
        assert result.canonical_path is not None

    def test_blocked_path_on_critic_rejection(self, tmp_path: Path) -> None:
        """A critic rejection must lead to BLOCKED state."""
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        result = run_item_pipeline(
            item=item,
            _source_dir=tmp_path,
            _evidence_packet={},
            _candidate={},
            critic_disposition="rejected",
            gate_results=self._ALL_GATES_PASS,
            output_root=tmp_path,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_blocked_path_on_blocking_issues(self, tmp_path: Path) -> None:
        """An item with blocking issues must reach BLOCKED even if gates pass."""
        item = ItemState(
            inventory_id="INV-001",
            state=ExtractionState.QUEUED,
            issue_ids=["ISSUE-001"],
        )
        result = run_item_pipeline(
            item=item,
            _source_dir=tmp_path,
            _evidence_packet={},
            _candidate={},
            critic_disposition="accepted",
            gate_results=self._ALL_GATES_PASS,
            output_root=tmp_path,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_blocked_path_on_gate_failure(self, tmp_path: Path) -> None:
        """A gate failure must lead to BLOCKED state."""
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        gates = dict(self._ALL_GATES_PASS)
        gates["g3_all_citations_valid"] = False
        result = run_item_pipeline(
            item=item,
            _source_dir=tmp_path,
            _evidence_packet={},
            _candidate={},
            critic_disposition="accepted",
            gate_results=gates,
            output_root=tmp_path,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED

    def test_blocked_path_on_welfare_leakage(self, tmp_path: Path) -> None:
        """Welfare leakage (G9 fail) must lead to BLOCKED state."""
        item = ItemState(inventory_id="INV-001", state=ExtractionState.QUEUED)
        gates = dict(self._ALL_GATES_PASS)
        gates["g9_leakage_report"] = {
            "leaked": True,
            "leaked_ids": ["INV-001"],
            "detector_version": "v1-content",
        }
        result = run_item_pipeline(
            item=item,
            _source_dir=tmp_path,
            _evidence_packet={},
            _candidate={},
            critic_disposition="accepted",
            gate_results=gates,
            output_root=tmp_path,
            execution_id="exec-001",
        )
        assert result.state == ExtractionState.BLOCKED
