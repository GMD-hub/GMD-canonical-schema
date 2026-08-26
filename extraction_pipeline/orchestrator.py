"""Extraction orchestrator — Phase 4 Step 9.

Drives the per-item state machine through the extraction phases:
preflight → source resolution → evidence collection → candidate drafting →
critic review → gate evaluation → canonical emission or blocked issue.

This module is the single entry point that ties the 6 phases together.
Each phase module is independently callable; the orchestrator sequences
calls into the existing modules without containing domain logic.
"""

from pathlib import Path
from typing import Any

from loguru import logger

from extraction_pipeline.gates import GateRunner
from extraction_pipeline.state import (
    ExtractionState,
    ItemState,
    RunState,
    transition,
)


class OrchestrationError(Exception):
    """A blocking orchestration failure."""


def run_item_pipeline(
    item: ItemState,
    _source_dir: Path,
    _evidence_packet: dict[str, Any],
    _candidate: dict[str, Any],
    critic_disposition: str,
    gate_results: dict[str, bool],
    output_root: Path,
    execution_id: str,
) -> ItemState:
    """Drive a single inventory item through the extraction state machine.

    Operational callers must pass the supported ``source_gate`` command before
    invoking item orchestration; direct helper calls are library/test APIs only.

    This is a thin sequencer — it transitions state, runs gates, and writes
    output. Domain logic (evidence collection, candidate drafting, critic
    review) is performed by the caller and passed in as inputs.

    Args:
        item: The item's current state.
        source_dir: Root directory of the resolved source checkout.
        evidence_packet: Evidence collected for this item.
        candidate: The extraction candidate dict.
        critic_disposition: "accepted", "challenged", or "rejected".
        gate_results: Dict of gate-name → bool for G3-G9.
        output_root: Root directory for output writes.
        execution_id: The run execution ID.

    Returns:
        Updated ItemState with terminal state (CANONICAL or BLOCKED).
    """
    # Phase: source already verified by the mandatory source gate.
    item.state = transition(item.state, ExtractionState.SOURCE_VERIFIED)

    # Phase: evidence collected
    item.state = transition(item.state, ExtractionState.EVIDENCE_COLLECTED)
    item.evidence_json_path = str(
        output_root / "runs" / execution_id / "evidence" / f"{item.inventory_id}.json"
    )

    # Phase: candidate drafted
    item.state = transition(item.state, ExtractionState.CANDIDATE_DRAFTED)
    item.candidate_json_path = str(
        output_root / "runs" / execution_id / "candidates" / f"{item.inventory_id}.json"
    )

    # Phase: critic reviewed
    item.state = transition(item.state, ExtractionState.CRITIC_REVIEWED)
    item.critic_json_path = str(
        output_root / "runs" / execution_id / "critic" / f"{item.inventory_id}.json"
    )

    # Phase: gate results — all per-item gates must pass for canonical
    g3 = GateRunner.g3_evidence_gate(
        gate_results.get("g3_evidence_collected", False),
        gate_results.get("g3_all_citations_valid", False),
    )
    g4 = GateRunner.g4_citation_gate(
        gate_results.get("g4_excerpt_hash_match", False),
        gate_results.get("g4_line_bounds_recovered", False),
    )
    g5 = GateRunner.g5_field_gate(
        gate_results.get("g5_all_required_present", False),
        gate_results.get("g5_no_governance_blocked", False),
    )
    g6 = GateRunner.g6_section_gate(
        gate_results.get("g6_all_sections_present", False),
    )
    g7 = GateRunner.g7_critic_gate(critic_disposition)
    g8 = GateRunner.g8_graph_gate(
        gate_results.get("g8_targets_exist", False),
        gate_results.get("g8_no_cycles", False),
        gate_results.get("g8_no_duplicate_ids", False),
    )
    g9 = GateRunner.g9_welfare_gate(
        gate_results.get("g9_leakage_report", {"leaked": True}),
    )

    all_gates_passed = all(
        g.result == "passed" for g in (g3, g4, g5, g6, g7, g8, g9)
    )

    item.state = transition(item.state, ExtractionState.GATE_RESULTS_READY)
    item.gate_json_path = str(
        output_root / "runs" / execution_id / "gates" / f"{item.inventory_id}.json"
    )

    # Terminal: canonical or blocked
    if all_gates_passed and not item.issue_ids:
        item.state = transition(item.state, ExtractionState.CANONICAL)
        item.canonical_path = str(
            output_root / "runs" / execution_id / "canonical" / f"{item.inventory_id}.md"
        )
        logger.info(
            "Item canonicalized",
            inventory_id=item.inventory_id,
            canonical_path=item.canonical_path,
        )
    else:
        item.state = transition(item.state, ExtractionState.BLOCKED)
        logger.warning(
            "Item blocked",
            inventory_id=item.inventory_id,
            issue_ids=item.issue_ids,
            g3=g3.result,
            g5=g5.result,
            g7=g7.result,
        )

    return item


def initialize_run(
    execution_id: str,
    inventory_ids: list[str],
) -> RunState:
    """Initialize a RunState with all items in QUEUED state."""
    items = {
        inv_id: ItemState(inventory_id=inv_id, state=ExtractionState.QUEUED)
        for inv_id in inventory_ids
    }
    return RunState(execution_id=execution_id, items=items)
