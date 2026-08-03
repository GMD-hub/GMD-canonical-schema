"""Tests for gates — Phase 4 Step 11."""

from extraction_pipeline.gates import GateRunner


class TestRunLevelGates:
    def test_g0_passes(self) -> None:
        report = GateRunner.g0_source_gate(True, True)
        assert report.result == "passed"

    def test_g0_fails_on_hash_mismatch(self) -> None:
        report = GateRunner.g0_source_gate(True, False)
        assert report.result == "failed"

    def test_g0_fails_on_both_false(self) -> None:
        report = GateRunner.g0_source_gate(False, False)
        assert report.result == "failed"

    def test_g1_passes(self) -> None:
        report = GateRunner.g1_parse_gate(True, True)
        assert report.result == "passed"

    def test_g1_fails_on_no_inventory(self) -> None:
        report = GateRunner.g1_parse_gate(True, False)
        assert report.result == "failed"

    def test_g1_fails_on_both_false(self) -> None:
        report = GateRunner.g1_parse_gate(False, False)
        assert report.result == "failed"

    def test_g2_passes(self) -> None:
        report = GateRunner.g2_inventory_gate(True, True, True)
        assert report.result == "passed"

    def test_g2_fails_on_unresolved(self) -> None:
        report = GateRunner.g2_inventory_gate(True, True, False)
        assert report.result == "failed"

    def test_g2_fails_on_incomplete(self) -> None:
        report = GateRunner.g2_inventory_gate(False, True, True)
        assert report.result == "failed"

    def test_g2_fails_on_missing_exclusions(self) -> None:
        report = GateRunner.g2_inventory_gate(True, False, True)
        assert report.result == "failed"


class TestPerItemGates:
    def test_g3_passes(self) -> None:
        report = GateRunner.g3_evidence_gate(True, True)
        assert report.result == "passed"

    def test_g4_passes(self) -> None:
        report = GateRunner.g4_citation_gate(True, True)
        assert report.result == "passed"

    def test_g4_fails_on_mismatch(self) -> None:
        report = GateRunner.g4_citation_gate(False, True)
        assert report.result == "failed"

    def test_g5_passes(self) -> None:
        report = GateRunner.g5_field_gate(True, True)
        assert report.result == "passed"

    def test_g6_passes(self) -> None:
        report = GateRunner.g6_section_gate(True)
        assert report.result == "passed"

    def test_g6_fails(self) -> None:
        report = GateRunner.g6_section_gate(False)
        assert report.result == "failed"

    def test_g7_accepted(self) -> None:
        report = GateRunner.g7_critic_gate("accepted")
        assert report.result == "passed"

    def test_g7_challenged(self) -> None:
        report = GateRunner.g7_critic_gate("challenged")
        assert report.result == "passed"

    def test_g7_rejected(self) -> None:
        report = GateRunner.g7_critic_gate("rejected")
        assert report.result == "failed"

    def test_g8_passes(self) -> None:
        report = GateRunner.g8_graph_gate(True, True, True)
        assert report.result == "passed"

    def test_g9_passes(self) -> None:
        report = GateRunner.g9_welfare_gate(True)
        assert report.result == "passed"

    def test_g9_fails_on_leakage(self) -> None:
        report = GateRunner.g9_welfare_gate(False)
        assert report.result == "failed"

    def test_g9_passes_with_structured_report_no_leakage(self) -> None:
        """Structured report with leaked=False must pass and record detector version."""
        report = GateRunner.g9_welfare_gate({
            "detector_version": "v1-content",
            "leaked": False,
            "leaked_ids": [],
            "excluded_source": "chapter8-CONS.qmd",
        })
        assert report.result == "passed"
        assert "v1-content" in report.details
        assert report.affected_items == []

    def test_g9_fails_with_structured_report_leakage(self) -> None:
        """Structured report with leaked=True must fail and record leaked IDs."""
        report = GateRunner.g9_welfare_gate({
            "detector_version": "v1-content",
            "leaked": True,
            "leaked_ids": ["INV-UTL-014"],
            "excluded_source": "chapter8-CONS.qmd",
        })
        assert report.result == "failed"
        assert "INV-UTL-014" in report.details
        assert report.affected_items == ["INV-UTL-014"]

    def test_g10_passes(self) -> None:
        report = GateRunner.g10_reproducibility_gate(True)
        assert report.result == "passed"

    def test_g10_fails(self) -> None:
        report = GateRunner.g10_reproducibility_gate(False)
        assert report.result == "failed"
