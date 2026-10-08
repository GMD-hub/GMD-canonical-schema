from extraction_pipeline.country_inputs.education_pathways import (
    discover_all_iso3,
    infer_country,
    infer_period,
)


def test_infers_school_path_and_excludes_isced_zero() -> None:
    period = {
        "effective_from": 1990,
        "effective_to": None,
        "value": [
            {"country_entry_id": "VNM-EDU-03", "isced_level": "1", "duration_years": 5},
            {"country_entry_id": "VNM-EDU-04", "isced_level": "2", "duration_years": 4},
            {"country_entry_id": "VNM-EDU-05", "isced_level": "3", "duration_years": 3, "national_label_en": "Upper secondary"},
        ],
    }

    rows = {row["country_entry_id"]: row for row in infer_period(period, "VNM")["rows"]}

    assert rows["VNM-EDU-05"]["parent_country_entry_ids"] == ["VNM-EDU-04"]
    assert rows["VNM-EDU-05"]["cum_years_schooling"] == 12
    assert rows["VNM-EDU-05"]["cum_years_computation_path"] == [
        "VNM-EDU-03",
        "VNM-EDU-04",
        "VNM-EDU-05",
    ]


def test_selects_minimum_multiple_tertiary_parent_path() -> None:
    period = {
        "value": [
            {"country_entry_id": "VNM-EDU-03", "isced_level": "1", "duration_years": 5},
            {"country_entry_id": "VNM-EDU-04", "isced_level": "2", "duration_years": 4},
            {"country_entry_id": "VNM-EDU-05", "isced_level": "3", "duration_years": 3, "national_label_en": "Upper secondary"},
            {"country_entry_id": "VNM-EDU-12", "isced_level": "6", "duration_years": 4, "national_label_en": "Bachelor"},
            {"country_entry_id": "VNM-EDU-13", "isced_level": "6", "duration_years": 5, "national_label_en": "Bachelor"},
            {"country_entry_id": "VNM-EDU-15", "isced_level": "7", "duration_years": 2, "national_label_en": "Master's"},
        ],
    }

    rows = {row["country_entry_id"]: row for row in infer_period(period, "VNM")["rows"]}

    assert rows["VNM-EDU-15"]["cum_years_status"] == "computed"
    assert rows["VNM-EDU-15"]["cum_years_schooling"] == 18
    assert "minimum parent path selected" in rows["VNM-EDU-15"]["review_flags"][0]


def test_full_country_sweep_never_raises_and_rows_have_valid_status() -> None:
    iso3_list = discover_all_iso3()
    assert len(iso3_list) > 100  # sanity check the crosswalk sweep found the real country set

    failures: dict[str, str] = {}
    for iso3 in iso3_list:
        try:
            data = infer_country(iso3)
        except Exception as exc:  # noqa: BLE001 - want to report every failing country, not just the first
            failures[iso3] = str(exc)
            continue

        for period in data["periods"]:
            for row in period["rows"]:
                assert row["cum_years_status"] in {"computed", "review_required"}
                if row["cum_years_status"] == "review_required":
                    assert row["review_flags"]

    assert not failures, f"education pathway inference failed for: {sorted(failures)}"
