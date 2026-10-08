---
country_id: CTY-JPN
iso3: JPN
schema_version: '0.2'
status: draft
country_name: JPN
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: JPN-EDU-01
    national_label_en: Integrated centre for early childhood education and care
    national_label_local: Yohorenkeigata-Nintei-Kodomo-En
    entry_age: 3
    duration_years: 1
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
  - country_entry_id: JPN-EDU-02
    national_label_en: Kindergarten
    national_label_local: Yochien
    entry_age: 3
    duration_years: 1
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 6
    parent_country_entry_ids: []
    cum_years_schooling: 0
    cum_years_computation_path: []
    cum_years_status: computed
    review_flags:
    - ISCED 0 excluded from school-year total
  - country_entry_id: JPN-EDU-03
    national_label_en: Kindergarten Department of Special Needs Education School
    national_label_local: Tokubetsu-shien-gakko Yochi-bu
    entry_age: 3
    duration_years: 1
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
  - country_entry_id: JPN-EDU-04
    national_label_en: Day care centre
    national_label_local: Hoikusho
    entry_age: 3
    duration_years: 1
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
  - country_entry_id: JPN-EDU-05
    national_label_en: Elementary school
    national_label_local: Shogakko
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - JPN-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: JPN-EDU-06
    national_label_en: Compulsory Education School
    national_label_local: Gimu-kyoiku-gakko (Zenki-katei)
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - JPN-EDU-06
    cum_years_status: computed
    review_flags: []
  - country_entry_id: JPN-EDU-07
    national_label_en: Elementary Department of Special Needs Education School
    national_label_local: Tokubetsu-shien-gakko Shogaku-bu
    entry_age: 6
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 11
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - JPN-EDU-07
    cum_years_status: computed
    review_flags: []
  - country_entry_id: JPN-EDU-08
    national_label_en: Lower secondary school
    national_label_local: Chugakko
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - JPN-EDU-05
    - JPN-EDU-06
    - JPN-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
  - country_entry_id: JPN-EDU-09
    national_label_en: Compulsory Education School
    national_label_local: Gimu-kyoiku-gakko (Koki-katei)
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - JPN-EDU-05
    - JPN-EDU-06
    - JPN-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
  - country_entry_id: JPN-EDU-10
    national_label_en: Secondary education school (lower division)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Zenki-katei\uFF09"
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - JPN-EDU-05
    - JPN-EDU-06
    - JPN-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
  - country_entry_id: JPN-EDU-11
    national_label_en: Lower secondary department of special needs education school
    national_label_local: Tokubetsu-shien-gakko Chugaku-bu
    entry_age: 12
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - JPN-EDU-05
    - JPN-EDU-06
    - JPN-EDU-07
    cum_years_schooling: 9
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
  - country_entry_id: JPN-EDU-12
    national_label_en: Upper secondary school, (full day school), short-term course
      (general)
    national_label_local: "Koto-gakko Zennichisei Bekka\u3000(Futsu)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-13
    national_label_en: Upper secondary school, (day/evening school), short-term course
      (general)
    national_label_local: "Koto-gakko Teijisei Bekka\u3000(Futsu)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-14
    national_label_en: Upper secondary school, (full day school), short-term course
      (integrated)
    national_label_local: "Koto-gakko Zennichisei Bekka\u3000(Sogo)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-15
    national_label_en: Upper secondary school, (day/evening school), short-term course
      (integrated)
    national_label_local: "Koto-gakko Teijisei Bekka\u3000(Sogo)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-16
    national_label_en: Secondary education school (upper division), full day short-term
      course (general)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Zennichisei Bekka\
      \ (Futsu)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-17
    national_label_en: Secondary education school (upper division), day/evening short-term
      course (general)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei) Teijisei Bekka (Futsu)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-18
    national_label_en: Secondary education school (upper division), full day short-term
      course (integrated)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Zennichisei Bekka\
      \ (Sogo)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-19
    national_label_en: "Secondary education school (upper division), \nday/evening\
      \ course  (integrated)"
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09\nTeijisei Bekka\
      \ (Sogo)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-20
    national_label_en: Upper Secondary Department of  Special Needs Education School,
      Short-term Course (general)
    national_label_local: "Tokubetsu-shien-gakko Koto-bu\u3000Bekka (Futsu)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-21
    national_label_en: Upper secondary school, (full day school), short-term course
      (specialized)
    national_label_local: "Koto-gakko Zennichisei Bekka\u3000(Senmon)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-22
    national_label_en: Upper secondary school, (day/evening school), short-term course
      (specialized)
    national_label_local: "Koto-gakko Teijisei Bekka\u3000(Senmon)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-23
    national_label_en: Secondary education school (upper division), full day short-term
      course (specialized)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Zennichisei  Bekka\
      \ (Senmon)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-24
    national_label_en: Secondary education school (upper division), day/evening short-term
      course (specialized)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09 Teijisei Bekka\
      \ (Senmon)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-25
    national_label_en: Upper Secondary Department of  Special Needs Education School,
      Short-term Course (specialized)
    national_label_local: "Tokubetsu-shien-gakko Koto-bu\u3000Bekka (Senmon)"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 29
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-26
    national_label_en: Upper secondary school, full day general course
    national_label_local: Koto-gakko Zennichisei Honka Futsu
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 30
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-27
    national_label_en: Upper secondary school, day/evening general course
    national_label_local: Koto-gakko Teijisei Honka Futsu
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 31
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-28
    national_label_en: Upper secondary school, correspondence general course
    national_label_local: Koto-gakko Tsushinsei Futsu
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 32
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-29
    national_label_en: Upper secondary school, full day integrated course
    national_label_local: Koto-gakko Zennichisei Honka Sogo
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 33
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-30
    national_label_en: Upper secondary school, day/evening integrated course
    national_label_local: Koto-gakko Teijisei Honka Sogo
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 34
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-31
    national_label_en: Secondary education school (upper division), full day general
      course
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Zennichisei Honka\
      \ Futsu"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 35
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-32
    national_label_en: Secondary education school (upper division), day/evening general
      course
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Teijisei Honka\
      \ Futsu"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 36
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-33
    national_label_en: Secondary education school (upper division), full day integrated
      course
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Zennichisei Honka\
      \ Sogo"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 37
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-34
    national_label_en: Secondary education school (upper division), day/evening integrated
      course
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Teijisei Honka\
      \ Sogo"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 38
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-35
    national_label_en: Upper Secondary Department of  Special Needs Education School,
      general course
    national_label_local: Tokubetsu-shien-gakko Koto-bu Honka Futsu
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 39
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-36
    national_label_en: Specialized Training College, Upper Secondary Course (Upper
      Secondary Specialized Training School)
    national_label_local: "Senshu-gakko Koto-katei\uFF08Koto-senshu-gakko\uFF09"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 40
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-37
    national_label_en: Upper secondary school, full day specialized course
    national_label_local: Koto-gakko Zennichisei  Honka Senmon
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 41
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-38
    national_label_en: Upper secondary school, day/evening specialized course
    national_label_local: Koto-gakko Teijisei Honka Senmon
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 42
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-39
    national_label_en: Upper secondary school, correspondence specialized course
    national_label_local: Koto-gakko Tsushinsei Senmon
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 43
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-40
    national_label_en: Secondary education school (upper division),full day specialized
      course
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Zennichisei Honka\
      \ Senmon"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 44
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-40
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-41
    national_label_en: Secondary education school (upper division), day/evening specialized
      course
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki-katei\uFF09Teijisei Honka\
      \ Senmon"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 45
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-41
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-42
    national_label_en: Upper Secondary Department of Special Needs Education School,
      specialized course
    national_label_local: Tokubetsu-shien-gakko Koto-bu Honka Senmon
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 46
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-42
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-43
    national_label_en: "College of technology, regular course \n1st to 3rd Grade"
    national_label_local: Koto-senmon-gakko Honka
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 47
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-43
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-44
    national_label_en: Specialized Training College, Upper Secondary Course (Upper
      Secondary Specialized Training School)
    national_label_local: "Senshu-gakko Koto-katei\uFF08Koto-senshu-gakko\uFF09"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 48
    parent_country_entry_ids:
    - JPN-EDU-08
    - JPN-EDU-09
    - JPN-EDU-10
    - JPN-EDU-11
    cum_years_schooling: 10
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-44
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
  - country_entry_id: JPN-EDU-45
    national_label_en: Upper secondary school, full day, advanced course (general)
    national_label_local: "Koto-gakko Zennichisei\u3000Senkoka (Futsu)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 49
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-45
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-46
    national_label_en: Upper secondary school, day/evening, advanced course (general)
    national_label_local: "Koto-gakko Teijisei\u3000Senkoka (Futsu)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 50
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-46
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-47
    national_label_en: Upper secondary school, full day,advanced course (integrated)
    national_label_local: "Koto-gakko Zennichisei\u3000Senkoka (Sogo)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 51
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-47
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-48
    national_label_en: Upper secondary school, day/evening, advanced course (integrated)
    national_label_local: "Koto-gakko Teijisei\u3000Senkoka (Sogo)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 52
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-48
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-49
    national_label_en: Secondary education school (upper division), full day, advanced
      course (general)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki katei\uFF09Zennichisei Senkoka\
      \ (Futsu)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 53
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-49
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-50
    national_label_en: Secondary education school (upper division), day/evening, advanced
      course (general)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki katei\uFF09\u3000Teijisei\
      \ Senkoka (Futsu)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 54
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-50
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-51
    national_label_en: Secondary education school (upper division), full day, advanced
      course (integrated)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki katei\uFF09Zennichisei Senkoka\
      \ (Sogo)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 55
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-51
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-52
    national_label_en: Secondary education school (upper division), day/evening, advanced
      course (integrated)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki katei\uFF09Teijisei Senkoka\
      \ (Sogo)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 56
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-52
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-53
    national_label_en: Upper Secondary Department of  Special Needs Education School,
      Advanced Course (general)
    national_label_local: "Tokubetsu-shien-gakko Koto-bu\u3000Senkoka (Futsu)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 57
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-53
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-54
    national_label_en: Upper secondary school, full day, advanced course (specialized)
    national_label_local: "Koto-gakko Zennichisei\u3000Senkoka (Senmon)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 58
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-54
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-55
    national_label_en: Upper secondary school, day/evening, advanced course (specialized)
    national_label_local: "Koto-gakko Teijisei\u3000Senkoka (Senmon)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 59
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-55
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-56
    national_label_en: Secondary education school (upper division), full day, advanced
      course (specialized)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki katei\uFF09Zennichisei Senkoka\
      \ (Senmon)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 60
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-56
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-57
    national_label_en: Secondary education school (upper division), day/evening, advanced
      course (specialized)
    national_label_local: "Chuto-kyoiku-gakko \uFF08Koki katei\uFF09Teijisei Senkoka\
      \ (Senmon)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 61
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-57
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-58
    national_label_en: Upper Secondary Department of  Special Needs Education School,
      Advanced Course (specialized)
    national_label_local: "Tokubetsu-shien-gakko Koto-bu\u3000Senkoka (Senmon)"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 62
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-58
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-59
    national_label_en: Junior college, short-term course
    national_label_local: Tanki-daigaku Bekka
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 63
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-59
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-60
    national_label_en: University, short-term course
    national_label_local: Daigaku Gakubu Bekka
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 64
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-60
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-61
    national_label_en: Junior college, regular course
    national_label_local: Tanki-daigaku Honka
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 65
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-61
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-62
    national_label_en: Junior college, advanced course
    national_label_local: Tanki-daigaku Senkoka
    entry_age: 20
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 66
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-62
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-63
    national_label_en: Junior college, correspondence course
    national_label_local: Tanki-daigaku Tsushinsei
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 67
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-63
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-64
    national_label_en: Professional and vocational junior college, regular course
    national_label_local: Senmonshoku-tanki-daigaku Honka
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 68
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-64
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-65
    national_label_en: Professional and vocational junior college, advanced course
    national_label_local: Senmonshoku-tanki-daigaku Senkoka
    entry_age: 20
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 69
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-65
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-66
    national_label_en: "College of technology, regular course \n4th to 5th Grade"
    national_label_local: Koto-senmon-gakko Honka
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 70
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-66
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-67
    national_label_en: College of technology, advanced course
    national_label_local: Koto-senmon-gakko Senkoka
    entry_age: 20
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 71
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-67
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-68
    national_label_en: Specialized Training College, Post-secondary Course (Professional
      Training College)
    national_label_local: "Senshu-gakko Senmon-katei\u3000(Senmon-gakko)"
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 72
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-68
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-69
    national_label_en: Specialized Training College, Post-secondary Course (Professional
      Training College)
    national_label_local: "Senshu-gakko Senmon-katei\u3000(Senmon-gakko)"
    entry_age: 18
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 73
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-69
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-70
    national_label_en: University, undergraduate
    national_label_local: Daigaku Gakubu
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 74
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 14
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-70
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-71
    national_label_en: Professional and vocational university, undergraduate
    national_label_local: Senmonshoku-daigaku Gakubu
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 75
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 14
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-71
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-72
    national_label_en: University, advanced course
    national_label_local: Daigaku Senkoka
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 76
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-72
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-73
    national_label_en: University, undergraduate, correspondence course
    national_label_local: Daigaku Gakubu Tsushinsei-katei
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 77
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 14
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-73
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-74
    national_label_en: Professional and vocational university, advanced course
    national_label_local: Senmonshoku-daigaku Senkoka
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 78
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-74
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-75
    national_label_en: Junior college, NIAD-QE validated advanced course
    national_label_local: Tanki-daigaku Senkoka (Tokurei-tekiyo Senko-ka)
    entry_age: 20
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 79
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 11
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-75
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-76
    national_label_en: College of technology, NIAD-QE validated advanced course
    national_label_local: Koto-senmon-gakko Senkoka (Tokurei-tekiyo Senko-ka)
    entry_age: 20
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 80
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-76
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-77
    national_label_en: bachelor's degree awarded to those who have successfully completed
      programs at those educational institutions operated by a government ministry
      or agency which are approved by NIAD-QE
    national_label_local: "Gakkyohou dai 104 jou 7 kou 2 gou ni motoduku NIAD no nintei\
      \ wo uketa katei\uFF08Gakushi\uFF09"
    entry_age: 18
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 81
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 14
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-77
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-78
    national_label_en: University, undergraduate of medicine, dentistry, pharmacy
      (only practical course) and veterinary medicine
    national_label_local: Daigaku Igaku, Shigaku,Yakugaku,Juigaku
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 82
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 16
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-78
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-79
    national_label_en: University, graduate school, Master's course correspondence
      course
    national_label_local: Daigakuin Shushi-katei Tsushinsei-katei
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 83
    parent_country_entry_ids:
    - JPN-EDU-70
    - JPN-EDU-71
    - JPN-EDU-72
    - JPN-EDU-73
    - JPN-EDU-74
    - JPN-EDU-75
    - JPN-EDU-76
    - JPN-EDU-77
    cum_years_schooling: 13
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-72
    - JPN-EDU-79
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-70, JPN-EDU-71, JPN-EDU-72, JPN-EDU-73,
      JPN-EDU-74, JPN-EDU-75, JPN-EDU-76, JPN-EDU-77'
  - country_entry_id: JPN-EDU-80
    national_label_en: University, professional graduate school, professional course
      correspondence course
    national_label_local: Daigakuin Senmonshoku-gakui-katei Tsushinsei-katei
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 84
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-80
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-81
    national_label_en: University, graduate school, master's course
    national_label_local: Daigakuin Shushi-katei
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 85
    parent_country_entry_ids:
    - JPN-EDU-70
    - JPN-EDU-71
    - JPN-EDU-72
    - JPN-EDU-73
    - JPN-EDU-74
    - JPN-EDU-75
    - JPN-EDU-76
    - JPN-EDU-77
    cum_years_schooling: 13
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-72
    - JPN-EDU-81
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-70, JPN-EDU-71, JPN-EDU-72, JPN-EDU-73,
      JPN-EDU-74, JPN-EDU-75, JPN-EDU-76, JPN-EDU-77'
  - country_entry_id: JPN-EDU-82
    national_label_en: University, professional graduate school, professional course
    national_label_local: Daigakuin Senmonshoku-gakui-katei
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 86
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 12
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-82
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-83
    national_label_en: University, professional graduate school, graduate law school
    national_label_local: Daigakuin Senmonshoku-gakui-katei Hokadaigakuin
    entry_age: 22
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 87
    parent_country_entry_ids:
    - JPN-EDU-12
    - JPN-EDU-13
    - JPN-EDU-14
    - JPN-EDU-15
    - JPN-EDU-16
    - JPN-EDU-17
    - JPN-EDU-18
    - JPN-EDU-19
    - JPN-EDU-20
    - JPN-EDU-21
    - JPN-EDU-22
    - JPN-EDU-23
    - JPN-EDU-24
    - JPN-EDU-25
    - JPN-EDU-26
    - JPN-EDU-27
    - JPN-EDU-28
    - JPN-EDU-29
    - JPN-EDU-30
    - JPN-EDU-31
    - JPN-EDU-32
    - JPN-EDU-33
    - JPN-EDU-34
    - JPN-EDU-35
    - JPN-EDU-36
    - JPN-EDU-37
    - JPN-EDU-38
    - JPN-EDU-39
    - JPN-EDU-40
    - JPN-EDU-41
    - JPN-EDU-42
    - JPN-EDU-43
    - JPN-EDU-44
    cum_years_schooling: 13
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-83
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
  - country_entry_id: JPN-EDU-84
    national_label_en: master's degree awarded to those who have successfully completed
      programs at those educational institutions operated by a government ministry
      or agency which are approved by NIAD-QE
    national_label_local: "Gakkyohou dai 104 jou 7 kou 2 gou ni motoduku NIAD no nintei\
      \ wo uketa katei\uFF08Shushi\uFF09"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 88
    parent_country_entry_ids:
    - JPN-EDU-70
    - JPN-EDU-71
    - JPN-EDU-72
    - JPN-EDU-73
    - JPN-EDU-74
    - JPN-EDU-75
    - JPN-EDU-76
    - JPN-EDU-77
    cum_years_schooling: 13
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-72
    - JPN-EDU-84
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-70, JPN-EDU-71, JPN-EDU-72, JPN-EDU-73,
      JPN-EDU-74, JPN-EDU-75, JPN-EDU-76, JPN-EDU-77'
  - country_entry_id: JPN-EDU-85
    national_label_en: University, graduate school, doctor's course
    national_label_local: Daigakuin Hakushi katei
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 89
    parent_country_entry_ids:
    - JPN-EDU-78
    - JPN-EDU-79
    - JPN-EDU-80
    - JPN-EDU-81
    - JPN-EDU-82
    - JPN-EDU-83
    - JPN-EDU-84
    cum_years_schooling: 15
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-80
    - JPN-EDU-85
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-78, JPN-EDU-79, JPN-EDU-80, JPN-EDU-81,
      JPN-EDU-82, JPN-EDU-83, JPN-EDU-84'
  - country_entry_id: JPN-EDU-86
    national_label_en: University, graduate school, doctor's course of  medicine,
      dentistry,pharmacy (only practical course),and veterinary medicine
    national_label_local: "Daigakuin Hakushi-katei\u3000Igaku,Shigaku,Yakugaku,Juigaku"
    entry_age: 24
    duration_years: 4
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 90
    parent_country_entry_ids:
    - JPN-EDU-78
    - JPN-EDU-79
    - JPN-EDU-80
    - JPN-EDU-81
    - JPN-EDU-82
    - JPN-EDU-83
    - JPN-EDU-84
    cum_years_schooling: 16
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-80
    - JPN-EDU-86
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-78, JPN-EDU-79, JPN-EDU-80, JPN-EDU-81,
      JPN-EDU-82, JPN-EDU-83, JPN-EDU-84'
  - country_entry_id: JPN-EDU-87
    national_label_en: University, graduate school, doctor's course correspondence
      course
    national_label_local: Daigakuin Hakushi-katei Tsushinsei-katei
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 91
    parent_country_entry_ids:
    - JPN-EDU-78
    - JPN-EDU-79
    - JPN-EDU-80
    - JPN-EDU-81
    - JPN-EDU-82
    - JPN-EDU-83
    - JPN-EDU-84
    cum_years_schooling: 15
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-80
    - JPN-EDU-87
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-78, JPN-EDU-79, JPN-EDU-80, JPN-EDU-81,
      JPN-EDU-82, JPN-EDU-83, JPN-EDU-84'
  - country_entry_id: JPN-EDU-88
    national_label_en: doctoral degree awarded to those who have successfully completed
      programs at those educational institutions operated by a government ministry
      or agency which are approved by NIAD-QE
    national_label_local: "Gakkyohou dai 104 jou 7 kou 2 gou ni motoduku NIAD no nintei\
      \ wo uketa katei\uFF08Hakushi\uFF09"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 92
    parent_country_entry_ids:
    - JPN-EDU-78
    - JPN-EDU-79
    - JPN-EDU-80
    - JPN-EDU-81
    - JPN-EDU-82
    - JPN-EDU-83
    - JPN-EDU-84
    cum_years_schooling: 15
    cum_years_computation_path:
    - JPN-EDU-05
    - JPN-EDU-08
    - JPN-EDU-12
    - JPN-EDU-80
    - JPN-EDU-88
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: JPN-EDU-05, JPN-EDU-06, JPN-EDU-07'
    - 'minimum parent path selected from: JPN-EDU-08, JPN-EDU-09, JPN-EDU-10, JPN-EDU-11'
    - 'minimum parent path selected from: JPN-EDU-12, JPN-EDU-13, JPN-EDU-14, JPN-EDU-15,
      JPN-EDU-16, JPN-EDU-17, JPN-EDU-18, JPN-EDU-19, JPN-EDU-20, JPN-EDU-21, JPN-EDU-22,
      JPN-EDU-23, JPN-EDU-24, JPN-EDU-25, JPN-EDU-26, JPN-EDU-27, JPN-EDU-28, JPN-EDU-29,
      JPN-EDU-30, JPN-EDU-31, JPN-EDU-32, JPN-EDU-33, JPN-EDU-34, JPN-EDU-35, JPN-EDU-36,
      JPN-EDU-37, JPN-EDU-38, JPN-EDU-39, JPN-EDU-40, JPN-EDU-41, JPN-EDU-42, JPN-EDU-43,
      JPN-EDU-44'
    - 'minimum parent path selected from: JPN-EDU-78, JPN-EDU-79, JPN-EDU-80, JPN-EDU-81,
      JPN-EDU-82, JPN-EDU-83, JPN-EDU-84'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Japan.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2015
  effective_to: null
  selectors: null
  value:
  - country_entry_id: JPN-SUBNAT-01
    survey_labels: '[1]Hokkaido'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: ADM1_CODE
    geo_id: '1661'
    geo_nvar: ADM1_NAME
    geo_name: Hokkaidoo
    source_row: 8121
  - country_entry_id: JPN-SUBNAT-02
    survey_labels: '[2]Tohoku'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '2'
    geo_nvar: ADM1_NAME
    geo_name: Akita & Aomori & Hukusima & Iwate & Miyagi & Yamagata
    source_row: 8122
  - country_entry_id: JPN-SUBNAT-03
    survey_labels: '[3]Kanto'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '3'
    geo_nvar: ADM1_NAME
    geo_name: Gunma & Ibaraki & Kanagawa & Saitama & Totigi & Tookyoo & Tiba
    source_row: 8123
  - country_entry_id: JPN-SUBNAT-04
    survey_labels: '[4]Chubu'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '4'
    geo_nvar: ADM1_NAME
    geo_name: Aiti & Hukui & Gifu & Isikawa & Nagano & Niigata & Sizuoka & Toyama
      & Yamanasi
    source_row: 8124
  - country_entry_id: JPN-SUBNAT-05
    survey_labels: '[5]Kinki'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '5'
    geo_nvar: ADM1_NAME
    geo_name: Hyoogo & Kyooto & Mie & Nara & Oosaka & Siga & Wakayama
    source_row: 8125
  - country_entry_id: JPN-SUBNAT-06
    survey_labels: '[6]Chugoku'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '6'
    geo_nvar: ADM1_NAME
    geo_name: Hirosima & Okayama & Simane & Tottori & Yamaguti
    source_row: 8126
  - country_entry_id: JPN-SUBNAT-07
    survey_labels: '[7]Shikoku'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '7'
    geo_nvar: ADM1_NAME
    geo_name: Ehime & Kagawa & Kooti & Tokusima
    source_row: 8127
  - country_entry_id: JPN-SUBNAT-08
    survey_labels: '[8]Kyushu'
    survey_variables: region_c
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: false
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 0
    gmd_subnatidsurvey: ''
    geo_year: '2015'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '8'
    geo_nvar: ADM1_NAME
    geo_name: Hukuoka & Kagosima & Kumamoto & Miyazaki & Nagasaki & Ooita & Okinawa
      & Saga
    source_row: 8128
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 2000
  effective_to: null
  selectors: null
  value: 15
  provenance:
    source: extraction\10_source\country-parameters-inputs\Labor\min_labor_age_panel_1990_2026.xlsx
      (ILO C138 ratified)
    verified_on: null
    human_reviewed: false
    reviewer: null
---

