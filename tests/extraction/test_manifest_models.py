"""Tests for fail-closed extraction manifest models."""

import copy

import pytest
from pydantic import ValidationError

from schema.extraction.manifest import (
    GovernanceRefs,
    ParserContract,
    RepositoryIdentity,
    ResolvedSource,
    SourceFileEntry,
    SourceManifest,
)


DIGEST = "a" * 64
COMMIT = "d46dc03d253764ad7bdef53f625d54fd2a0a9ea1"
URL = "https://github.com/GMD-hub/GMD-guidelines"


def manifest_data() -> dict:
    return {
        "manifest_version": "1.0",
        "repository": {"url": URL, "commit_sha": COMMIT},
        "source_files": [{"path": "chapters/chapter2-IDN.qmd", "scope": "included", "sha256": DIGEST}],
        "supporting_files": [{"path": "docs/GMD_household_survey_harmonization.md", "scope": "supporting", "sha256": "b" * 64}],
        "governance": {
            "module_registry_version": "v1",
            "field_classification_version": "v1",
            "schema_version": "0.1",
            "gmd_version": "3.0",
        },
        "parser_contract": {
            "tool": "pandoc",
            "version": "3.1.12",
            "installation_method": "pandoc/actions/setup@commit",
            "reader": "markdown",
            "writer": "json",
            "normalization_version": "1.0",
        },
        "output": {"root": "extraction/20_drafts/", "allowlist": ["extraction/20_drafts/runs/"]},
    }


@pytest.mark.parametrize("url", ["http://github.com/GMD-hub/GMD-guidelines", URL + "/", URL + ".git", "https://example.com/repo"])
def test_repository_rejects_url_variants(url: str) -> None:
    with pytest.raises(ValidationError, match="governed GMD-guidelines URL"):
        RepositoryIdentity(url=url, commit_sha=COMMIT)


@pytest.mark.parametrize("commit", [None, "a" * 39, "a" * 41, "g" * 40, "A" * 40, "main"])
def test_repository_rejects_malformed_commit(commit: object) -> None:
    with pytest.raises(ValidationError, match="commit_sha"):
        RepositoryIdentity(url=URL, commit_sha=commit)


@pytest.mark.parametrize("digest", [None, "a" * 63, "a" * 65, "g" * 64, "A" * 64])
def test_source_entry_rejects_unpinned_or_malformed_hash(digest: object) -> None:
    with pytest.raises(ValidationError, match="sha256"):
        SourceFileEntry(path="chapters/chapter2-IDN.qmd", scope="included", sha256=digest)


def test_source_entry_requires_hash() -> None:
    with pytest.raises(ValidationError, match="sha256"):
        SourceFileEntry(path="x", scope="included")


@pytest.mark.parametrize("field", ["version", "installation_method"])
@pytest.mark.parametrize("value", ["", "  "])
def test_parser_rejects_blank_identity(field: str, value: str) -> None:
    data = manifest_data()["parser_contract"]
    data[field] = value
    with pytest.raises(ValidationError, match="nonblank"):
        ParserContract.model_validate(data)


def test_parser_rejects_alternate_tool() -> None:
    data = manifest_data()["parser_contract"]
    data["tool"] = "quarto"
    with pytest.raises(ValidationError) as caught:
        ParserContract.model_validate(data)
    assert caught.value.errors()[0]["loc"] == ("tool",)


def test_parser_requires_installation_method() -> None:
    data = manifest_data()["parser_contract"]
    data.pop("installation_method")
    with pytest.raises(ValidationError) as caught:
        ParserContract.model_validate(data)
    assert caught.value.errors()[0]["loc"] == ("installation_method",)


@pytest.mark.parametrize("field", ["module_registry_version", "field_classification_version", "schema_version", "gmd_version"])
def test_governance_refs_reject_blank_values(field: str) -> None:
    data = manifest_data()["governance"]
    data[field] = " "
    with pytest.raises(ValidationError, match="nonblank"):
        GovernanceRefs.model_validate(data)


def test_complete_manifest_and_resolved_source_round_trip() -> None:
    manifest = SourceManifest.model_validate(manifest_data())
    resolved = ResolvedSource(
        manifest_version=manifest.manifest_version,
        repository=manifest.repository,
        resolved_at="2026-08-26T12:00:00Z",
        source_files=manifest.source_files,
        supporting_files=manifest.supporting_files,
        verified_sha256=True,
    )
    assert resolved.source_files[0].scope == "included"
    assert resolved.supporting_files[0].sha256 == "b" * 64


def test_manifest_forbids_extra_fields() -> None:
    data = copy.deepcopy(manifest_data())
    data["extra"] = True
    with pytest.raises(ValidationError, match="extra"):
        SourceManifest.model_validate(data)
