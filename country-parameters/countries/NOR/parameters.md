---
country_id: CTY-NOR
iso3: NOR
schema_version: '0.2'
status: draft
country_name: NOR
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: NOR-EDU-01
    national_label_en: Kindergartens and Family kindergartens, 0-2 years
    national_label_local: "Barnehage og Familiebarnehage, 0-2 \xE5ringer"
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
  - country_entry_id: NOR-EDU-02
    national_label_en: Kindergartens and Family kindergartens, 3-5 years
    national_label_local: "Barnehage og Familiebarnehage, 3-5 \xE5ringer"
    entry_age: 3
    duration_years: 3
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
  - country_entry_id: NOR-EDU-03
    national_label_en: Primary level
    national_label_local: Barnetrinnet
    entry_age: 6
    duration_years: 7
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 7
    parent_country_entry_ids: []
    cum_years_schooling: 7
    cum_years_computation_path:
    - NOR-EDU-03
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: NOR-EDU-04
    national_label_en: Lower secondary level
    national_label_local: Ungdomstrinnet
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 8
    parent_country_entry_ids:
    - NOR-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-05
    national_label_en: Upper secondary, alternative course
    national_label_local: "Videreg\xE5ende oppl\xE6ring, Alternativ oppl\xE6ring"
    entry_age: 16
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 11
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-06
    national_label_en: The training candidate scheme
    national_label_local: "L\xE6rekandidatordningen"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-07
    national_label_en: Upper secondary education, basic competence, study preparation
      education program
    national_label_local: "Videreg\xE5ende oppl\xE6ring, grunnkompetanse, studieforberedende\
      \ utdanningsprogram"
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-08
    national_label_en: Upper secondary, general programmes
    national_label_local: "Videreg\xE5ende oppl\xE6ring, studieforberedende utdanningsprogram"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-09
    national_label_en: Preparatory courses
    national_label_local: "P\xE5bygg/forkurs utdanningsprogram"
    entry_age: 17
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-10
    national_label_en: Upper secondary, vocational programmes
    national_label_local: "Videreg\xE5ende oppl\xE6ring, yrkesfaglige utdanningsprogram"
    entry_age: 16
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 13
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-11
    national_label_en: Folk high school
    national_label_local: "Videreg\xE5ende utdanning ved folkeh\xF8gskoler"
    entry_age: 19
    duration_years: 0
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 10
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-12
    national_label_en: The Certificate of Practice
    national_label_local: Praksisbrev
    entry_age: 16
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - NOR-EDU-04
    cum_years_schooling: 12
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: NOR-EDU-13
    national_label_en: Post-secondary vocational education, short (< 2 years)/Tertiary
      vocational education
    national_label_local: "Halv\xE5rig til halvannet\xE5rig h\xF8yere yrkesfaglig\
      \ utdanning (fagskoleutdanning)"
    entry_age: 19
    duration_years: 0
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 10
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-14
    national_label_en: Post-secondary vocational education, 2 years/Tertiary vocational
      education
    national_label_local: "2-\xE5rig h\xF8yere yrkesfaglig utdanning (fagskoleutdanning)"
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 12
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-15
    national_label_en: University college short-degree degree programme, 2 years
    national_label_local: "H\xF8gskolekandidatutdanning"
    entry_age: 19
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 12
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-16
    national_label_en: Bachelor programme, 3 years
    national_label_local: "Bachelorutdannning, 3-\xE5rig"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 13
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-17
    national_label_en: Bachelor programme, 4 years
    national_label_local: "Bachelorutdanning, 4-\xE5rig"
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-18
    national_label_en: Programmes in general teacher education and special subject
      teacher education in practical-aesthetic subjects - outside the Ba-Ma cycle
    national_label_local: "Allmennl\xE6rerutdanning,  grunnskolel\xE6rerutdanning\
      \ og fagl\xE6rerutdanning i praktisk-estetiske fag"
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-19
    national_label_en: Specialisation courses
    national_label_local: Videreutdanning
    entry_age: 22
    duration_years: 31
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 41
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-20
    national_label_en: Master programme, 1 - 1,5 yrs
    national_label_local: "Masterutdanning, 1 - 1,5-\xE5rig"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - NOR-EDU-15
    - NOR-EDU-16
    - NOR-EDU-17
    - NOR-EDU-18
    - NOR-EDU-19
    cum_years_schooling: 13
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
  - country_entry_id: NOR-EDU-21
    national_label_en: Master programme, 2 years
    national_label_local: "Masterutdanning, 2-\xE5rig"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - NOR-EDU-15
    - NOR-EDU-16
    - NOR-EDU-17
    - NOR-EDU-18
    - NOR-EDU-19
    cum_years_schooling: 14
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
  - country_entry_id: NOR-EDU-22
    national_label_en: Master programme, 5 years
    national_label_local: "Masterutdanning, 5-\xE5rig"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - NOR-EDU-15
    - NOR-EDU-16
    - NOR-EDU-17
    - NOR-EDU-18
    - NOR-EDU-19
    cum_years_schooling: 17
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
  - country_entry_id: NOR-EDU-23
    national_label_en: Experience-based Master's programme
    national_label_local: Erfaringsbasert masterprogram
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - NOR-EDU-15
    - NOR-EDU-16
    - NOR-EDU-17
    - NOR-EDU-18
    - NOR-EDU-19
    cum_years_schooling: 13
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
  - country_entry_id: NOR-EDU-24
    national_label_en: Long professional programmes in Theology, Psychology, Medicine
      and Veterinary Science
    national_label_local: Lengre profesjonsutdanninger
    entry_age: 19
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 16
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-25
    national_label_en: Specialist courses/Supplementary courses for foreign education
    national_label_local: Spesialistutdanninger
    entry_age: 24
    duration_years: 31
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - NOR-EDU-05
    - NOR-EDU-06
    - NOR-EDU-07
    - NOR-EDU-08
    - NOR-EDU-09
    - NOR-EDU-11
    - NOR-EDU-12
    cum_years_schooling: 41
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
  - country_entry_id: NOR-EDU-26
    national_label_en: PhD programme
    national_label_local: Doktorgradsprogram for Philosophiae doctor (ph.d.)
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - NOR-EDU-20
    - NOR-EDU-21
    - NOR-EDU-22
    - NOR-EDU-23
    - NOR-EDU-24
    - NOR-EDU-25
    cum_years_schooling: 16
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-20
    - NOR-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
    - 'minimum parent path selected from: NOR-EDU-20, NOR-EDU-21, NOR-EDU-22, NOR-EDU-23,
      NOR-EDU-24, NOR-EDU-25'
  - country_entry_id: NOR-EDU-27
    national_label_en: Artistic Research Fellowship Programme
    national_label_local: Stipendprogram for kunstnerisk utviklingsarbeid
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - NOR-EDU-20
    - NOR-EDU-21
    - NOR-EDU-22
    - NOR-EDU-23
    - NOR-EDU-24
    - NOR-EDU-25
    cum_years_schooling: 16
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-20
    - NOR-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
    - 'minimum parent path selected from: NOR-EDU-20, NOR-EDU-21, NOR-EDU-22, NOR-EDU-23,
      NOR-EDU-24, NOR-EDU-25'
  - country_entry_id: NOR-EDU-28
    national_label_en: Doctorate
    national_label_local: Doctor philosophiae (dr.philos.)
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - NOR-EDU-20
    - NOR-EDU-21
    - NOR-EDU-22
    - NOR-EDU-23
    - NOR-EDU-24
    - NOR-EDU-25
    cum_years_schooling: 16
    cum_years_computation_path:
    - NOR-EDU-03
    - NOR-EDU-04
    - NOR-EDU-09
    - NOR-EDU-15
    - NOR-EDU-20
    - NOR-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: NOR-EDU-05, NOR-EDU-06, NOR-EDU-07, NOR-EDU-08,
      NOR-EDU-09, NOR-EDU-11, NOR-EDU-12'
    - 'minimum parent path selected from: NOR-EDU-15, NOR-EDU-16, NOR-EDU-17, NOR-EDU-18,
      NOR-EDU-19'
    - 'minimum parent path selected from: NOR-EDU-20, NOR-EDU-21, NOR-EDU-22, NOR-EDU-23,
      NOR-EDU-24, NOR-EDU-25'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Norway.xlsx
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

