---
country_id: CTY-POL
iso3: POL
schema_version: '0.2'
status: draft
country_name: POL
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: POL-EDU-01
    national_label_en: Pre-school education
    national_label_local: Wychowanie przedszkolne
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
  - country_entry_id: POL-EDU-02
    national_label_en: Special pre-school education
    national_label_local: Wychowanie przedszkolne specjalne
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
  - country_entry_id: POL-EDU-03
    national_label_en: General primary 1st level music school (grades 1-4)
    national_label_local: "Og\xF3lnokszta\u0142c\u0105ca szko\u0142a muzyczna I stopnia\
      \ (klasy 1-4)"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - POL-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: POL-EDU-04
    national_label_en: General primary 1st level music school (grades 5-8)
    national_label_local: "Og\xF3lnokszta\u0142c\u0105ca szko\u0142a muzyczna I stopnia\
      \ (klasy 5-8)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 8
    parent_country_entry_ids:
    - POL-EDU-03
    - POL-EDU-05
    - POL-EDU-07
    - POL-EDU-09
    - POL-EDU-12
    cum_years_schooling: 8
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-04
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
  - country_entry_id: POL-EDU-05
    national_label_en: Primary school for children and youth (grades 1-4)
    national_label_local: "Szko\u0142a podstawowa dla dzieci i m\u0142odzie\u017C\
      y (klasy 1-4)"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 9
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - POL-EDU-05
    cum_years_status: computed
    review_flags: []
  - country_entry_id: POL-EDU-06
    national_label_en: Primary school for children and youth (grades 5-8)
    national_label_local: "Szko\u0142a podstawowa dla dzieci i m\u0142odzie\u017C\
      y (klasy 5-8)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - POL-EDU-03
    - POL-EDU-05
    - POL-EDU-07
    - POL-EDU-09
    - POL-EDU-12
    cum_years_schooling: 8
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
  - country_entry_id: POL-EDU-07
    national_label_en: Special primary  school for children and youth (grades 1-4)
    national_label_local: "Szko\u0142a podstawowa specjalna dla dzieci i m\u0142odzie\u017C\
      y (klasy 1-4)"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 11
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - POL-EDU-07
    cum_years_status: computed
    review_flags: []
  - country_entry_id: POL-EDU-08
    national_label_en: Special primary  school for children and youth (grades 5-8)
    national_label_local: "Szko\u0142a podstawowa specjalna dla dzieci i m\u0142odzie\u017C\
      y (klasy 5-8)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - POL-EDU-03
    - POL-EDU-05
    - POL-EDU-07
    - POL-EDU-09
    - POL-EDU-12
    cum_years_schooling: 8
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
  - country_entry_id: POL-EDU-09
    national_label_en: Primary special school for children with moderate or severe
      intellectual disabilities (grades 1-4)
    national_label_local: "Szko\u0142a podstawowa specjalna dla uczni\xF3w z niepe\u0142\
      nosprawno\u015Bci\u0105 intelektualn\u0105 w stopniu umiarkowanym lub w stopniu\
      \ znacznym (klasy 1-4)"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 13
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - POL-EDU-09
    cum_years_status: computed
    review_flags: []
  - country_entry_id: POL-EDU-10
    national_label_en: Primary special school for children with moderate or severe
      intellectual disabilities (grades 5-8)
    national_label_local: "Szko\u0142a podstawowa specjalna dla uczni\xF3w z niepe\u0142\
      nosprawno\u015Bci\u0105 intelektualn\u0105 w stopniu umiarkowanym lub w stopniu\
      \ znacznym (klasy 5-8)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - POL-EDU-03
    - POL-EDU-05
    - POL-EDU-07
    - POL-EDU-09
    - POL-EDU-12
    cum_years_schooling: 8
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
  - country_entry_id: POL-EDU-11
    national_label_en: Primary school (for adults)
    national_label_local: "Szko\u0142a podstawowa (dla doros\u0142ych)"
    entry_age: 18
    duration_years: 2
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 15
    parent_country_entry_ids: []
    cum_years_schooling: 2
    cum_years_computation_path:
    - POL-EDU-11
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: POL-EDU-12
    national_label_en: Primary sports and sports masterclass school for youth            (grades
      1-4)
    national_label_local: "Szko\u0142a podstawowa sportowa i mistrzostwa sportowego\
      \ (klasy 1-4)"
    entry_age: 7
    duration_years: 4
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 16
    parent_country_entry_ids: []
    cum_years_schooling: 4
    cum_years_computation_path:
    - POL-EDU-12
    cum_years_status: computed
    review_flags: []
  - country_entry_id: POL-EDU-13
    national_label_en: Primary sports and sports masterclass school for youth         (grades
      5-8)
    national_label_local: "Szko\u0142a podstawowa sportowa i mistrzostwa sportowego\
      \ (klasy 5-8)"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - POL-EDU-03
    - POL-EDU-05
    - POL-EDU-07
    - POL-EDU-09
    - POL-EDU-12
    cum_years_schooling: 8
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
  - country_entry_id: POL-EDU-14
    national_label_en: Three year special school preparing for employment (for youth
      with moderate or severe intelectual impariment or with multiple disability including
      intelectual disability)
    national_label_local: "Trzyletnia szko\u0142a specjalna przysposabiaj\u0105ca\
      \ do pracy (dla uczni\xF3w z niepe\u0142nosprawno\u015Bci\u0105 intelektualn\u0105\
      \ w stopniu umiarkowanym lub  znacznym oraz dla uczni\xF3w z niepe\u0142nosprawno\u015B\
      ciami sprz\u0119\u017Conymi)"
    entry_age: 16
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - POL-EDU-03
    - POL-EDU-05
    - POL-EDU-07
    - POL-EDU-09
    - POL-EDU-12
    cum_years_schooling: 7
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
  - country_entry_id: POL-EDU-15
    national_label_en: General ballet school
    national_label_local: "Og\xF3lnokszta\u0142c\u0105ca szko\u0142a baletowa"
    entry_age: 11
    duration_years: 9
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 16
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-16
    national_label_en: General primary  2nd level music school
    national_label_local: "Og\xF3lnokszta\u0142c\u0105ca szko\u0142a muzyczna II stopnia"
    entry_age: 13
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-17
    national_label_en: 2nd level music school
    national_label_local: "Szko\u0142a muzyczna II stopnia"
    entry_age: 10
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-18
    national_label_en: School of Fine Arts
    national_label_local: "Og\xF3lnokszta\u0142c\u0105ca szko\u0142a sztuk pi\u0119\
      knych"
    entry_age: 13
    duration_years: 6
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 13
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-19
    national_label_en: Secondary School of Fine Arts
    national_label_local: Liceum sztuk plastycznych
    entry_age: 16
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-20
    national_label_en: Circus Arts School (2nd level arts school)
    national_label_local: "Szko\u0142a sztuki cyrkowej - szko\u0142a artystyczna II\
      \ stopnia"
    entry_age: 13
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-21
    national_label_en: Vocational qualification course
    national_label_local: Kwalifikacyjny kurs zawodowy/KKZ
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 26
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 8
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-22
    national_label_en: Technical secondary school (for youth)
    national_label_local: "Technikum (dla m\u0142odzie\u017Cy)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 27
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-23
    national_label_en: Special  technical secondary school (for youth)
    national_label_local: "Technikum specjalne (dla m\u0142odzie\u017Cy)"
    entry_age: 15
    duration_years: 5
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 28
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 12
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-24
    national_label_en: General secondary school (for youth)
    national_label_local: "Liceum og\xF3lnokszta\u0142c\u0105ce (dla m\u0142odzie\u017C\
      y)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 29
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-25
    national_label_en: Special general secondary school (for youth)
    national_label_local: "Liceum og\xF3lnokszta\u0142c\u0105ce specjalne (dla m\u0142\
      odzie\u017Cy)"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 30
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-26
    national_label_en: General secondary school (for adults)
    national_label_local: "Liceum og\xF3lnokszta\u0142c\u0105ce (dla doros\u0142ych)"
    entry_age: 0
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 31
    parent_country_entry_ids:
    - POL-EDU-11
    cum_years_schooling: 6
    cum_years_computation_path:
    - POL-EDU-11
    - POL-EDU-26
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: POL-EDU-27
    national_label_en: Sports and sports masterclass secondary school (lasts 3 years,
      for youth)
    national_label_local: "Liceum sportowe i mistrzostwa sportowego dla m\u0142odzie\u017C\
      y"
    entry_age: 15
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 32
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-28
    national_label_en: Stage I sectoral vocational school (for youth)
    national_label_local: "Bran\u017Cowa szko\u0142a I stopnia (dla m\u0142odzie\u017C\
      y)"
    entry_age: 18
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 33
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-29
    national_label_en: Special stage I sectoral  vocational school (for youth)
    national_label_local: "Bran\u017Cowa szko\u0142a I stopnia specjalna (dla m\u0142\
      odzie\u017Cy)"
    entry_age: 18
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 34
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-30
    national_label_en: Stage I sectoral vocational school (for youth) - juvenile workers
    national_label_local: "Bran\u017Cowa szko\u0142a I stopnia (dla m\u0142odzie\u017C\
      y) - m\u0142odociani pracownicy"
    entry_age: 18
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 35
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 10
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-31
    national_label_en: School of dance arts
    national_label_local: "Szko\u0142a sztuki ta\u0144ca"
    entry_age: 7
    duration_years: 9
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 36
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 16
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-32
    national_label_en: Stage II sectoral vocational school
    national_label_local: "Bran\u017Cowa szko\u0142a II stopnia"
    entry_age: 19
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 37
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 9
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-33
    national_label_en: Special stage II sectoral vocational school
    national_label_local: "Bran\u017Cowa szko\u0142a II stopnia specjalna"
    entry_age: 19
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 38
    parent_country_entry_ids:
    - POL-EDU-04
    - POL-EDU-06
    - POL-EDU-08
    - POL-EDU-10
    - POL-EDU-13
    - POL-EDU-14
    cum_years_schooling: 9
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
  - country_entry_id: POL-EDU-34
    national_label_en: Post-secondary school
    national_label_local: "Szko\u0142a policealna"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - POL-EDU-15
    - POL-EDU-16
    - POL-EDU-17
    - POL-EDU-18
    - POL-EDU-19
    - POL-EDU-20
    - POL-EDU-24
    - POL-EDU-25
    - POL-EDU-27
    - POL-EDU-31
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    - POL-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
    - 'minimum parent path selected from: POL-EDU-15, POL-EDU-16, POL-EDU-17, POL-EDU-18,
      POL-EDU-19, POL-EDU-20, POL-EDU-24, POL-EDU-25, POL-EDU-27, POL-EDU-31'
  - country_entry_id: POL-EDU-35
    national_label_en: Special post-secondary school
    national_label_local: "Szko\u0142a policealna specjalna"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - POL-EDU-15
    - POL-EDU-16
    - POL-EDU-17
    - POL-EDU-18
    - POL-EDU-19
    - POL-EDU-20
    - POL-EDU-24
    - POL-EDU-25
    - POL-EDU-27
    - POL-EDU-31
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    - POL-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
    - 'minimum parent path selected from: POL-EDU-15, POL-EDU-16, POL-EDU-17, POL-EDU-18,
      POL-EDU-19, POL-EDU-20, POL-EDU-24, POL-EDU-25, POL-EDU-27, POL-EDU-31'
  - country_entry_id: POL-EDU-36
    national_label_en: Post- secondary music school
    national_label_local: "Szko\u0142a policealna muzyczna"
    entry_age: 19
    duration_years: 3
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 41
    parent_country_entry_ids:
    - POL-EDU-15
    - POL-EDU-16
    - POL-EDU-17
    - POL-EDU-18
    - POL-EDU-19
    - POL-EDU-20
    - POL-EDU-24
    - POL-EDU-25
    - POL-EDU-27
    - POL-EDU-31
    cum_years_schooling: 13
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    - POL-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
    - 'minimum parent path selected from: POL-EDU-15, POL-EDU-16, POL-EDU-17, POL-EDU-18,
      POL-EDU-19, POL-EDU-20, POL-EDU-24, POL-EDU-25, POL-EDU-27, POL-EDU-31'
  - country_entry_id: POL-EDU-37
    national_label_en: Post- secondary school of fine arts
    national_label_local: "Szko\u0142a policealna plastyczna"
    entry_age: 19
    duration_years: 2
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 42
    parent_country_entry_ids:
    - POL-EDU-15
    - POL-EDU-16
    - POL-EDU-17
    - POL-EDU-18
    - POL-EDU-19
    - POL-EDU-20
    - POL-EDU-24
    - POL-EDU-25
    - POL-EDU-27
    - POL-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    - POL-EDU-37
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
    - 'minimum parent path selected from: POL-EDU-15, POL-EDU-16, POL-EDU-17, POL-EDU-18,
      POL-EDU-19, POL-EDU-20, POL-EDU-24, POL-EDU-25, POL-EDU-27, POL-EDU-31'
  - country_entry_id: POL-EDU-38
    national_label_en: Colleges of social work
    national_label_local: "Kolegium pracownik\xF3w s\u0142u\u017Cb spo\u0142ecznych"
    entry_age: 19
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 43
    parent_country_entry_ids:
    - POL-EDU-15
    - POL-EDU-16
    - POL-EDU-17
    - POL-EDU-18
    - POL-EDU-19
    - POL-EDU-20
    - POL-EDU-24
    - POL-EDU-25
    - POL-EDU-27
    - POL-EDU-31
    cum_years_schooling: 13
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    - POL-EDU-38
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
    - 'minimum parent path selected from: POL-EDU-15, POL-EDU-16, POL-EDU-17, POL-EDU-18,
      POL-EDU-19, POL-EDU-20, POL-EDU-24, POL-EDU-25, POL-EDU-27, POL-EDU-31'
  - country_entry_id: POL-EDU-39
    national_label_en: Specialist programmes
    national_label_local: "Kszta\u0142cenie specjalistyczne"
    entry_age: 19
    duration_years: 1
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 44
    parent_country_entry_ids:
    - POL-EDU-15
    - POL-EDU-16
    - POL-EDU-17
    - POL-EDU-18
    - POL-EDU-19
    - POL-EDU-20
    - POL-EDU-24
    - POL-EDU-25
    - POL-EDU-27
    - POL-EDU-31
    cum_years_schooling: 11
    cum_years_computation_path:
    - POL-EDU-03
    - POL-EDU-14
    - POL-EDU-20
    - POL-EDU-39
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: POL-EDU-03, POL-EDU-05, POL-EDU-07, POL-EDU-09,
      POL-EDU-12'
    - 'minimum parent path selected from: POL-EDU-04, POL-EDU-06, POL-EDU-08, POL-EDU-10,
      POL-EDU-13, POL-EDU-14'
    - 'minimum parent path selected from: POL-EDU-15, POL-EDU-16, POL-EDU-17, POL-EDU-18,
      POL-EDU-19, POL-EDU-20, POL-EDU-24, POL-EDU-25, POL-EDU-27, POL-EDU-31'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Poland.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: POL-SUBNAT-01
    survey_labels: 1-PL2
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL2
    geo_nvar: NAME_LATN
    geo_name: "Makroregion po\u0142udniowy"
    source_row: 12385
  - country_entry_id: POL-SUBNAT-02
    survey_labels: 2-PL4
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL4
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL4
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL4
    geo_nvar: NAME_LATN
    geo_name: "Makroregion p\xF3\u0142nocno-zachodni"
    source_row: 12386
  - country_entry_id: POL-SUBNAT-03
    survey_labels: 3-PL5
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL5
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL5
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL5
    geo_nvar: NAME_LATN
    geo_name: "Makroregion po\u0142udniowo-zachodni"
    source_row: 12387
  - country_entry_id: POL-SUBNAT-04
    survey_labels: 4-PL6
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL6
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL6
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL6
    geo_nvar: NAME_LATN
    geo_name: "Makroregion p\xF3\u0142nocny"
    source_row: 12388
  - country_entry_id: POL-SUBNAT-05
    survey_labels: 5-PL7
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL7
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL7
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL7
    geo_nvar: NAME_LATN
    geo_name: Makroregion centralny
    source_row: 12389
  - country_entry_id: POL-SUBNAT-06
    survey_labels: 6-PL8
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL8
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL8
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL8
    geo_nvar: NAME_LATN
    geo_name: Makroregion wschodni
    source_row: 12390
  - country_entry_id: POL-SUBNAT-07
    survey_labels: 7-PL9
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: POL_2021_NUTS1_PL9
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: POL_2021_NUTS1_PL9
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '1'
    geo_idvar: NUTS_ID
    geo_id: PL9
    geo_nvar: NAME_LATN
    geo_name: "Makroregion wojew\xF3dztwo mazowieckie"
    source_row: 12403
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-LBR-MIN-WORKING-AGE
  effective_from: 1990
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

