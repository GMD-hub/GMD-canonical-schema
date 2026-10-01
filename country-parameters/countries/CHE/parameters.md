---
country_id: CTY-CHE
iso3: CHE
schema_version: '0.2'
status: draft
country_name: CHE
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHE-EDU-01
    national_label_en: Kindergarten
    national_label_local: "Kindergarten , Eingangsstufe, Ecole enfantine , cycle \xE9\
      l\xE9mentaire\nScuola dell\u2019infanzia"
    entry_age: 4
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
  - country_entry_id: CHE-EDU-02
    national_label_en: Special needs education programmes
    national_label_local: "Besonderer Lehrplan, programme d'enseignement sp\xE9cial,\
      \ programma scolastico speciale"
    entry_age: 4
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
  - country_entry_id: CHE-EDU-03
    national_label_en: primary school
    national_label_local: "Primarschule, \xE9cole primaire, scuola elementare"
    entry_age: 6
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
    - CHE-EDU-03
    cum_years_status: computed
    review_flags: []
  - country_entry_id: CHE-EDU-04
    national_label_en: special needs education programmes
    national_label_local: "Besonderer Lehrplan, programme d'enseignement sp\xE9cial,\
      \ programma scolastico speciale"
    entry_age: 5
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
    - CHE-EDU-04
    cum_years_status: computed
    review_flags: []
  - country_entry_id: CHE-EDU-05
    national_label_en: secondary education, first stage
    national_label_local: Sekundarschule, Realschule, Oberschule, (Pro-)Gymnasium,
      Cycle d'orientation, Scuola media
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - CHE-EDU-03
    - CHE-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
  - country_entry_id: CHE-EDU-06
    national_label_en: special needs education programmes
    national_label_local: "Besonderer Lehrplan, programme d'enseignement sp\xE9cial,\
      \ programma scolastico speciale"
    entry_age: 11
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - CHE-EDU-03
    - CHE-EDU-04
    cum_years_schooling: 9
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-06
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
  - country_entry_id: CHE-EDU-07
    national_label_en: bridge-year courses, 1 year
    national_label_local: "Br\xFCckenangebote, offres transitoires, formazione transitoria"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-08
    national_label_en: general education programmes, short
    national_label_local: "Allgemeinbildende Schule, \xE9cole de culture g\xE9n\xE9\
      rale, 2 Jahre/ann\xE9es"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-08
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-09
    national_label_en: "specialised middle schools \u2013 3 years"
    national_label_local: "Fachmittelschule, \xE9cole de culture g\xE9n\xE9rale, scuola\
      \ specializzate, 3 Jahre/ann\xE9es"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-09
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-10
    national_label_en: specialised baccalaureat gives acces to univerities of applied
      sciences
    national_label_local: "Fachmaturit\xE4tsschule, Maturit\xE9 sp\xE9cialis\xE9e"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-10
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-11
    national_label_en: vocational baccalaureat, dual system, 3 and 4 years
    national_label_local: "Berufsmaturit\xE4t, maturit\xE9 professionnelle, maturit\xE0\
      \ professionale, 3 und/et 4 Jahre/ann\xE9es"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-11
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-12
    national_label_en: vocational baccalaureate after obtention of the certificate
      of vocational education, 1 year
    national_label_local: "Berufsmaturit\xE4t nach der Lehre, maturit\xE9 professionnelle\
      \ apr\xE8s l'apprentissage, 1 Jahr/ann\xE9e"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-12
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-13
    national_label_en: school preparing for the university entrance certificate
    national_label_local: "Gymnasiale Maturit\xE4t, maturit\xE9 gymnasiale, maturit\xE0"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-13
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-14
    national_label_en: Foreign (non Swiss) programmes giving acces giving acces to
      the tertiary level
    national_label_local: "Ausl\xE4ndisches allg. Ausbildung mit Zugang zur n\xE4\
      chsten Stufe, formation g\xE9n\xE9rale avec acc\xE8s direct \xE0 l\u2019enseignement\
      \ sup\xE9rieur"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-14
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-15
    national_label_en: preparatory course for vocational education, 1 year
    national_label_local: "Vorlehre, pr\xE9apprentissage, corsi preparatori"
    entry_age: 15
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 19
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 10
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-15
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-16
    national_label_en: elementary vocational education, dual system
    national_label_local: "Anlehre, formation professionnelle \xE9l\xE9mentaire, formazione\
      \ empirica"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 20
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-16
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-17
    national_label_en: vocational education, in dual system 2 years.
    national_label_local: "2-j\xE4hrige berufliche Grundbildung mit Berufsattest /\
      \  formation professionnelle initiale de deux ans aboutissant \xE0 une attestation\
      \ f\xE9d\xE9rale de formation professionnelle / formazione professionale di\
      \ base della durata di due anni con certificato federale d"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 21
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-17
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-18
    national_label_en: vocational education without regulation on the federal level
    national_label_local: "Nicht vom Bund reglementierte berufliche Grundbildung /\
      \ Formation professionnelle initiale non r\xE9glement\xE9e par la LFPr"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 22
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-18
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-19
    national_label_en: 'vocational education, in school and in the dual system, 3
      and 4 years leading to a Federal Diploma of Vocational

      Education and Training (Federal VET Diploma)'
    national_label_local: "Berufliche Grundbildung mit Eidgen\xF6ssischem F\xE4higkeitszeugnis\
      \ 3-4 Jahre/  formation professionnelle initiale aboutissant \xE0 un certificat\
      \ f\xE9d\xE9ral de capacit\xE9 3 - 4 ans/ formazione professionale di base della\
      \ durata di due anni con attestato federale di cap"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 23
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-19
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-20
    national_label_en: 'Trade school

      Education and Training (Federal VET Diploma)'
    national_label_local: Handelsmittelschule, Ecoles de commerce, Scuole medie di
      commercio
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 24
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-20
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-21
    national_label_en: vocational education without regulation on the federal level
      giving acces to the next level
    national_label_local: "Nicht vom Bund reglementierte berufliche Grundbildung /\
      \ Formation professionnelle initiale non r\xE9glement\xE9e par la LFPr"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 25
    parent_country_entry_ids:
    - CHE-EDU-05
    - CHE-EDU-06
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-21
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
  - country_entry_id: CHE-EDU-22
    national_label_en: preparatory course for University for persons with vocational
      baccalaureate
    national_label_local: Passerellenlehrgang / passerelle / passerella
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-22
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-23
    national_label_en: Other preparatory programmes giving acces to the tertiary level
    national_label_local: "Andere \xDCbergangsausbildungen Sek. II- Terti\xE4rstufe\
      \ / Autres formations transitoires sec. II \u2013 degr\xE9 tertiaire"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-23
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-24
    national_label_en: Other complementary programmes for people having attained a
      upper secondary qualification
    national_label_local: "Andere Zusatzausbildungen / Autres formations compl\xE9\
      mentaires"
    entry_age: 19
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-24
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-25
    national_label_en: higher vocational education, stage I (no regulation on the
      federal level)
    national_label_local: "Nicht vom Bund reglementierte h\xF6here Berufsbildung I"
    entry_age: 20
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-25
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-26
    national_label_en: university of applied science diploma
    national_label_local: "Fachhochschule Diplom, haute \xE9cole sp\xE9cialis\xE9\
      e dipl\xF4me, scuole universitarie professionali diploma"
    entry_age: 20
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 13
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-26
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-27
    national_label_en: university bachelor
    national_label_local: "Hochschulen, hautes \xE9coles; Bachelor"
    entry_age: 19
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 13
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-28
    national_label_en: university of applied science, post-graduate / Master of Advanced
      Studies
    national_label_local: "Fachhochschule Nachdiplom/Master of Advanced Studies, haute\
      \ \xE9cole sp\xE9cialis\xE9e dipl\xF4me postgrade /Master of Advanced Studies"
    entry_age: 23
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - CHE-EDU-26
    - CHE-EDU-27
    - CHE-EDU-28
    - CHE-EDU-29
    - CHE-EDU-30
    - CHE-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-31
    - CHE-EDU-28
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
    - 'minimum parent path selected from: CHE-EDU-26, CHE-EDU-27, CHE-EDU-28, CHE-EDU-29,
      CHE-EDU-30, CHE-EDU-31'
  - country_entry_id: CHE-EDU-29
    national_label_en: Federal PET Diploma examination / higher vocational education,
      stage I
    national_label_local: "Berufspr\xFCfung, examen professionnel"
    entry_age: 20
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-29
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-30
    national_label_en: PET College /technical school
    national_label_local: "H\xF6here Fachschule, \xE9cole sup\xE9rieure"
    entry_age: 18
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-31
    national_label_en: Postgraduate course PET college
    national_label_local: "h\xF6here Fachschule Nachdiplom / Dipl\xF4me postgrade\
      \ d'une \xE9cole sup\xE9rieure / Diploma postgraduate di scuole professionali\
      \ superiori"
    entry_age: 24
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 11
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-31
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-32
    national_label_en: university diploma
    national_label_local: "Hochschulen, hautes \xE9coles universitaire ; Lizentiat,\
      \ licence, Diplom"
    entry_age: 19
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 15
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-32
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-33
    national_label_en: university master
    national_label_local: "Hochschulen, hautes \xE9coles; Master"
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - CHE-EDU-26
    - CHE-EDU-27
    - CHE-EDU-28
    - CHE-EDU-29
    - CHE-EDU-30
    - CHE-EDU-31
    cum_years_schooling: 13
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-31
    - CHE-EDU-33
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
    - 'minimum parent path selected from: CHE-EDU-26, CHE-EDU-27, CHE-EDU-28, CHE-EDU-29,
      CHE-EDU-30, CHE-EDU-31'
  - country_entry_id: CHE-EDU-34
    national_label_en: teacher education diploma for upper secondary level teaching
      / university post-graduate /Master of Advanced Studies
    national_label_local: "Lehrdiplom Sek. II / Universit\xE4t Weiterbildung /Aufbau-\
      \ und Vertiefungsstudien, Dipl\xF4me des enseignants sec. II / formation continue\
      \ universitaire/ Etudes sp\xE9cialis\xE9es et approfondies"
    entry_age: 24
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - CHE-EDU-26
    - CHE-EDU-27
    - CHE-EDU-28
    - CHE-EDU-29
    - CHE-EDU-30
    - CHE-EDU-31
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-31
    - CHE-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
    - 'minimum parent path selected from: CHE-EDU-26, CHE-EDU-27, CHE-EDU-28, CHE-EDU-29,
      CHE-EDU-30, CHE-EDU-31'
  - country_entry_id: CHE-EDU-35
    national_label_en: Advanced Federal PET diploma examination / higher vocational
      education, stage II
    national_label_local: "H\xF6here Fachpr\xFCfung, examen professionnel sup\xE9\
      rieur"
    entry_age: 23
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - CHE-EDU-07
    - CHE-EDU-08
    - CHE-EDU-09
    - CHE-EDU-10
    - CHE-EDU-13
    - CHE-EDU-14
    - CHE-EDU-20
    cum_years_schooling: 12
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
  - country_entry_id: CHE-EDU-36
    national_label_en: university doctorate
    national_label_local: Doktorat, doctorat
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - CHE-EDU-32
    - CHE-EDU-33
    - CHE-EDU-34
    - CHE-EDU-35
    cum_years_schooling: 15
    cum_years_computation_path:
    - CHE-EDU-03
    - CHE-EDU-05
    - CHE-EDU-07
    - CHE-EDU-31
    - CHE-EDU-34
    - CHE-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: CHE-EDU-03, CHE-EDU-04'
    - 'minimum parent path selected from: CHE-EDU-05, CHE-EDU-06'
    - 'minimum parent path selected from: CHE-EDU-07, CHE-EDU-08, CHE-EDU-09, CHE-EDU-10,
      CHE-EDU-13, CHE-EDU-14, CHE-EDU-20'
    - 'minimum parent path selected from: CHE-EDU-26, CHE-EDU-27, CHE-EDU-28, CHE-EDU-29,
      CHE-EDU-30, CHE-EDU-31'
    - 'minimum parent path selected from: CHE-EDU-32, CHE-EDU-33, CHE-EDU-34, CHE-EDU-35'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Switzerland.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: CHE-SUBNAT-01
    survey_labels: 1-CH01
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH01
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH01
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH01
    geo_nvar: NAME_LATN
    geo_name: "R\xE9gion l\xE9manique"
    source_row: 2148
  - country_entry_id: CHE-SUBNAT-02
    survey_labels: 2-CH02
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH02
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH02
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH02
    geo_nvar: NAME_LATN
    geo_name: Espace Mittelland
    source_row: 2149
  - country_entry_id: CHE-SUBNAT-03
    survey_labels: 3-CH03
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH03
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH03
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH03
    geo_nvar: NAME_LATN
    geo_name: Nordwestschweiz
    source_row: 2150
  - country_entry_id: CHE-SUBNAT-04
    survey_labels: 4-CH04
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH04
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH04
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH04
    geo_nvar: NAME_LATN
    geo_name: "Z\xFCrich"
    source_row: 2151
  - country_entry_id: CHE-SUBNAT-05
    survey_labels: 5-CH05
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH05
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH05
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH05
    geo_nvar: NAME_LATN
    geo_name: Ostschweiz
    source_row: 2152
  - country_entry_id: CHE-SUBNAT-06
    survey_labels: 6-CH06
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH06
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH06
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH06
    geo_nvar: NAME_LATN
    geo_name: Zentralschweiz
    source_row: 2153
  - country_entry_id: CHE-SUBNAT-07
    survey_labels: 7-CH07
    survey_variables: subnatid
    gmd_subnatid1: CHE_2021_NUTS2_CH07
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: CHE_2021_NUTS2_CH07
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: CH07
    geo_nvar: NAME_LATN
    geo_name: Ticino
    source_row: 2154
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
---

