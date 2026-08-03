"""Tests for state machine — Phase 4 Step 9."""

from pathlib import Path

import pytest

from extraction_pipeline.state import (
    ExtractionState,
    ItemState,
    RunState,
    StateTransitionError,
    load_run_state,
    save_run_state,
    transition,
    VALID_TRANSITIONS,
)


class TestTransitions:
    def test_valid_transition(self) -> None:
        result = transition(ExtractionState.QUEUED, ExtractionState.SOURCE_VERIFIED)
        assert result == ExtractionState.SOURCE_VERIFIED

    def test_invalid_transition_raises(self) -> None:
        with pytest.raises(StateTransitionError, match="Invalid transition"):
            transition(ExtractionState.QUEUED, ExtractionState.CANONICAL)

    def test_canonical_is_terminal(self) -> None:
        assert VALID_TRANSITIONS[ExtractionState.CANONICAL] == set()

    def test_blocked_is_terminal(self) -> None:
        assert VALID_TRANSITIONS[ExtractionState.BLOCKED] == set()

    def test_gate_can_go_to_canonical_or_blocked(self) -> None:
        targets = VALID_TRANSITIONS[ExtractionState.GATE_RESULTS_READY]
        assert ExtractionState.CANONICAL in targets
        assert ExtractionState.BLOCKED in targets

    def test_full_blocked_sequence(self) -> None:
        state = ExtractionState.QUEUED
        for target in [
            ExtractionState.SOURCE_VERIFIED,
            ExtractionState.EVIDENCE_COLLECTED,
            ExtractionState.CANDIDATE_DRAFTED,
            ExtractionState.CRITIC_REVIEWED,
            ExtractionState.GATE_RESULTS_READY,
            ExtractionState.BLOCKED,
        ]:
            state = transition(state, target)
        assert state == ExtractionState.BLOCKED

    @pytest.mark.parametrize("current,target", [
        (ExtractionState.CANONICAL, ExtractionState.QUEUED),
        (ExtractionState.BLOCKED, ExtractionState.EVIDENCE_COLLECTED),
        (ExtractionState.QUEUED, ExtractionState.EVIDENCE_COLLECTED),
        (ExtractionState.QUEUED, ExtractionState.BLOCKED),
        (ExtractionState.CANONICAL, ExtractionState.BLOCKED),
    ])
    def test_invalid_transition_raises_parametrized(
        self, current: ExtractionState, target: ExtractionState
    ) -> None:
        with pytest.raises(StateTransitionError, match="Invalid transition"):
            transition(current, target)


class TestRunState:
    def test_save_and_load(self, tmp_path: Path) -> None:
        state = RunState(
            execution_id="exec-001",
            items={
                "INV-001": ItemState(
                    inventory_id="INV-001",
                    state=ExtractionState.QUEUED,
                )
            },
        )
        state_dir = tmp_path / "runs" / "exec-001"
        save_run_state(state, state_dir)
        loaded = load_run_state(state_dir)
        assert loaded.execution_id == "exec-001"
        assert len(loaded.items) == 1
        assert loaded.items["INV-001"].state == ExtractionState.QUEUED

    def test_load_missing(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            load_run_state(tmp_path / "nonexistent")
