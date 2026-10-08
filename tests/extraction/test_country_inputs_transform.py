from types import SimpleNamespace

from extraction_pipeline.country_inputs.transform import (
    transform_education_rows,
    transform_wash_rows,
)


def test_transform_education_rows_maps_expected_fields() -> None:
    row = SimpleNamespace(
        programme="Primary",
        programme_national="Primaria",
        entrance_age={"min": 6},
        duration_years={"min": 6},
        isced="1",
        isced_label="ISCED 1 Primary",
        gmd="primary",
        completion="full",
        source_row=12,
    )
    instruction = SimpleNamespace(rows=[row])
    result = {"instruction": instruction}

    mapped = transform_education_rows(result)

    assert len(mapped) == 1
    assert mapped[0]["national_label_en"] == "Primary"
    assert mapped[0]["national_label_local"] == "Primaria"
    assert mapped[0]["entry_age"] == 6
    assert mapped[0]["duration_years"] == 6
    assert mapped[0]["isced_level"] == "1"
    assert mapped[0]["gmd_educat4_target"] == "primary"


def test_transform_wash_rows_maps_expected_fields() -> None:
    row = SimpleNamespace(
        code="covered_well",
        label="Covered well",
        jmp_label_local="Pozo cubierto",
        jmp="Ground water > Protected well",
        jmp_id="ground_water.protected_well",
        gmd="protected_well",
        spans=[],
        improved=True,
        shared=False,
        source_row=33,
    )
    instruction = SimpleNamespace(rows=[row])
    result = {"domains": {"water": {"instruction": instruction}}}

    mapped = transform_wash_rows(result, "water")

    assert len(mapped) == 1
    assert mapped[0]["source_category_code"] == "covered_well"
    assert mapped[0]["national_label_local"] == "Pozo cubierto"
    assert mapped[0]["jmp_id"] == "ground_water.protected_well"
    assert mapped[0]["improved_flag"] is True
