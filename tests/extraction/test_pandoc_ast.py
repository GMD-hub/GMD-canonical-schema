"""Tests for Pandoc AST parsing — Phase 2 Step 4."""

import json
from pathlib import Path

import pytest

from extraction_pipeline.pandoc_ast import (
    PandocASTError,
    find_headings,
    find_tables,
    generate_node_id,
    is_inventory_bearing,
    normalize_ast,
    parse_pandoc_json,
    recover_line_bounds,
)


SIMPLE_AST = {
    "pandoc-api-version": [1, 23],
    "meta": {},
    "blocks": [
        {"t": "Header", "c": [1, ["heading-1", [], []], [{"t": "Str", "c": "IDN"}]],},
        {"t": "Para", "c": [{"t": "Str", "c": "Content paragraph."}]},
        {
            "t": "Table",
            "c": [
                ["", [], []],  # caption
                [],  # colspecs
                [{"t": "AlignDefault"}],  # alignment
                [1, 0],  # width
                [  # headers
                    [{"t": "Plain", "c": [{"t": "Str", "c": "Variable"}]}],
                ],
                [  # rows
                    [[{"t": "Plain", "c": [{"t": "Str", "c": "age"}]}]],
                ],
            ],
        },
    ],
}

AST_WITH_MULTIPLE_HEADINGS = {
    "pandoc-api-version": [1, 23],
    "meta": {},
    "blocks": [
        {"t": "Header", "c": [2, ["idn-section", [], []], [{"t": "Str", "c": "Identification"}]],},
        {"t": "Header", "c": [2, ["geo-section", [], []], [{"t": "Str", "c": "Geography"}]],},
        {"t": "Header", "c": [3, ["var-age", [], []], [{"t": "Str", "c": "Age"}]],},
        {"t": "Para", "c": [{"t": "Str", "c": "Member age in years."}]},
    ],
}


class TestPandocAST:
    def test_parse_valid_json(self, tmp_path: Path) -> None:
        f = tmp_path / "ast.json"
        f.write_text(json.dumps(SIMPLE_AST), encoding="utf-8")
        ast = parse_pandoc_json(f)
        assert "blocks" in ast

    def test_parse_missing_file(self) -> None:
        with pytest.raises(PandocASTError, match="not found"):
            parse_pandoc_json(Path("/nonexistent.json"))

    def test_parse_invalid_json(self, tmp_path: Path) -> None:
        f = tmp_path / "ast.json"
        f.write_text("not json", encoding="utf-8")
        with pytest.raises(PandocASTError, match="Invalid JSON"):
            parse_pandoc_json(f)

    def test_parse_dict_without_blocks(self, tmp_path: Path) -> None:
        f = tmp_path / "ast.json"
        f.write_text('{"pandoc-api-version":[1,23]}', encoding="utf-8")
        with pytest.raises(PandocASTError, match="blocks"):
            parse_pandoc_json(f)

    def test_find_headings(self) -> None:
        headings = find_headings(SIMPLE_AST)
        assert len(headings) == 1
        assert headings[0]["level"] == 1

    def test_find_multiple_headings(self) -> None:
        headings = find_headings(AST_WITH_MULTIPLE_HEADINGS)
        assert len(headings) == 3

    def test_find_tables(self) -> None:
        tables = find_tables(SIMPLE_AST)
        assert len(tables) == 1

    def test_is_inventory_bearing(self) -> None:
        assert is_inventory_bearing(SIMPLE_AST)
        assert is_inventory_bearing(AST_WITH_MULTIPLE_HEADINGS)

    def test_empty_ast_not_inventory_bearing(self) -> None:
        empty = {"pandoc-api-version": [1, 23], "meta": {}, "blocks": []}
        assert not is_inventory_bearing(empty)

    def test_normalize_is_deterministic(self) -> None:
        n1 = normalize_ast(SIMPLE_AST)
        n2 = normalize_ast(SIMPLE_AST)
        assert n1 == n2

    def test_normalize_sorts_keys(self) -> None:
        unordered = {"blocks": [], "meta": {}, "pandoc-api-version": [1, 23]}
        normalized = normalize_ast(unordered)
        keys = list(normalized.keys())
        assert keys[0] == "blocks"
        assert keys[1] == "meta"

    def test_generate_node_id_is_stable(self) -> None:
        id1 = generate_node_id("ch2.qmd", "3", "var-age")
        id2 = generate_node_id("ch2.qmd", "3", "var-age")
        assert id1 == id2

    def test_generate_node_id_differs_by_path(self) -> None:
        id1 = generate_node_id("ch2.qmd", "3", "var-age")
        id2 = generate_node_id("ch3.qmd", "3", "var-age")
        assert id1 != id2

    def test_generate_node_id_differs_by_position(self) -> None:
        id1 = generate_node_id("ch2.qmd", "3", "var-age")
        id2 = generate_node_id("ch2.qmd", "5", "var-age")
        assert id1 != id2

    def test_recover_line_bounds_found(self) -> None:
        source = b"line 1\nline 2\nline 3 with excerpt here\nline 4\n"
        bounds = recover_line_bounds("excerpt", source)
        assert bounds == (3, 3)

    def test_recover_line_bounds_multiline(self) -> None:
        source = b"start\nmiddle with TARGET text\nend\n"
        bounds = recover_line_bounds("middle with TARGET", source)
        assert bounds == (2, 2)

    def test_recover_line_bounds_not_found(self) -> None:
        source = b"line 1\nline 2\n"
        assert recover_line_bounds("missing", source) is None
