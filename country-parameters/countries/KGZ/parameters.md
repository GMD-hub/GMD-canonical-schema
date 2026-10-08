---
country_id: CTY-KGZ
iso3: KGZ
schema_version: '0.2'
status: draft
country_name: KGZ
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: KGZ-EDU-01
    national_label_en: Pre-primary education for young children (under 3 years-old)
    national_label_local: "\u041C\u0435\u043A\u0442\u0435\u043F \u0436\u0430\u0448\
      \u044B\u043D\u0430 \u0447\u0435\u0439\u0438\u043D\u043A\u0438 \u043A\u0438\u0447\
      \u04AF\u04AF \u0431\u0430\u043B\u0434\u0430\u0440 \u04AF\u0447\u04AF\u043D \u043F\
      \u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0430 (3 \u0436\u0430\u0448\u043A\
      \u0430 \u0447\u0435\u0439\u0438\u043D)"
    entry_age: 1
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
  - country_entry_id: KGZ-EDU-02
    national_label_en: Pre-primary education
    national_label_local: "\u041C\u0435\u043A\u0442\u0435\u043F \u0436\u0430\u0448\
      \u044B\u043D\u0430 \u0447\u0435\u0439\u0438\u043D\u043A\u0438 \u0431\u0438\u043B\
      \u0438\u043C \u0431\u0435\u0440\u04AF\u04AF \u043F\u0440\u043E\u0433\u0440\u0430\
      \u043C\u043C\u0430\u0441\u044B"
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 8
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: KGZ-EDU-03
    national_label_en: Preparation for school
    national_label_local: "\u041C\u0435\u043A\u0442\u0435\u043F\u043A\u0435  \u0447\
      \u0435\u0439\u0438\u043D\u043A\u0438 \u0434\u0430\u044F\u0440\u0434\u044B\u043A\
      \u0442\u044B\u043D \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0430\u0441\
      \u044B"
    entry_age: 6
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: KGZ-EDU-04
    national_label_en: Primary general education
    national_label_local: "\u0411\u0430\u0448\u0442\u0430\u043F\u043A\u044B \u0436\
      \u0430\u043B\u043F\u044B \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\
      \u04AF"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - KGZ-EDU-04
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: KGZ-EDU-05
    national_label_en: "Basic general secondary education \n(1st stage of secondary)"
    national_label_local: "\u041D\u0435\u0433\u0438\u0437\u0433\u0438 \u0436\u0430\
      \u043B\u043F\u044B (\u043E\u0440\u0442\u043E \u0431\u0438\u043B\u0438\u043C\u0434\
      \u0438\u043D 1-\u044D\u0442\u0430\u0431\u044B)"
    entry_age: 11
    duration_years: 5
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - KGZ-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-06
    national_label_en: "Secondary general education \n(2nd stage of secondary)"
    national_label_local: "\u041E\u0440\u0442\u043E \u0436\u0430\u043B\u043F\u044B\
      \ (\u043E\u0440\u0442\u043E \u0431\u0438\u043B\u0438\u043C\u0434\u0438\u043D\
      \ 2-\u044D\u0442\u0430\u0431\u044B)"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - KGZ-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-07
    national_label_en: Basic vocational education based on basic general secondary
    national_label_local: "\u041D\u0435\u0433\u0438\u0437\u0433\u0438 \u0436\u0430\
      \u043B\u043F\u044B \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\
      \u043D\u04AF\u043D \u0431\u0430\u0437\u0430\u0441\u044B\u043D\u0434\u0430\u0433\
      \u044B \u0431\u0430\u0448\u0442\u0430\u043F\u043A\u044B \u043A\u0435\u0441\u0438\
      \u043F\u0442\u0438\u043A \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\
      \u04AF\u043D\u0443\u043D \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0430\
      \u0441\u044B"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - KGZ-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-08
    national_label_en: Grades 1-2 of secondary vocational education based on Basic
      General Secondary
    national_label_local: "\u041D\u0435\u0433\u0438\u0437\u0433\u0438 \u0436\u0430\
      \u043B\u043F\u044B \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\
      \u043D\u04AF\u043D \u0431\u0430\u0437\u0430\u0441\u044B\u043D\u0434\u0430\u0433\
      \u044B \u043E\u0440\u0442\u043E \u043A\u0435\u0441\u0438\u043F\u0442\u0438\u043A\
      \ \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\u043D\u04AF\u043D\
      \ 1-2-\u043A\u0443\u0440\u0441\u0442\u0430\u0440"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - KGZ-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-09
    national_label_en: Basic vocational education based on secondary general education
    national_label_local: "\u041E\u0440\u0442\u043E \u0436\u0430\u043B\u043F\u044B\
      \ \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\u043D\u04AF\u043D\
      \ \u0431\u0430\u0437\u0430\u0441\u044B\u043D\u0434\u0430\u0433\u044B \u0431\u0430\
      \u0448\u0442\u0430\u043F\u043A\u044B \u043A\u0435\u0441\u0438\u043F\u0442\u0438\
      \u043A \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\u043D\u0443\
      \u043D \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0430\u0441\u044B"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
    parent_country_entry_ids:
    - KGZ-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-10
    national_label_en: Grades 3-4 of secondary vocational education based on Basic
      General Secondary
    national_label_local: "\u041D\u0435\u0433\u0438\u0437\u0433\u0438 \u0436\u0430\
      \u043B\u043F\u044B \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\
      \u043D\u04AF\u043D \u0431\u0430\u0437\u0430\u0441\u044B\u043D\u0434\u0430\u0433\
      \u044B \u043E\u0440\u0442\u043E \u043A\u0435\u0441\u0438\u043F\u0442\u0438\u043A\
      \ \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\u043D\u04AF\u043D\
      \ 3-4-\u043A\u0443\u0440\u0441\u0442\u0430\u0440"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
    parent_country_entry_ids:
    - KGZ-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-11
    national_label_en: Secondary Vocational education based on General Secondary education
    national_label_local: "\u041E\u0440\u0442\u043E \u0436\u0430\u043B\u043F\u044B\
      \ \u0431\u0438\u043B\u0438\u043C \u0431\u0435\u0440\u04AF\u04AF\u043D\u04AF\u043D\
      \ \u0431\u0430\u0437\u0430\u0441\u044B\u043D\u0434\u0430\u0433\u044B \u043E\u0440\
      \u0442\u043E \u043A\u0435\u0441\u0438\u043F\u0442\u0438\u043A \u0431\u0438\u043B\
      \u0438\u043C \u0431\u0435\u0440\u04AF\u04AF"
    entry_age: 18
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - KGZ-EDU-06
    cum_years_schooling: 14
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-12
    national_label_en: Higher professional education
    national_label_local: "\u0416\u043E\u0433\u043E\u0440\u043A\u0443 \u043A\u0435\
      \u0441\u0438\u043F\u0442\u0438\u043A \u0431\u0438\u043B\u0438\u043C \u0431\u0435\
      \u0440\u04AF\u04AF"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - KGZ-EDU-06
    cum_years_schooling: 15
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-13
    national_label_en: Higher professional education (leading to entry into advanced
      research programmes)
    national_label_local: "\u0416\u043E\u0433\u043E\u0440\u043A\u0443 \u043A\u0435\
      \u0441\u0438\u043F\u0442\u0438\u043A \u0431\u0438\u043B\u0438\u043C \u0431\u0435\
      \u0440\u04AF\u04AF \n(\u0442\u0435\u0440\u0435\u04A3\u0434\u0435\u0442\u0438\
      \u043B\u0433\u0435\u043D \u0438\u043B\u0438\u043C\u0438\u0439 \u0438\u0437\u0438\
      \u043B\u0434\u04E9\u04E9 \n\u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0430\
      \u043B\u0430\u0440\u044B\u043D\u0430 \u043A\u0438\u0440\u04AF\u04AF\u0433\u04E9\
      \ \u0430\u043B\u044B\u043F \u0431\u0430\u0440\u0443\u0443\u0447\u0443)"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - KGZ-EDU-06
    cum_years_schooling: 16
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-14
    national_label_en: Higher professional education (leading to entry into advanced
      research programmes)
    national_label_local: "\u0416\u043E\u0433\u043E\u0440\u043A\u0443 \u043A\u0435\
      \u0441\u0438\u043F\u0442\u0438\u043A \u0431\u0438\u043B\u0438\u043C \u0431\u0435\
      \u0440\u04AF\u04AF \n(\u0442\u0435\u0440\u0435\u04A3\u0434\u0435\u0442\u0438\
      \u043B\u0433\u0435\u043D \u0438\u043B\u0438\u043C\u0438\u0439 \u0438\u0437\u0438\
      \u043B\u0434\u04E9\u04E9 \n\u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0430\
      \u043B\u0430\u0440\u044B\u043D\u0430 \u043A\u0438\u0440\u04AF\u04AF\u0433\u04E9\
      \ \u0430\u043B\u044B\u043F \u0431\u0430\u0440\u0443\u0443\u0447\u0443)"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - KGZ-EDU-06
    cum_years_schooling: 13
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: KGZ-EDU-15
    national_label_en: 'Post-graduate professional education

      (Aspirantura)'
    national_label_local: "\u0416\u043E\u0433\u043E\u0440\u043A\u0443 \u043E\u043A\
      \u0443\u0443 \u0436\u0430\u0439\u044B\u043D \u0431\u04AF\u0442\u04AF\u0440\u0433\
      \u04E9\u043D\u0434\u04E9\u043D \u043A\u0438\u0439\u0438\u043D\u043A\u0438 \u043A\
      \u0435\u0441\u0438\u043F\u0442\u0438\u043A \u0431\u0438\u043B\u0438\u043C \u0431\
      \u0435\u0440\u04AF\u04AF (\u0410\u0441\u043F\u0438\u0440\u0430\u043D\u0442\u0443\
      \u0440\u0430)"
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - KGZ-EDU-13
    - KGZ-EDU-14
    cum_years_schooling: 16
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-14
    - KGZ-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: KGZ-EDU-13, KGZ-EDU-14'
  - country_entry_id: KGZ-EDU-16
    national_label_en: 'Post-graduate professional education

      (Doctorantura)'
    national_label_local: "\u0416\u043E\u0433\u043E\u0440\u043A\u0443 \u043E\u043A\
      \u0443\u0443 \u0436\u0430\u0439\u044B\u043D \u0431\u04AF\u0442\u04AF\u0440\u0433\
      \u04E9\u043D\u0434\u04E9\u043D \u043A\u0438\u0439\u0438\u043D\u043A\u0438 \u043A\
      \u0435\u0441\u0438\u043F\u0442\u0438\u043A \u0431\u0438\u043B\u0438\u043C \u0431\
      \u0435\u0440\u04AF\u04AF (\u0414\u043E\u043A\u0442\u043E\u0440\u0430\u043D\u0442\
      \u0443\u0440\u0430)"
    entry_age: 26
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - KGZ-EDU-13
    - KGZ-EDU-14
    cum_years_schooling: 16
    cum_years_computation_path:
    - KGZ-EDU-04
    - KGZ-EDU-05
    - KGZ-EDU-06
    - KGZ-EDU-14
    - KGZ-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: KGZ-EDU-13, KGZ-EDU-14'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Kyrgyzstan.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: 2015
  selectors: null
  value:
  - country_entry_id: KGZ-SUBNAT-01
    survey_labels: 1 - Bishkek | 1-Bishkek | Bishkek
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_147293
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_147293
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147293'
    geo_nvar: ADM1_NAME
    geo_name: Bishkek
    source_row: 8768
  - country_entry_id: KGZ-SUBNAT-02
    survey_labels: 2-Issyk-kul | Issyk-kul
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_1752
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_1752
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1752'
    geo_nvar: ADM1_NAME
    geo_name: Ysyk-Kol
    source_row: 8769
  - country_entry_id: KGZ-SUBNAT-03
    survey_labels: 3-Jalal-Abad | Jalal-Abad
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_1748
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_1748
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1748'
    geo_nvar: ADM1_NAME
    geo_name: Jalal-Abad
    source_row: 8770
  - country_entry_id: KGZ-SUBNAT-04
    survey_labels: 4-Naryn | Naryn
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_1749
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_1749
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1749'
    geo_nvar: ADM1_NAME
    geo_name: Naryn
    source_row: 8771
  - country_entry_id: KGZ-SUBNAT-05
    survey_labels: 6-Osh | Osh
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_1750
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_1750
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1750'
    geo_nvar: ADM1_NAME
    geo_name: Osh
    source_row: 8772
  - country_entry_id: KGZ-SUBNAT-06
    survey_labels: 7-Talas | Talas
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_1751
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_1751
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1751'
    geo_nvar: ADM1_NAME
    geo_name: Talas
    source_row: 8773
  - country_entry_id: KGZ-SUBNAT-07
    survey_labels: 8-Chui | Chui
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_147294
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2015_GAUL1_147294
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '147294'
    geo_nvar: ADM1_NAME
    geo_name: Chuy
    source_row: 8774
  - country_entry_id: KGZ-SUBNAT-08
    survey_labels: Batken
    survey_variables: subnatid1
    gmd_subnatid1: KGZ_2015_GAUL1_1746
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1746'
    geo_nvar: ADM1_NAME
    geo_name: Batken
    source_row: 8790
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2022
  effective_to: null
  selectors: null
  value:
  - country_entry_id: KGZ-SUBNAT-01
    survey_labels: 1 - Bishkek | 1-Bishkek
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.2_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.2_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.2_1
    geo_nvar: NAME_1
    geo_name: "Bi\u0161kek"
    source_row: 8804
  - country_entry_id: KGZ-SUBNAT-02
    survey_labels: 2 - Issyk-kul | 2-Issyk-kul | Issykul
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.9_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.9_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.9_1
    geo_nvar: NAME_1
    geo_name: "Ysyk-K\xF6l"
    source_row: 8805
  - country_entry_id: KGZ-SUBNAT-03
    survey_labels: 3 - Jalal-Abad | 3-Jalal-Abad | Jalal-Abad
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.4_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.4_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.4_1
    geo_nvar: NAME_1
    geo_name: Jalal-Abad
    source_row: 8806
  - country_entry_id: KGZ-SUBNAT-04
    survey_labels: 4 - Naryn | 4-Naryn | Naryn
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.5_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.5_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.5_1
    geo_nvar: NAME_1
    geo_name: Naryn
    source_row: 8807
  - country_entry_id: KGZ-SUBNAT-05
    survey_labels: 5 - Batken | 5-Batken | Batken
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.1_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.1_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.1_1
    geo_nvar: NAME_1
    geo_name: Batken
    source_row: 8808
  - country_entry_id: KGZ-SUBNAT-06
    survey_labels: 6 - Osh | 6-Osh | Osh
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.7_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.7_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.7_1
    geo_nvar: NAME_1
    geo_name: Osh
    source_row: 8809
  - country_entry_id: KGZ-SUBNAT-07
    survey_labels: 7 - Talas | 7-Talas | Talas
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.8_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.8_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.8_1
    geo_nvar: NAME_1
    geo_name: Talas
    source_row: 8810
  - country_entry_id: KGZ-SUBNAT-08
    survey_labels: 8 - Chui | 8-Chui | Chui
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.3_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.3_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.3_1
    geo_nvar: NAME_1
    geo_name: "Ch\xFCy"
    source_row: 8811
  - country_entry_id: KGZ-SUBNAT-09
    survey_labels: 16 - Osh city | 9 - Osh c. | 9-Osh c.
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: KGZ_2022_GADM1_KGZ.6_1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: KGZ_2022_GADM1_KGZ.6_1
    geo_year: '2022'
    geo_source: GADM
    geo_level: '1'
    geo_idvar: GID_1
    geo_id: KGZ.6_1
    geo_nvar: NAME_1
    geo_name: Osh (city)
    source_row: 8812
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: null
  effective_to: 2014
  selectors:
    geo_year: unknown
  value:
  - country_entry_id: KGZ-SUBNAT-01
    survey_labels: 2 - Other urban | 3 - Rural | rural | urban
    survey_variables: subnatid
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: ''
    geo_year: ''
    geo_source: ''
    geo_level: ''
    geo_idvar: ''
    geo_id: ''
    geo_nvar: ''
    geo_name: ''
    source_row: 8776
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: KGZ-SAN-01
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: "\u041A\u043E\u043C\u043F\u043E\u0441\u0442\u0438\u0440\u0443\
      \u044E\u0449\u0438\u0435 \u0442\u0443\u0430\u043B\u0435\u0442\u044B"
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 128
  - country_entry_id: KGZ-SAN-02
    source_category_code: flush_pour_flush_to_open_drain
    national_label_en: flush/pour flush to open drain
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: KGZ-SAN-03
    source_category_code: to_open_drain
    national_label_en: to open drain
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 65
  - country_entry_id: KGZ-SAN-04
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: flush/pour flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: KGZ-SAN-05
    source_category_code: to_piped_sewer_system
    national_label_en: to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: KGZ-SAN-06
    source_category_code: flush_pour_flush_to_pit_latrine
    national_label_en: flush/pour flush to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: KGZ-SAN-07
    source_category_code: to_pit
    national_label_en: to pit
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 63
  - country_entry_id: KGZ-SAN-08
    source_category_code: flush_pour_flush_to_septic_tank
    national_label_en: flush/pour flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: KGZ-SAN-09
    source_category_code: to_septic_tank
    national_label_en: to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: KGZ-SAN-10
    source_category_code: flush_pour_flush_to_dk_where
    national_label_en: flush/pour flush to DK where
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: KGZ-SAN-11
    source_category_code: to_do_not_know_where
    national_label_en: to do not know where
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 64
  - country_entry_id: KGZ-SAN-12
    source_category_code: flush_toilet_in_house
    national_label_en: FLUSH TOILET IN HOUSE
    national_label_local: "\u0422\u0443\u0430\u043B\u0435\u0442\u044B \u0441\u043E\
      \ \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: KGZ-SAN-13
    source_category_code: own_flush_toilet
    national_label_en: Own flush toilet
    national_label_local: "\u0421\u043E\u0431\u0441\u0442\u0432\u0435\u043D\u043D\u044B\
      \u0439 \u0442\u0443\u0430\u043B\u0435\u0442 \u0441\u043E \u0441\u043C\u044B\u0432\
      \u043E\u043C"
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 72
  - country_entry_id: KGZ-SAN-14
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: KGZ-SAN-15
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit (latrine)
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 75
  - country_entry_id: KGZ-SAN-16
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: KGZ-SAN-17
    source_category_code: shared_flush_toilet
    national_label_en: Shared flush toilet
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439/\u0441\u043E\u0432\u043C\u0435\u0441\u0442\u043D\u043E\u0433\u043E\
      \ \u043F\u043E\u043B\u044C\u0437\u043E\u0432\u0430\u043D\u0438\u044F \u0442\u0443\
      \u0430\u043B\u0435\u0442 \u0441\u043E \u0441\u043C\u044B\u0432\u043E\u043C"
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 78
  - country_entry_id: KGZ-SAN-18
    source_category_code: flush_to_somewhere_else
    national_label_en: Flush to somewhere else
    national_label_local: "\u043A\u0443\u0434\u0430-\u0442\u043E \u0432 \u0434\u0440\
      \u0443\u0433\u043E\u0435 \u043C\u0435\u0441\u0442\u043E"
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 71
  - country_entry_id: KGZ-SAN-19
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: "\u0432 \u0442\u0440\u0443\u0431\u043E\u043F\u0440\u043E\
      \u0432\u043E\u0434\u043D\u0443\u044E \u043A\u0430\u043D\u0430\u043B\u0438\u0437\
      \u0430\u0446\u0438\u043E\u043D\u043D\u0443\u044E \u0441\u0438\u0441\u0442\u0435\
      \u043C\u0443"
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: KGZ-SAN-20
    source_category_code: flush_to_pit
    national_label_en: Flush to pit
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: KGZ-SAN-21
    source_category_code: flush_to_pit_latrine
    national_label_en: Flush to pit latrine
    national_label_local: "\u0432 \u0432\u044B\u0433\u0440\u0435\u0431\u043D\u0443\
      \u044E \u044F\u043C\u0443"
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 69
  - country_entry_id: KGZ-SAN-22
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: "\u0432 \u0441\u0435\u043F\u0442\u0438\u043A\u0442\u0435\
      \u043D\u043A"
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: KGZ-SAN-23
    source_category_code: flush_don_t_know_where
    national_label_en: Flush, don't know where
    national_label_local: "\u0432 \u043D\u0435\u0438\u0437\u0432\u0435\u0441\u0442\
      \u043D\u043E\u0435 \u043C\u0435\u0441\u0442\u043E/\u043D\u0435 \u0437\u043D\u0430\
      \u044E/\u043D\u0435 \u0443\u0432\u0435\u0440\u0435\u043D(\u0430)"
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: KGZ-SAN-24
    source_category_code: bucket
    national_label_en: Bucket
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u043E\
      \u0442\u0445\u043E\u0436\u0438\u043C \u0432\u0435\u0434\u0440\u043E\u043C"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: KGZ-SAN-25
    source_category_code: bucket_toilet
    national_label_en: Bucket toilet
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u043E\
      \u0442\u0445\u043E\u0436\u0438\u043C \u0432\u0435\u0434\u0440\u043E\u043C"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: KGZ-SAN-26
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: "\u041F\u043E\u0434\u0432\u0435\u0441\u043D\u043E\u0439\
      \ \u0442\u0443\u0430\u043B\u0435\u0442/\u043F\u043E\u0434\u0432\u0435\u0441\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 109
  - country_entry_id: KGZ-SAN-27
    source_category_code: pit_latirne_with_slab
    national_label_en: Pit latirne with slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: KGZ-SAN-28
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: KGZ-SAN-29
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab / Open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: KGZ-SAN-30
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: KGZ-SAN-31
    source_category_code: out_door_latrine
    national_label_en: OUT DOOR LATRINE
    national_label_local: "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043E\u043D\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: KGZ-SAN-32
    source_category_code: traditional_pit_toilet
    national_label_en: Traditional pit toilet
    national_label_local: "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043E\u043D\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: KGZ-SAN-33
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated improved pit latrine
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: KGZ-SAN-34
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit latrine (VIP)
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 105
  - country_entry_id: KGZ-SAN-35
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging toilet/hanging latrine
    national_label_local: "\u041F\u043E\u0434\u0432\u0435\u0441\u043D\u043E\u0439\
      \ \u0442\u0443\u0430\u043B\u0435\u0442/\u043F\u043E\u0434\u0432\u0435\u0441\u043D\
      \u0430\u044F \u0443\u0431\u043E\u0440\u043D\u0430\u044F"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.private_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 117
  - country_entry_id: KGZ-SAN-36
    source_category_code: pit_latrine_with_slab_covered_latrine
    national_label_en: Pit latrine with slab/covered latrine
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0441\
      \ \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\u0438\u0442\
      \u043E\u0439/\u0441 \u043A\u0440\u044B\u0442\u043E\u0439 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: KGZ-SAN-37
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: "\u0423\u0431\u043E\u0440\u043D\u0430\u044F \u0441 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439 \u0431\
      \u0435\u0437 \u043D\u0430\u043F\u043E\u043B\u044C\u043D\u043E\u0439 \u043F\u043B\
      \u0438\u0442\u044B/\u0441 \u043E\u0442\u043A\u0440\u044B\u0442\u043E\u0439 \u0432\
      \u044B\u0433\u0440\u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine without
      slab/open pit
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 116
  - country_entry_id: KGZ-SAN-38
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated Improved Pit latrine
    national_label_local: "\u0412\u0435\u043D\u0442\u0438\u043B\u0438\u0440\u0443\u0435\
      \u043C\u044B\u0435 \u0443\u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435\
      \ \u0443\u0431\u043E\u0440\u043D\u044B\u0435 \u0441 \u0432\u044B\u0433\u0440\
      \u0435\u0431\u043D\u043E\u0439 \u044F\u043C\u043E\u0439"
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 113
  - country_entry_id: KGZ-SAN-39
    source_category_code: no_facilities_or_bush_or_field
    national_label_en: No facilities or bush or field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: KGZ-SAN-40
    source_category_code: no_facility
    national_label_en: No facility
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: KGZ-SAN-41
    source_category_code: no_facility_bush_field
    national_label_en: No facility, Bush, Field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: KGZ-SAN-42
    source_category_code: no_facility_bush_field
    national_label_en: No facility/bush/field
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: KGZ-SAN-43
    source_category_code: no_toilet
    national_label_en: NO TOILET
    national_label_local: "\u0421\u043E\u043E\u0440\u0443\u0436\u0435\u043D\u0438\u0439\
      \ \u043D\u0435\u0442, \u043A\u0443\u0441\u0442\u044B, \u043F\u043E\u043B\u0435"
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: KGZ-SAN-44
    source_category_code: flush_toilet_in_another_dwelling
    national_label_en: FLUSH TOILET IN ANOTHER DWELLING
    national_label_local: "\u0414\u0440\u0443\u0433\u0438\u0435 \u0443\u043B\u0443\
      \u0447\u0448\u0435\u043D\u043D\u044B\u0435"
    jmp_classification: Other improved
    jmp_id: other_improved
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 131
  - country_entry_id: KGZ-SAN-45
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_KGZ_Kyrgyzstan_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: KGZ-WAS-01
    source_category_code: spring
    national_label_en: SPRING
    national_label_local: "\u0412\u0441\u0435 \u0440\u043E\u0434\u043D\u0438\u043A\
      \u0438"
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 74
  - country_entry_id: KGZ-WAS-02
    source_category_code: well_in_residence
    national_label_en: Well in residence
    national_label_local: "\u0427\u0430\u0441\u0442\u043D\u044B\u0439"
    jmp_classification: Ground water > All wells > Private
    jmp_id: ground_water.all_wells.private
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 55
  - country_entry_id: KGZ-WAS-03
    source_category_code: public_well
    national_label_en: Public well
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439"
    jmp_classification: Ground water > All wells > Public
    jmp_id: ground_water.all_wells.public
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: true
    source_row: 56
  - country_entry_id: KGZ-WAS-04
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 78
  - country_entry_id: KGZ-WAS-05
    source_category_code: dug_protected_well
    national_label_en: Dug protected well
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: KGZ-WAS-06
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: "\u0417\u0430\u0449\u0438\u0449\u0451\u043D\u043D\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 66
  - country_entry_id: KGZ-WAS-07
    source_category_code: well
    national_label_en: WELL
    national_label_local: "\u0422\u0440\u0430\u0434\u0438\u0446\u0438\u043E\u043D\u043D\
      \u044B\u0435 \u043A\u043E\u043B\u043E\u0434\u0446\u044B"
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 62
  - country_entry_id: KGZ-WAS-08
    source_category_code: tube_well_or_borehole
    national_label_en: Tube well or borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: KGZ-WAS-09
    source_category_code: tubewell_borehole
    national_label_en: tubewell, borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: KGZ-WAS-10
    source_category_code: tubewell_borehole
    national_label_en: Tubewell/borehole
    national_label_local: "\u0422\u0440\u0443\u0431\u0447\u0430\u0442\u044B\u0439\
      \ \u043A\u043E\u043B\u043E\u0434\u0435\u0446, \u0441\u043A\u0432\u0430\u0436\
      \u0438\u043D\u0430"
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: KGZ-WAS-11
    source_category_code: unprotected_spring
    national_label_en: Unprotected spring
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u0440\u043E\u0434\u043D\u0438\u043A"
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 82
  - country_entry_id: KGZ-WAS-12
    source_category_code: dug_unprotected_well
    national_label_en: Dug unprotected well
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: KGZ-WAS-13
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: "\u041D\u0435\u0437\u0430\u0449\u0438\u0449\u0451\u043D\u043D\
      \u044B\u0439 \u043A\u043E\u043B\u043E\u0434\u0435\u0446"
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 70
  - country_entry_id: KGZ-WAS-14
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: KGZ-WAS-15
    source_category_code: cart_with_small_tank_drum
    national_label_en: Cart with small tank/drum
    national_label_local: "\u0422\u0435\u043B\u0435\u0436\u043A\u0430 \u0441 \u043D\
      \u0435\u0431\u043E\u043B\u044C\u0448\u0438\u043C \u0431\u0430\u043A\u043E\u043C\
      /\u0431\u043E\u0447\u043A\u043E\u0439"
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 101
  - country_entry_id: KGZ-WAS-16
    source_category_code: centralized_pipeline
    national_label_en: CENTRALIZED PIPELINE
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: KGZ-WAS-17
    source_category_code: centralized_pipeline_other
    national_label_en: CENTRALIZED PIPELINE OTHER
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 103
  - country_entry_id: KGZ-WAS-18
    source_category_code: brought_in_water_truck
    national_label_en: BROUGHT-IN WATER (TRUCK)
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: KGZ-WAS-19
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: KGZ-WAS-20
    source_category_code: tanker_truck
    national_label_en: Tanker-truck
    national_label_local: "\u0414\u043E\u0441\u0442\u0430\u0432\u043B\u044F\u0435\u0442\
      \u0441\u044F \u0430\u0432\u0442\u043E\u0446\u0438\u0441\u0442\u0435\u0440\u043D\
      \u043E\u0439"
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: KGZ-WAS-21
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u0438\u0435 \u043D\u0435\u0443\
      \u043B\u0443\u0447\u0448\u0435\u043D\u043D\u044B\u0435"
    jmp_classification: Other non-improved
    jmp_id: other_non_improved
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 105
  - country_entry_id: KGZ-WAS-22
    source_category_code: other
    national_label_en: Other
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: KGZ-WAS-23
    source_category_code: other
    national_label_en: OTHER
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: KGZ-WAS-24
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0424\u0430\u0441\u043E\u0432\u0430\u043D\u043D\u0430\u044F\
      \ \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water
    jmp_id: packaged_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 89
  - country_entry_id: KGZ-WAS-25
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: "\u0411\u0443\u0442\u0438\u043B\u0438\u0440\u043E\u0432\u0430\
      \u043D\u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 90
  - country_entry_id: KGZ-WAS-26
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: "\u0412\u043E\u0434\u0430 \u0432 \u043F\u0430\u043A\u0435\
      \u0442\u0430\u0445"
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 91
  - country_entry_id: KGZ-WAS-27
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: "\u0414\u043E\u0436\u0434\u0435\u0432\u0430\u044F \u0432\
      \u043E\u0434\u0430"
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: KGZ-WAS-28
    source_category_code: rainwater
    national_label_en: RAINWATER
    national_label_local: "\u041A\u0440\u044B\u0442\u0430\u044F \u0446\u0438\u0441\
      \u0442\u0435\u0440\u043D\u0430/\u0440\u0435\u0437\u0435\u0440\u0432\u0443\u0430\
      \u0440"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: KGZ-WAS-29
    source_category_code: rainwater_collection
    national_label_en: rainwater collection
    national_label_local: "\u041A\u0440\u044B\u0442\u0430\u044F \u0446\u0438\u0441\
      \u0442\u0435\u0440\u043D\u0430/\u0440\u0435\u0437\u0435\u0440\u0432\u0443\u0430\
      \u0440"
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: KGZ-WAS-30
    source_category_code: river_lake_pond
    national_label_en: RIVER, LAKE, POND
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: KGZ-WAS-31
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: KGZ-WAS-32
    source_category_code: spring_river_lake_pond
    national_label_en: SPRING, RIVER, LAKE, POND
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: KGZ-WAS-33
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: KGZ-WAS-34
    source_category_code: surface_water_river_stream_dam_lake_etc
    national_label_en: Surface water (river, stream, dam, lake, etc.)
    national_label_local: "\u041F\u043E\u0432\u0435\u0440\u0445\u043D\u043E\u0441\u0442\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430"
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: KGZ-WAS-35
    source_category_code: pond_lake
    national_label_en: Pond/ lake
    national_label_local: "\u041F\u0440\u0443\u0434"
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 96
  - country_entry_id: KGZ-WAS-36
    source_category_code: river_stream
    national_label_en: River/ stream
    national_label_local: "\u0420\u0435\u043A\u0430"
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 93
  - country_entry_id: KGZ-WAS-37
    source_category_code: own_system_of_water_supply
    national_label_en: OWN SYSTEM OF WATER SUPPLY
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: KGZ-WAS-38
    source_category_code: piped_to_neighbour
    national_label_en: Piped to neighbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: KGZ-WAS-39
    source_category_code: piped_to_neughbour
    national_label_en: piped to neughbour
    national_label_local: "\u0414\u0440\u0443\u0433\u043E\u0435"
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 42
  - country_entry_id: KGZ-WAS-40
    source_category_code: piped_into_residence
    national_label_en: Piped into residence
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: KGZ-WAS-41
    source_category_code: running_water_in_house
    national_label_en: Running water in house
    national_label_local: "\u041F\u043E\u0434\u043A\u043B\u044E\u0447\u0435\u043D\u0438\
      \u044F \u043A \u0434\u043E\u043C\u0443"
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: KGZ-WAS-42
    source_category_code: centralized_pipeline_inside_the_house
    national_label_en: CENTRALIZED PIPELINE INSIDE THE HOUSE
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: KGZ-WAS-43
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: KGZ-WAS-44
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432 \u0436\u0438\u043B\u0438\u0449\u0435"
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: KGZ-WAS-45
    source_category_code: centralized_pipeline_in_the_yard
    national_label_en: CENTRALIZED PIPELINE IN THE YARD
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: KGZ-WAS-46
    source_category_code: piped_into_compound
    national_label_en: piped into compound
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: KGZ-WAS-47
    source_category_code: piped_into_yard_or_plot
    national_label_en: Piped into yard or plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: KGZ-WAS-48
    source_category_code: piped_to_yard_plot
    national_label_en: Piped to yard/plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: KGZ-WAS-49
    source_category_code: piped_water_to_yard_plot
    national_label_en: Piped water to yard/plot
    national_label_local: "\u0412\u043E\u0434\u043E\u043F\u0440\u043E\u0432\u043E\u0434\
      \u043D\u0430\u044F \u0432\u043E\u0434\u0430 \u043F\u043E\u0434\u0430\u0435\u0442\
      \u0441\u044F \u0432\u043E \u0434\u0432\u043E\u0440/\u043D\u0430 \u0443\u0447\
      \u0430\u0441\u0442\u043E\u043A"
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: KGZ-WAS-50
    source_category_code: centralized_pipeline_in_the_street
    national_label_en: CENTRALIZED PIPELINE IN THE STREET
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: KGZ-WAS-51
    source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: KGZ-WAS-52
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: KGZ-WAS-53
    source_category_code: public_tap_standpipe
    national_label_en: Public tap/standpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  - country_entry_id: KGZ-WAS-54
    source_category_code: public_tap_stanpipe
    national_label_en: public tap/stanpipe
    national_label_local: "\u041E\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043D\u043D\
      \u044B\u0439 \u043A\u0440\u0430\u043D, \u043A\u043E\u043B\u043E\u043D\u043A\u0430"
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_KGZ_Kyrgyzstan_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1992
  effective_to: null
  selectors: null
  value: 16
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

