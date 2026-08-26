"""Compile and validate the deterministic non-welfare inventory ledger."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import loguru
import pydantic
import yaml

from schema.extraction.evidence import Citation
from schema.extraction.inventory import (
    InventoryDiscrepancy,
    InventoryLedger,
    InventoryOccurrence,
    ModuleCount,
    RowDisposition,
    SourceReference,
)

SOURCE_COMMIT = "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1"
CLAIM_COMMIT = "de5d6dbcc918261036073c83b46bacdba53da6e0"
CLAIM_PATH = "extraction/20_drafts/runs/inventory-2026-08-13.md"
PLAN_PATH = ".cg-docs/plans/2026-08-25-canonical-non-welfare-inventory-ledger.md"
MODULE_COUNTS = {
    "MOD-IDN": 9,
    "MOD-GEO": 14,
    "MOD-DEM": 24,
    "MOD-LBR": 90,
    "MOD-UTL": 61,
    "MOD-DWL": 69,
}
CHAPTERS = [
    ("chapters/chapter2-IDN.qmd", "MOD-IDN", 10, 9, "helper"),
    ("chapters/chapter3-GEO.qmd", "MOD-GEO", 18, 14, "inventory"),
    ("chapters/chapter4-DEM.qmd", "MOD-DEM", 29, 24, "inventory"),
    ("chapters/chapter5-LMR.qmd", "MOD-LBR", 95, 90, "shared"),
    ("chapters/chapter6-UTL.qmd", "MOD-UTL", 65, 61, "shared"),
    ("chapters/chapter7-DWL.qmd", "MOD-DWL", 73, 69, "inventory"),
    ("chapters/chapter8-CONS.qmd", "MOD-CONS", 28, 0, "welfare"),
]
ALIASES = {
    "gual_adm2_code": "VAR-gauladm2code",
    "eye_dsablty": "VAR-eyedisability",
    "hear_dsablty": "VAR-heardisability",
    "walk_dsablty": "VAR-walkdisability",
    "conc_dsord": "VAR-concentrationdisorder",
    "slfcre_dsablty": "VAR-selfcaredisability",
    "comm_dsablty": "VAR-communicationdisability",
    "wage_noc": "VAR-wagenc",
    "t_wage_nc_total": "VAR-twagencotal",
    "t_wage_nc_total_year": "VAR-twagencototalyear",
    "elec_exp": "VAR-elecxp",
    "kerosene_exp": "VAR-kerosenexp",
}
ANNOTATED_NAMES = {
    "water_exp", "waste_exp", "gas_exp", "liquid_exp", "solid_exp",
    "utl_exp", "othhousing_exp", "tel_exp", "comm_exp", "tvintph_exp",
}
EXPECTED_HASHES = {
    "chapters/chapter2-IDN.qmd": "5e25f7bc25031e102f8152feab8236c6384f1a3a438fcfb4e9d7b85f16da3e39",
    "chapters/chapter3-GEO.qmd": "850d635bb2cb36703e756d307e24cf33c94101e95c6ba5b9027fb44f1044e32e",
    "chapters/chapter4-DEM.qmd": "f091a0c110d931b911799618005a31dab9375794f68aca270653f9dc5d07acd0",
    "chapters/chapter5-LMR.qmd": "c46796103d86412daf8d38bd56fbe118e669aa319d7948822a3476239c6d0d40",
    "chapters/chapter6-UTL.qmd": "e8cb9818dd8c69317e7bb752d7afab9d6d3bc60c22526a72f751fe449bea1ba0",
    "chapters/chapter7-DWL.qmd": "3d881952d4ec0f21c88fd31101a0b0224681a19a7a1a7ec822f8bdab9d700743",
    "chapters/chapter8-CONS.qmd": "1fc00a05f15422d7217c41147df24dc76f82417f8fc3c725889ef97354946b31",
}


class InventoryError(RuntimeError):
    """Raised when inventory inputs violate the closed v1 contract."""


@dataclass(frozen=True)
class ParsedRow:
    """A bounded source-table row parsed from immutable chapter bytes."""

    line: int
    table_key: str
    occurrence_index: int
    raw_name: str
    tier: int | None
    excerpt: str
    annotation_removed: bool


def _clean_cell(value: str) -> tuple[str, bool]:
    value = value.strip()
    while len(value) >= 4 and value.startswith("**") and value.endswith("**"):
        value = value[2:-2].strip()
    while len(value) >= 2 and value.startswith("*") and value.endswith("*"):
        value = value[1:-1].strip()
    annotated = value.endswith("\\*")
    if annotated:
        value = value[:-2].rstrip()
    return value, annotated


def _table_key(source_path: str, caption: str, caption_index: int) -> str:
    chapter = re.search(r"chapter(\d+)", source_path)
    slug = re.sub(r"[^a-z0-9]+", "-", caption.lower()).strip("-")
    return f"ch{chapter.group(1) if chapter else 'x'}.{caption_index:02d}.{slug}"


def parse_inventory_rows(source_bytes: bytes, source_path: str) -> tuple[list[ParsedRow], list[dict[str, Any]]]:
    """Parse configured numeric grid/pipe rows and their preceding captions."""
    rows: list[ParsedRow] = []
    captions: list[dict[str, Any]] = []
    current_key: str | None = None
    current_count = 0
    table_started = False
    for line_number, line in enumerate(source_bytes.decode("utf-8").splitlines(), 1):
        caption_match = re.match(r"^###\s+(Table\s+[2-8]\.\d+:.+?)\s*(?:\{.*\})?$", line.strip())
        if caption_match:
            caption = caption_match.group(1).strip()
            current_key = _table_key(source_path, caption, len(captions) + 1)
            captions.append({"table_key": current_key, "caption": caption, "line": line_number})
            current_count = 0
            table_started = False
            continue
        if current_key and re.match(r"^#{1,6}\s+", line.strip()):
            current_key = None
            table_started = False
            continue
        if not current_key:
            continue
        stripped = line.strip()
        if not stripped:
            if table_started:
                table_started = False
            continue
        if re.match(r"^\|\s*\d+\s*\|", line):
            table_started = True
        elif stripped.startswith(("|", "+")):
            table_started = True
            if stripped.startswith("|") and not (
                re.match(r"^\|\s*\|", stripped)
                or re.match(r"^\|\s*:?-+", stripped)
                or re.search(r"variable|module|tier", stripped, re.IGNORECASE)
            ):
                raise InventoryError(
                    f"unsupported inventory row at {source_path}:{line_number}"
                )
            continue
        elif table_started:
            raise InventoryError(
                f"unsupported inventory construct at {source_path}:{line_number}"
            )
        else:
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) < 3:
            raise InventoryError(f"unsupported inventory row at {source_path}:{line_number}")
        raw_name, annotated = _clean_cell(cells[2])
        tier_match = re.search(r"\d+", cells[-1])
        current_count += 1
        rows.append(ParsedRow(
            line=line_number,
            table_key=current_key,
            occurrence_index=current_count,
            raw_name=raw_name,
            tier=int(tier_match.group()) if tier_match else None,
            excerpt=line,
            annotation_removed=annotated,
        ))
    return rows, captions


def normalize_variable_id(raw_name: str) -> str:
    """Apply the closed v1 mechanical rules and reviewed aliases."""
    cleaned, _ = _clean_cell(raw_name)
    cleaned = cleaned.replace("\\_", "_")
    cleaned = re.sub(r"\s*_\s*", "_", cleaned).lower()
    if cleaned in ALIASES:
        return ALIASES[cleaned]
    normalized = cleaned.replace("_", "")
    if not re.fullmatch(r"[a-z][a-z0-9]*", normalized):
        raise InventoryError(f"unknown or malformed source name: {raw_name!r}")
    return f"VAR-{normalized}"


def read_git_object(repo: Path, commit: str, source_path: str) -> bytes:
    """Read immutable source bytes without consulting the working tree."""
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "show", f"{commit}:{source_path}"],
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as exc:
        raise InventoryError(f"cannot read Git object {commit}:{source_path}") from exc


def _section_hash(plan_text: str, heading: str, next_heading: str) -> str:
    start = plan_text.find(heading)
    end = plan_text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        raise InventoryError(f"missing durable plan section: {heading}")
    excerpt = plan_text[start:end].rstrip() + "\n"
    return hashlib.sha256(excerpt.encode("utf-8")).hexdigest()


def _toolchain() -> dict[str, str]:
    return {
        "python": f"{os.sys.version_info.major}.{os.sys.version_info.minor}.{os.sys.version_info.micro}",
        "pydantic": pydantic.__version__,
        "pyyaml": yaml.__version__,
        "loguru": loguru.__version__,
    }


def _classify(path: str, index: int, total: int, module: str, treatment: str) -> tuple[str, str | None]:
    if treatment == "welfare":
        return RowDisposition.WELFARE_EXCLUDED.value, None
    non_counting = total - MODULE_COUNTS.get(module, 0)
    if treatment == "helper" and index > total - non_counting:
        return RowDisposition.HELPER_OR_METADATA.value, None
    if treatment == "shared" and index <= non_counting:
        return RowDisposition.SHARED_IDENTIFIER_OCCURRENCE.value, "MOD-IDN"
    if treatment == "inventory" and index <= non_counting:
        return RowDisposition.INVENTORY_ONLY.value, "MOD-IDN"
    return RowDisposition.CANONICAL_OUTPUT.value, module


def build_source_map(source_repo: Path, source_commit: str, plan_path: Path) -> dict[str, Any]:
    """Build the exhaustive closed v1 source-map data from immutable objects."""
    plan_text = plan_path.read_text(encoding="utf-8")
    all_rows: list[dict[str, Any]] = []
    all_captions: list[dict[str, Any]] = []
    chapter_records: list[dict[str, Any]] = []
    for path, module, expected_rows, canonical_rows, treatment in CHAPTERS:
        source = read_git_object(source_repo, source_commit, path)
        digest = hashlib.sha256(source).hexdigest()
        if digest != EXPECTED_HASHES[path]:
            raise InventoryError(f"chapter SHA-256 mismatch: {path}")
        rows, captions = parse_inventory_rows(source, path)
        if len(rows) != expected_rows:
            raise InventoryError(f"source-row delta for {path}: expected {expected_rows}, found {len(rows)}")
        all_captions.extend({"source_path": path, **caption} for caption in captions)
        chapter_records.append({
            "source_path": path, "sha256": digest, "module": module,
            "source_rows": expected_rows, "canonical_rows": canonical_rows,
        })
        for index, row in enumerate(rows, 1):
            disposition, owner = _classify(path, index, expected_rows, module, treatment)
            variable_id = None if disposition in {
                RowDisposition.HELPER_OR_METADATA.value,
                RowDisposition.WELFARE_EXCLUDED.value,
            } else normalize_variable_id(row.raw_name)
            key = f"{row.table_key}.{row.occurrence_index:03d}"
            all_rows.append({
                "occurrence_key": key,
                "source_path": path,
                "table_key": row.table_key,
                "line": row.line,
                "raw_name": row.raw_name,
                "variable_id": variable_id,
                "owner_module": owner,
                "occurrence_module": module,
                "tier": row.tier,
                "disposition": disposition,
                "annotation_removed": row.annotation_removed,
                "excerpt_sha256": hashlib.sha256(row.excerpt.encode("utf-8")).hexdigest(),
            })
    if len(all_captions) != 28 or len(all_rows) != 318:
        raise InventoryError("caption/source-row baseline mismatch")
    repository_root = _repository_root(plan_path)
    claim_blob = read_git_object(repository_root, CLAIM_COMMIT, CLAIM_PATH)
    return {
        "source_map_version": "v1",
        "source_repository": "https://github.com/GMD-hub/GMD-guidelines.git",
        "source_commit": source_commit,
        "source_identity_status": "pending_task_b_approval",
        "toolchain": _toolchain(),
        "normalization_contract": {
            "version": "v1", "aliases": ALIASES,
            "annotation_removals": sorted(ANNOTATED_NAMES),
            "module_alias": {"LMR": "MOD-LBR"},
        },
        "approval": {
            "plan_path": PLAN_PATH,
            "date": "2026-08-25",
            "authority": "human project operator",
            "approval_record_sha256": _section_hash(plan_text, "## Approval Record", "## Source Reconciliation Baseline"),
            "denominator_decision_sha256": _section_hash(plan_text, "## Denominator Decision", "## Approval Record"),
        },
        "discrepancy_claim": {
            "repository": "https://github.com/GMD-hub/GMD-canonical-schema.git",
            "commit": CLAIM_COMMIT,
            "path": CLAIM_PATH,
            "blob_sha256": hashlib.sha256(claim_blob).hexdigest(),
        },
        "expected": {
            "captions": 28, "inventory_tables": 27, "source_rows": 318,
            "canonical_rows": 267, "non_counting_rows": 51,
            "module_counts": MODULE_COUNTS, "shared_rows": 9, "discrepancies": 1,
        },
        "table_disambiguations": {
            "table_6_2_physical_fragments": [5, 4],
            "table_7_7_keys": ["agricultural-land", "legal-documentation-image-non-inventory"],
            "table_5_6_semantic_period": "12-month",
            "table_6_3_name_column": 3,
            "table_7_7_name_header": "Variable",
        },
        "chapters": chapter_records,
        "captions": all_captions,
        "rows": all_rows,
    }


def _load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise InventoryError(f"expected YAML mapping: {path}")
    return data


def _require_closed_source_map(
    source_map: dict[str, Any], expected_map: dict[str, Any]
) -> None:
    """Reject any source-map field not reproduced from governed inputs."""
    if source_map != expected_map:
        differing = sorted(
            key for key in set(source_map) | set(expected_map)
            if source_map.get(key) != expected_map.get(key)
        )
        raise InventoryError(f"closed source-map mismatch: {differing}")


def _repository_root(path: Path) -> Path:
    """Resolve the containing Git repository without trusting the process cwd."""
    anchor = path if path.is_dir() else path.parent
    try:
        value = subprocess.check_output(
            ["git", "-C", str(anchor.resolve()), "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.PIPE,
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise InventoryError(f"cannot resolve repository root from {path}") from exc
    return Path(value).resolve()


def _drafts(draft_root: Path, repository_root: Path) -> dict[str, tuple[str, str]]:
    governed_root = (repository_root / "extraction/20_drafts").resolve()
    if draft_root.resolve() != governed_root:
        raise InventoryError(
            f"draft root must be the governed repository path: {governed_root}"
        )
    found: dict[str, tuple[str, str]] = {}
    for module in ("idn", "geo", "dem", "lbr", "utl", "dwl"):
        for path in sorted((draft_root / module).glob("VAR-*.md")):
            try:
                relative_path = path.resolve(strict=True).relative_to(governed_root)
            except (FileNotFoundError, ValueError) as exc:
                raise InventoryError(f"draft path escapes governed root: {path}") from exc
            variable_id = path.stem
            if variable_id in found:
                raise InventoryError(f"duplicate draft ID: {variable_id}")
            found[variable_id] = (
                f"MOD-{module.upper()}",
                (Path("extraction/20_drafts") / relative_path).as_posix(),
            )
    return found


def compile_ledger(source_repo: Path, source_commit: str, source_map_path: Path, draft_root: Path) -> InventoryLedger:
    """Compile and validate a ledger from immutable source objects and drafts."""
    source_map = _load_yaml(source_map_path)
    if source_map.get("source_commit") != source_commit or source_commit != SOURCE_COMMIT:
        raise InventoryError("wrong Task C source commit")
    if source_map.get("toolchain") != _toolchain():
        raise InventoryError("toolchain mismatch")
    repository_root = _repository_root(source_map_path)
    plan_path = repository_root / source_map["approval"]["plan_path"]
    expected_map = build_source_map(source_repo, source_commit, plan_path)
    _require_closed_source_map(source_map, expected_map)
    plan_text = plan_path.read_text(encoding="utf-8")
    if source_map["approval"]["approval_record_sha256"] != _section_hash(plan_text, "## Approval Record", "## Source Reconciliation Baseline"):
        raise InventoryError("Approval Record section hash mismatch")
    if source_map["approval"]["denominator_decision_sha256"] != _section_hash(plan_text, "## Denominator Decision", "## Approval Record"):
        raise InventoryError("Denominator Decision section hash mismatch")
    source_bytes: dict[str, bytes] = {}
    parsed_by_path: dict[str, dict[int, ParsedRow]] = {}
    for chapter in source_map["chapters"]:
        path = chapter["source_path"]
        content = read_git_object(source_repo, source_commit, path)
        if hashlib.sha256(content).hexdigest() != chapter["sha256"]:
            raise InventoryError(f"chapter SHA-256 mismatch: {path}")
        parsed, _ = parse_inventory_rows(content, path)
        parsed_by_path[path] = {row.line: row for row in parsed}
        source_bytes[path] = content
    drafts = _drafts(draft_root, repository_root)
    occurrences: list[InventoryOccurrence] = []
    canonical_seen: set[str] = set()
    for record in source_map["rows"]:
        parsed = parsed_by_path.get(record["source_path"], {}).get(record["line"])
        if parsed is None or parsed.raw_name != record["raw_name"] or parsed.table_key != record["table_key"]:
            raise InventoryError(f"source-map row mismatch: {record['occurrence_key']}")
        if hashlib.sha256(parsed.excerpt.encode("utf-8")).hexdigest() != record["excerpt_sha256"]:
            raise InventoryError(f"source-map excerpt mismatch: {record['occurrence_key']}")
        if parsed.annotation_removed != record["annotation_removed"]:
            raise InventoryError(f"annotation mapping mismatch: {record['occurrence_key']}")
        if parsed.annotation_removed and parsed.raw_name not in ANNOTATED_NAMES:
            raise InventoryError(f"unknown annotation removal: {parsed.raw_name}")
        disposition = RowDisposition(record["disposition"])
        variable_id = record["variable_id"]
        draft_path = None
        if disposition == RowDisposition.CANONICAL_OUTPUT:
            if variable_id not in drafts:
                raise InventoryError(f"missing canonical draft: {variable_id}")
            draft_owner, draft_path = drafts[variable_id]
            if draft_owner != record["owner_module"]:
                raise InventoryError(f"wrong draft owner for {variable_id}")
            canonical_seen.add(variable_id)
        citation = Citation(
            citation_id=f"CIT-{record['occurrence_key']}",
            source_path=record["source_path"], node_id=record["table_key"],
            heading_anchor=record["table_key"], line_start=record["line"],
            line_end=record["line"], excerpt=parsed.excerpt,
            excerpt_sha256=record["excerpt_sha256"], evidence_role="defines",
        )
        occurrence = InventoryOccurrence(
            occurrence_id=f"INV-v1-{record['occurrence_key']}",
            occurrence_key=record["occurrence_key"],
            source=SourceReference(
                source_name="GMD-guidelines", source_path=record["source_path"],
                table_key=record["table_key"], occurrence_key=record["occurrence_key"],
            ),
            raw_name=record["raw_name"], variable_id=variable_id,
            owner_module=record["owner_module"], occurrence_module=record["occurrence_module"],
            tier=record["tier"], derivation_status="derived" if record["annotation_removed"] else "atomic",
            disposition=disposition,
            counts_toward_denominator=disposition == RowDisposition.CANONICAL_OUTPUT,
            citation=citation, draft_path=draft_path,
            reason=None if disposition == RowDisposition.CANONICAL_OUTPUT else disposition.value,
        )
        occurrence.validate_citation(source_bytes[record["source_path"]])
        occurrences.append(occurrence)
    if set(drafts) != canonical_seen:
        extra = sorted(set(drafts) - canonical_seen)
        raise InventoryError(f"extra or renamed drafts: {extra[:5]}")
    claim_identity = source_map["discrepancy_claim"]
    claim_blob = read_git_object(
        repository_root, claim_identity["commit"], claim_identity["path"]
    )
    if hashlib.sha256(claim_blob).hexdigest() != claim_identity["blob_sha256"]:
        raise InventoryError("obsolete inventory claim blob hash mismatch")
    claim_lines = claim_blob.decode("utf-8").splitlines()
    claim_excerpt = "66 variables (4 ID + 15 WASH access + 9 energy access + 20 WASH/energy expenditure + 12 additional expenditure)."
    if len(claim_lines) < 90 or claim_lines[89] != claim_excerpt:
        raise InventoryError("obsolete inventory claim citation mismatch")
    claim = Citation(
        citation_id="CIT-OBSOLETE-UTL-66", source_path=claim_identity["path"],
        node_id="utl", heading_anchor="utl-chapter6-utl-module-mod-utl", line_start=90, line_end=90,
        excerpt=claim_excerpt, excerpt_sha256=hashlib.sha256(claim_excerpt.encode()).hexdigest(),
        evidence_role="references",
    )
    discrepancy = InventoryDiscrepancy(
        discrepancy_id="DISC-UTL-PHANTOM-001", module="MOD-UTL", claimed_count=66,
        resolved_count=65, status="retired_non_counting", claim_citation=claim,
        claim_repository_commit=claim_identity["commit"],
        claim_blob_sha256=claim_identity["blob_sha256"],
        decision_reference=f"{PLAN_PATH}#denominator-decision",
        decision_sha256=source_map["approval"]["denominator_decision_sha256"],
        explanation="The unsupported fifth UTL count is retired and is not a source occurrence.",
    )
    ledger = InventoryLedger(
        inventory_version="v1", status="draft_pending_human_inventory_review",
        source_identity_status="pending_task_b_approval", source_commit=source_commit,
        source_repository=source_map["source_repository"],
        chapter_sha256={item["source_path"]: item["sha256"] for item in source_map["chapters"]},
        normalization_contract="v1", toolchain=source_map["toolchain"],
        approval_plan=PLAN_PATH,
        approval_record_sha256=source_map["approval"]["approval_record_sha256"],
        denominator_decision_sha256=source_map["approval"]["denominator_decision_sha256"],
        source_row_count=len(occurrences),
        non_counting_row_count=sum(not row.counts_toward_denominator for row in occurrences),
        denominator=267,
        module_counts=[ModuleCount(module=module, count=count) for module, count in MODULE_COUNTS.items()],
        occurrences=occurrences, discrepancies=[discrepancy],
    )
    _validate_fixed_set(ledger)
    return ledger


def _validate_fixed_set(ledger: InventoryLedger) -> None:
    if ledger.source_row_count != 318 or len(ledger.occurrences) != 318:
        raise InventoryError("source occurrence total must be 318")
    if ledger.non_counting_row_count != 51:
        raise InventoryError("non-counting occurrence total must be 51")
    actual = {item.module: item.count for item in ledger.module_counts}
    if actual != MODULE_COUNTS or ledger.denominator != 267:
        raise InventoryError("canonical denominator/module totals mismatch")
    shared = [row for row in ledger.occurrences if row.disposition == RowDisposition.SHARED_IDENTIFIER_OCCURRENCE]
    if len(shared) != 9 or {row.owner_module for row in shared} != {"MOD-IDN"}:
        raise InventoryError("shared identifier occurrence set mismatch")
    if len(ledger.discrepancies) != 1:
        raise InventoryError("exactly one non-source discrepancy is required")
    if any(row.counts_toward_denominator for row in ledger.occurrences if "chapter8-CONS.qmd" in row.source.source_path):
        raise InventoryError("Chapter 8 welfare leakage")


def serialize_ledger(ledger: InventoryLedger) -> bytes:
    """Serialize a validated ledger with stable UTF-8 YAML settings."""
    data = ledger.model_dump(mode="json")
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=False, width=120)
    return text.replace("\r\n", "\n").encode("utf-8")


def atomic_write(output: Path, content: bytes) -> None:
    """Write bytes under an exclusive sibling lock and atomic replacement."""
    output.parent.mkdir(parents=True, exist_ok=True)
    lock = output.with_name(f".{output.name}.lock")
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise InventoryError(f"output lock is already held: {lock}") from exc
    temporary: Path | None = None
    try:
        os.close(fd)
        with tempfile.NamedTemporaryFile(dir=output.parent, prefix=f".{output.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output)
        directory_fd = os.open(output.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


def _validate_ledger_file(path: Path) -> InventoryLedger:
    return InventoryLedger.model_validate(_load_yaml(path))


def _require_approved_output(path: Path) -> None:
    approved = Path("extraction/20_drafts/runs").resolve()
    try:
        path.resolve().relative_to(approved)
    except ValueError as exc:
        raise InventoryError(f"output escapes approved runs directory: {path}") from exc


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("compile", "validate"):
        command = subparsers.add_parser(name)
        command.add_argument("--source-repo", type=Path, required=True)
        command.add_argument("--source-commit", required=True)
        command.add_argument("--source-map", type=Path, required=True)
        command.add_argument("--draft-root", type=Path, required=True)
        command.add_argument("--output" if name == "compile" else "--ledger", type=Path, required=True)
    promote = subparsers.add_parser("promote")
    promote.add_argument("--source-repo", type=Path, required=True)
    promote.add_argument("--source-commit", required=True)
    promote.add_argument("--source-map", type=Path, required=True)
    promote.add_argument("--draft-root", type=Path, required=True)
    promote.add_argument("--candidate", type=Path, required=True)
    promote.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    """Run compile, validation, or atomic promotion."""
    args = _parser().parse_args(argv)
    if args.command == "promote":
        _require_approved_output(args.candidate)
        _require_approved_output(args.output)
        compiled = serialize_ledger(
            compile_ledger(
                args.source_repo, args.source_commit, args.source_map, args.draft_root
            )
        )
        candidate = args.candidate.read_bytes()
        if candidate != compiled:
            raise InventoryError(
                "promotion candidate bytes differ from immutable recompilation"
            )
        atomic_write(args.output, compiled)
        return 0
    ledger = compile_ledger(args.source_repo, args.source_commit, args.source_map, args.draft_root)
    content = serialize_ledger(ledger)
    target = args.output if args.command == "compile" else args.ledger
    if args.command == "compile":
        _require_approved_output(target)
        atomic_write(target, content)
    elif target.read_bytes() != content:
        raise InventoryError("ledger bytes differ from deterministic compilation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
