"""Extraction state machine — Phase 4 Step 9.

Deterministic state transitions from inventory item to evidence packet,
candidate, critic result, gate results, and canonical set or blocked issue.
"""

import json
from enum import Enum
from pathlib import Path

from loguru import logger
from pydantic import BaseModel, Field


class ExtractionState(str, Enum):
    """Valid states in the extraction pipeline."""
    QUEUED = "queued"
    SOURCE_VERIFIED = "source_verified"
    EVIDENCE_COLLECTED = "evidence_collected"
    CANDIDATE_DRAFTED = "candidate_drafted"
    CRITIC_REVIEWED = "critic_reviewed"
    GATE_RESULTS_READY = "gate_results_ready"
    CANONICAL = "canonical"
    BLOCKED = "blocked"


VALID_TRANSITIONS: dict[ExtractionState, set[ExtractionState]] = {
    ExtractionState.QUEUED: {ExtractionState.SOURCE_VERIFIED},
    ExtractionState.SOURCE_VERIFIED: {ExtractionState.EVIDENCE_COLLECTED},
    ExtractionState.EVIDENCE_COLLECTED: {ExtractionState.CANDIDATE_DRAFTED},
    ExtractionState.CANDIDATE_DRAFTED: {ExtractionState.CRITIC_REVIEWED},
    ExtractionState.CRITIC_REVIEWED: {ExtractionState.GATE_RESULTS_READY},
    ExtractionState.GATE_RESULTS_READY: {ExtractionState.CANONICAL, ExtractionState.BLOCKED},
    ExtractionState.CANONICAL: set(),  # terminal
    ExtractionState.BLOCKED: set(),  # terminal
}


class StateTransitionError(Exception):
    """Invalid state transition."""


class ItemState(BaseModel):
    """Persisted state for a single inventory item."""
    inventory_id: str
    state: ExtractionState
    evidence_json_path: str | None = None
    candidate_json_path: str | None = None
    critic_json_path: str | None = None
    gate_json_path: str | None = None
    canonical_path: str | None = None
    issue_ids: list[str] = Field(default_factory=list)


def transition(current: ExtractionState, target: ExtractionState) -> ExtractionState:
    """Validate and execute a state transition."""
    if target not in VALID_TRANSITIONS.get(current, set()):
        raise StateTransitionError(
            f"Invalid transition: {current.value} -> {target.value}"
        )
    logger.info("State transition", current=current.value, target=target.value)
    return target


class RunState(BaseModel):
    """Top-level run state for a single execution."""
    execution_id: str
    items: dict[str, ItemState]  # inventory_id -> ItemState


def load_run_state(state_dir: Path) -> RunState:
    """Load persisted run state or return empty."""
    state_file = state_dir / "run-state.json"
    if not state_file.exists():
        raise FileNotFoundError(f"Run state not found: {state_file}")
    data = json.loads(state_file.read_text(encoding="utf-8"))
    return RunState(**data)


def save_run_state(state: RunState, state_dir: Path) -> None:
    """Persist run state atomically."""
    state_dir.mkdir(parents=True, exist_ok=True)
    tmp = state_dir / "run-state.json.tmp"
    tmp.write_text(state.model_dump_json(indent=2), encoding="utf-8")
    tmp.rename(state_dir / "run-state.json")
