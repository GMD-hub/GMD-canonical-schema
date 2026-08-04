"""Tests for manifest models — Phase 2 Step 3."""

import pytest

from schema.extraction.manifest import (
    GovernanceRefs,
    OutputConfig,
    ParserContract,
    RepositoryIdentity,
    ResolvedSource,
    SourceFileEntry,
    SourceManifest,
)
from schema.extraction.run import ContentRunManifest, RunLedgerEvent


class TestRepositoryIdentity:
    def test_valid_https_url(self) -> None:
        repo = RepositoryIdentity(
            url="https://github.com/GMD-hub/GMD-guidelines",
            commit_sha="d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
        )
        assert repo.url == "https://github.com/GMD-hub/GMD-guidelines"

    def test_rejects_non_https_url(self) -> None:
        with pytest.raises(ValueError, match="HTTPS"):
            RepositoryIdentity(
                url="http://github.com/GMD-hub/repo",
                commit_sha="d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
            )

    def test_rejects_non_40_char_sha(self) -> None:
        with pytest.raises(ValueError, match="40-character"):
            RepositoryIdentity(
                url="https://github.com/GMD-hub/repo",
                commit_sha="abc123",
            )

    def test_normalizes_sha_to_lowercase(self) -> None:
        repo = RepositoryIdentity(
            url="https://github.com/GMD-hub/repo",
            commit_sha="D46DC03D253764AD7BDEF53F625D54FD2A0A9EA1",
        )
        assert repo.commit_sha == "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1"


class TestSourceFileEntry:
    def test_valid_entry(self) -> None:
        entry = SourceFileEntry(
            path="chapter2-IDN.qmd",
            scope="included",
            sha256=None,
        )
        assert entry.path == "chapter2-IDN.qmd"
        assert entry.scope == "included"

    def test_rejects_extra_fields(self) -> None:
        with pytest.raises(ValueError):
            SourceFileEntry(
                path="x.qmd",
                scope="included",
                bonus_field="nope",
            )

    def test_valid_scopes(self) -> None:
        for scope in ("included", "supporting", "welfare-excluded"):
            entry = SourceFileEntry(path="x.qmd", scope=scope)
            assert entry.scope == scope

    def test_rejects_invalid_scope(self) -> None:
        with pytest.raises(ValueError):
            SourceFileEntry(path="x.qmd", scope="invalid")


class TestParserContract:
    def test_valid_contract(self) -> None:
        contract = ParserContract(
            tool="pandoc",
            version="3.1.12",
            reader="markdown+pipe_tables",
            writer="json",
            normalization_version="1.0",
        )
        assert contract.tool == "pandoc"

    def test_rejects_extra_fields(self) -> None:
        with pytest.raises(ValueError):
            ParserContract(
                tool="pandoc",
                version="3.1",
                reader="markdown",
                writer="json",
                normalization_version="1.0",
                extra=42,
            )


class TestOutputConfig:
    def test_valid_config(self) -> None:
        config = OutputConfig(
            root="extraction/20_drafts/runs/",
            allowlist=["extraction/20_drafts/runs/"],
        )
        assert config.root.startswith("extraction/20_drafts/")


class TestGovernanceRefs:
    def test_valid_refs(self) -> None:
        refs = GovernanceRefs(
            module_registry_version="v1",
            field_classification_version="v1",
            schema_version="0.1",
            gmd_version="1.0",
        )
        assert refs.schema_version == "0.1"


class TestSourceManifest:
    def test_build_from_yaml(self) -> None:
        data = {
            "manifest_version": "1.0",
            "repository": {
                "url": "https://github.com/GMD-hub/GMD-guidelines",
                "commit_sha": "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
            },
            "source_files": [
                {"path": "chapter2-IDN.qmd", "scope": "included"},
            ],
            "supporting_files": [],
            "governance": {
                "module_registry_version": "v1",
                "field_classification_version": "v1",
                "schema_version": "0.1",
                "gmd_version": "1.0",
            },
            "parser_contract": {
                "tool": "pandoc",
                "version": "3.1.12",
                "reader": "markdown+pipe_tables+grid_tables+footnotes",
                "writer": "json",
                "normalization_version": "1.0",
            },
            "output": {
                "root": "extraction/20_drafts/runs/",
                "allowlist": ["extraction/20_drafts/runs/"],
            },
        }
        manifest = SourceManifest(**data)
        assert manifest.manifest_version == "1.0"
        assert manifest.repository.commit_sha == "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1"

    def test_forbids_extra_keys(self) -> None:
        data = {
            "manifest_version": "1.0",
            "repository": {
                "url": "https://github.com/GMD-hub/repo",
                "commit_sha": "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
            },
            "source_files": [],
            "supporting_files": [],
            "governance": {
                "module_registry_version": "v1",
                "field_classification_version": "v1",
                "schema_version": "0.1",
                "gmd_version": "1.0",
            },
            "parser_contract": {
                "tool": "pandoc",
                "version": "3.1",
                "reader": "markdown",
                "writer": "json",
                "normalization_version": "1.0",
            },
            "output": {"root": "e/", "allowlist": ["e/"]},
            "extra_key": "should be forbidden",
        }
        with pytest.raises(ValueError):
            SourceManifest(**data)


class TestResolvedSource:
    def _base_data(self) -> dict:
        return {
            "manifest_version": "1.0",
            "repository": {
                "url": "https://github.com/GMD-hub/repo",
                "commit_sha": "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
            },
            "resolved_at": "2026-08-03T00:00:00Z",
            "source_files": [
                {"path": "chapter2-IDN.qmd", "scope": "included"},
            ],
            "verified_sha256": True,
        }

    def test_valid_resolved_source(self) -> None:
        rs = ResolvedSource(**self._base_data())
        assert rs.verified_sha256 is True
        assert rs.manifest_version == "1.0"

    def test_forbids_extra(self) -> None:
        data = self._base_data()
        data["extra"] = "no"
        with pytest.raises(ValueError):
            ResolvedSource(**data)


class TestRunModels:
    def test_content_run_manifest_forbids_extra(self) -> None:
        with pytest.raises(ValueError):
            ContentRunManifest(
                execution_id="exec-1",
                content_run_id="run-1",
                manifest_version="1.0",
                source_commit_sha="d46dc03d253764ad7bdef53f625d54fd2a0a9ea1",
                parser_version="3.1.12",
                normalization_version="1.0",
                governance_versions={},
                agent_response_hashes=[],
                finalized_at="2026-08-03T00:00:00Z",
                extra="no",
            )

    def test_run_ledger_event_forbids_extra(self) -> None:
        with pytest.raises(ValueError):
            RunLedgerEvent(
                execution_id="exec-1",
                timestamp="2026-08-03T00:00:00Z",
                event_type="start",
                details="run started",
                extra="no",
            )
