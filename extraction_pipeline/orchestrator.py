"""Extraction orchestrator — Phase 4 Step 9.

Drives the per-item state machine through the extraction phases:
preflight → source resolution → evidence collection → candidate drafting →
critic review → gate evaluation → canonical emission or blocked issue.

This module is the single entry point that ties the 6 phases together.
Each phase module is independently callable; the orchestrator sequences
calls into the existing modules without containing domain logic.
"""

from pathlib import Path, PurePosixPath
import re
from typing import Any

from loguru import logger
from pydantic import ValidationError

from extraction_pipeline.evidence import validate_citation
from extraction_pipeline.gates import GateRunner
from extraction_pipeline.preflight import (
    PROJECT_ROOT,
    PreflightError,
    check_output_allowlist,
)
from extraction_pipeline.source import SourceResolutionError, verify_resolved_source
from extraction_pipeline.state import (
    ExtractionState,
    ItemState,
    RunState,
    transition,
)
from schema.extraction.candidate import (
    REQUIRED_SOURCE_EXPLICIT_FIELDS,
    ExtractionCandidate,
)
from schema.extraction.evidence import CollectedEvidencePacket
from schema.extraction.manifest import ResolvedSource, SourceManifest


_SAFE_COMPONENT_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


class OrchestrationError(Exception):
    """A blocking orchestration failure."""


def run_item_pipeline(
    item: ItemState,
    source_repository: Path,
    source_manifest: SourceManifest,
    resolved_source: ResolvedSource | None,
    _evidence_packet: dict[str, Any],
    _candidate: dict[str, Any],
    critic_disposition: str,
    gate_results: dict[str, Any],
    execution_id: str,
) -> ItemState:
    """Drive a single inventory item through the extraction state machine.

    This is a thin sequencer — it transitions state, runs gates, and writes
    output. Domain logic (evidence collection, candidate drafting, critic
    review) is performed by the caller and passed in as inputs.

    Args:
        item: The item's current state.
        source_repository: Repository whose immutable Git objects are trusted.
        source_manifest: Complete versioned source policy for this run.
        resolved_source: Exact verified source proof with immutable Git bytes.
        evidence_packet: Evidence collected for this item.
        candidate: The extraction candidate dict.
        critic_disposition: "accepted", "challenged", or "rejected".
        gate_results: Dict of gate-name → bool for G3-G9.
        execution_id: The run execution ID.

    Returns:
        Updated ItemState with terminal state (CANONICAL or BLOCKED).
    """
    if resolved_source is None:
        raise OrchestrationError("A verified ResolvedSource proof is required")
    try:
        proof = ResolvedSource.model_validate(resolved_source.model_dump())
    except (AttributeError, ValidationError) as exc:
        raise OrchestrationError("The ResolvedSource proof is invalid") from exc
    try:
        verify_resolved_source(source_repository, source_manifest, proof)
    except SourceResolutionError as exc:
        raise OrchestrationError(
            "The ResolvedSource proof does not match trusted source policy"
        ) from exc

    proof_sha256 = proof.proof_sha256()
    try:
        evidence_packet = CollectedEvidencePacket.model_validate(_evidence_packet)
        candidate = ExtractionCandidate.model_validate(_candidate)
        evidence_source = proof.get_file(evidence_packet.source_path)
    except (KeyError, ValidationError) as exc:
        raise OrchestrationError("Evidence or candidate validation failed") from exc
    expected_evidence = {
        "inventory_id": item.inventory_id,
        "source_sha256": evidence_source.sha256,
        "source_blob_sha": evidence_source.blob_sha,
        "source_commit_sha": proof.repository.commit_sha,
        "source_proof_sha256": proof_sha256,
    }
    for field, expected in expected_evidence.items():
        if getattr(evidence_packet, field) != expected:
            raise OrchestrationError(
                f"Evidence field {field} does not match the ResolvedSource proof"
            )
    if candidate.inventory_id != item.inventory_id:
        raise OrchestrationError("Candidate inventory_id does not match the item")
    if candidate.source_proof_sha256 != proof_sha256:
        raise OrchestrationError(
            "Candidate source_proof_sha256 does not match the ResolvedSource proof"
        )
    citation_ids = {
        citation.citation_id for citation in evidence_packet.citations
    }
    candidate_evidence_ids = {
        citation_id
        for field_ids in candidate.evidence_ids.values()
        for citation_id in field_ids
    }
    if not candidate_evidence_ids or not candidate_evidence_ids.issubset(citation_ids):
        raise OrchestrationError(
            "Candidate evidence_ids must reference validated proof-backed citations"
        )
    unknown_evidence_fields = set(candidate.evidence_ids) - set(
        ExtractionCandidate.model_fields
    )
    if unknown_evidence_fields:
        raise OrchestrationError(
            "Candidate evidence_ids contains unknown candidate fields"
        )
    required_fields_present = all(
        getattr(candidate, field) is not None
        for field in REQUIRED_SOURCE_EXPLICIT_FIELDS
    )
    required_field_evidence_valid = all(
        bool(candidate.evidence_ids.get(field))
        and set(candidate.evidence_ids[field]).issubset(citation_ids)
        for field in REQUIRED_SOURCE_EXPLICIT_FIELDS
    )
    for citation in evidence_packet.citations:
        validation = validate_citation(
            proof,
            citation.source_path,
            citation.excerpt,
            citation.excerpt_sha256,
        )
        if (
            not validation.valid
            or validation.line_start != citation.line_start
            or validation.line_end != citation.line_end
        ):
            raise OrchestrationError(
                "Evidence citation does not validate against proof bytes"
            )

    try:
        check_output_allowlist(source_manifest.model_dump(mode="json"))
    except PreflightError as exc:
        raise OrchestrationError("Source manifest output policy is invalid") from exc
    for label, value in (
        ("execution_id", execution_id),
        ("inventory_id", item.inventory_id),
    ):
        if (
            _SAFE_COMPONENT_PATTERN.fullmatch(value) is None
            or value in (".", "..")
        ):
            raise OrchestrationError(f"{label} must be a safe path component")

    output_root = (
        PROJECT_ROOT / PurePosixPath(source_manifest.output.run_root)
    ).resolve()
    allowlist_roots = [
        (PROJECT_ROOT / PurePosixPath(path)).resolve()
        for path in source_manifest.output.allowlist
    ]

    def governed_output_path(category: str, suffix: str) -> Path:
        output_path = (
            output_root / execution_id / category / f"{item.inventory_id}.{suffix}"
        ).resolve()
        try:
            output_path.relative_to(output_root)
        except ValueError as exc:
            raise OrchestrationError(
                "Generated output path escaped the output root"
            ) from exc
        if not any(
            output_path.is_relative_to(allowlist_root)
            for allowlist_root in allowlist_roots
        ):
            raise OrchestrationError(
                "Generated output path is outside the manifest allowlist"
            )
        return output_path

    output_paths = {
        "evidence": governed_output_path("evidence", "json"),
        "candidate": governed_output_path("candidates", "json"),
        "critic": governed_output_path("critic", "json"),
        "gate": governed_output_path("gates", "json"),
        "canonical": governed_output_path("canonical", "md"),
    }

    # The proof carries committed bytes, so orchestration has no mutable checkout
    # path that can drift after source verification.
    selected_paths = len(proof.source_files) + len(proof.supporting_files)
    logger.info(
        "Resolved source proof consumed",
        commit_sha=proof.repository.commit_sha,
        proof_sha256=proof_sha256,
        selected_paths=selected_paths,
    )
    item.state = transition(item.state, ExtractionState.SOURCE_VERIFIED)

    # Phase: evidence collected
    item.state = transition(item.state, ExtractionState.EVIDENCE_COLLECTED)
    item.evidence_json_path = str(output_paths["evidence"])

    # Phase: candidate drafted
    item.state = transition(item.state, ExtractionState.CANDIDATE_DRAFTED)
    item.candidate_json_path = str(output_paths["candidate"])

    # Phase: critic reviewed
    item.state = transition(item.state, ExtractionState.CRITIC_REVIEWED)
    item.critic_json_path = str(output_paths["critic"])

    # Phase: gate results — all per-item gates must pass for canonical
    g3 = GateRunner.g3_evidence_gate(bool(evidence_packet.citations), True)
    g4 = GateRunner.g4_citation_gate(
        all(bool(citation.excerpt_sha256) for citation in evidence_packet.citations),
        all(
            citation.line_start > 0 and citation.line_end >= citation.line_start
            for citation in evidence_packet.citations
        ),
    )
    g5 = GateRunner.g5_field_gate(
        required_fields_present and required_field_evidence_valid,
        not candidate.blocking_issue_ids,
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
    item.gate_json_path = str(output_paths["gate"])

    # Terminal: canonical or blocked
    if all_gates_passed and not item.issue_ids and not candidate.blocking_issue_ids:
        item.state = transition(item.state, ExtractionState.CANONICAL)
        item.canonical_path = str(output_paths["canonical"])
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
