"""Tests for the canonical non-welfare inventory contracts and compiler."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError
from unittest.mock import patch

from schema.extraction.evidence import Citation
from schema.extraction.inventory import (
    InventoryDiscrepancy,
    InventoryLedger,
    InventoryOccurrence,
    ModuleCount,
    RowDisposition,
    SourceReference,
)
from extraction_pipeline.inventory import (
    InventoryError,
    _drafts,
    _require_closed_source_map,
    _require_approved_output,
    atomic_write,
    main,
    normalize_variable_id,
    parse_inventory_rows,
    read_git_object,
)
import yaml


def citation(path: str = "chapters/chapter2-IDN.qmd", line: int = 10) -> Citation:
    excerpt = "| hhid | Household identifier |"
    return Citation(
        citation_id="CIT-IDN-HHID",
        source_path=path,
        node_id="table-2.1",
        heading_anchor="identification",
        line_start=line,
        line_end=line,
        excerpt=excerpt,
        excerpt_sha256=hashlib.sha256(excerpt.encode()).hexdigest(),
        evidence_role="defines",
    )


def occurrence(**overrides: object) -> InventoryOccurrence:
    values: dict[str, object] = {
        "occurrence_id": "INV-v1-idn-table-2-1-001",
        "occurrence_key": "idn.table-2-1.001",
        "source": SourceReference(
            source_name="GMD-guidelines",
            source_path="chapters/chapter2-IDN.qmd",
            table_key="idn.table-2-1",
            occurrence_key="idn.table-2-1.001",
        ),
        "raw_name": "hhid",
        "variable_id": "VAR-hhid",
        "owner_module": "MOD-IDN",
        "occurrence_module": "MOD-IDN",
        "tier": 1,
        "derivation_status": "atomic",
        "disposition": RowDisposition.CANONICAL_OUTPUT,
        "counts_toward_denominator": True,
        "citation": citation(),
        "draft_path": "extraction/20_drafts/idn/VAR-hhid.md",
        "reason": None,
    }
    values.update(overrides)
    return InventoryOccurrence.model_validate(values)


def test_model_forbids_extra_fields() -> None:
    with pytest.raises(ValidationError):
        occurrence(unexpected=True)


@pytest.mark.parametrize(
    ("disposition", "counts"),
    [
        (RowDisposition.CANONICAL_OUTPUT, False),
        (RowDisposition.INVENTORY_ONLY, True),
    ],
)
def test_counting_is_biconditional(disposition: RowDisposition, counts: bool) -> None:
    with pytest.raises(ValidationError, match="counts_toward_denominator"):
        occurrence(disposition=disposition, counts_toward_denominator=counts)


def test_citation_detects_tampered_excerpt() -> None:
    source = b"first\n| hhid | Household identifier |\nlast\n"
    row = occurrence(citation=citation(line=2))
    row.validate_citation(source)
    tampered = row.model_copy(
        update={"citation": row.citation.model_copy(update={"excerpt": "tampered"})}
    )
    with pytest.raises(ValueError, match="excerpt"):
        tampered.validate_citation(source)


def test_discrepancy_requires_claim_and_decision_references() -> None:
    with pytest.raises(ValidationError):
        InventoryDiscrepancy(
            discrepancy_id="DISC-UTL-PHANTOM-001",
            module="MOD-UTL",
            claimed_count=66,
            resolved_count=65,
            status="retired_non_counting",
            claim_citation=None,
            claim_repository_commit="0" * 40,
            claim_blob_sha256="0" * 64,
            decision_reference="plan#denominator-decision",
            decision_sha256="0" * 64,
            explanation="Obsolete unsupported count.",
        )


def test_ledger_rejects_duplicate_canonical_id() -> None:
    first = occurrence()
    second = occurrence(
        occurrence_id="INV-v1-idn-table-2-1-002",
        occurrence_key="idn.table-2-1.002",
        source=first.source.model_copy(update={"occurrence_key": "idn.table-2-1.002"}),
    )
    with pytest.raises(ValidationError, match="duplicate canonical"):
        InventoryLedger(
            inventory_version="v1",
            status="draft_pending_human_inventory_review",
            source_identity_status="pending_task_b_approval",
            source_commit="d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
            source_repository="https://github.com/GMD-hub/GMD-guidelines.git",
            chapter_sha256={
                path: "0" * 64
                for path in (
                    "chapters/chapter2-IDN.qmd",
                    "chapters/chapter3-GEO.qmd",
                    "chapters/chapter4-DEM.qmd",
                    "chapters/chapter5-LMR.qmd",
                    "chapters/chapter6-UTL.qmd",
                    "chapters/chapter7-DWL.qmd",
                    "chapters/chapter8-CONS.qmd",
                )
            },
            normalization_contract="v1",
            toolchain={},
            approval_plan=".cg-docs/plans/example.md",
            approval_record_sha256="0" * 64,
            denominator_decision_sha256="1" * 64,
            source_row_count=2,
            non_counting_row_count=0,
            denominator=2,
            module_counts=[ModuleCount(module="MOD-IDN", count=2)],
            occurrences=[first, second],
            discrepancies=[],
        )


def test_ledger_rejects_module_aggregate_that_misstates_ownership() -> None:
    row = occurrence()
    values = {
        "inventory_version": "v1",
        "status": "draft_pending_human_inventory_review",
        "source_identity_status": "pending_task_b_approval",
        "source_commit": "0" * 40,
        "source_repository": "https://github.com/GMD-hub/GMD-guidelines.git",
        "chapter_sha256": {
            path: "0" * 64
            for path in (
                "chapters/chapter2-IDN.qmd",
                "chapters/chapter3-GEO.qmd",
                "chapters/chapter4-DEM.qmd",
                "chapters/chapter5-LMR.qmd",
                "chapters/chapter6-UTL.qmd",
                "chapters/chapter7-DWL.qmd",
                "chapters/chapter8-CONS.qmd",
            )
        },
        "normalization_contract": "v1",
        "toolchain": {},
        "approval_plan": ".cg-docs/plans/example.md",
        "approval_record_sha256": "0" * 64,
        "denominator_decision_sha256": "1" * 64,
        "source_row_count": 1,
        "non_counting_row_count": 0,
        "denominator": 1,
        "module_counts": [ModuleCount(module="MOD-GEO", count=1)],
        "occurrences": [row],
        "discrepancies": [],
    }
    with pytest.raises(ValidationError, match="owner_module"):
        InventoryLedger.model_validate(values)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("source_commit", "main", "Git SHA-1"),
        ("source_repository", "https://example.com/source.git", "literal_error"),
        ("chapter_sha256", {"chapters/chapter2-IDN.qmd": "0" * 64}, "seven governed"),
    ],
)
def test_ledger_rejects_invalid_source_identity(
    field: str, value: object, message: str
) -> None:
    ledger = yaml.safe_load(
        Path("extraction/20_drafts/runs/non-welfare-inventory.v1.yaml").read_text(
            encoding="utf-8"
        )
    )
    ledger[field] = value
    with pytest.raises(ValidationError, match=message):
        InventoryLedger.model_validate(ledger)


def test_welfare_row_cannot_be_canonical() -> None:
    with pytest.raises(ValidationError, match="Chapter 8"):
        occurrence(
            occurrence_key="cons.table-8-1.001",
            source=SourceReference(
                source_name="GMD-guidelines",
                source_path="chapters/chapter8-CONS.qmd",
                table_key="cons.table-8-1",
                occurrence_key="cons.table-8-1.001",
            ),
            citation=citation("chapters/chapter8-CONS.qmd"),
        )


def test_inventory_module_imports_from_repo() -> None:
    assert Path("schema/extraction/inventory.py").is_file()


def test_parser_reads_grid_and_pipe_numeric_rows() -> None:
    source = b"""### Table 2.1: Example
+---+---+---+---+
|   | Module | **Variable name** | **Tier** |
+===+========+===================+==========+
| 1 | ID     | **hhid**          | 1        |
+---+--------+-------------------+----------+
### Table 2.2: Pipe
| | Module | Variable | Tier |
|---|---|---|---|
| 1 | UTL | water_exp\\* | 2 |
"""
    rows, captions = parse_inventory_rows(source, "chapters/chapter2-IDN.qmd")
    assert len(captions) == 2
    assert [row.raw_name for row in rows] == ["hhid", "water_exp"]
    assert rows[1].annotation_removed


@pytest.mark.parametrize(
    "unsupported",
    [
        "| X | ID | **hhid** | 1 |",
        "1  ID  hhid  1",
    ],
)
def test_parser_rejects_unsupported_construct_inside_table(unsupported: str) -> None:
    source = (
        "### Table 2.1: Example\n"
        "| | Module | Variable | Tier |\n"
        "|---|---|---|---|\n"
        "| 1 | ID | **year** | 1 |\n"
        f"{unsupported}\n"
    ).encode()
    with pytest.raises(InventoryError, match="unsupported inventory"):
        parse_inventory_rows(source, "chapters/chapter2-IDN.qmd")


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("marital", "VAR-marital"),
        ("t_hours \\_total", "VAR-thourstotal"),
        ("LPG_exp", "VAR-lpgexp"),
        ("gual_adm2_code", "VAR-gauladm2code"),
    ],
)
def test_alias_and_mechanical_normalization(raw: str, expected: str) -> None:
    assert normalize_variable_id(raw) == expected


def test_git_object_reader_ignores_dirty_checkout(tmp_path: Path) -> None:
    subprocess.run(["git", "init", "-q", tmp_path], check=True)
    subprocess.run(["git", "-C", tmp_path, "config", "user.email", "test@example.com"], check=True)
    subprocess.run(["git", "-C", tmp_path, "config", "user.name", "Test"], check=True)
    chapter = tmp_path / "chapters" / "chapter2-IDN.qmd"
    chapter.parent.mkdir()
    chapter.write_text("committed\n", encoding="utf-8")
    subprocess.run(["git", "-C", tmp_path, "add", "."], check=True)
    subprocess.run(["git", "-C", tmp_path, "commit", "-qm", "fixture"], check=True)
    sha = subprocess.check_output(["git", "-C", tmp_path, "rev-parse", "HEAD"], text=True).strip()
    chapter.write_text("dirty\n", encoding="utf-8")
    assert read_git_object(tmp_path, sha, "chapters/chapter2-IDN.qmd") == b"committed\n"


def test_atomic_writer_is_deterministic_and_rejects_lock(tmp_path: Path) -> None:
    output = tmp_path / "ledger.yaml"
    atomic_write(output, b"stable\n")
    assert output.read_bytes() == b"stable\n"
    lock = output.with_name(f".{output.name}.lock")
    lock.write_text("busy", encoding="utf-8")
    with pytest.raises(InventoryError, match="lock"):
        atomic_write(output, b"changed\n")
    assert output.read_bytes() == b"stable\n"


def test_source_map_has_closed_fixed_set() -> None:
    source_map = yaml.safe_load(
        Path("extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml").read_text(encoding="utf-8")
    )
    assert source_map["expected"] == {
        "captions": 28,
        "inventory_tables": 27,
        "source_rows": 318,
        "canonical_rows": 267,
        "non_counting_rows": 51,
        "module_counts": {
            "MOD-IDN": 9,
            "MOD-GEO": 14,
            "MOD-DEM": 24,
            "MOD-LBR": 90,
            "MOD-UTL": 61,
            "MOD-DWL": 69,
        },
        "shared_rows": 9,
        "discrepancies": 1,
    }
    assert len(source_map["captions"]) == 28
    assert len(source_map["rows"]) == 318
    assert sum(row["disposition"] == "canonical_output" for row in source_map["rows"]) == 267
    assert sum(row["disposition"] == "shared_identifier_occurrence" for row in source_map["rows"]) == 9
    assert sum(row["disposition"] == "welfare_excluded" for row in source_map["rows"]) == 28
    assert source_map["discrepancy_claim"] == {
        "repository": "https://github.com/GMD-hub/GMD-canonical-schema.git",
        "commit": "de5d6dbcc918261036073c83b46bacdba53da6e0",
        "path": "extraction/20_drafts/runs/inventory-2026-08-13.md",
        "blob_sha256": "0d878bec414aa2cbab99b5d2bb65b256d86cfe61435f90bec817303a47a51a79",
    }


@pytest.mark.parametrize(
    "field",
    ["source_map_version", "source_repository", "source_commit", "source_identity_status"],
)
def test_closed_source_map_rejects_top_level_identity_changes(field: str) -> None:
    expected = {
        "source_map_version": "v1",
        "source_repository": "repository",
        "source_commit": "0" * 40,
        "source_identity_status": "pending_task_b_approval",
    }
    changed = dict(expected)
    changed[field] = "tampered"
    with pytest.raises(InventoryError, match=field):
        _require_closed_source_map(changed, expected)


def test_candidate_ledger_matches_exact_draft_corpus() -> None:
    ledger_path = os.environ.get("INVENTORY_LEDGER_PATH")
    if not ledger_path:
        pytest.skip("candidate-directed integration test")
    ledger = InventoryLedger.model_validate(yaml.safe_load(Path(ledger_path).read_text(encoding="utf-8")))
    canonical = [row for row in ledger.occurrences if row.counts_toward_denominator]
    expected_paths = {
        path.as_posix()
        for module in ("idn", "geo", "dem", "lbr", "utl", "dwl")
        for path in Path("extraction/20_drafts", module).glob("VAR-*.md")
    }
    assert {row.draft_path for row in canonical} == expected_paths
    assert {row.variable_id for row in canonical} == {Path(path).stem for path in expected_paths}
    assert len(canonical) == 267
    assert len(ledger.occurrences) == 318
    assert ledger.non_counting_row_count == 51
    assert all(
        row.disposition == RowDisposition.WELFARE_EXCLUDED
        for row in ledger.occurrences
        if row.source.source_path == "chapters/chapter8-CONS.qmd"
    )


def test_unknown_punctuation_name_is_blocking() -> None:
    with pytest.raises(InventoryError, match="unknown or malformed"):
        normalize_variable_id("unknown.name")


def test_cli_output_escape_is_blocking(tmp_path: Path) -> None:
    with pytest.raises(InventoryError, match="escapes approved"):
        _require_approved_output(tmp_path / "ledger.yaml")


def test_drafts_require_governed_repository_root(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    governed = repository / "extraction" / "20_drafts"
    governed.mkdir(parents=True)
    redirected = tmp_path / "redirected"
    redirected.mkdir()
    with pytest.raises(InventoryError, match="governed repository path"):
        _drafts(redirected, repository)


def test_drafts_serialize_repository_relative_paths(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    draft = repository / "extraction" / "20_drafts" / "idn" / "VAR-hhid.md"
    draft.parent.mkdir(parents=True)
    draft.write_bytes(b"draft\n")
    assert _drafts(repository / "extraction" / "20_drafts", repository) == {
        "VAR-hhid": ("MOD-IDN", "extraction/20_drafts/idn/VAR-hhid.md")
    }


@pytest.mark.skipif(sys.platform == "win32", reason="symlink semantics differ on Windows")
def test_drafts_reject_symlink_escape(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    module = repository / "extraction" / "20_drafts" / "idn"
    module.mkdir(parents=True)
    outside = tmp_path / "VAR-escape.md"
    outside.write_bytes(b"outside\n")
    (module / "VAR-escape.md").symlink_to(outside)
    with pytest.raises(InventoryError, match="escapes governed root"):
        _drafts(repository / "extraction" / "20_drafts", repository)


def test_promote_requires_byte_equal_immutable_recompilation(tmp_path: Path) -> None:
    candidate = Path("extraction/20_drafts/runs/test-candidate.yaml")
    output = Path("extraction/20_drafts/runs/test-promoted.yaml")
    candidate.write_bytes(b"hand-authored\n")
    try:
        with patch("extraction_pipeline.inventory.compile_ledger") as compile_mock, patch(
            "extraction_pipeline.inventory.serialize_ledger", return_value=b"compiled\n"
        ):
            compile_mock.return_value = object()
            with pytest.raises(InventoryError, match="immutable recompilation"):
                main([
                    "promote",
                    "--source-repo", str(tmp_path),
                    "--source-commit", "0" * 40,
                    "--source-map", "source-map.yaml",
                    "--draft-root", "extraction/20_drafts",
                    "--candidate", str(candidate),
                    "--output", str(output),
                ])
        assert not output.exists()
    finally:
        candidate.unlink(missing_ok=True)
        output.unlink(missing_ok=True)


def test_promote_writes_recompiled_bytes(tmp_path: Path) -> None:
    candidate = Path("extraction/20_drafts/runs/test-candidate.yaml")
    output = Path("extraction/20_drafts/runs/test-promoted.yaml")
    candidate.write_bytes(b"compiled\n")
    try:
        with patch("extraction_pipeline.inventory.compile_ledger") as compile_mock, patch(
            "extraction_pipeline.inventory.serialize_ledger", return_value=b"compiled\n"
        ):
            compile_mock.return_value = object()
            assert main([
                "promote",
                "--source-repo", str(tmp_path),
                "--source-commit", "0" * 40,
                "--source-map", "source-map.yaml",
                "--draft-root", "extraction/20_drafts",
                "--candidate", str(candidate),
                "--output", str(output),
            ]) == 0
        assert output.read_bytes() == b"compiled\n"
    finally:
        candidate.unlink(missing_ok=True)
        output.unlink(missing_ok=True)
