"""Tests for extraction manifest and immutable source-proof models."""

import copy
import hashlib

import pytest

from schema.extraction.manifest import (
    GovernanceRefs,
    OutputConfig,
    ParserContract,
    RepositoryIdentity,
    ResolvedSource,
    ResolvedSourceFile,
    SourceFileEntry,
    SourceManifest,
    source_manifest_sha256,
)
from schema.extraction.run import ContentRunManifest, RunLedgerEvent


COMMIT = "a" * 40
DIGEST = "b" * 64
REPOSITORY_URL = "https://example.com/acme/source-repository"


def _manifest_data() -> dict:
    return {
        "manifest_version": "fixture-v1",
        "repository": {"url": REPOSITORY_URL, "commit_sha": COMMIT},
        "source_files": [
            {"path": "docs/source.md", "scope": "primary", "sha256": DIGEST},
        ],
        "supporting_files": [],
        "governance": {
            "module_registry_version": "registry-v1",
            "field_classification_version": "fields-v1",
            "schema_version": "schema-v1",
            "gmd_version": "guidelines-v1",
        },
        "parser_contract": {
            "tool": "fixture-parser",
            "version": "1.2.3",
            "reader": "fixture-reader",
            "writer": "fixture-writer",
            "normalization_version": "normalization-v1",
        },
        "output": {
            "root": "extraction/20_drafts/",
            "run_root": "extraction/20_drafts/runs/",
            "allowlist": ["extraction/20_drafts/runs/"],
        },
    }


def _resolved_source_data() -> dict:
    content = b"verified source bytes\n"
    git_blob = f"blob {len(content)}\0".encode("ascii") + content
    entry = {
        "path": "docs/source.md",
        "scope": "primary",
        "sha256": hashlib.sha256(content).hexdigest(),
        "blob_sha": hashlib.sha1(git_blob, usedforsecurity=False).hexdigest(),
        "content": content,
    }
    manifest = _manifest_data()
    return {
        "manifest_version": manifest["manifest_version"],
        "manifest_sha256": source_manifest_sha256(manifest),
        "repository": manifest["repository"],
        "parser_contract": manifest["parser_contract"],
        "governance": manifest["governance"],
        "resolved_at": "2026-08-30T12:00:00Z",
        "source_files": [entry],
        "supporting_files": [],
        "verified_sha256": True,
    }


class TestRepositoryIdentity:
    def test_valid_https_url(self) -> None:
        repo = RepositoryIdentity(
            url=REPOSITORY_URL,
            commit_sha=COMMIT,
        )
        assert repo.url == REPOSITORY_URL

    def test_rejects_non_https_url(self) -> None:
        with pytest.raises(ValueError, match="HTTPS"):
            RepositoryIdentity(
                url="http://example.com/acme/source-repository",
                commit_sha=COMMIT,
            )

    def test_rejects_non_40_char_sha(self) -> None:
        with pytest.raises(ValueError, match="40-character"):
            RepositoryIdentity(
                url=REPOSITORY_URL,
                commit_sha="abc123",
            )

    def test_rejects_uppercase_sha(self) -> None:
        with pytest.raises(ValueError, match="lowercase"):
            RepositoryIdentity(url=REPOSITORY_URL, commit_sha="A" * 40)

    @pytest.mark.parametrize(
        "url",
        [
            "https://example.com",
            "https://user@example.com/acme/repository",
            "https://example.com/acme/repository?ref=main",
            "https://example.com/acme/repository#fragment",
        ],
    )
    def test_rejects_incomplete_or_ambiguous_https_identity(self, url: str) -> None:
        with pytest.raises(ValueError, match="HTTPS repository identity"):
            RepositoryIdentity(url=url, commit_sha=COMMIT)


class TestSourceFileEntry:
    def test_valid_entry(self) -> None:
        entry = SourceFileEntry(
            path="docs/source.md",
            scope="primary",
            sha256=DIGEST,
        )
        assert entry.path == "docs/source.md"
        assert entry.scope == "primary"

    def test_rejects_extra_fields(self) -> None:
        with pytest.raises(ValueError):
            SourceFileEntry(
                path="x.qmd",
                scope="included",
                sha256=DIGEST,
                bonus_field="nope",
            )

    def test_valid_scopes(self) -> None:
        for scope in ("primary", "supporting", "excluded-by-policy"):
            entry = SourceFileEntry(path="x.qmd", scope=scope, sha256=DIGEST)
            assert entry.scope == scope

    def test_rejects_invalid_scope(self) -> None:
        with pytest.raises(ValueError, match="kebab-case"):
            SourceFileEntry(path="x.qmd", scope="Not Valid", sha256=DIGEST)

    @pytest.mark.parametrize(
        "path",
        ["../source.md", "docs/../source.md", "/docs/source.md", "docs//source.md"],
    )
    def test_rejects_unsafe_repository_path(self, path: str) -> None:
        with pytest.raises(ValueError, match="repository-relative"):
            SourceFileEntry(path=path, scope="primary", sha256=DIGEST)

    @pytest.mark.parametrize(
        "digest",
        ["a" * 63, "a" * 65, "A" * 64, "g" * 64],
    )
    def test_rejects_invalid_sha256_identity(self, digest: str) -> None:
        with pytest.raises(ValueError, match="64-character"):
            SourceFileEntry(path="source.md", scope="primary", sha256=digest)


class TestParserContract:
    def test_valid_contract(self) -> None:
        contract = ParserContract(
            tool="fixture-parser",
            version="1.2.3",
            reader="fixture-reader",
            writer="fixture-writer",
            normalization_version="normalization-v1",
        )
        assert contract.tool == "fixture-parser"

    def test_rejects_extra_fields(self) -> None:
        with pytest.raises(ValueError):
            ParserContract(
                tool="fixture-parser",
                version="1.2.3",
                reader="fixture-reader",
                writer="fixture-writer",
                normalization_version="normalization-v1",
                extra=42,
            )

    def test_rejects_blank_identity(self) -> None:
        with pytest.raises(ValueError, match="nonblank"):
            ParserContract(
                tool=" ",
                version="1.2.3",
                reader="fixture-reader",
                writer="fixture-writer",
                normalization_version="normalization-v1",
            )


class TestOutputConfig:
    def test_valid_config(self) -> None:
        config = OutputConfig(
            root="extraction/20_drafts/",
            run_root="extraction/20_drafts/runs/",
            allowlist=["extraction/20_drafts/runs/"],
        )
        expected = {
            "root": "extraction/20_drafts/",
            "run_root": "extraction/20_drafts/runs/",
            "allowlist": ["extraction/20_drafts/runs/"],
        }
        assert config.model_dump() == expected
        assert OutputConfig.model_validate_json(config.model_dump_json()) == config


class TestGovernanceRefs:
    def test_valid_refs(self) -> None:
        refs = GovernanceRefs(
            module_registry_version="registry-v1",
            field_classification_version="fields-v1",
            schema_version="schema-v1",
            gmd_version="guidelines-v1",
        )
        assert refs.schema_version == "schema-v1"


class TestSourceManifest:
    def test_build_from_yaml(self) -> None:
        data = _manifest_data()
        manifest = SourceManifest(**data)
        assert manifest.manifest_version == "fixture-v1"
        assert manifest.repository.commit_sha == COMMIT

    def test_forbids_extra_keys(self) -> None:
        data = _manifest_data()
        data["extra_key"] = "should be forbidden"
        with pytest.raises(ValueError):
            SourceManifest(**data)

    def test_rejects_duplicate_selected_paths(self) -> None:
        data = _manifest_data()
        data["supporting_files"] = [dict(data["source_files"][0])]
        with pytest.raises(ValueError, match="unique"):
            SourceManifest(**data)

    @pytest.mark.parametrize("version", ["", " ", "\n"])
    def test_rejects_blank_manifest_version(self, version: str) -> None:
        data = _manifest_data()
        data["manifest_version"] = version
        with pytest.raises(ValueError, match="nonblank"):
            SourceManifest(**data)

    def test_manifest_digest_fixed_vector_and_mutation_sensitivity(self) -> None:
        data = _manifest_data()
        digest = source_manifest_sha256(data)
        assert digest == (
            "02a8efa6749209e0e7d9c143bfef9e98"
            "adeab8b8070a187c7ddf8cd358677d50"
        )

        mutations = []
        for section, field, value in (
            ("repository", "commit_sha", "c" * 40),
            ("parser_contract", "version", "2.0.0"),
            ("governance", "schema_version", "schema-v2"),
            ("output", "root", "extraction/20_drafts/other/"),
        ):
            changed = copy.deepcopy(data)
            changed[section][field] = value
            mutations.append(changed)
        changed_source = copy.deepcopy(data)
        changed_source["source_files"][0]["sha256"] = "d" * 64
        mutations.append(changed_source)
        assert all(source_manifest_sha256(changed) != digest for changed in mutations)


class TestResolvedSource:
    def _base_data(self) -> dict:
        return _resolved_source_data()

    def test_valid_resolved_source(self) -> None:
        rs = ResolvedSource(**self._base_data())
        assert rs.verified_sha256 is True
        assert rs.manifest_version == "fixture-v1"
        assert rs.get_bytes("docs/source.md") == b"verified source bytes\n"

    def test_forbids_extra(self) -> None:
        data = self._base_data()
        data["extra"] = "no"
        with pytest.raises(ValueError):
            ResolvedSource(**data)

    def test_json_round_trip_preserves_verified_bytes(self) -> None:
        proof = ResolvedSource(**self._base_data())
        restored = ResolvedSource.model_validate_json(proof.model_dump_json())
        assert restored == proof
        assert restored.proof_sha256() == proof.proof_sha256()

    def test_proof_digest_fixed_vector_and_mutation_sensitivity(self) -> None:
        data = self._base_data()
        proof = ResolvedSource(**data)
        digest = proof.proof_sha256()
        assert digest == (
            "f3b72656fa3318c10dae8d9c3d2786ae"
            "467553f85bd54fc363a45ebbf1e3722f"
        )

        mutations = []
        for section, field, value in (
            ("repository", "commit_sha", "c" * 40),
            ("parser_contract", "version", "2.0.0"),
            ("governance", "schema_version", "schema-v2"),
        ):
            changed = copy.deepcopy(data)
            changed[section][field] = value
            mutations.append(ResolvedSource(**changed))

        changed_content = copy.deepcopy(data)
        content = b"different verified source bytes\n"
        git_blob = f"blob {len(content)}\0".encode("ascii") + content
        changed_content["source_files"][0].update(
            {
                "sha256": hashlib.sha256(content).hexdigest(),
                "blob_sha": hashlib.sha1(
                    git_blob,
                    usedforsecurity=False,
                ).hexdigest(),
                "content": content,
            }
        )
        mutations.append(ResolvedSource(**changed_content))
        assert all(changed.proof_sha256() != digest for changed in mutations)

    def test_rejects_tampered_content(self) -> None:
        data = self._base_data()
        data["source_files"][0]["content"] = b"changed"
        with pytest.raises(ValueError, match="content does not match"):
            ResolvedSource(**data)

    def test_rejects_unverified_proof(self) -> None:
        data = self._base_data()
        data["verified_sha256"] = False
        with pytest.raises(ValueError, match="True"):
            ResolvedSource(**data)


class TestResolvedSourceFile:
    def test_rejects_invalid_blob_identity(self) -> None:
        data = _resolved_source_data()["source_files"][0]
        data["blob_sha"] = "c" * 40
        with pytest.raises(ValueError, match="Git blob identity"):
            ResolvedSourceFile(**data)


class TestRunModels:
    def test_content_run_manifest_round_trip(self) -> None:
        manifest = ContentRunManifest(
            execution_id="exec-1",
            content_run_id="run-1",
            manifest_version="fixture-v1",
            source_commit_sha=COMMIT,
            parser_version="1.2.3",
            normalization_version="normalization-v1",
            governance_versions={"schema": "schema-v1"},
            agent_response_hashes=[DIGEST],
            finalized_at="2026-08-30T12:00:00Z",
        )
        assert manifest.model_dump()["source_commit_sha"] == COMMIT
        assert manifest.model_dump()["governance_versions"] == {
            "schema": "schema-v1"
        }
        assert ContentRunManifest.model_validate_json(
            manifest.model_dump_json()
        ) == manifest

    def test_content_run_manifest_forbids_extra(self) -> None:
        with pytest.raises(ValueError):
            ContentRunManifest(
                execution_id="exec-1",
                content_run_id="run-1",
                manifest_version="1.0",
                source_commit_sha=COMMIT,
                parser_version="1.2.3",
                normalization_version="normalization-v1",
                governance_versions={},
                agent_response_hashes=[],
                finalized_at="2026-08-03T00:00:00Z",
                extra="no",
            )

    def test_run_ledger_event_round_trip(self) -> None:
        event = RunLedgerEvent(
            execution_id="exec-1",
            timestamp="2026-08-30T12:00:00Z",
            event_type="source_verified",
            details="immutable source proof consumed",
        )
        assert event.model_dump() == {
            "execution_id": "exec-1",
            "timestamp": "2026-08-30T12:00:00Z",
            "event_type": "source_verified",
            "details": "immutable source proof consumed",
        }
        assert RunLedgerEvent.model_validate_json(event.model_dump_json()) == event

    def test_run_ledger_event_forbids_extra(self) -> None:
        with pytest.raises(ValueError):
            RunLedgerEvent(
                execution_id="exec-1",
                timestamp="2026-08-03T00:00:00Z",
                event_type="start",
                details="run started",
                extra="no",
            )
