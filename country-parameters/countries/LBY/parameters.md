---
country_id: CTY-LBY
iso3: LBY
schema_version: '0.2'
status: draft
country_name: LBY
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LBY-EDU-01
    national_label_en: Pre-primary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0645\u0627\
      \ \u0642\u0628\u0644 \u0627\u0644\u0627\u0628\u062A\u062F\u0627\u0626\u064A"
    entry_age: 4
    duration_years: 2
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: LBY-EDU-02
    national_label_en: First stage of basic education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0627\u0633\u0627\u0633\u064A - \u0627\u0644\u0634\u0642 \u0627\u0644\u0627\
      \u0648\u0644"
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - LBY-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: LBY-EDU-03
    national_label_en: Second stage of basic education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u0623\u0633\u0627\u0633\u064A - \u0627\u0644\u0634\u0642 \u0627\u0644\u062B\
      \u0627\u0646\u064A"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - LBY-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-04
    national_label_en: General secondary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u0639\u0627\u0645"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 10
    parent_country_entry_ids:
    - LBY-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-05
    national_label_en: Technical secondary education
    national_label_local: "\u0627\u0644\u062A\u0639\u0644\u064A\u0645 \u0627\u0644\
      \u062B\u0627\u0646\u0648\u064A \u0627\u0644\u0641\u0646\u064A"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - LBY-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-06
    national_label_en: Higher technical diploma
    national_label_local: "\u0627\u0644\u062F\u0628\u0644\u0648\u0645 \u0627\u0644\
      \u0639\u0627\u0644\u064A \u0627\u0644\u062A\u0642\u0646\u064A"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 12
    parent_country_entry_ids:
    - LBY-EDU-04
    cum_years_schooling: 15
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-07
    national_label_en: Bachelor's and licence programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0628\u0643\
      \u0627\u0644\u0648\u0631\u064A\u0648\u0633 \u0648\u0627\u0644\u0644\u064A\u0633\
      \u0627\u0646\u0633"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
    parent_country_entry_ids:
    - LBY-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-08
    national_label_en: Technical Bachelor's Programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0628\u0643\
      \u0627\u0644\u0648\u0631\u064A\u0648\u0633 \u0627\u0644\u062A\u0642\u0646\u064A"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
    parent_country_entry_ids:
    - LBY-EDU-04
    cum_years_schooling: 16
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-09
    national_label_en: Bachelor's programmes in medicine, engineering, pharmacology
      and medical technology
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0628\u0643\
      \u0627\u0644\u0648\u0631\u064A\u0648\u0633 \u0641\u064A \u0627\u0644\u0637\u0628\
      \u060C \u0627\u0644\u0647\u0646\u062F\u0633\u0629\u060C \u0627\u0644\u0635\u064A\
      \u062F\u0644\u0629 \u0648\u062A\u0643\u0646\u0648\u0644\u0648\u062C\u064A\u0627\
      \ \u0627\u0644\u0637\u0628"
    entry_age: 18
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - LBY-EDU-04
    cum_years_schooling: 17
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LBY-EDU-10
    national_label_en: Master's programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0627\
      \u062C\u0633\u062A\u064A\u0631"
    entry_age: 22
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - LBY-EDU-07
    - LBY-EDU-08
    - LBY-EDU-09
    cum_years_schooling: 19
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-07
    - LBY-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBY-EDU-07, LBY-EDU-08, LBY-EDU-09'
  - country_entry_id: LBY-EDU-11
    national_label_en: Technical Master's Programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u0645\u0627\
      \u062C\u0633\u062A\u064A\u0631 \u0627\u0644\u062A\u0642\u0646\u064A"
    entry_age: 22
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - LBY-EDU-07
    - LBY-EDU-08
    - LBY-EDU-09
    cum_years_schooling: 19
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-07
    - LBY-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBY-EDU-07, LBY-EDU-08, LBY-EDU-09'
  - country_entry_id: LBY-EDU-12
    national_label_en: Doctorate programmes
    national_label_local: "\u0628\u0631\u0627\u0645\u062C \u0627\u0644\u062F\u0643\
      \u062A\u0648\u0631\u0627\u0647"
    entry_age: 25
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - LBY-EDU-10
    - LBY-EDU-11
    cum_years_schooling: 22
    cum_years_computation_path:
    - LBY-EDU-02
    - LBY-EDU-03
    - LBY-EDU-04
    - LBY-EDU-07
    - LBY-EDU-10
    - LBY-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LBY-EDU-07, LBY-EDU-08, LBY-EDU-09'
    - 'minimum parent path selected from: LBY-EDU-10, LBY-EDU-11'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Libya.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LBY-SAN-01
    source_category_code: flush_or_pour_flush_toilet
    national_label_en: Flush or pour/flush toilet
    national_label_local: "\u0634\u0637\u0641 \u0648\u0635\u0628 \u062F\u0627\u0641\
      \u0642"
    jmp_classification: Flush and pour flush
    jmp_id: flush_and_pour_flush
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 60
  - country_entry_id: LBY-SAN-02
    source_category_code: bucket_toilet
    national_label_en: Bucket toilet
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062F\u0644\u0648"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: LBY-SAN-03
    source_category_code: hanging_toilet_latrine
    national_label_en: Hanging toilet/latrine
    national_label_local: "\u062F\u0648\u0631\u0629 \u0645\u064A\u0627\u0647 \u0645\
      \u0639\u0644\u0642\u0629 / \u0645\u0631\u062D\u0627\u0636 \u0645\u0639\u0644\
      \u0642"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: LBY-SAN-04
    source_category_code: open_hole
    national_label_en: Open hole
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 111
  - country_entry_id: LBY-SAN-05
    source_category_code: plastic_bag
    national_label_en: Plastic bag
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 111
  - country_entry_id: LBY-SAN-06
    source_category_code: pit_latrine_with_a_slab_and_platform
    national_label_en: Pit latrine with a slab and platform
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0645\u0639 \u0628\u0644\u0627\u0637\u0629 / \u0645\u0631\u062D\u0627\u0636\
      \ \u0645\u063A\u0637\u0649"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: LBY-SAN-07
    source_category_code: pit_latrine_without_a_slab_and_platform
    national_label_en: Pit latrine without a slab and platform
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0628\u062F\u0648\u0646 \u0628\u0644\u0627\u0637\u0629 / \u062D\u0641\u0631\
      \u0629 \u0645\u0641\u062A\u0648\u062D\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: LBY-SAN-08
    source_category_code: pit_latrine_without_a_slab_or_platform
    national_label_en: Pit latrine without a slab or platform
    national_label_local: "\u0645\u0631\u062D\u0627\u0636 \u062D\u0641\u0631\u0629\
      \ \u0628\u062F\u0648\u0646 \u0628\u0644\u0627\u0637\u0629 / \u062D\u0641\u0631\
      \u0629 \u0645\u0641\u062A\u0648\u062D\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: LBY-SAN-09
    source_category_code: pit_vip_toilet_pit_latrine_with_ventilation
    national_label_en: Pit VIP toilet (Pit latrine with ventilation)
    national_label_local: "\u0645\u0631\u0627\u062D\u064A\u0636 \u062D\u0641\u0631\
      \u0629 \u0645\u062D\u0633\u0646\u0629 \u062C\u064A\u062F\u0629 \u0627\u0644\u062A\
      \u0647\u0648\u064A\u0629"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: LBY-SAN-10
    source_category_code: none_open_hole
    national_label_en: None + open hole
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: LBY-SAN-11
    source_category_code: none_of_the_above_open_defecation
    national_label_en: None of the above, open defecation
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: LBY-SAN-12
    source_category_code: none_of_the_above_open_defecation_open_hole
    national_label_en: None of the above, open defecation + open hole
    national_label_local: "\u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0646\u0634\
      \u0623\u0629 \u060C \u0634\u062C\u064A\u0631\u0629 \u060C \u062D\u0642\u0644"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: LBY-SAN-13
    source_category_code: other_specify
    national_label_en: Other (specify)
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: LBY-SAN-14
    source_category_code: plastic_bag
    national_label_en: Plastic bag
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_LBY_Libya_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LBY-WAS-01
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: "\u064A\u0646\u0628\u0648\u0639 \u0627\u0644\u0645\u062D\
      \u0645\u064A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: LBY-WAS-02
    source_category_code: protected_well_e_g_in_your_house_or_in_the_mosque
    national_label_en: Protected well (e.g. in your house or in the mosque)
    national_label_local: "\u0645\u062D\u0645\u064A \u0628\u0634\u0643\u0644 \u062C\
      \u064A\u062F"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: LBY-WAS-03
    source_category_code: borehole_or_tubewell
    national_label_en: Borehole or tubewell
    national_label_local: "\u0628\u0626\u0631 \u0623\u0646\u0628\u0648\u0628\u064A\
      \ \u060C \u0628\u0626\u0631"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: LBY-WAS-04
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: "\u0628\u0626\u0631 \u063A\u064A\u0631 \u0645\u062D\u0645\
      \u064A"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: LBY-WAS-05
    source_category_code: water_kiosk
    national_label_en: Water kiosk
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: LBY-WAS-06
    source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: LBY-WAS-07
    source_category_code: water_trucking
    national_label_en: Water trucking
    national_label_local: "\u064A\u062A\u0645 \u062A\u0648\u0641\u064A\u0631 \u0634\
      \u0627\u062D\u0646\u0629 \u0635\u0647\u0631\u064A\u062C"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: LBY-WAS-08
    source_category_code: other_please_specify
    national_label_en: Other (please specify)
    national_label_local: "\u0622\u062E\u0631"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: LBY-WAS-09
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0645\u064A\u0627\u0647 \u0645\u0639\u0628\u0623\u0629"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: LBY-WAS-10
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: "\u0643\u064A\u0633 \u0645\u0627\u0621"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: LBY-WAS-11
    source_category_code: rainwater
    national_label_en: rainwater
    national_label_local: "\u0645\u064A\u0627\u0647 \u0627\u0644\u0623\u0645\u0637\
      \u0627\u0631"
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: LBY-WAS-12
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: "\u062E\u0632\u0627\u0646 / \u062E\u0632\u0627\u0646 \u0645\
      \u063A\u0637\u0649"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: LBY-WAS-13
    source_category_code: surface_water_lakes_ponds_rivers_etc
    national_label_en: Surface water (lakes, ponds, rivers, etc.)
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: LBY-WAS-14
    source_category_code: surface_water_river_dam_lake_pond_stream_canal_irrigation_channel
    national_label_en: Surface water (river, dam, lake, pond, stream, canal, irrigation
      channel)
    national_label_local: "\u0633\u0637\u062D \u0627\u0644\u0645\u0627\u0621"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: LBY-WAS-15
    source_category_code: public_network
    national_label_en: Public network
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: LBY-WAS-16
    source_category_code: public_network_connected_to_the_shelter
    national_label_en: Public network (connected to the shelter)
    national_label_local: "\u0627\u0644\u0645\u0627\u0621 \u0628\u0627\u0644\u0623\
      \u0646\u0627\u0628\u064A\u0628 \u0641\u064A \u0627\u0644\u0645\u0633\u0643\u0646"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: LBY-WAS-17
    source_category_code: public_network_connected_to_the_neighbour_s_shelter
    national_label_en: Public network (connected to the neighbour's shelter)
    national_label_local: "\u0627\u0644\u0645\u064A\u0627\u0647 \u0627\u0644\u0645\
      \u0646\u0642\u0648\u0644\u0629 \u0628\u0627\u0644\u0623\u0646\u0627\u0628\u064A\
      \u0628 \u0625\u0644\u0649 \u0633\u0627\u062D\u0629 / \u0642\u0637\u0639\u0629\
      \ \u0623\u0631\u0636"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: LBY-WAS-18
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: "\u0627\u0644\u062D\u0646\u0641\u064A\u0629 \u0627\u0644\
      \u0639\u0627\u0645\u0629 \u0648\u0627\u0644\u0635\u0646\u0628\u0648\u0631 \u0627\
      \u0644\u0631\u0623\u0633\u064A"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: LBY-WAS-19
    source_category_code: tap_accessible_to_the_public
    national_label_en: Tap accessible to the public
    national_label_local: "\u0627\u0644\u062D\u0646\u0641\u064A\u0629 \u0627\u0644\
      \u0639\u0627\u0645\u0629 \u0648\u0627\u0644\u0635\u0646\u0628\u0648\u0631 \u0627\
      \u0644\u0631\u0623\u0633\u064A"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_LBY_Libya_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

