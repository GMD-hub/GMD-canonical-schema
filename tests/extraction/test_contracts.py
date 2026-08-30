"""Strict contract tests — Phase 3 Step 6-8."""

import pytest

from schema.extraction.candidate import BlockingIssue, ExtractionCandidate
from schema.extraction.evidence import Citation, EvidencePacket
from schema.extraction.run import GateReport, ModuleDefinition


class TestCitation:
    def test_valid_citation(self) -> None:
        c = Citation(
            citation_id="CIT-001",
            source_path="chapter2-IDN.qmd",
            node_id="abc123",
            heading_anchor="var-age",
            line_start=42,
            line_end=45,
            excerpt="Age of household member in years",
            excerpt_sha256="a" * 64,
            evidence_role="defines",
        )
        assert c.citation_id == "CIT-001"
        assert c.source_path == "chapter2-IDN.qmd"
        assert c.node_id == "abc123"
        assert c.heading_anchor == "var-age"
        assert c.line_start == 42
        assert c.line_end == 45
        assert c.excerpt == "Age of household member in years"
        assert c.excerpt_sha256 == "a" * 64
        assert c.evidence_role == "defines"

    def test_forbids_extra_fields(self) -> None:
        with pytest.raises(ValueError):
            Citation(
                citation_id="CIT-001",
                source_path="x.qmd",
                node_id="abc",
                heading_anchor="h",
                line_start=1,
                line_end=2,
                excerpt="e",
                excerpt_sha256="a" * 64,
                evidence_role="defines",
                extra="nope",
            )


class TestEvidencePacket:
    def test_valid_packet(self) -> None:
        packet = EvidencePacket(
            inventory_id="INV-IDN-001",
            module_code="IDN",
            variable_name="age",
            citations=[],
            source_document="GMD guidelines",
            extraction_method_version="1.0",
        )
        assert packet.inventory_id == "INV-IDN-001"
        assert packet.module_code == "IDN"
        assert packet.variable_name == "age"
        assert packet.citations == []
        assert packet.source_document == "GMD guidelines"
        assert packet.extraction_method_version == "1.0"


class TestExtractionCandidate:
    def test_candidate_rejects_invalid_source_proof_identity(self) -> None:
        with pytest.raises(ValueError, match="source_proof_sha256"):
            ExtractionCandidate(
                inventory_id="INV-IDN-001",
                source_proof_sha256="not-a-digest",
                module_code="IDN",
                variable_name="age",
                field_classifications={},
                evidence_ids={},
                blocking_issue_ids=["ISSUE-MISSING-FIELDS"],
            )

    def test_minimal_candidate(self) -> None:
        """A candidate with null required fields must have blocking issues."""
        candidate = ExtractionCandidate(
            inventory_id="INV-IDN-001",
            source_proof_sha256="a" * 64,
            module_code="IDN",
            variable_name="age",
            field_classifications={},
            evidence_ids={},
            blocking_issue_ids=["ISSUE-MISSING-FIELDS"],
        )
        assert candidate.canonical_label is None
        assert candidate.inventory_id == "INV-IDN-001"
        assert candidate.module_code == "IDN"
        assert candidate.variable_name == "age"
        assert candidate.field_classifications == {}
        assert candidate.evidence_ids == {}
        assert candidate.blocking_issue_ids == ["ISSUE-MISSING-FIELDS"]

    def test_candidate_with_all_required_fields_no_blocking_issues(self) -> None:
        """A candidate with all required source-explicit fields present needs no blocking issues."""
        candidate = ExtractionCandidate(
            inventory_id="INV-IDN-001",
            source_proof_sha256="a" * 64,
            module_code="IDN",
            variable_name="age",
            canonical_label="Age",
            tier="canonical",
            value_codes=[{"value": 0, "label": "zero"}],
            allowed_range={"min": 0, "max": 120},
            missing_codes=[{"code": -1, "label": "missing"}],
            field_classifications={},
            evidence_ids={},
            blocking_issue_ids=[],
        )
        assert candidate.canonical_label == "Age"
        assert candidate.blocking_issue_ids == []

    def test_candidate_null_required_without_blocking_issues_raises(self) -> None:
        """Null required fields with empty blocking_issue_ids must raise."""
        with pytest.raises(ValueError, match="blocking_issue_ids is empty"):
            ExtractionCandidate(
                inventory_id="INV-IDN-001",
                source_proof_sha256="a" * 64,
                module_code="IDN",
                variable_name="age",
                field_classifications={},
                evidence_ids={},
                blocking_issue_ids=[],
            )

    def test_candidate_with_missing_evidence(self) -> None:
        candidate = ExtractionCandidate(
            inventory_id="INV-IDN-002",
            source_proof_sha256="a" * 64,
            module_code="IDN",
            variable_name="relationship",
            canonical_label=None,
            field_classifications={"canonical_label": "source-explicit"},
            evidence_ids={},
            confidence_scores={"canonical_label": 0.0},
            blocking_issue_ids=["ISSUE-001"],
        )
        assert candidate.blocking_issue_ids == ["ISSUE-001"]

    def test_candidate_confidence_out_of_range_raises(self) -> None:
        """confidence_scores above 1.0 must raise (P1.3 fix)."""
        with pytest.raises(ValueError, match="out of range"):
            ExtractionCandidate(
                inventory_id="INV-IDN-001",
                source_proof_sha256="a" * 64,
                module_code="IDN",
                variable_name="age",
                field_classifications={},
                evidence_ids={},
                confidence_scores={"age": 1.5},
                blocking_issue_ids=["ISSUE-001"],
            )

    def test_candidate_confidence_negative_raises(self) -> None:
        """confidence_scores below 0.0 must raise (P1.3 fix)."""
        with pytest.raises(ValueError, match="out of range"):
            ExtractionCandidate(
                inventory_id="INV-IDN-001",
                source_proof_sha256="a" * 64,
                module_code="IDN",
                variable_name="age",
                field_classifications={},
                evidence_ids={},
                confidence_scores={"age": -0.3},
                blocking_issue_ids=["ISSUE-001"],
            )

    def test_candidate_confidence_boundary_values_ok(self) -> None:
        """confidence_scores of exactly 0.0 and 1.0 must be accepted."""
        candidate = ExtractionCandidate(
            inventory_id="INV-IDN-001",
            source_proof_sha256="a" * 64,
            module_code="IDN",
            variable_name="age",
            field_classifications={},
            evidence_ids={},
            confidence_scores={"age": 0.0, "label": 1.0},
            blocking_issue_ids=["ISSUE-001"],
        )
        assert candidate.confidence_scores == {"age": 0.0, "label": 1.0}


class TestBlockingIssue:
    def test_blocking_issue(self) -> None:
        issue = BlockingIssue(
            issue_id="ISSUE-001",
            inventory_id="INV-IDN-001",
            severity="blocking",
            category="missing-evidence",
            description="Cannot determine canonical label",
            owner="extractor",
            disposition="open",
        )
        assert issue.severity == "blocking"
        assert issue.issue_id == "ISSUE-001"
        assert issue.inventory_id == "INV-IDN-001"
        assert issue.category == "missing-evidence"
        assert issue.description == "Cannot determine canonical label"
        assert issue.owner == "extractor"
        assert issue.disposition == "open"


class TestGateReport:
    def test_gate_passed(self) -> None:
        report = GateReport(
            gate="G1",
            result="passed",
            details="All inventory-bearing constructs parsed",
        )
        assert report.result == "passed"
        assert report.gate == "G1"
        assert report.details == "All inventory-bearing constructs parsed"
        assert report.affected_items == []

    def test_gate_failed(self) -> None:
        report = GateReport(
            gate="G4",
            result="failed",
            details="Invalid citation: excerpt hash mismatch",
            affected_items=["INV-IDN-003"],
        )
        assert report.result == "failed"
        assert report.gate == "G4"
        assert report.details == "Invalid citation: excerpt hash mismatch"
        assert report.affected_items == ["INV-IDN-003"]


class TestModuleDefinition:
    def test_valid_module(self) -> None:
        mod = ModuleDefinition(
            module_id="MOD-IDN",
            module_name="Identification",
            tier="canonical",
            source_chapter="chapter2-IDN.qmd",
            description="Household member identification variables",
        )
        assert mod.module_id == "MOD-IDN"
        assert mod.module_name == "Identification"
        assert mod.tier == "canonical"
        assert mod.source_chapter == "chapter2-IDN.qmd"
        assert mod.description == "Household member identification variables"

    def test_forbids_extra(self) -> None:
        with pytest.raises(ValueError):
            ModuleDefinition(
                module_id="MOD-IDN",
                module_name="IDN",
                tier="canonical",
                source_chapter="ch2.qmd",
                description="desc",
                extra="no",
            )

    def test_provenance_optional(self) -> None:
        """ModuleDefinition.provenance is optional per Decision 9 (P1.5 fix)."""
        mod = ModuleDefinition(
            module_id="MOD-IDN",
            module_name="Identification",
            tier="canonical",
            source_chapter="chapter2-IDN.qmd",
            description="Household member identification variables",
            provenance="governance-constant",
        )
        assert mod.provenance == "governance-constant"

    def test_provenance_defaults_to_none(self) -> None:
        """ModuleDefinition.provenance defaults to None when omitted."""
        mod = ModuleDefinition(
            module_id="MOD-IDN",
            module_name="Identification",
            tier="canonical",
            source_chapter="chapter2-IDN.qmd",
            description="Household member identification variables",
        )
        assert mod.provenance is None
