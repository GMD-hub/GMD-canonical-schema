"""Tests for the canonical non-welfare inventory contracts and compiler."""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

import pytest
from pydantic import ValidationError

import extraction_pipeline.inventory as inventory_module

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
    CHAPTERS,
    InventoryError,
    _drafts,
    _require_closed_source_map,
    _resolve_approved_output,
    atomic_write,
    build_source_map,
    compile_ledger,
    main,
    normalize_variable_id,
    parse_inventory_rows,
    read_git_object,
    serialize_ledger,
)
import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SOURCE_MAP_PATH = (
    REPOSITORY_ROOT
    / "extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml"
)


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


def discrepancy(**overrides: object) -> InventoryDiscrepancy:
    values: dict[str, object] = {
        "discrepancy_id": "DISC-UTL-PHANTOM-001",
        "module": "MOD-UTL",
        "claimed_count": 66,
        "resolved_count": 65,
        "status": "retired_non_counting",
        "claim_citation": citation(),
        "claim_repository_commit": "0" * 40,
        "claim_blob_sha256": "0" * 64,
        "decision_reference": "plan#denominator-decision",
        "decision_sha256": "0" * 64,
        "explanation": "Obsolete unsupported count.",
    }
    values.update(overrides)
    return InventoryDiscrepancy.model_validate(values)


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
            discrepancies=[discrepancy()],
        )


def test_ledger_rejects_module_aggregate_that_misstates_ownership() -> None:
    row = occurrence()
    values = {
        "inventory_version": "v1",
        "status": "draft_pending_human_inventory_review",
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
        "discrepancies": [discrepancy()],
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
        "discrepancy_id": "DISC-UTL-PHANTOM-001",
        "repository": "https://github.com/GMD-hub/GMD-canonical-schema.git",
        "commit": "de5d6dbcc918261036073c83b46bacdba53da6e0",
        "path": "extraction/20_drafts/runs/inventory-2026-08-13.md",
        "blob_sha256": "0d878bec414aa2cbab99b5d2bb65b256d86cfe61435f90bec817303a47a51a79",
    }


@pytest.mark.parametrize(
    "field",
    ["source_map_version", "source_repository", "source_commit"],
)
def test_closed_source_map_rejects_top_level_identity_changes(field: str) -> None:
    expected = {
        "source_map_version": "v1",
        "source_repository": "repository",
        "source_commit": "0" * 40,
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
        _resolve_approved_output(tmp_path / "ledger.yaml", REPOSITORY_ROOT)


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


@dataclass(frozen=True)
class InventoryRepositories:
    canonical_repo: Path
    source_repo: Path
    source_commit: str
    source_map_path: Path
    source_map: dict[str, object]
    draft_root: Path
    external_cwd: Path
    candidate_a: Path
    candidate_b: Path
    promoted: Path
    ledger_data: dict[str, object]


def _git_commit(repository: Path, message: str) -> str:
    subprocess.run(["git", "-C", repository, "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            repository,
            "commit",
            "--no-gpg-sign",
            "--no-verify",
            "-qm",
            message,
        ],
        check=True,
    )
    return subprocess.check_output(
        ["git", "-C", repository, "rev-parse", "HEAD"], text=True
    ).strip()


def _initialize_git_repository(repository: Path) -> None:
    repository.mkdir()
    subprocess.run(
        ["git", "init", "--object-format=sha1", "-q", repository], check=True
    )
    subprocess.run(
        ["git", "-C", repository, "config", "user.email", "test@example.com"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", repository, "config", "user.name", "Test"], check=True
    )


def _synthetic_chapter(
    source_path: str, baseline: dict[str, object]
) -> bytes:
    captions = [
        caption
        for caption in baseline["captions"]
        if caption["source_path"] == source_path
    ]
    rows = [
        row for row in baseline["rows"] if row["source_path"] == source_path
    ]
    lines: list[str] = []
    for caption in captions:
        lines.append(f"### {caption['caption']}")
        table_rows = [
            row for row in rows if row["table_key"] == caption["table_key"]
        ]
        if table_rows:
            lines.extend(
                [
                    "| | Module | Variable | Tier |",
                    "|---|---|---|---|",
                ]
            )
        for index, row in enumerate(table_rows, 1):
            raw_name = row["raw_name"]
            if row["annotation_removed"]:
                raw_name = f"{raw_name}\\*"
            tier = "" if row["tier"] is None else str(row["tier"])
            lines.append(
                f"| {index} | {row['occurrence_module']} | {raw_name} | {tier} |"
            )
        lines.append("")
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def _run_from(cwd: Path, argv: list[str]) -> int:
    previous = Path.cwd()
    os.chdir(cwd)
    try:
        return main(argv)
    finally:
        os.chdir(previous)


def _cli_inputs(
    repositories: InventoryRepositories,
    source_map_path: Path | None = None,
    source_commit: str | None = None,
) -> list[str]:
    return [
        "--source-repo",
        str(repositories.source_repo),
        "--source-commit",
        source_commit or repositories.source_commit,
        "--source-map",
        str(source_map_path or repositories.source_map_path),
        "--draft-root",
        "extraction/20_drafts",
    ]


def _write_source_map(
    repositories: InventoryRepositories,
    name: str,
    data: dict[str, object],
) -> Path:
    path = repositories.source_map_path.with_name(name)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=False, width=120),
        encoding="utf-8",
    )
    return path


def _clone_source_repository(
    repositories: InventoryRepositories, destination: Path
) -> Path:
    subprocess.run(
        ["git", "clone", "-q", repositories.source_repo, destination], check=True
    )
    subprocess.run(
        ["git", "-C", destination, "config", "user.email", "test@example.com"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", destination, "config", "user.name", "Test"], check=True
    )
    subprocess.run(
        ["git", "-C", destination, "checkout", "-q", repositories.source_commit],
        check=True,
    )
    return destination


def _assert_no_writer_debris(output: Path) -> None:
    assert not output.with_name(f".{output.name}.lock").exists()
    assert not list(output.parent.glob(f".{output.name}.*.tmp"))


@pytest.fixture(scope="module")
def inventory_repositories(
    tmp_path_factory: pytest.TempPathFactory,
) -> InventoryRepositories:
    root = tmp_path_factory.mktemp("inventory-repositories")
    source_repo = root / "guidelines"
    canonical_repo = root / "canonical"
    external_cwd = root / "external"
    external_cwd.mkdir()
    _initialize_git_repository(source_repo)
    _initialize_git_repository(canonical_repo)

    baseline = yaml.safe_load(SOURCE_MAP_PATH.read_text(encoding="utf-8"))
    expected_draft_ids = {
        path.stem
        for module in ("idn", "geo", "dem", "lbr", "utl", "dwl")
        for path in (REPOSITORY_ROOT / "extraction/20_drafts" / module).glob(
            "VAR-*.md"
        )
    }
    assert len(expected_draft_ids) == 267

    chapter_hashes: dict[str, str] = {}
    for source_path, _, source_rows, canonical_rows, _ in CHAPTERS:
        chapter = source_repo / source_path
        chapter.parent.mkdir(parents=True, exist_ok=True)
        chapter.write_bytes(_synthetic_chapter(source_path, baseline))
        parsed, _ = parse_inventory_rows(chapter.read_bytes(), source_path)
        baseline_rows = [
            row for row in baseline["rows"] if row["source_path"] == source_path
        ]
        assert len(parsed) == len(baseline_rows) == source_rows
        assert sum(
            row["disposition"] == RowDisposition.CANONICAL_OUTPUT.value
            for row in baseline_rows
        ) == canonical_rows
        chapter_hashes[source_path] = hashlib.sha256(chapter.read_bytes()).hexdigest()
    assert sum(
        len(
            [
                caption
                for caption in baseline["captions"]
                if caption["source_path"] == source_path
            ]
        )
        for source_path, *_ in CHAPTERS
    ) == 28
    source_commit = _git_commit(source_repo, "synthetic guidelines")

    plan_path = canonical_repo / inventory_module.PLAN_PATH
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(
        "# Fixture Plan\n\n"
        "## Denominator Decision\n\nFixture decision.\n\n"
        "## Approval Record\n\nFixture approval.\n\n"
        "## Source Reconciliation Baseline\n\nFixture baseline.\n",
        encoding="utf-8",
    )
    claim_path = canonical_repo / inventory_module.CLAIM_PATH
    claim_path.parent.mkdir(parents=True, exist_ok=True)
    claim_excerpt = (
        "66 variables (4 ID + 15 WASH access + 9 energy access + 20 WASH/energy "
        "expenditure + 12 additional expenditure)."
    )
    claim_path.write_text(
        "\n".join(["Fixture claim context."] * 89 + [claim_excerpt]) + "\n",
        encoding="utf-8",
    )
    claim_commit = _git_commit(canonical_repo, "synthetic claim and plan")

    draft_root = canonical_repo / "extraction/20_drafts"
    copied_draft_ids: set[str] = set()
    for module in ("idn", "geo", "dem", "lbr", "utl", "dwl"):
        for source in sorted(
            (REPOSITORY_ROOT / "extraction/20_drafts" / module).glob("VAR-*.md")
        ):
            target = draft_root / module / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            copied_draft_ids.add(source.stem)
    assert copied_draft_ids == expected_draft_ids

    patcher = pytest.MonkeyPatch()
    patcher.setattr(inventory_module, "SOURCE_COMMIT", source_commit)
    patcher.setattr(inventory_module, "CLAIM_COMMIT", claim_commit)
    patcher.setattr(inventory_module, "EXPECTED_HASHES", chapter_hashes)
    try:
        source_map = build_source_map(source_repo, source_commit, plan_path)
        canonical_ids = {
            row["variable_id"]
            for row in source_map["rows"]
            if row["disposition"] == RowDisposition.CANONICAL_OUTPUT.value
        }
        assert canonical_ids == expected_draft_ids
        source_map_path = draft_root / "runs/source-map.yaml"
        source_map_path.parent.mkdir(parents=True, exist_ok=True)
        source_map_path.write_text(
            yaml.safe_dump(
                source_map, sort_keys=False, allow_unicode=False, width=120
            ),
            encoding="utf-8",
        )
        _git_commit(canonical_repo, "synthetic canonical inputs")

        candidate_a = draft_root / "runs/candidate-a.yaml"
        candidate_b = draft_root / "runs/candidate-b.yaml"
        promoted = draft_root / "runs/promoted.yaml"
        common = [
            "--source-repo",
            str(source_repo),
            "--source-commit",
            source_commit,
            "--source-map",
            str(source_map_path),
            "--draft-root",
            "extraction/20_drafts",
        ]
        assert _run_from(
            external_cwd,
            ["compile", *common, "--output", "extraction/20_drafts/runs/candidate-a.yaml"],
        ) == 0
        assert _run_from(
            external_cwd,
            ["compile", *common, "--output", "extraction/20_drafts/runs/candidate-b.yaml"],
        ) == 0
        assert candidate_a.read_bytes() == candidate_b.read_bytes()
        assert _run_from(
            external_cwd,
            ["validate", *common, "--ledger", "extraction/20_drafts/runs/candidate-a.yaml"],
        ) == 0
        compiled = compile_ledger(
            source_repo, source_commit, source_map_path, draft_root
        )
        assert serialize_ledger(compiled) == candidate_a.read_bytes()
        assert _run_from(
            external_cwd,
            [
                "promote",
                *common,
                "--candidate",
                "extraction/20_drafts/runs/candidate-a.yaml",
                "--output",
                "extraction/20_drafts/runs/promoted.yaml",
            ],
        ) == 0
        assert promoted.read_bytes() == candidate_a.read_bytes()
        for output in (candidate_a, candidate_b, promoted):
            _assert_no_writer_debris(output)

        repositories = InventoryRepositories(
            canonical_repo=canonical_repo,
            source_repo=source_repo,
            source_commit=source_commit,
            source_map_path=source_map_path,
            source_map=source_map,
            draft_root=draft_root,
            external_cwd=external_cwd,
            candidate_a=candidate_a,
            candidate_b=candidate_b,
            promoted=promoted,
            ledger_data=yaml.safe_load(candidate_a.read_text(encoding="utf-8")),
        )
        yield repositories
    finally:
        patcher.undo()


def test_real_end_to_end_promotion_from_external_cwd(
    inventory_repositories: InventoryRepositories,
) -> None:
    assert inventory_repositories.candidate_a.read_bytes() == (
        inventory_repositories.candidate_b.read_bytes()
    )
    assert inventory_repositories.promoted.read_bytes() == (
        inventory_repositories.candidate_a.read_bytes()
    )


def test_source_byte_drift_is_blocking(
    inventory_repositories: InventoryRepositories,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source_repo = _clone_source_repository(
        inventory_repositories, tmp_path / "source-byte-drift"
    )
    chapter = source_repo / CHAPTERS[0][0]
    chapter.write_bytes(chapter.read_bytes() + b"\nSource drift.\n")
    drift_commit = _git_commit(source_repo, "source drift")
    changed = deepcopy(inventory_repositories.source_map)
    changed["source_commit"] = drift_commit
    changed_path = _write_source_map(
        inventory_repositories, "source-byte-drift.yaml", changed
    )
    monkeypatch.setattr(inventory_module, "SOURCE_COMMIT", drift_commit)
    drift_hashes = dict(inventory_module.EXPECTED_HASHES)
    drift_hashes[CHAPTERS[0][0]] = hashlib.sha256(chapter.read_bytes()).hexdigest()
    monkeypatch.setattr(inventory_module, "EXPECTED_HASHES", drift_hashes)
    with pytest.raises(InventoryError, match="closed source-map mismatch"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                "--source-repo",
                str(source_repo),
                "--source-commit",
                drift_commit,
                "--source-map",
                str(changed_path),
                "--draft-root",
                "extraction/20_drafts",
                "--output",
                "extraction/20_drafts/runs/source-byte-drift-output.yaml",
            ],
        )


def test_configured_hash_mismatch_is_blocking(
    inventory_repositories: InventoryRepositories,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    wrong_hashes = dict(inventory_module.EXPECTED_HASHES)
    wrong_hashes[CHAPTERS[0][0]] = "0" * 64
    monkeypatch.setattr(inventory_module, "EXPECTED_HASHES", wrong_hashes)
    with pytest.raises(InventoryError, match="chapter SHA-256 mismatch"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                *_cli_inputs(inventory_repositories),
                "--output",
                "extraction/20_drafts/runs/hash-mismatch-output.yaml",
            ],
        )


def test_missing_source_row_is_blocking(
    inventory_repositories: InventoryRepositories,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    source_repo = _clone_source_repository(
        inventory_repositories, tmp_path / "missing-source-row"
    )
    chapter = source_repo / CHAPTERS[0][0]
    lines = chapter.read_text(encoding="utf-8").splitlines()
    row_index = next(
        index for index, line in enumerate(lines) if re.match(r"^\|\s*\d+\s*\|", line)
    )
    del lines[row_index]
    chapter.write_text("\n".join(lines) + "\n", encoding="utf-8")
    changed_commit = _git_commit(source_repo, "remove source row")
    changed = deepcopy(inventory_repositories.source_map)
    changed["source_commit"] = changed_commit
    changed_path = _write_source_map(
        inventory_repositories, "missing-row.yaml", changed
    )
    changed_hashes = dict(inventory_module.EXPECTED_HASHES)
    changed_hashes[CHAPTERS[0][0]] = hashlib.sha256(chapter.read_bytes()).hexdigest()
    monkeypatch.setattr(inventory_module, "SOURCE_COMMIT", changed_commit)
    monkeypatch.setattr(inventory_module, "EXPECTED_HASHES", changed_hashes)
    with pytest.raises(InventoryError, match="source-row delta"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                "--source-repo",
                str(source_repo),
                "--source-commit",
                changed_commit,
                "--source-map",
                str(changed_path),
                "--draft-root",
                "extraction/20_drafts",
                "--output",
                "extraction/20_drafts/runs/missing-row-output.yaml",
            ],
        )


def test_wrong_source_map_ownership_is_blocking(
    inventory_repositories: InventoryRepositories,
) -> None:
    changed = deepcopy(inventory_repositories.source_map)
    canonical = next(
        row
        for row in changed["rows"]
        if row["disposition"] == RowDisposition.CANONICAL_OUTPUT.value
    )
    canonical["owner_module"] = "MOD-DWL"
    changed_path = _write_source_map(
        inventory_repositories, "wrong-ownership.yaml", changed
    )
    with pytest.raises(InventoryError, match="closed source-map mismatch"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                *_cli_inputs(inventory_repositories, changed_path),
                "--output",
                "extraction/20_drafts/runs/wrong-owner-output.yaml",
            ],
        )


def test_wrong_draft_ownership_is_blocking(
    inventory_repositories: InventoryRepositories,
) -> None:
    canonical = next(
        row
        for row in inventory_repositories.source_map["rows"]
        if row["disposition"] == RowDisposition.CANONICAL_OUTPUT.value
        and row["owner_module"] != "MOD-DWL"
    )
    module = canonical["owner_module"].removeprefix("MOD-").lower()
    original = (
        inventory_repositories.draft_root
        / module
        / f"{canonical['variable_id']}.md"
    )
    wrong = inventory_repositories.draft_root / "dwl" / original.name
    original.replace(wrong)
    try:
        with pytest.raises(InventoryError, match="wrong draft owner"):
            _run_from(
                inventory_repositories.external_cwd,
                [
                    "compile",
                    *_cli_inputs(inventory_repositories),
                    "--output",
                    "extraction/20_drafts/runs/wrong-draft-owner-output.yaml",
                ],
            )
    finally:
        wrong.replace(original)


def test_serialized_occurrence_ordering_mutation_is_blocking(
    inventory_repositories: InventoryRepositories,
) -> None:
    changed = deepcopy(inventory_repositories.ledger_data)
    changed["occurrences"][0], changed["occurrences"][1] = (
        changed["occurrences"][1],
        changed["occurrences"][0],
    )
    changed_path = inventory_repositories.candidate_a.with_name(
        "occurrence-ordering.yaml"
    )
    changed_path.write_text(
        yaml.safe_dump(changed, sort_keys=False, allow_unicode=False, width=120),
        encoding="utf-8",
    )
    with pytest.raises(InventoryError, match="deterministic compilation"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "validate",
                *_cli_inputs(inventory_repositories),
                "--ledger",
                "extraction/20_drafts/runs/occurrence-ordering.yaml",
            ],
        )


def test_modified_candidate_is_blocking(
    inventory_repositories: InventoryRepositories,
) -> None:
    modified = inventory_repositories.candidate_a.with_name("modified.yaml")
    modified.write_bytes(inventory_repositories.candidate_a.read_bytes() + b"# modified\n")
    output = inventory_repositories.promoted.with_name("modified-output.yaml")
    with pytest.raises(InventoryError, match="immutable recompilation"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "promote",
                *_cli_inputs(inventory_repositories),
                "--candidate",
                "extraction/20_drafts/runs/modified.yaml",
                "--output",
                "extraction/20_drafts/runs/modified-output.yaml",
            ],
        )
    assert not output.exists()


def test_external_lookalike_output_path_is_blocking(
    inventory_repositories: InventoryRepositories, tmp_path: Path
) -> None:
    external_output = tmp_path / "extraction/20_drafts/runs/candidate.yaml"
    with pytest.raises(InventoryError, match="escapes approved"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                *_cli_inputs(inventory_repositories),
                "--output",
                str(external_output),
            ],
        )
    assert not external_output.exists()


def test_nested_runs_output_is_blocking(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    (repository / "extraction/20_drafts/runs/subdir").mkdir(parents=True)
    with pytest.raises(InventoryError, match="direct child"):
        _resolve_approved_output(
            Path("extraction/20_drafts/runs/subdir/ledger.yaml"), repository
        )


@pytest.mark.skipif(sys.platform == "win32", reason="symlink semantics differ on Windows")
def test_symlinked_runs_directory_is_blocking(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    outside = tmp_path / "outside"
    (repository / "extraction/20_drafts").mkdir(parents=True)
    outside.mkdir()
    (repository / "extraction/20_drafts/runs").symlink_to(outside)
    with pytest.raises(InventoryError, match="runs directory escapes"):
        _resolve_approved_output(
            Path("extraction/20_drafts/runs/ledger.yaml"), repository
        )


@pytest.mark.skipif(sys.platform == "win32", reason="symlink semantics differ on Windows")
def test_runs_symlink_to_draft_directory_is_blocking(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    draft_module = repository / "extraction/20_drafts/idn"
    draft_module.mkdir(parents=True)
    (repository / "extraction/20_drafts/runs").symlink_to(draft_module)
    with pytest.raises(InventoryError, match="runs directory escapes"):
        _resolve_approved_output(
            Path("extraction/20_drafts/runs/VAR-hhid.md"), repository
        )


def test_output_cannot_overwrite_source_map(
    inventory_repositories: InventoryRepositories,
) -> None:
    original = inventory_repositories.source_map_path.read_bytes()
    with pytest.raises(InventoryError, match="overwrite governed input"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                *_cli_inputs(inventory_repositories),
                "--output",
                str(inventory_repositories.source_map_path),
            ],
        )
    assert inventory_repositories.source_map_path.read_bytes() == original


def test_source_map_copy_cannot_overwrite_canonical_source_map(
    inventory_repositories: InventoryRepositories,
) -> None:
    canonical_source_map = (
        inventory_repositories.canonical_repo / inventory_module.SOURCE_MAP_PATH
    )
    canonical_source_map.write_bytes(inventory_repositories.source_map_path.read_bytes())
    original = canonical_source_map.read_bytes()
    source_map_copy = _write_source_map(
        inventory_repositories,
        "source-map-copy.yaml",
        deepcopy(inventory_repositories.source_map),
    )
    with pytest.raises(InventoryError, match="overwrite governed input"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                *_cli_inputs(inventory_repositories, source_map_copy),
                "--output",
                str(canonical_source_map),
            ],
        )
    assert canonical_source_map.read_bytes() == original


def test_case_variant_cannot_overwrite_canonical_source_map(
    inventory_repositories: InventoryRepositories,
) -> None:
    canonical_source_map = (
        inventory_repositories.canonical_repo / inventory_module.SOURCE_MAP_PATH
    )
    canonical_source_map.write_bytes(inventory_repositories.source_map_path.read_bytes())
    alias = canonical_source_map.with_name(canonical_source_map.name.upper())
    if not alias.exists() or not alias.samefile(canonical_source_map):
        pytest.skip("filesystem is case-sensitive")
    with pytest.raises(InventoryError, match="overwrite governed input"):
        _run_from(
            inventory_repositories.external_cwd,
            [
                "compile",
                *_cli_inputs(inventory_repositories),
                "--output",
                str(alias),
            ],
        )


@pytest.mark.skipif(sys.platform == "win32", reason="symlink semantics differ on Windows")
def test_atomic_write_rejects_parent_symlink_swap(tmp_path: Path) -> None:
    runs = tmp_path / "runs"
    original = tmp_path / "runs-original"
    outside = tmp_path / "outside"
    runs.mkdir()
    outside.mkdir()
    target = runs / "ledger.yaml"
    runs.rename(original)
    runs.symlink_to(outside)
    with pytest.raises(InventoryError, match="stable real directory"):
        atomic_write(target, b"ledger\n")
    assert not (outside / "ledger.yaml").exists()


def test_ledger_rejects_false_source_row_count(
    inventory_repositories: InventoryRepositories,
) -> None:
    changed = deepcopy(inventory_repositories.ledger_data)
    changed["source_row_count"] -= 1
    with pytest.raises(ValidationError, match="source_row_count"):
        InventoryLedger.model_validate(changed)


def test_ledger_rejects_false_non_counting_row_count(
    inventory_repositories: InventoryRepositories,
) -> None:
    changed = deepcopy(inventory_repositories.ledger_data)
    changed["non_counting_row_count"] -= 1
    with pytest.raises(ValidationError, match="non_counting_row_count"):
        InventoryLedger.model_validate(changed)


def test_ledger_rejects_false_denominator_relation(
    inventory_repositories: InventoryRepositories,
) -> None:
    changed = deepcopy(inventory_repositories.ledger_data)
    changed["denominator"] -= 1
    with pytest.raises(ValidationError, match="source_row_count minus"):
        InventoryLedger.model_validate(changed)


def test_ledger_rejects_duplicate_discrepancy_ids(
    inventory_repositories: InventoryRepositories,
) -> None:
    changed = deepcopy(inventory_repositories.ledger_data)
    changed["discrepancies"].append(deepcopy(changed["discrepancies"][0]))
    with pytest.raises(ValidationError, match="duplicate discrepancy ID"):
        InventoryLedger.model_validate(changed)


@pytest.mark.parametrize("replacement", [[], [{"discrepancy_id": "DISC-WRONG"}]])
def test_ledger_rejects_wrong_or_zero_discrepancy_cardinality(
    inventory_repositories: InventoryRepositories,
    replacement: list[dict[str, object]],
) -> None:
    changed = deepcopy(inventory_repositories.ledger_data)
    if replacement:
        wrong = deepcopy(changed["discrepancies"][0])
        wrong.update(replacement[0])
        changed["discrepancies"] = [wrong]
    else:
        changed["discrepancies"] = []
    with pytest.raises(ValidationError, match="v1 discrepancies must be exactly"):
        InventoryLedger.model_validate(changed)
