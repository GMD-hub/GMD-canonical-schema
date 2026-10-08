---
country_id: CTY-HRV
iso3: HRV
schema_version: '0.2'
status: draft
country_name: HRV
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HRV-EDU-01
    national_label_en: Educational programs for children under 3 years of age
    national_label_local: Obrazovni programi za djecu ispod 3 godine starosti
    entry_age: 0
    duration_years: 2
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
  - country_entry_id: HRV-EDU-02
    national_label_en: Pre-school education programme
    national_label_local: "Pred\u0161kolsko obrazovanje"
    entry_age: 3
    duration_years: 4
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
  - country_entry_id: HRV-EDU-03
    national_label_en: Initial primary education, the first stage of basic education
    national_label_local: "Po\u010Detno osnovno obrazovanje, prvi stupanj osnovnog\
      \ obrazovanja"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_complete
    gmd_educat7_target: primary_complete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - HRV-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: HRV-EDU-04
    national_label_en: Formal education in the upper grades of elementary school
    national_label_local: "Programi redovnog obrazovanja u vi\u0161im razredima osnovne\
      \ \u0161kole"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 8
    parent_country_entry_ids:
    - HRV-EDU-03
    cum_years_schooling: 8
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: HRV-EDU-05
    national_label_en: Art education at the elementary level
    national_label_local: "Programi osnovnog umjetni\u010Dkog obrazovanja"
    entry_age: 7
    duration_years: 6
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
    parent_country_entry_ids:
    - HRV-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: HRV-EDU-06
    national_label_en: Elementary education - Adult education
    national_label_local: "Osnovno \u0161kolovanje odraslih"
    entry_age: 15
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
    parent_country_entry_ids: []
    cum_years_schooling: 3
    cum_years_computation_path:
    - HRV-EDU-06
    cum_years_status: computed
    review_flags: &id002 []
  - country_entry_id: HRV-EDU-07
    national_label_en: Vocational training programmes for adult persons that enable
      access to labour market, and which do not lead to continuation of education.
      In order to access this level person has to succesfully complete Level 2.
    national_label_local: "Programi osposobljavanja za odrasle koji omogu\u0107uju\
      \ pristup tr\u017Ei\u0161tu rada, a ne vode nastavku obrazovanja. Uvjet upisa\
      \ je zavr\u0161ena razina 2"
    entry_age: 15
    duration_years: 120
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 123
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-07
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-08
    national_label_en: Vocational education programmes within regular education in
      duration of one year, that enable access to labour market
    national_label_local: "Programi strukovnog obrazovanja u trajanju od jedne godine\
      \ u sklopu redovnog obrazovanja koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
    parent_country_entry_ids:
    - HRV-EDU-04
    - HRV-EDU-05
    cum_years_schooling: 9
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
  - country_entry_id: HRV-EDU-09
    national_label_en: Vocational education programmes within adult education system
      in duration of one year , that enable access to labour market or entry to ISCED
      level 3
    national_label_local: "Programi strukovnog obrazovanja u trajanju od jedne godine\
      \ u sklopu obrazovanja odraslih koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada i upis u programe obrazovanja odraslih na ISCED razini 3"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 13
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 4
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-09
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-10
    national_label_en: Vocational education programmes within regular education system
      in duration up to two years, that enable access to labour market
    national_label_local: "Programi strukovnog obrazovanja u trajanju do dvije godine\
      \ u sklopu redovnog obrazovanja koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 14
    parent_country_entry_ids:
    - HRV-EDU-04
    - HRV-EDU-05
    cum_years_schooling: 10
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
  - country_entry_id: HRV-EDU-11
    national_label_en: Vocational education programmes within adult education system
      in duration up to two years, that enable access to labour market or entry to
      ISCED level 3
    national_label_local: "Programi strukovnog obrazovanja u trajanju do dvije godine\
      \ u sklopu obrazovanja odraslih koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada i upis u programe obrazovanja odraslih na ISCED razini 3"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 15
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 5
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-11
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-12
    national_label_en: Vocational education programmes within regular education system
      in duration of three or three years , that enable access to labour market  or
      entry to ISCED level 03.08
    national_label_local: "Programi strukovnog obrazovanja u trajanju od tri  godine\
      \ u sklopu redovnog obrazovanja koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada i upis u programe 03.08"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 16
    parent_country_entry_ids:
    - HRV-EDU-04
    - HRV-EDU-05
    cum_years_schooling: 11
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
  - country_entry_id: HRV-EDU-13
    national_label_en: Vocational education programmes within adult education system
      in duration of three years that enable access to labour market or entry to ISCED
      level 03.09
    national_label_local: "Programi strukovnog obrazovanja u trajanju od tri godine\
      \ u sklopu obrazovanja odraslih koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada i upis u programe obrazovanja odraslih 03.09"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 17
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 6
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-13
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-14
    national_label_en: Vocational education programmes within regular education system
      in duration of four or more years , that enable access to labour market or entry
      to ISCED levels 5 and 6
    national_label_local: "Programi strukovnog obrazovanja u trajanju \u010Detiri\
      \ ili vi\u0161e godina u sklopu redovnog obrazovanja koji omogu\u0107uju ulazak\
      \ na tr\u017Ei\u0161te rada i upis u programe na ISCED razini 5 i 6"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 18
    parent_country_entry_ids:
    - HRV-EDU-04
    - HRV-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
  - country_entry_id: HRV-EDU-15
    national_label_en: Vocational education programmes within adult education system
      in duration of four or more years , that enable access to labour market or entry
      to ISCED levels 5 and 6
    national_label_local: "Programi strukovnog obrazovanja u trajanju \u010Detiri\
      \ u sklopu obrazovanja odraslih koji omogu\u0107uju ulazak na tr\u017Ei\u0161\
      te rada i upis u programe na ISCED razini 5 i 6"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 19
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-15
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-16
    national_label_en: Art education - duration 4 years
    national_label_local: "Umjetni\u010Dko obrazovanje u trajanju od 4 godine"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 20
    parent_country_entry_ids:
    - HRV-EDU-04
    - HRV-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
  - country_entry_id: HRV-EDU-17
    national_label_en: Art education within adult education system-duration 4 years
    national_label_local: "Umjetni\u010Dko obrazovanje u trajanju od 4 godine u sklopu\
      \ obrazovanja odraslih"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 21
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-17
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-18
    national_label_en: Grammar secondary school educational programs - duration 4
      years
    national_label_local: Gimnazijski obrazovni programi u trajanju od 4 godine
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 22
    parent_country_entry_ids:
    - HRV-EDU-04
    - HRV-EDU-05
    cum_years_schooling: 12
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
  - country_entry_id: HRV-EDU-19
    national_label_en: Grammar secondary school educational programs within adult
      education system-duration 4 years
    national_label_local: Gimnazijski obrazovni programi u trajanju od 4 godine u
      sklopu obrazovanja odraslih
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 23
    parent_country_entry_ids:
    - HRV-EDU-06
    cum_years_schooling: 7
    cum_years_computation_path:
    - HRV-EDU-06
    - HRV-EDU-19
    cum_years_status: computed
    review_flags: *id002
  - country_entry_id: HRV-EDU-20
    national_label_en: Short-cycle professional study
    national_label_local: "Kratki stru\u010Dni studij \n(u trajanju kra\u0107em od\
      \ tri godine)"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 14
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-21
    national_label_en: Professional (undergraduate) study
    national_label_local: "Preddiplomski stru\u010Dni studij\n(u trajanju od najmanje\
      \ tri godine)"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 15
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-22
    national_label_en: Undergraduate university study
    national_label_local: "Preddiplomski sveu\u010Dili\u0161ni studij"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 15
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-23
    national_label_en: "Graduate university\n study"
    national_label_local: "Diplomski sveu\u010Dili\u0161ni studij"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 13
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-24
    national_label_en: Integrated undergraduate and graduate university study
    national_label_local: "Integrirani preddiplomski i diplomski sveu\u010Dili\u0161\
      ni studij"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 17
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-25
    national_label_en: Specialist graduate professional study
    national_label_local: "Specijalisti\u010Dki diplomski stru\u010Dni studij"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 13
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-26
    national_label_en: Postgraduate specialist study
    national_label_local: "Poslijediplomski specijalisti\u010Dki studij"
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - HRV-EDU-16
    - HRV-EDU-18
    cum_years_schooling: 13
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
  - country_entry_id: HRV-EDU-27
    national_label_en: Postgraduate university (doctoral) study
    national_label_local: "Poslijediplomski sveu\u010Dili\u0161ni studij"
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - HRV-EDU-23
    - HRV-EDU-24
    - HRV-EDU-25
    - HRV-EDU-26
    cum_years_schooling: 16
    cum_years_computation_path:
    - HRV-EDU-03
    - HRV-EDU-04
    - HRV-EDU-16
    - HRV-EDU-23
    - HRV-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: HRV-EDU-04, HRV-EDU-05'
    - 'minimum parent path selected from: HRV-EDU-16, HRV-EDU-18'
    - 'minimum parent path selected from: HRV-EDU-23, HRV-EDU-24, HRV-EDU-25, HRV-EDU-26'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Croatia.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2006
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HRV-SUBNAT-01
    survey_labels: 1-HR01
    survey_variables: subnatid
    gmd_subnatid1: HRV_2006_NUTS2_HR01
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: HRV_2006_NUTS2_HR01
    geo_year: '2006'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: HR01
    geo_nvar: NAME_LATN
    geo_name: Sjeverozapadna Hrvatska
    source_row: 6117
  - country_entry_id: HRV-SUBNAT-02
    survey_labels: 2-HR02
    survey_variables: subnatid
    gmd_subnatid1: HRV_2006_NUTS2_HR02
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: HRV_2006_NUTS2_HR02
    geo_year: '2006'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: HR02
    geo_nvar: NAME_LATN
    geo_name: "Sredi\u0161nja i Isto\u010Dna (Panonska) Hrvatska"
    source_row: 6118
  - country_entry_id: HRV-SUBNAT-03
    survey_labels: 3-HR03
    survey_variables: subnatid
    gmd_subnatid1: HRV_2006_NUTS2_HR03
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: HRV_2006_NUTS2_HR03
    geo_year: '2006'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: HR03
    geo_nvar: NAME_LATN
    geo_name: Jadranska Hrvatska
    source_row: 6119
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
  - country_entry_id: HRV-SAN-01
    source_category_code: flush_to_piped_sewage_system
    national_label_en: Flush to piped sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 61
  - country_entry_id: HRV-SAN-02
    source_category_code: flush_to_septic_tank
    national_label_en: Flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 62
  - country_entry_id: HRV-SAN-03
    source_category_code: indoor_flushing_toilet_for_sole_use_of_household
    national_label_en: Indoor flushing toilet for sole use of household
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: HRV-SAN-04
    source_category_code: indoor_flushing_toilet_shared
    national_label_en: Indoor flushing toilet, shared
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: HRV-SAN-05
    source_category_code: bucket_latrine_where_fresh_excreta_are_manually_removed
    national_label_en: Bucket latrine (where fresh excreta are manually removed)
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 110
  - country_entry_id: HRV-SAN-06
    source_category_code: covered_latrine_with_privacy
    national_label_en: Covered latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 106
  - country_entry_id: HRV-SAN-07
    source_category_code: uncovered_latrine_without_privacy
    national_label_en: Uncovered latrine (without privacy)
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: HRV-SAN-08
    source_category_code: pour_flush_latrine
    national_label_en: Pour flush latrine
    national_label_local: Pour flush latrines
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 85
  - country_entry_id: HRV-SAN-09
    source_category_code: no_facilities_open_defecation
    national_label_en: No facilities (open defecation)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 134
  - country_entry_id: HRV-SAN-10
    source_category_code: no_indoor_flush_toilet
    national_label_en: No indoor flush toilet
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 136
  - country_entry_id: HRV-SAN-11
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
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_HRV_Croatia_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: HRV-WAS-01
    source_category_code: protected_dug_well_or_protected_spring
    national_label_en: Protected dug well or protected spring
    national_label_local: Protected wells or springs
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: true
    shared_flag: false
    source_row: 46
  - country_entry_id: HRV-WAS-02
    source_category_code: protected_tube_well_or_bore_hole
    national_label_en: Protected tube well or bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 58
  - country_entry_id: HRV-WAS-03
    source_category_code: unprotected_dug_well_or_spring
    national_label_en: Unprotected dug well or spring
    national_label_local: Unprotected wells or springs
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: false
    shared_flag: false
    source_row: 50
  - country_entry_id: HRV-WAS-04
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker-truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 102
  - country_entry_id: HRV-WAS-05
    source_category_code: no_adequate_plumbing_water_installation
    national_label_en: No adequate plumbing/water installation
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 106
  - country_entry_id: HRV-WAS-06
    source_category_code: no_plumbling_water_installation
    national_label_en: No plumbling/water installation
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 107
  - country_entry_id: HRV-WAS-07
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 86
  - country_entry_id: HRV-WAS-08
    source_category_code: water_taken_directly_from_pond_water_or_stream
    national_label_en: Water taken directly from pond-water or stream
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 92
  - country_entry_id: HRV-WAS-09
    source_category_code: adequate_plumbing_water_installation
    national_label_en: Adequate plumbing/water installation
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: HRV-WAS-10
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 39
  - country_entry_id: HRV-WAS-11
    source_category_code: public_standpipe
    national_label_en: Public standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_HRV_Croatia_1.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1991
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

