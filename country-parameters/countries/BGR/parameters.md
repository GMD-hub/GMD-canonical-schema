---
country_id: CTY-BGR
iso3: BGR
schema_version: '0.2'
status: draft
country_name: BGR
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: BGR-EDU-01
    national_label_en: Pre-school education
    national_label_local: "\u041F\u0440\u0435\u0434\u0443\u0447\u0438\u043B\u0438\u0449\
      \u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435"
    entry_age: 3
    duration_years: 4
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 5
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: BGR-EDU-02
    national_label_en: Primary stage of basic education
    national_label_local: "\u041D\u0430\u0447\u0430\u043B\u0435\u043D \u0435\u0442\
      \u0430\u043F \u043D\u0430 \u043E\u0441\u043D\u043E\u0432\u043D\u043E\u0442\u043E\
      \ \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 6
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - BGR-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: BGR-EDU-03
    national_label_en: Lower secondary stage of basic education
    national_label_local: "\u041F\u0440\u043E\u0433\u0438\u043C\u043D\u0430\u0437\u0438\
      \u0430\u043B\u0435\u043D \u0435\u0442\u0430\u043F \u043D\u0430 \u043E\u0441\u043D\
      \u043E\u0432\u043D\u043E\u0442\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\
      \u0430\u043D\u0438\u0435"
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 7
    parent_country_entry_ids:
    - BGR-EDU-02
    cum_years_schooling: 7
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: BGR-EDU-04
    national_label_en: First gymnasium stage of upper secondary general and upper
      secondary special profile education
    national_label_local: "\u041F\u044A\u0440\u0432\u0438 \u0433\u0438\u043C\u043D\
      \u0430\u0437\u0438\u0430\u043B\u0435\u043D \u0435\u0442\u0430\u043F \u043D\u0430\
      \ \u0441\u0440\u0435\u0434\u043D\u043E \u043E\u0431\u0449\u043E \u0438 \u0441\
      \u0440\u0435\u0434\u043D\u043E \u043F\u0440\u043E\u0444\u0438\u043B\u0438\u0440\
      \u0430\u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\
      \u0435"
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 8
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 7
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-04
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-05
    national_label_en: First gymnasium stage of upper secondary vocational education
    national_label_local: "\u041F\u044A\u0440\u0432\u0438 \u0433\u0438\u043C\u043D\
      \u0430\u0437\u0438\u0430\u043B\u0435\u043D \u0435\u0442\u0430\u043F \u043D\u0430\
      \ \u0441\u0440\u0435\u0434\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\
      \u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\
      \u0430\u043D\u0438\u0435"
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 7
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-06
    national_label_en: Second gymnasium stage of upper secondary general and upper
      secondary special profile education
    national_label_local: "\u0412\u0442\u043E\u0440\u0438 \u0433\u0438\u043C\u043D\
      \u0430\u0437\u0438\u0430\u043B\u0435\u043D \u0435\u0442\u0430\u043F \u043D\u0430\
      \ \u0441\u0440\u0435\u0434\u043D\u043E \u043E\u0431\u0449\u043E \u0438 \u0441\
      \u0440\u0435\u0434\u043D\u043E \u043F\u0440\u043E\u0444\u0438\u043B\u0438\u0440\
      \u0430\u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\
      \u0435"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 6
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-07
    national_label_en: Second  gymnasium stage of upper secondary vocational education
    national_label_local: "\u0412\u0442\u043E\u0440\u0438 \u0433\u0438\u043C\u043D\
      \u0430\u0437\u0438\u0430\u043B\u0435\u043D \u0435\u0442\u0430\u043F \u043D\u0430\
      \ \u0441\u0440\u0435\u0434\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\
      \u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\
      \u0430\u043D\u0438\u0435"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 6
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-08
    national_label_en: General secondary education - not profiled
    national_label_local: "\u0421\u0440\u0435\u0434\u043D\u043E \u043E\u0431\u0449\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 -\
      \ \u043D\u0435\u043F\u0440\u043E\u0444\u0438\u043B\u0438\u0440\u0430\u043D\u043E"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-09
    national_label_en: General profiled secondary education
    national_label_local: "\u0421\u0440\u0435\u0434\u043D\u043E \u043E\u0431\u0449\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 -\
      \ \u043F\u0440\u043E\u0444\u0438\u043B\u0438\u0440\u0430\u043D\u043E"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-10
    national_label_en: VET programmes for second level of professional qualification
    national_label_local: "\u041F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0438 \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u0438 \u0432\u0442\
      \u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-11
    national_label_en: VET programmes for third  level of professional qualification
      after 8 Grade
    national_label_local: "\u041F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0438 \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u0438 \u0442\u0440\
      \u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0441\u043B\u0435\u0434 8\
      \ \u043A\u043B\u0430\u0441"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-12
    national_label_en: VET programmes for third level of professional qualification
      after 7 Grade
    national_label_local: "\u041F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0438 \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u0438 \u0442\u0440\
      \u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F, \u0441\u043B\u0435\u0434 7\
      \ \u043A\u043B\u0430\u0441"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-13
    national_label_en: VET programmes for first level of professional qualification
      after 7 Grade
    national_label_local: "\u041F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0438 \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u0438 \u043F\u044A\
      \u0440\u0432\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F, \u0441\u043B\u0435\u0434 7\
      \ \u043A\u043B\u0430\u0441"
    entry_age: 14
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-14
    national_label_en: "Framework programmes A1-\u04108 for initial vocational training\
      \ with obtaining of first level of professional qualification"
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04101-\u04108 \u0437\u0430 \u043D\u0430\
      \u0447\u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\
      \u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435\
      \ \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435\
      \ \u043D\u0430 \u043F\u044A\u0440\u0432\u0430 \u0441\u0442\u0435\u043F\u0435\
      \u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\
      \u0438\u044F"
    entry_age: 14
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 7
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-15
    national_label_en: Framework programme A9 for initial vocational training with
      obtaining of first level of professional qualification for pupils under additional
      state admission plan  learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 A9 \u0437\u0430 \u043D\u0430\u0447\u0430\
      \u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0441 \u043F\
      \u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u043F\
      \u044A\u0440\u0432\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\
      \u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\
      \u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0437\u0430\
      \ \u0443\u0447\u0435\u043D\u0438\u0446\u0438 \u043F\u043E \u0434\u043E\u043F\
      \u044A\u043B\u043D\u0438\u0442\u0435\u043B\u0435\u043D \u0434\u044A\u0440\u0436\
      \u0430\u0432\u0435\u043D \u043F\u043B\u0430\u043D-\u043F\u0440\u0438\u0435\u043C\
      \ \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\u0437\
      \ \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-16
    national_label_en: Framework programme A10 for initial vocational training with
      obtaining of first level of professional qualification for persons older than
      16 years
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 A10 \u0437\u0430 \u043D\u0430\u0447\u0430\
      \u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0441 \u043F\
      \u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u043F\
      \u044A\u0440\u0432\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\
      \u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\
      \u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0437\u0430\
      \ \u043B\u0438\u0446\u0430, \u043D\u0430\u0432\u044A\u0440\u0448\u0438\u043B\
      \u0438 16 \u0433\u043E\u0434\u0438\u043D\u0438"
    entry_age: 0
    duration_years: 0
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - BGR-EDU-02
    cum_years_schooling: 4
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: BGR-EDU-17
    national_label_en: Framework programme B1-B3 and B7-B8 for initial vocational
      training with obtaining of second level of professional qualification
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04111-\u04113 \u0438 \u04117-\u04118\
      \ \u0437\u0430 \u043D\u0430\u0447\u0430\u043B\u043D\u043E \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\
      \u0447\u0435\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\
      \u0432\u0430\u043D\u0435 \u043D\u0430 \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\
      \u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\
      \u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\
      \u043A\u0430\u0446\u0438\u044F"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-18
    national_label_en: Framework programme B4-B6 for initial vocational training with
      obtaining of second level of professional qualification learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04114-\u04116 \u0437\u0430 \u043D\u0430\
      \u0447\u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\
      \u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435\
      \ \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435\
      \ \u043D\u0430 \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\
      \u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\
      \u0438\u044F \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\
      \u0437 \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 14
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 8
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-19
    national_label_en: Framework programmes B9-B11 for continuing vocational training
      with obtaining second level of professional qualification for students under
      additional state admission plan
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04119-\u041111 \u0437\u0430 \u043F\u0440\
      \u043E\u0434\u044A\u043B\u0436\u0430\u0432\u0430\u0449\u043E \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\
      \u0447\u0435\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\
      \u0432\u0430\u043D\u0435 \u043D\u0430 \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\
      \u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\
      \u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\
      \u043A\u0430\u0446\u0438\u044F \u0437\u0430 \u0443\u0447\u0435\u043D\u0438\u0446\
      \u0438 \u043F\u043E \u0434\u043E\u043F\u044A\u043B\u043D\u0438\u0442\u0435\u043B\
      \u0435\u043D \u0434\u044A\u0440\u0436\u0430\u0432\u0435\u043D \u043F\u043B\u0430\
      \u043D-\u043F\u0440\u0438\u0435\u043C"
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-20
    national_label_en: Framework programme B12 for continuing vocational training
      with obtaining second level of professional qualification for students under
      additional admission plan learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041112 \u0437\u0430 \u043F\u0440\u043E\
      \u0434\u044A\u043B\u0436\u0430\u0432\u0430\u0449\u043E \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\
      \u0435\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\
      \u0430\u043D\u0435 \u043D\u0430 \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\
      \u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\
      \u0430\u0446\u0438\u044F \u0437\u0430 \u0443\u0447\u0435\u043D\u0438\u0446\u0438\
      \ \u043F\u043E \u0434\u043E\u043F\u044A\u043B\u043D\u0438\u0442\u0435\u043B\u0435\
      \u043D \u0434\u044A\u0440\u0436\u0430\u0432\u0435\u043D \u043F\u043B\u0430\u043D\
      -\u043F\u0440\u0438\u0435\u043C \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435\
      \ \u0447\u0440\u0435\u0437 \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-21
    national_label_en: Framework programmes B13-B14 for initial vocational training
      with obtaining second level of professional qualification for persons older
      than 16 years
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u041113-\u041114 \u0437\u0430 \u043D\u0430\
      \u0447\u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\
      \u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435\
      \ \u0437\u0430 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435\
      \ \u043D\u0430 \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\
      \u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\
      \u0438\u044F \u0437\u0430 \u043B\u0438\u0446\u0430, \u043D\u0430\u0432\u044A\
      \u0440\u0448\u0438\u043B\u0438 16 \u0433\u043E\u0434\u0438\u043D\u0438"
    entry_age: 0
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-22
    national_label_en: Framework programme B15 for initial vocational training with
      obtaining second level of professional qualification for persons older than
      16 years learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041115 \u0437\u0430 \u043D\u0430\u0447\
      \u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\
      \u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u0437\u0430 \u043B\u0438\u0446\u0430, \u043D\u0430\u0432\u044A\u0440\u0448\
      \u0438\u043B\u0438 16 \u0433\u043E\u0434\u0438\u043D\u0438 \u043E\u0431\u0443\
      \u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\u0437 \u0440\u0430\u0431\u043E\
      \u0442\u0430"
    entry_age: 0
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-23
    national_label_en: Framework programmes B16-B17 for initial vocational training
      with obtaining third level of professional qualification for persons older than
      16 years
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u041116-\u041117 \u0437\u0430 \u043D\u0430\
      \u0447\u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\
      \u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435\
      \ \u0437\u0430 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435\
      \ \u043D\u0430 \u0442\u0440\u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\
      \u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\
      \u0438\u044F \u0437\u0430 \u043B\u0438\u0446\u0430, \u043D\u0430\u0432\u044A\
      \u0440\u0448\u0438\u043B\u0438 16 \u0433\u043E\u0434\u0438\u043D\u0438"
    entry_age: 0
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-24
    national_label_en: Framework programme B18 for initial vocational training with
      obtaining third level of professional qualification for persons older than 16
      years learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041118 \u0437\u0430 \u043D\u0430\u0447\
      \u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\
      \u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0442\u0440\u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u0437\u0430 \u043B\u0438\u0446\u0430, \u043D\u0430\u0432\u044A\u0440\u0448\
      \u0438\u043B\u0438 16 \u0433\u043E\u0434\u0438\u043D\u0438 \u043E\u0431\u0443\
      \u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\u0437 \u0440\u0430\u0431\u043E\
      \u0442\u0430"
    entry_age: 0
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-25
    national_label_en: Framework programmes V1-V6, V16 and V18 for vocational education
      with obtaining of second level of professional qualification
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04121-\u04126, \u041216 \u0438 \u0412\
      18 \u0437\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\
      \u0435 \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435\
      \ \u043D\u0430 \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\
      \u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\
      \u0438\u044F"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 29
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-26
    national_label_en: Framework programmes V7-V9 for vocational education with obtaining
      of third level of professional qualification in art schools/ sport schools/
      spiritual schools
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04127-\u04129 \u0437\u0430 \u043F\u0440\
      \u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\
      \u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\
      \u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u0442\u0440\u0435\
      \u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\
      \u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0432 \u0443\u0447\u0438\
      \u043B\u0438\u0449\u0430 \u043F\u043E \u0438\u0437\u043A\u0443\u0441\u0442\u0432\
      \u0430\u0442\u0430/ \u0441\u043F\u043E\u0440\u0442\u043D\u0438\u0442\u0435 \u0443\
      \u0447\u0438\u043B\u0438\u0449\u0430/ \u0434\u0443\u0445\u043E\u0432\u043D\u0438\
      \u0442\u0435 \u0443\u0447\u0438\u043B\u0438\u0449\u0430"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 30
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-27
    national_label_en: Framework programmes V10, V12 and V14 for vocational education
      with obtaining of second level of professional qualification learning through
      work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u041210, \u041212 \u0438 \u041214 \u0437\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\u0437\
      \ \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 31
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-28
    national_label_en: Framework programme V11, V13 and V15 for vocational education
      with obtaining of third level of professional qualification learning through
      work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u041211, \u041213 \u0438 \u041215 \u0437\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0442\u0440\u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\u0437\
      \ \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 32
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-29
    national_label_en: Framework programme V17 and V19 for vocational education with
      obtaining of third level of professional qualification
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041217 \u0438 \u041219 \u0437\u0430 \u043F\
      \u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\
      \u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441 \u043F\u0440\
      \u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u0442\u0440\
      \u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\
      \u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\
      \u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F"
    entry_age: 14
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 33
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-30
    national_label_en: Framework programme V20, V24 and V26 for vocational education
      with obtaining second level of professional qualification for students under
      additional state admission plan
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041220, \u041224 \u0438 \u041226 \u0437\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u0437\u0430 \u0443\u0447\u0435\u043D\u0438\u0446\u0438 \u043F\u043E \u0434\
      \u043E\u043F\u044A\u043B\u043D\u0438\u0442\u0435\u043B\u0435\u043D \u0434\u044A\
      \u0440\u0436\u0430\u0432\u0435\u043D \u043F\u043B\u0430\u043D-\u043F\u0440\u0438\
      \u0435\u043C"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 34
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 6
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-31
    national_label_en: Framework programme V21, V25 and V27 for vocational education
      with obtaining third level of professional qualification
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041221, \u041225 \u0438 \u041227 \u0437\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0442\u0440\u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 35
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 6
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-32
    national_label_en: Framework programme V22 for vocational education with obtaining
      second level of professional qualification for students in additional state
      admission plan learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041222 \u0437\u0430 \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0440\
      \u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\
      \u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u0432\u0442\u043E\u0440\
      \u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0437\u0430 \u0443\u0447\u0435\
      \u043D\u0438\u0446\u0438 \u043F\u043E \u0434\u043E\u043F\u044A\u043B\u043D\u0438\
      \u0442\u0435\u043B\u0435\u043D \u0434\u044A\u0440\u0436\u0430\u0432\u0435\u043D\
      \ \u043F\u043B\u0430\u043D-\u043F\u0440\u0438\u0435\u043C \u043E\u0431\u0443\
      \u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\u0437 \u0440\u0430\u0431\u043E\
      \u0442\u0430"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 36
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 6
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-33
    national_label_en: Framework programme V23 for vocational education with obtaining
      third level of professional qualification learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041223 \u0437\u0430 \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0440\
      \u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\
      \u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u0442\u0440\u0435\u0442\
      \u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u043E\u0431\u0443\u0447\u0435\
      \u043D\u0438\u0435 \u0447\u0440\u0435\u0437 \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 37
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 6
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-34
    national_label_en: Framework programmes V28, V32 and V34 for vocational education
      with obtaining second level of professional qualification for students
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041228, \u041232 \u0438 \u041234 \u0437\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0432\u0442\u043E\u0440\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u0437\u0430 \u0443\u0447\u0435\u043D\u0438\u0446\u0438"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 38
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-35
    national_label_en: Framework programmes V29, V33 and V35 for vocational education
      with obtaining third level of professional qualification for students
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041229, \u041233 \u0438 \u041235 \u0437\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0442\u0440\u0435\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\
      \u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\
      \u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F\
      \ \u0437\u0430 \u0443\u0447\u0435\u043D\u0438\u0446\u0438"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 39
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-36
    national_label_en: Framework programme V30 for vocational education with obtaining
      second level of professional qualification for students, learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041230 \u0437\u0430 \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0440\
      \u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\
      \u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u0432\u0442\u043E\u0440\
      \u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0437\u0430 \u0443\u0447\u0435\
      \u043D\u0438\u0446\u0438, \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\
      \u0440\u0435\u0437 \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 40
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-37
    national_label_en: Framework programme V31 for vocational education with obtaining
      third level of professional qualification for students, learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u041231 \u0437\u0430 \u043F\u0440\u043E\
      \u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0440\
      \u0430\u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\
      \u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430 \u0442\u0440\u0435\u0442\
      \u0430 \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F \u0437\u0430 \u0443\u0447\u0435\
      \u043D\u0438\u0446\u0438, \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\
      \u0440\u0435\u0437 \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 41
    parent_country_entry_ids:
    - BGR-EDU-03
    - BGR-EDU-16
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
  - country_entry_id: BGR-EDU-38
    national_label_en: Framework programme G1-G3 for initial vocational training with
      obtaining fourth level of professional qualification
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0438 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0438 \u04131-\u04133 \u0437\u0430 \u043D\u0430\
      \u0447\u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\
      \u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435\
      \ \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435\
      \ \u043D\u0430 \u0447\u0435\u0442\u0432\u044A\u0440\u0442\u0430 \u0441\u0442\
      \u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\
      \u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\
      \u043A\u0430\u0446\u0438\u044F"
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - BGR-EDU-04
    - BGR-EDU-06
    - BGR-EDU-08
    - BGR-EDU-09
    - BGR-EDU-10
    - BGR-EDU-11
    - BGR-EDU-12
    - BGR-EDU-13
    cum_years_schooling: 7
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
  - country_entry_id: BGR-EDU-39
    national_label_en: Framework programmes G4 for initial vocational training with
      obtaining fourth level of professional qualification learning through work
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u04134 \u0437\u0430 \u043D\u0430\u0447\
      \u0430\u043B\u043D\u043E \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\
      \u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0441\
      \ \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\u0430\u043D\u0435 \u043D\u0430\
      \ \u0447\u0435\u0442\u0432\u044A\u0440\u0442\u0430 \u0441\u0442\u0435\u043F\u0435\
      \u043D \u043D\u0430 \u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\
      \u043B\u043D\u0430 \u043A\u0432\u0430\u043B\u0438\u0444\u0438\u043A\u0430\u0446\
      \u0438\u044F \u043E\u0431\u0443\u0447\u0435\u043D\u0438\u0435 \u0447\u0440\u0435\
      \u0437 \u0440\u0430\u0431\u043E\u0442\u0430"
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - BGR-EDU-04
    - BGR-EDU-06
    - BGR-EDU-08
    - BGR-EDU-09
    - BGR-EDU-10
    - BGR-EDU-11
    - BGR-EDU-12
    - BGR-EDU-13
    cum_years_schooling: 7
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
  - country_entry_id: BGR-EDU-40
    national_label_en: Framework programme G5 for continuing vocational training with
      obtaining fourth level of professional qualification
    national_label_local: "\u0420\u0430\u043C\u043A\u043E\u0432\u0430 \u043F\u0440\
      \u043E\u0433\u0440\u0430\u043C\u0430 \u04135 \u0437\u0430 \u043F\u0440\u043E\
      \u0434\u044A\u043B\u0436\u0430\u0432\u0430\u0449\u043E \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u043E \u043E\u0431\u0443\u0447\
      \u0435\u043D\u0438\u0435 \u0441 \u043F\u0440\u0438\u0434\u043E\u0431\u0438\u0432\
      \u0430\u043D\u0435 \u043D\u0430 \u0447\u0435\u0442\u0432\u044A\u0440\u0442\u0430\
      \ \u0441\u0442\u0435\u043F\u0435\u043D \u043D\u0430 \u043F\u0440\u043E\u0444\
      \u0435\u0441\u0438\u043E\u043D\u0430\u043B\u043D\u0430 \u043A\u0432\u0430\u043B\
      \u0438\u0444\u0438\u043A\u0430\u0446\u0438\u044F"
    entry_age: 0
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 44
    parent_country_entry_ids:
    - BGR-EDU-04
    - BGR-EDU-06
    - BGR-EDU-08
    - BGR-EDU-09
    - BGR-EDU-10
    - BGR-EDU-11
    - BGR-EDU-12
    - BGR-EDU-13
    cum_years_schooling: 5
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-40
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
  - country_entry_id: BGR-EDU-41
    national_label_en: "Tertiary education \u2013 Professional Bachelor's educational\
      \ and qualification degree"
    national_label_local: "\u0412\u0438\u0441\u0448\u0435 \u043E\u0431\u0440\u0430\
      \u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u2013 \u043E\u0431\u0440\u0430\u0437\
      \u043E\u0432\u0430\u0442\u0435\u043B\u043D\u043E-\u043A\u0432\u0430\u043B\u0438\
      \u0444\u0438\u043A\u0430\u0446\u0438\u043E\u043D\u043D\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u201E\u043F\u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\
      \u0430\u043B\u0435\u043D \u0431\u0430\u043A\u0430\u043B\u0430\u0432\u044A\u0440\
      \u201C"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 45
    parent_country_entry_ids:
    - BGR-EDU-04
    - BGR-EDU-06
    - BGR-EDU-08
    - BGR-EDU-09
    - BGR-EDU-10
    - BGR-EDU-11
    - BGR-EDU-12
    - BGR-EDU-13
    cum_years_schooling: 8
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-41
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
  - country_entry_id: BGR-EDU-42
    national_label_en: "Tertiary education \u2013 Bachelor's educational and qualification\
      \ degree"
    national_label_local: "\u0412\u0438\u0441\u0448\u0435 \u043E\u0431\u0440\u0430\
      \u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u2013 \u043E\u0431\u0440\u0430\u0437\
      \u043E\u0432\u0430\u0442\u0435\u043B\u043D\u043E-\u043A\u0432\u0430\u043B\u0438\
      \u0444\u0438\u043A\u0430\u0446\u0438\u043E\u043D\u043D\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u201E\u0431\u0430\u043A\u0430\u043B\u0430\u0432\u044A\u0440\
      \u201C"
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 46
    parent_country_entry_ids:
    - BGR-EDU-04
    - BGR-EDU-06
    - BGR-EDU-08
    - BGR-EDU-09
    - BGR-EDU-10
    - BGR-EDU-11
    - BGR-EDU-12
    - BGR-EDU-13
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-42
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
  - country_entry_id: BGR-EDU-43
    national_label_en: "Tertiary education \u2013 Master's educational and qualification\
      \ degree after completed secondary education"
    national_label_local: "\u0412\u0438\u0441\u0448\u0435 \u043E\u0431\u0440\u0430\
      \u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u2013 \u043E\u0431\u0440\u0430\u0437\
      \u043E\u0432\u0430\u0442\u0435\u043B\u043D\u043E-\u043A\u0432\u0430\u043B\u0438\
      \u0444\u0438\u043A\u0430\u0446\u0438\u043E\u043D\u043D\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u201E\u043C\u0430\u0433\u0438\u0441\u0442\u044A\u0440\u201C\
      \ \u0441\u043B\u0435\u0434 \u0437\u0430\u0432\u044A\u0440\u0448\u0435\u043D\u043E\
      \ \u0441\u0440\u0435\u0434\u043D\u043E \u043E\u0431\u0440\u0430\u0437\u043E\u0432\
      \u0430\u043D\u0438\u0435"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 47
    parent_country_entry_ids:
    - BGR-EDU-41
    - BGR-EDU-42
    cum_years_schooling: 13
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-41
    - BGR-EDU-43
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
    - 'minimum parent path selected from: BGR-EDU-41, BGR-EDU-42'
  - country_entry_id: BGR-EDU-44
    national_label_en: "Tertiary education \u2013 Master's educational and qualification\
      \ degree after a Bachelor degree"
    national_label_local: "\u0412\u0438\u0441\u0448\u0435 \u043E\u0431\u0440\u0430\
      \u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u2013 \u043E\u0431\u0440\u0430\u0437\
      \u043E\u0432\u0430\u0442\u0435\u043B\u043D\u043E-\u043A\u0432\u0430\u043B\u0438\
      \u0444\u0438\u043A\u0430\u0446\u0438\u043E\u043D\u043D\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u201E\u043C\u0430\u0433\u0438\u0441\u0442\u044A\u0440\u201C\
      \ \u0441\u043B\u0435\u0434 \u0441\u0442\u0435\u043F\u0435\u043D \u201E\u0431\
      \u0430\u043A\u0430\u043B\u0430\u0432\u044A\u0440\u201C"
    entry_age: 23
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 48
    parent_country_entry_ids:
    - BGR-EDU-41
    - BGR-EDU-42
    cum_years_schooling: 9
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-41
    - BGR-EDU-44
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
    - 'minimum parent path selected from: BGR-EDU-41, BGR-EDU-42'
  - country_entry_id: BGR-EDU-45
    national_label_en: "Tertiary education \u2013 Master's educational and qualification\
      \ degree after a Professional Bachelor degree"
    national_label_local: "\u0412\u0438\u0441\u0448\u0435 \u043E\u0431\u0440\u0430\
      \u0437\u043E\u0432\u0430\u043D\u0438\u0435 \u2013 \u043E\u0431\u0440\u0430\u0437\
      \u043E\u0432\u0430\u0442\u0435\u043B\u043D\u043E-\u043A\u0432\u0430\u043B\u0438\
      \u0444\u0438\u043A\u0430\u0446\u0438\u043E\u043D\u043D\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u201E\u043C\u0430\u0433\u0438\u0441\u0442\u044A\u0440\u201C\
      \ \u0441\u043B\u0435\u0434 \u0441\u0442\u0435\u043F\u0435\u043D \u201E\u043F\
      \u0440\u043E\u0444\u0435\u0441\u0438\u043E\u043D\u0430\u043B\u0435\u043D \u0431\
      \u0430\u043A\u0430\u043B\u0430\u0432\u044A\u0440\u201C"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 49
    parent_country_entry_ids:
    - BGR-EDU-41
    - BGR-EDU-42
    cum_years_schooling: 10
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-41
    - BGR-EDU-45
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
    - 'minimum parent path selected from: BGR-EDU-41, BGR-EDU-42'
  - country_entry_id: BGR-EDU-46
    national_label_en: Doctor's educational and scientific degree (PhD)
    national_label_local: "\u041E\u0431\u0440\u0430\u0437\u043E\u0432\u0430\u0442\u0435\
      \u043B\u043D\u0430 \u0438 \u043D\u0430\u0443\u0447\u043D\u0430 \u0441\u0442\u0435\
      \u043F\u0435\u043D \u201E\u0434\u043E\u043A\u0442\u043E\u0440\u201C"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 50
    parent_country_entry_ids:
    - BGR-EDU-43
    - BGR-EDU-44
    - BGR-EDU-45
    cum_years_schooling: 12
    cum_years_computation_path:
    - BGR-EDU-02
    - BGR-EDU-16
    - BGR-EDU-13
    - BGR-EDU-41
    - BGR-EDU-44
    - BGR-EDU-46
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: BGR-EDU-03, BGR-EDU-16'
    - 'minimum parent path selected from: BGR-EDU-04, BGR-EDU-06, BGR-EDU-08, BGR-EDU-09,
      BGR-EDU-10, BGR-EDU-11, BGR-EDU-12, BGR-EDU-13'
    - 'minimum parent path selected from: BGR-EDU-41, BGR-EDU-42'
    - 'minimum parent path selected from: BGR-EDU-43, BGR-EDU-44, BGR-EDU-45'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Bulgaria.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: BGR-SUBNAT-01
    survey_labels: 1-BG3
    survey_variables: subnatid
    gmd_subnatid1: BGR_2021_NUTS1_BG3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: BGR_2021_NUTS1_BG3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: BG3
    geo_nvar: NAME_LATN
    geo_name: Severna i Yugoiztochna Bulgaria
    source_row: 822
  - country_entry_id: BGR-SUBNAT-02
    survey_labels: 2-BG4
    survey_variables: subnatid
    gmd_subnatid1: BGR_2021_NUTS1_BG4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: BGR_2021_NUTS1_BG4
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: BG4
    geo_nvar: NAME_LATN
    geo_name: Yugozapadna i Yuzhna tsentralna Bulgaria
    source_row: 823
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
  - country_entry_id: BGR-SAN-01
    source_category_code: toilet
    national_label_en: Toilet
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 66
  - country_entry_id: BGR-SAN-02
    source_category_code: flush_toilet
    national_label_en: Flush toilet
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: BGR-SAN-03
    source_category_code: public_sewerage
    national_label_en: Public sewerage
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: BGR-SAN-04
    source_category_code: toilet
    national_label_en: Toilet
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 67
  - country_entry_id: BGR-SAN-05
    source_category_code: septic_tank
    national_label_en: Septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 68
  - country_entry_id: BGR-SAN-06
    source_category_code: cesspit
    national_label_en: Cesspit
    national_label_local: to pit
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 88
  - country_entry_id: BGR-SAN-07
    source_category_code: pit_latrine
    national_label_en: Pit latrine
    national_label_local: to pit
    jmp_classification: Latrines > Pour flush latrines > to pit
    jmp_id: latrines.pour_flush_latrines.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 88
  - country_entry_id: BGR-SAN-08
    source_category_code: no_toilet
    national_label_en: No, toilet
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: BGR-SAN-09
    source_category_code: other_sw_type
    national_label_en: Other SW type
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 132
  - country_entry_id: BGR-SAN-10
    source_category_code: no_toilet
    national_label_en: no toilet
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: BGR-SAN-11
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: BGR-SAN-12
    source_category_code: unknown
    national_label_en: Unknown
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_BGR_Bulgaria_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: BGR-WAS-01
    source_category_code: own_sistem_pump_well
    national_label_en: Own sistem / pump /well
    national_label_local: All wells
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: BGR-WAS-02
    source_category_code: own_system_pump_well
    national_label_en: Own system/pump/well
    national_label_local: All wells
    jmp_classification: Ground water > All wells
    jmp_id: ground_water.all_wells
    gmd_target: ''
    gmd_spans: borehole|protected_well|unprotected_well
    improved_flag: false
    shared_flag: false
    source_row: 54
  - country_entry_id: BGR-WAS-03
    source_category_code: unknown_source
    national_label_en: Unknown source
    national_label_local: Other non-improved
    jmp_classification: Other non-improved
    jmp_id: other_non_improved
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 105
  - country_entry_id: BGR-WAS-04
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: BGR-WAS-05
    source_category_code: other_no_water_supply_system
    national_label_en: Other/no water supply system
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: BGR-WAS-06
    source_category_code: river
    national_label_en: River
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: BGR-WAS-07
    source_category_code: piped_public
    national_label_en: Piped public
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: BGR-WAS-08
    source_category_code: piped_public_inside_dwelling
    national_label_en: Piped public, Inside dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: BGR-WAS-09
    source_category_code: water_supply_system
    national_label_en: Water supply system
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: BGR-WAS-10
    source_category_code: piped_public_inside_building
    national_label_en: Piped public, Inside building
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 40
  - country_entry_id: BGR-WAS-11
    source_category_code: piped_public_outside_building
    national_label_en: Piped public, Outside building
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_BGR_Bulgaria_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1990
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

