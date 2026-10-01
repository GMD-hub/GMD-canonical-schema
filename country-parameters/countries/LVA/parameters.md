---
country_id: CTY-LVA
iso3: LVA
schema_version: '0.2'
status: draft
country_name: LVA
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LVA-EDU-01
    national_label_en: Pre-primary education programmes (part of the programme up
      until the age of 3 years) (early childhood education)
    national_label_local: "Pirmskolas izglitibas programmas (l\u012Bdz 3 gadu vecumam)"
    entry_age: 0
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
  - country_entry_id: LVA-EDU-02
    national_label_en: Pre-primary education programmes (part of the programme from
      the age of 3 years on)
    national_label_local: Pirmskolas izglitibas programmas (no 3 gadu vecuma)
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
  - country_entry_id: LVA-EDU-03
    national_label_en: General basic education, first stage (grades 1-6)
    national_label_local: "Visp\u0101r\u0113j\u0101 izgl\u012Bt\u012Bba, pamatizgl\u012B\
      t\u012Bbas pirm\u0101 posma (1.-6. klase)  programmas"
    entry_age: 7
    duration_years: 6
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 6
    cum_years_computation_path:
    - LVA-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: LVA-EDU-04
    national_label_en: General basic education, offered as 9 years long programme
      (grades 1-9), spanning two ISCED 2011 levels. This part of the programme covers
      grades 1-6, corresponding to ISCED Level 1
    national_label_local: "Visp\u0101r\u0113j\u0101 izgl\u012Bt\u012Bba, pamatizgl\u012B\
      t\u012Bbas (1.-9.klase) programmas - 1.-6 klase"
    entry_age: 7
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
    - LVA-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: LVA-EDU-05
    national_label_en: General basic education  (grades 1-9), special education programmes
      for students with mental development disorders; special education programmes
      for students with grave mental development disorders or multiple grave development
      disorders;  This part of th
    national_label_local: "Visp\u0101r\u0113j\u0101 izgl\u012Bt\u012Bba, pamatizgl\u012B\
      t\u012Bbas (1.-9.klase) programmas - Speci\u0101l\u0101s izgl\u012Bt\u012Bbas\
      \ programmas izgl\u012Btojamajiem ar gar\u012Bg\u0101s att\u012Bst\u012Bbas\
      \ trauc\u0113jumiem (koda 5. un 6. cipars 58) un Speci\u0101l\u0101s izgl\u012B\
      t\u012Bbas programmas izgl\u012Btojamajiem ar smagiem gar\u012Bg\u0101s att\u012B\
      st\u012Bbas tr"
    entry_age: 7
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - LVA-EDU-03
    - LVA-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
  - country_entry_id: LVA-EDU-06
    national_label_en: General basic education, offered as 9 years long programme
      (grades 1-9), spanning two ISCED 2011 levels. This part of the programme covers
      grades 7-9, corresponding to ISCED Level 2
    national_label_local: "Visp\u0101r\u0113j\u0101 izgl\u012Bt\u012Bba, pamatizgl\u012B\
      t\u012Bbas (1.-9.klase) programmas - 7.-9. klase"
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - LVA-EDU-03
    - LVA-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
  - country_entry_id: LVA-EDU-07
    national_label_en: General basic education, second stage (grades7-9)
    national_label_local: "Visp\u0101r\u0113j\u0101 izgl\u012Bt\u012Bba, pamatizgl\u012B\
      t\u012Bbas otr\u0101 posma (7.-9. klase) programmas"
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - LVA-EDU-03
    - LVA-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
  - country_entry_id: LVA-EDU-08
    national_label_en: Vocational basic education, implemented without limitations
      to previous educational attainment
    national_label_local: "Profesion\u0101l\u0101 pamatizgl\u012Bt\u012Bba, \u012B\
      stenojama bez iepriek\u0161\u0113j\u0101s izgl\u012Bt\u012Bbas ierobe\u017E\
      ojuma"
    entry_age: 13
    duration_years: 1
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - LVA-EDU-03
    - LVA-EDU-04
    cum_years_schooling: 7
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
  - country_entry_id: LVA-EDU-09
    national_label_en: Vocational education (acquisition of 2nd level professional
      qualification), for children who have not completed full basic education. Duration
      of programme 3 years.
    national_label_local: "Arodizgl\u012Bt\u012Bba (2.l\u012Bme\u0146a profesion\u0101\
      l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113c da\u013C\u0113jas pamatizgl\u012B\
      t\u012Bbas programmas apguves. M\u0101c\u012Bbu ilgums 3 gadi."
    entry_age: 17
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - LVA-EDU-03
    - LVA-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
  - country_entry_id: LVA-EDU-10
    national_label_en: Secondary (upper secondary) General Education implemented after
      acquisition of basic education
    national_label_local: "Visp\u0101r\u0113j\u0101 vid\u0113j\u0101 izgl\u012Bt\u012B\
      ba, \u012Bstenojama p\u0113c pamatizgl\u012Bt\u012Bbas ieguves"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - LVA-EDU-05
    - LVA-EDU-06
    - LVA-EDU-07
    - LVA-EDU-08
    - LVA-EDU-09
    cum_years_schooling: 10
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    cum_years_status: computed
    review_flags: &id001
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
  - country_entry_id: LVA-EDU-11
    national_label_en: Upper Secondary General education, acquisition of full upper
      secondary level education, following vocational education prog.32.00(1). Duration
      of programme 1 year.
    national_label_local: "Visp\u0101r\u0113j\u0101 vid\u0113j\u0101 izgl\u012Bt\u012B\
      ba, turpin\u0101jums izgl\u012Bt\u012Bbas programmai ar kodu 32. M\u0101c\u012B\
      bu ilgums 1 gads."
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - LVA-EDU-05
    - LVA-EDU-06
    - LVA-EDU-07
    - LVA-EDU-08
    - LVA-EDU-09
    cum_years_schooling: 8
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
  - country_entry_id: LVA-EDU-12
    national_label_en: Vocational education (acquisition of 2nd level professional
      qualification), implemented after acquisition of basic education. Duration of
      programme 1 year.
    national_label_local: "Arodizgl\u012Bt\u012Bba (2.l\u012Bme\u0146a profesion\u0101\
      l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113c pamatizgl\u012Bt\u012B\
      bas ieguves. M\u0101c\u012Bbu ilgums 1 gads."
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - LVA-EDU-05
    - LVA-EDU-06
    - LVA-EDU-07
    - LVA-EDU-08
    - LVA-EDU-09
    cum_years_schooling: 8
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
  - country_entry_id: LVA-EDU-13
    national_label_en: Vocational education (acquisition of 2nd level professional
      qualification), implemented after acquisition of basic education. Duration of
      programme 3 years.
    national_label_local: "Arodizgl\u012Bt\u012Bba (2.l\u012Bme\u0146a profesion\u0101\
      l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113c pamatizgl\u012Bt\u012B\
      bas ieguves. M\u0101c\u012Bbu ilgums 3 gadi."
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - LVA-EDU-05
    - LVA-EDU-06
    - LVA-EDU-07
    - LVA-EDU-08
    - LVA-EDU-09
    cum_years_schooling: 10
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
  - country_entry_id: LVA-EDU-14
    national_label_en: Upper-secondary vocational education (acquisition of 3rd level
      professional qualification), implemented after acquisition of basic education.
      Duration of programme 4 years.
    national_label_local: "Profesion\u0101l\u0101 vid\u0113j\u0101 izgl\u012Bt\u012B\
      ba (3.l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101cija), \u012Bstenojama\
      \ p\u0113c pamatizgl\u012Bt\u012Bbas ieguves. M\u0101c\u012Bbu ilgums 4 gadi."
    entry_age: 16
    duration_years: 4
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - LVA-EDU-05
    - LVA-EDU-06
    - LVA-EDU-07
    - LVA-EDU-08
    - LVA-EDU-09
    cum_years_schooling: 11
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
  - country_entry_id: LVA-EDU-15
    national_label_en: Upper-secondary vocational education(acquisition of 3rd level
      professional qualification) following vocational education prog.32.00(1) and
      32.00(2). Duration of programme 2 years.
    national_label_local: "Profesion\u0101l\u0101 vid\u0113j\u0101 izgl\u012Bt\u012B\
      ba (3. l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101cija), turpin\u0101\
      jums izgl\u012Bt\u012Bbas programmai ar kodu 32.00(1) un 32.00 (2). M\u0101\
      c\u012Bbu ilgums 2 gadi."
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - LVA-EDU-05
    - LVA-EDU-06
    - LVA-EDU-07
    - LVA-EDU-08
    - LVA-EDU-09
    cum_years_schooling: 9
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
  - country_entry_id: LVA-EDU-16
    national_label_en: Vocational education (acquisition of 2nd level professional
      qualification), implemented after acquisition of general or vocational secondary
      education. Duration of programme 1 year.
    national_label_local: "Arodizgl\u012Bt\u012Bba (2.l\u012Bme\u0146a profesion\u0101\
      l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113c visp\u0101r\u0113j\u0101\
      s vai profesion\u0101l\u0101s vid\u0113j\u0101s izgl\u012Bt\u012Bbas ieguves.\
      \ M\u0101c\u012Bbu ilgums 1 gads."
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-17
    national_label_en: Upper-secondary vocational education(acquisition of 3rd level
      professional qualification) implemented  after acquisition of general secondary
      education. Duration of programme 1,5-3 years.
    national_label_local: "Profesion\u0101l\u0101 vid\u0113j\u0101 izgl\u012Bt\u012B\
      ba (3. l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101cija), \u012Bstenojama\
      \ p\u0113c visp\u0101r\u0113j\u0101s vid\u0113j\u0101s izgl\u012Bt\u012Bbas\
      \ ieguves. M\u0101c\u012Bbu ilgums 1,5-3 gadi."
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-17
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-18
    national_label_en: First level of professional higher (college) education  (acquisition
      of 4th level professional qualification), implemented after acquisition of general
      or vocational secondary education. Duration of programme 2-3 years (short cycle).
    national_label_local: "1.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ (koled\u017Eas) izgl\u012Bt\u012Bba (4.l\u012Bme\u0146a profesion\u0101l\u0101\
      \ kvalifik\u0101cija), \u012Bstenojama p\u0113c visp\u0101r\u0113j\u0101s vai\
      \ profesion\u0101l\u0101s vid\u0113j\u0101s izgl\u012Bt\u012Bbas ieguves.  Studiju\
      \ ilgums pilna laika studij\u0101s  2\u20133 gadi."
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 12
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-18
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-19
    national_label_en: Academic higher education (bachelor degree) implemented after
      acquisition of general or vocational scondary education. Duration of programme
      34 years.
    national_label_local: "Akad\u0113misk\u0101 izgl\u012Bt\u012Bba (bakalaura gr\u0101\
      ds), \u012Bstenojama p\u0113c visp\u0101r\u0113j\u0101s vai profesion\u0101\
      l\u0101s vid\u0113j\u0101s izgl\u012Bt\u012Bbas ieguves. Studiju ilgums pilna\
      \ laika studij\u0101s \u2013 3\u20134 gadi"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 13
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-19
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-20
    national_label_en: Second level of professional higher education (acquisition
      of 5th level professional qualification and a degree of professional bachelor)
      or second level of professional higher education (acquisition of 5th level professional
      qualification) implemented af
    national_label_local: "2.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ izgl\u012Bt\u012Bba (5.l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101\
      cija) un profesion\u0101l\u0101 bakalaura gr\u0101ds) vai 2.l\u012Bme\u0146\
      a profesion\u0101l\u0101 augst\u0101k\u0101 izgl\u012Bt\u012Bba (5.l\u012Bme\u0146\
      a profesion\u0101l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113c visp\u0101\
      rej\u0101s vai profesion\u0101l\u0101s vid\u0113j\u0101s izgl\u012Bt\u012B"
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 14
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-20
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-21
    national_label_en: Second level of professional higher education (acquisition
      of 5th level professional qualification) continuation of college (short cycle)
      education. Duration of programme 1-2 years.  Cumulative duration in higher education
      at least 4 years.
    national_label_local: "2.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ izgl\u012Bt\u012Bba (5.l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101\
      cija), turpin\u0101jums koled\u017Eas izgl\u012Bt\u012Bbai. Studiju ilgums pilna\
      \ laika studij\u0101s \u2013 vismaz 1\u20132 gadi. Kop\u0113jais pilna laika\
      \ studiju ilgums \u2013 vismaz 4 gadi"
    entry_age: 21
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-21
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-22
    national_label_en: Second level of professional higher education (acquisition
      of 5th level professional qualification and a degree of professional bachelor)
      or second level of professional higher education (acquisition of 5th level professional
      qualification) implemented af
    national_label_local: "2.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ izgl\u012Bt\u012Bba (5.l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101\
      cija) un profesion\u0101l\u0101 bakalaura gr\u0101ds) vai 2.l\u012Bme\u0146\
      a profesion\u0101l\u0101 augst\u0101k\u0101 izgl\u012Bt\u012Bba (5.l\u012Bme\u0146\
      a profesion\u0101l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113c visp\u0101\
      rej\u0101s vai profesion\u0101l\u0101s vid\u0113j\u0101s izgl\u012Bt\u012B"
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 14
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-22
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-23
    national_label_en: Second level of professional higher education (acquisition
      of 5th level professional qualification), implemented after acquisition of bachelor's
      degree. Duration of programme at least 1 year. Cumulative duration in higher
      education at least 4 years.
    national_label_local: "2.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ izgl\u012Bt\u012Bba (5.l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101\
      cija), \u012Bstenojama p\u0113c bakalaura, profesion\u0101l\u0101 bakalaura\
      \ gr\u0101da vai 5.l\u012Bme\u0146a profesion\u0101l\u0101s kvalifik\u0101cijas\
      \ ieguves. Studiju ilgums pilna laika studij\u0101s \u2013 vismaz gads. Kop\u0113\
      jais pilna lai"
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 11
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-23
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-24
    national_label_en: Academic higher education (Master's degree), implemented after
      acquisition of bachelor's degree. Duration of programme 12 years. Cumulative
      duration in higher education at least 5 years.
    national_label_local: "Akad\u0113misk\u0101 izgl\u012Bt\u012Bba (ma\u0123istra\
      \ gr\u0101ds), \u012Bstenojama p\u0113c bakalaura vai profesion\u0101l\u0101\
      \ bakalaura gr\u0101da ieguvas. Studiju ilgums pilna laika studij\u0101s 1\u2013\
      2 gadi. Kop\u0113jais pilna laika studiju ilgums \u2013 vismaz 5 gadi"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - LVA-EDU-19
    - LVA-EDU-20
    - LVA-EDU-21
    - LVA-EDU-22
    - LVA-EDU-23
    cum_years_schooling: 12
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-21
    - LVA-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
    - 'minimum parent path selected from: LVA-EDU-19, LVA-EDU-20, LVA-EDU-21, LVA-EDU-22,
      LVA-EDU-23'
  - country_entry_id: LVA-EDU-25
    national_label_en: "Second level of professional higher education (acquisition\
      \ of 5th level professional qualification), implemented after  acquisition of\
      \ general or vocational secondary education. Duration of programme at least\
      \ 5 years. \n (Medical doctor, pharmacist, dentis"
    national_label_local: "2.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ izgl\u012Bt\u012Bba (5.l\u012Bme\u0146a profesion\u0101l\u0101 kvalifik\u0101\
      cija), \u012Bstenojama p\u0113c visp\u0101r\u0113j\u0101s vai profesion\u0101\
      l\u0101s vid\u0113j\u0101s izgl\u012Bt\u012Bbas ieguves. Studiju ilgums pilna\
      \ laika studij\u0101s - vismaz 5 gadi. \n(\u0100rstu,farmaceitu, zob\u0101rstu\
      \  u.c. gar\u0101s programma"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - LVA-EDU-10
    cum_years_schooling: 15
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-25
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: LVA-EDU-26
    national_label_en: Second level of professional higher education (professional
      Master's degree or  5th level professional qualification), implemented after
      acquisition bachelor's or professional bachelor's degree. Duration of programme
      at least 1 year. Cumulative duration i
    national_label_local: "2.l\u012Bme\u0146a profesion\u0101l\u0101 augst\u0101k\u0101\
      \ izgl\u012Bt\u012Bba (profesion\u0101l\u0101 ma\u0123istra gr\u0101ds vai 5.l\u012B\
      me\u0146a profesion\u0101l\u0101 kvalifik\u0101cija), \u012Bstenojama p\u0113\
      c bakalaura, profesion\u0101l\u0101 bakalaura gr\u0101da vai 5.l\u012Bme\u0146\
      a profesion\u0101l\u0101s kvalifik\u0101cijas ieguves. Studiju ilgums pilna\
      \ laika studij\u0101s \u2013"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - LVA-EDU-19
    - LVA-EDU-20
    - LVA-EDU-21
    - LVA-EDU-22
    - LVA-EDU-23
    cum_years_schooling: 12
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-21
    - LVA-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
    - 'minimum parent path selected from: LVA-EDU-19, LVA-EDU-20, LVA-EDU-21, LVA-EDU-22,
      LVA-EDU-23'
  - country_entry_id: LVA-EDU-27
    national_label_en: Doctorate (Doctor's degree), implemented after master's or
      professional master's degree or after acquisition of programme 49. Duration
      of programme 3-4 years.
    national_label_local: "Doktora studijas (doktora gr\u0101ds), \u012Bstenojama\
      \ p\u0113c ma\u0123istra vai profesion\u0101l\u0101 ma\u0123istra gr\u0101da\
      \ ieguves vai turpin\u0101jums izgl\u012Bt\u012Bbas programmai ar kodu 49. Studiju\
      \ ilgums pilna laika studij\u0101s 3-4 gadi."
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - LVA-EDU-19
    - LVA-EDU-20
    - LVA-EDU-21
    - LVA-EDU-22
    - LVA-EDU-23
    cum_years_schooling: 14
    cum_years_computation_path:
    - LVA-EDU-03
    - LVA-EDU-08
    - LVA-EDU-10
    - LVA-EDU-21
    - LVA-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: LVA-EDU-03, LVA-EDU-04'
    - 'minimum parent path selected from: LVA-EDU-05, LVA-EDU-06, LVA-EDU-07, LVA-EDU-08,
      LVA-EDU-09'
    - 'minimum parent path selected from: LVA-EDU-19, LVA-EDU-20, LVA-EDU-21, LVA-EDU-22,
      LVA-EDU-23'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Latvia.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LVA-SAN-01
    source_category_code: private_domestic_connection_to_sewage_system
    national_label_en: Private domestic connection to sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Private flush/toilet > to piped sewer system
    jmp_id: flush_toilets.private_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 73
  - country_entry_id: LVA-SAN-02
    source_category_code: private_flush_to_septic_tank
    national_label_en: Private flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 74
  - country_entry_id: LVA-SAN-03
    source_category_code: shared_domestic_connection_to_sewage_system
    national_label_en: Shared domestic connection to sewage system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to piped sewer
      system
    jmp_id: flush_toilets.public_shared_flush_toilet.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 79
  - country_entry_id: LVA-SAN-04
    source_category_code: shared_flush_to_septic_tank
    national_label_en: Shared flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > Public/shared flush/toilet > to septic tank
    jmp_id: flush_toilets.public_shared_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 80
  - country_entry_id: LVA-SAN-05
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
  - country_entry_id: LVA-SAN-06
    source_category_code: uncovered_dry_latrine_without_privacy
    national_label_en: Uncovered dry latrine (without privacy)
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: false
    shared_flag: false
    source_row: 108
  - country_entry_id: LVA-SAN-07
    source_category_code: private_covered_dry_latrine_with_privacy
    national_label_en: Private covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine with
      slab/covered latrine
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 114
  - country_entry_id: LVA-SAN-08
    source_category_code: shared_covered_dry_latrine_with_privacy
    national_label_en: Shared covered dry latrine (with privacy)
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: true
    shared_flag: true
    source_row: 122
  - country_entry_id: LVA-SAN-09
    source_category_code: private_pour_flush_latrine
    national_label_en: Private pour flush latrine
    national_label_local: Private pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: false
    source_row: 91
  - country_entry_id: LVA-SAN-10
    source_category_code: shared_pour_flush_latrine
    national_label_en: Shared pour flush latrine
    national_label_local: Public/shared pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: false
    shared_flag: true
    source_row: 97
  - country_entry_id: LVA-SAN-11
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
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_LVA_Latvia_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: LVA-WAS-01
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
  - country_entry_id: LVA-WAS-02
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
  - country_entry_id: LVA-WAS-03
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
  - country_entry_id: LVA-WAS-04
    source_category_code: rainwater_into_tank_or_cistern
    national_label_en: Rainwater (into tank or cistern )
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 87
  - country_entry_id: LVA-WAS-05
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
  - country_entry_id: LVA-WAS-06
    source_category_code: piped_water_through_house_connection_or_yard
    national_label_en: Piped water through house connection or yard
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: true
    shared_flag: false
    source_row: 38
  - country_entry_id: LVA-WAS-07
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
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_LVA_Latvia_0.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

