"""Gate implementations — Phase 4 Step 11 / Phase 3 Steps 7-8.

G0-G2 are run-level prerequisites. G3-G9 are per-item.
G10 is a pilot/release checkpoint.
"""

from schema.extraction.run import GateReport


def _emit(
    gate: str,
    passed: bool,
    ok_msg: str,
    fail_msg: str,
    affected_items: list[str] | None = None,
) -> GateReport:
    """Helper to emit a GateReport with pass/fail details (DRY — P2.9)."""
    return GateReport(
        gate=gate,
        result="passed" if passed else "failed",
        details=ok_msg if passed else fail_msg,
        affected_items=affected_items or [],
    )


class GateRunner:
    """Runs gate checks and emits machine-readable results."""

    # --- Run-level gates ---

    @staticmethod
    def g0_source_gate(manifest_ok: bool, hashes_verified: bool) -> GateReport:
        """Source resolution gate: manifest validates + hashes match."""
        passed = manifest_ok and hashes_verified
        return _emit(
            "G0", passed,
            "Source resolved and hashes verified",
            "Source resolution or hash verification failed",
        )

    @staticmethod
    def g1_parse_gate(ast_valid: bool, inventory_bearing: bool) -> GateReport:
        """Parse gate: AST is valid and contains inventory-bearing constructs."""
        passed = ast_valid and inventory_bearing
        return _emit(
            "G1", passed,
            "AST parsed with inventory-bearing constructs",
            "Parse failure or no inventory-bearing constructs found",
        )

    @staticmethod
    def g2_inventory_gate(
        inventory_complete: bool, exclusions_recorded: bool, conflicts_resolved: bool,
    ) -> GateReport:
        """Inventory gate: complete inventory with exclusions and resolved conflicts."""
        passed = inventory_complete and exclusions_recorded and conflicts_resolved
        return _emit(
            "G2", passed,
            "Inventory complete with exclusions ledger and resolved conflicts",
            "Inventory incomplete, exclusions missing, or conflicts unresolved",
        )

    # --- Per-item gates ---

    @staticmethod
    def g3_evidence_gate(evidence_collected: bool, all_citations_valid: bool) -> GateReport:
        """Evidence gate: evidence packet exists and all citations validate."""
        passed = evidence_collected and all_citations_valid
        return _emit(
            "G3", passed,
            "All evidence collected and citations valid",
            "Missing evidence or invalid citations",
        )

    @staticmethod
    def g4_citation_gate(excerpt_hash_match: bool, line_bounds_recovered: bool) -> GateReport:
        """Citation validation gate: excerpt hashes match and line bounds recovered."""
        passed = excerpt_hash_match and line_bounds_recovered
        return _emit(
            "G4", passed,
            "All citations validated against source bytes",
            "Citation hash mismatch or line bounds unrecoverable",
        )

    @staticmethod
    def g5_field_gate(
        all_required_present: bool, no_governance_blocked: bool,
    ) -> GateReport:
        """Field coverage gate: all required fields present, no governance blocks."""
        passed = all_required_present and no_governance_blocked
        return _emit(
            "G5", passed,
            "All required fields present",
            "Missing required fields or governance blocks",
        )

    @staticmethod
    def g6_section_gate(all_sections_present: bool) -> GateReport:
        """Body section gate: all required body sections present."""
        return _emit(
            "G6", all_sections_present,
            "All required body sections present",
            "Missing required body sections",
        )

    @staticmethod
    def g7_critic_gate(disposition: str) -> GateReport:
        """Critic gate: critic review completed without rejection."""
        passed = disposition in ("accepted", "challenged")
        return _emit(
            "G7", passed,
            f"Critic disposition: {disposition}",
            "Critic rejected the candidate",
        )

    @staticmethod
    def g8_graph_gate(
        targets_exist: bool, no_cycles: bool, no_duplicate_ids: bool,
    ) -> GateReport:
        """Graph integrity gate: all reference targets exist, no cycles, unique IDs."""
        passed = targets_exist and no_cycles and no_duplicate_ids
        return _emit(
            "G8", passed,
            "Graph integrity verified",
            "Graph error: missing targets, cycles, or duplicate IDs",
        )

    @staticmethod
    def g9_welfare_gate(leakage_report: dict) -> GateReport:
        """Welfare leakage gate: no chapter 8 content in canonical output.

        Accepts a structured leakage report from
        :func:`extraction_pipeline.reports.check_welfare_leakage_content`
        (or a compatible dict with a ``leaked`` key). This ensures the
        gate is wired to the detector rather than receiving an unverified
        bare boolean.

        For backward compatibility, a bare ``bool`` is still accepted
        (treated as ``{"leaked": not value}``), but callers should migrate
        to the structured report.
        """
        if isinstance(leakage_report, bool):
            # Backward-compatible bare-bool path
            no_leakage = leakage_report
            return _emit(
                "G9", no_leakage,
                "No welfare leakage detected",
                "Welfare content detected in non-welfare output",
            )

        leaked = leakage_report.get("leaked", False)
        detector_version = leakage_report.get("detector_version", "unknown")
        leaked_ids = leakage_report.get("leaked_ids", [])
        excluded_source = leakage_report.get("excluded_source", "chapter8-CONS.qmd")

        if not leaked:
            details = (
                f"No welfare leakage detected (detector: {detector_version}, "
                f"excluded source: {excluded_source})"
            )
        else:
            details = (
                f"Welfare content detected in non-welfare output "
                f"(detector: {detector_version}, leaked IDs: {leaked_ids}, "
                f"excluded source: {excluded_source})"
            )

        return GateReport(
            gate="G9",
            result="passed" if not leaked else "failed",
            details=details,
            affected_items=leaked_ids,
        )

    @staticmethod
    def g10_reproducibility_gate(bytes_identical: bool) -> GateReport:
        """Reproducibility gate: repeated run produces identical content."""
        return _emit(
            "G10", bytes_identical,
            "Content is byte-identical to reference run",
            "Content differs from reference run",
        )
