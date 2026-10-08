---
country_id: CTY-FRA
iso3: FRA
schema_version: '0.2'
status: draft
country_name: FRA
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: null
  effective_to: null
  selectors: null
  value:
  - country_entry_id: FRA-EDU-01
    national_label_en: Pre-primary education
    national_label_local: "Enseignement pr\xE9\xE9l\xE9mentaire"
    entry_age: 3
    duration_years: 3
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
  - country_entry_id: FRA-EDU-02
    national_label_en: Primary education
    national_label_local: Enseignement primaire
    entry_age: 6
    duration_years: 5
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 6
    parent_country_entry_ids: []
    cum_years_schooling: 5
    cum_years_computation_path:
    - FRA-EDU-02
    cum_years_status: computed
    review_flags: &id001 []
  - country_entry_id: FRA-EDU-03
    national_label_en: Secondary education (1st cycle)
    national_label_local: "Enseignement du premier cycle du second degr\xE9 \u2013\
      \ Coll\xE8ge"
    entry_age: 11
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_incomplete
    source_row: 7
    parent_country_entry_ids:
    - FRA-EDU-02
    cum_years_schooling: 9
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-04
    national_label_en: Vocational secondary education (2nd cycle) preparing to Certificat
      d'aptitude professionnelle (CAP)
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant au CAP"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 8
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-04
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-05
    national_label_en: Vocational secondary education (2nd cycle) preparing to Certificat
      d'aptitude professionnelle (CAP)
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant au CAP"
    entry_age: 15
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 9
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-05
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-06
    national_label_en: "Vocational secondary education (2nd cycle) preparing to Mention\
      \ Compl\xE9mentaire (MC)"
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant \xE0 une mention compl\xE9mentaire ou \xE9quivalent"
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 10
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-06
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-07
    national_label_en: "Vocational secondary education (2nd cycle) preparing to Mention\
      \ Compl\xE9mentaire (MC)"
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant \xE0 une mention compl\xE9mentaire ou \xE9quivalent"
    entry_age: 17
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 11
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-07
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-08
    national_label_en: Vocational secondary education (2nd cycle) in health and social
      services institutions, preparing to qualifications of child care assistants  and
      equivalents
    national_label_local: "Enseignement de second cycle professionnel des \xE9coles\
      \ sanitaires et sociales conduisant aux dipl\xF4mes d'auxiliaires de pu\xE9\
      riculture et \xE9quivalents"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 12
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-08
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-09
    national_label_en: Vocational secondary education (2nd cycle) preparing to Brevet
      Professionnel (BP)
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant au brevet professionnel"
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 13
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-09
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-10
    national_label_en: Vocational secondary education (2nd cycle) preparing to Bac
      Professionnel or to an equivalent diploma
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant au Bacccalaur\xE9at Professionnel ou \xE0 un \xE9quivalent"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 14
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-10
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-11
    national_label_en: Vocational secondary education (2nd cycle) preparing to Bac
      Professionnel or to an equivalent diploma
    national_label_local: "Enseignement de second cycle professionnel du second degr\xE9\
      \ conduisant au Bacccalaur\xE9at Professionnel ou \xE0 un \xE9quivalent"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 15
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-11
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-12
    national_label_en: "General secondary education (2nd cycle), preparing to Bac\
      \ g\xE9n\xE9ral, technologique and Brevet de technicien"
    national_label_local: "Enseignement de second cycle g\xE9n\xE9ral du second degr\xE9\
      \ conduisant au baccalaur\xE9at g\xE9n\xE9ral ou technologique ou au brevet\
      \ de technicien"
    entry_age: 15
    duration_years: 3
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 16
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 12
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-13
    national_label_en: "Vocational secondary education (2nd cycle) in health and care\
      \ institutions preparing to qualifications of Moniteur \xE9ducateur (and equivalent)"
    national_label_local: "Enseignement de second cycle professionnel des \xE9coles\
      \ sociales conduisant aux dipl\xF4mes de moniteurs \xE9ducateurs et \xE9quivalents"
    entry_age: 18
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 17
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 11
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-13
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-14
    national_label_en: "Vocational secondary training programme (ISCED 3) preparing\
      \ to Titre Habilit\xE9 (TH)"
    national_label_local: "Formation de second cycle professionnel du second degr\xE9\
      \ conduisant \xE0 un titre professionnel"
    entry_age: 18
    duration_years: 1
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_incomplete
    source_row: 18
    parent_country_entry_ids:
    - FRA-EDU-03
    cum_years_schooling: 10
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-14
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-15
    national_label_en: Bridge programmes (university) to allow access to levels 5
      or 6
    national_label_local: "Enseignement pr\xE9-universitaire"
    entry_age: 20
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 13
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-15
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-16
    national_label_en: Preparatory courses to competitive entrance examinations
    national_label_local: "Classes de mise \xE0 niveau des STS, classes pr\xE9paratoires\
      \ aux \xE9coles param\xE9dicales, aux \xE9coles d'arts et aux concours de la\
      \ fonction publique niveau bac, dipl\xF4mes d'universit\xE9 post secondaires\
      \ et certificats d'\xE9coles"
    entry_age: 18
    duration_years: 1
    isced_level: '4'
    isced_label: ISCED 4 Post-secondary non-tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 20
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 13
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-16
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-17
    national_label_en: School certificates in arts, university degrees
    national_label_local: "Certificats d'\xE9cole en arts, dipl\xF4mes d'universit\xE9\
      \ bac \xE0 bac+1"
    entry_age: 18
    duration_years: 0
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 21
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 12
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-17
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-18
    national_label_en: Professional tertiary education in universities (IUT)
    national_label_local: Enseignement en institut universitaire de technologie (IUT)
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 22
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-18
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-19
    national_label_en: "Professional tertiary education preparing to Brevets de techniciens\
      \ sup\xE9rieurs (BTS)"
    national_label_local: "Enseignement conduisant aux Brevets de techniciens sup\xE9\
      rieurs et \xE9quivalent"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 23
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-19
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-20
    national_label_en: Professional tertiary education in universities and other institutions
      preparing to health and care qualifications and to few diploma in technics,
      law and arts
    national_label_local: "Enseignement dispens\xE9 en \xE9coles sp\xE9cialis\xE9\
      es ou \xE0 l'universit\xE9 conduisant principalement aux dipl\xF4mes professionnels\
      \ param\xE9dicaux et sociaux, et \xE0 quelques dipl\xF4mes professionnels de\
      \ technologie, de droit et d'art, commerce"
    entry_age: 18
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 24
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-20
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-21
    national_label_en: "Academic tertiary education preparing students to the competitive\
      \ entrance examinations for \u201Cgrandes \xE9coles\u201D"
    national_label_local: "Enseignement des classes pr\xE9paratoires aux grandes \xE9\
      coles (CPGE)"
    entry_age: 17
    duration_years: 2
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 25
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-21
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-22
    national_label_en: University education, 1st graduation
    national_label_local: "Enseignement universitaire de premier grade (LMD) conduisant\
      \ \xE0 la Licence ou dipl\xF4me d'\xE9coles priv\xE9es ou grandes \xE9coles,\
      \ EHESS, Dauphine et IEP niveau licence"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 26
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-22
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-23
    national_label_en: University education, 1st graduation
    national_label_local: "Enseignement universitaire de premier grade (LMD) conduisant\
      \ \xE0 la Licence professionnelle"
    entry_age: 18
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 27
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 13
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-23
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-24
    national_label_en: Business schools in 3 years
    national_label_local: "Enseignement en \xE9cole de commerce conduisant au niveau\
      \ bac+3"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 28
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-24
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-25
    national_label_en: Professional tertiary education in 3 years in health (nurses
      from 2012), diploma in applied arts, accountability
    national_label_local: "Formations param\xE9dicales de grade Licence, d'arts appliqu\xE9\
      s, de comptabilit\xE9, diverses formations conduisant au niveau bac+3"
    entry_age: 18
    duration_years: 3
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 29
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-25
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-26
    national_label_en: Preparation for the entrance exam and training certificate
      for lawyers, Preparation for the entrance exam to the National School of Magistracy,
      Preparation for administrative exams
    national_label_local: "Pr\xE9paration \xE0 l'examen d'entr\xE9e et certificat\
      \ de formation \xE0 la profession d'avocat, Pr\xE9paration au concours d'acc\xE8\
      s \xE0 l'Ecole Nationale de la Magistrature, Pr\xE9paration aux concours administratifs\
      \ de niveau \xE9quivalent."
    entry_age: 21
    duration_years: 0
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 30
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 12
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-26
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-27
    national_label_en: Academic tertiary education in universities and diverse institutions
      leading to Master-type degrees
    national_label_local: "Enseignements g\xE9n\xE9raux d'\xE9coles, de facult\xE9\
      s priv\xE9es et d'universit\xE9s conduisant au niveau bac+5"
    entry_age: 18
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 31
    parent_country_entry_ids:
    - FRA-EDU-21
    - FRA-EDU-22
    - FRA-EDU-23
    - FRA-EDU-24
    - FRA-EDU-25
    cum_years_schooling: 16
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-23
    - FRA-EDU-27
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: FRA-EDU-21, FRA-EDU-22, FRA-EDU-23, FRA-EDU-24,
      FRA-EDU-25'
  - country_entry_id: FRA-EDU-28
    national_label_en: Professional tertiary education preparing to an engineer degree
    national_label_local: "Enseignement conduisant \xE0 un dipl\xF4me d'ing\xE9nieur"
    entry_age: 20
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 32
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 15
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-28
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-29
    national_label_en: Business schools in 5 years
    national_label_local: "Enseignement en \xE9cole de commerce conduisant  au niveau\
      \ bac+5"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 33
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 17
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-29
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-30
    national_label_en: Professional tertiary education in applied arts, veterinaries,
      etc. leading to Master-type degrees
    national_label_local: "Enseignement en \xE9cole sup\xE9rieure d'art, d'architecture,\
      \ d'\xE9cole v\xE9t\xE9rinaire conduisant au niveau bac+5"
    entry_age: 18
    duration_years: 5
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 34
    parent_country_entry_ids:
    - FRA-EDU-21
    - FRA-EDU-22
    - FRA-EDU-23
    - FRA-EDU-24
    - FRA-EDU-25
    cum_years_schooling: 18
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-23
    - FRA-EDU-30
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: FRA-EDU-21, FRA-EDU-22, FRA-EDU-23, FRA-EDU-24,
      FRA-EDU-25'
  - country_entry_id: FRA-EDU-31
    national_label_en: Programmes (universities) in medicine, pharmacy, odontology
      and midwife studies.
    national_label_local: "Enseignement en sant\xE9 (m\xE9decine, pharmacie, chirurgie\
      \ dentaire, kin\xE9, osth\xE9opathie, odontologie) dans les universit\xE9s,\
      \ \xE9tudes de sages-femmes."
    entry_age: 18
    duration_years: 6
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 35
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 18
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-31
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-32
    national_label_en: University education, 2nd graduation
    national_label_local: Enseignement universitaire de deuxieme grade conduisant
      au master
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 36
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-32
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-33
    national_label_en: Education for teachers in ESPE
    national_label_local: "Enseignement des \xE9tablissements de formation des professionnels\
      \ de l'enseignement (ESPE)"
    entry_age: 21
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 37
    parent_country_entry_ids:
    - FRA-EDU-12
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-33
    cum_years_status: computed
    review_flags: *id001
  - country_entry_id: FRA-EDU-34
    national_label_en: Second tertiary programmes in professional fields (law, accountability)
      leading to a master type degree
    national_label_local: "Enseignements professionnels de droit, de comptabilit\xE9\
      , d'affaires et dipl\xF4mes d'universit\xE9"
    entry_age: 21
    duration_years: 3
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 38
    parent_country_entry_ids:
    - FRA-EDU-21
    - FRA-EDU-22
    - FRA-EDU-23
    - FRA-EDU-24
    - FRA-EDU-25
    cum_years_schooling: 16
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-23
    - FRA-EDU-34
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: FRA-EDU-21, FRA-EDU-22, FRA-EDU-23, FRA-EDU-24,
      FRA-EDU-25'
  - country_entry_id: FRA-EDU-35
    national_label_en: Specialized tertiary professional degrees following a Master
    national_label_local: "Enseignements conduisant aux dipl\xF4mes compl\xE9mentaires\
      \ de sant\xE9 (capacit\xE9,\u2026) et diverses sp\xE9cialisations"
    entry_age: 22
    duration_years: 1
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 39
    parent_country_entry_ids:
    - FRA-EDU-21
    - FRA-EDU-22
    - FRA-EDU-23
    - FRA-EDU-24
    - FRA-EDU-25
    cum_years_schooling: 14
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-23
    - FRA-EDU-35
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: FRA-EDU-21, FRA-EDU-22, FRA-EDU-23, FRA-EDU-24,
      FRA-EDU-25'
  - country_entry_id: FRA-EDU-36
    national_label_en: University education, 3rd cycle, doctorate
    national_label_local: "Enseignement de troisi\xE8me cycle des \xE9tudes universitaires\
      \ conduisant au Doctorat"
    entry_age: 23
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 40
    parent_country_entry_ids:
    - FRA-EDU-26
    - FRA-EDU-27
    - FRA-EDU-28
    - FRA-EDU-29
    - FRA-EDU-30
    - FRA-EDU-31
    - FRA-EDU-32
    - FRA-EDU-33
    - FRA-EDU-34
    - FRA-EDU-35
    cum_years_schooling: 15
    cum_years_computation_path:
    - FRA-EDU-02
    - FRA-EDU-03
    - FRA-EDU-12
    - FRA-EDU-26
    - FRA-EDU-36
    cum_years_status: computed
    review_flags:
    - 'minimum parent path selected from: FRA-EDU-26, FRA-EDU-27, FRA-EDU-28, FRA-EDU-29,
      FRA-EDU-30, FRA-EDU-31, FRA-EDU-32, FRA-EDU-33, FRA-EDU-34, FRA-EDU-35'
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_France.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2013
  effective_to: 2013
  selectors: null
  value:
  - country_entry_id: FRA-SUBNAT-01
    survey_labels: 1-FR10
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR10
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR10
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR10
    geo_nvar: NAME_LATN
    geo_name: "\xCEle de France"
    source_row: 4862
  - country_entry_id: FRA-SUBNAT-02
    survey_labels: 10-FR42
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR42
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR42
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR42
    geo_nvar: NAME_LATN
    geo_name: Alsace
    source_row: 4863
  - country_entry_id: FRA-SUBNAT-03
    survey_labels: 11-FR43
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR43
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR43
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR43
    geo_nvar: NAME_LATN
    geo_name: "Franche-Comt\xE9"
    source_row: 4864
  - country_entry_id: FRA-SUBNAT-04
    survey_labels: 12-FR51
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR51
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR51
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR51
    geo_nvar: NAME_LATN
    geo_name: Pays de la Loire
    source_row: 4865
  - country_entry_id: FRA-SUBNAT-05
    survey_labels: 13-FR52
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR52
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR52
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR52
    geo_nvar: NAME_LATN
    geo_name: Bretagne
    source_row: 4866
  - country_entry_id: FRA-SUBNAT-06
    survey_labels: 14-FR53
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR53
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR53
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR53
    geo_nvar: NAME_LATN
    geo_name: Poitou-Charentes
    source_row: 4867
  - country_entry_id: FRA-SUBNAT-07
    survey_labels: 15-FR61
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR61
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR61
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR61
    geo_nvar: NAME_LATN
    geo_name: Aquitaine
    source_row: 4868
  - country_entry_id: FRA-SUBNAT-08
    survey_labels: 16-FR62
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR62
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR62
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR62
    geo_nvar: NAME_LATN
    geo_name: "Midi-Pyr\xE9n\xE9es"
    source_row: 4869
  - country_entry_id: FRA-SUBNAT-09
    survey_labels: 17-FR63
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR63
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR63
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR63
    geo_nvar: NAME_LATN
    geo_name: Limousin
    source_row: 4870
  - country_entry_id: FRA-SUBNAT-10
    survey_labels: 18-FR71
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR71
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR71
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR71
    geo_nvar: NAME_LATN
    geo_name: "Rh\xF4ne-Alpes"
    source_row: 4871
  - country_entry_id: FRA-SUBNAT-11
    survey_labels: 19-FR72
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR72
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR72
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR72
    geo_nvar: NAME_LATN
    geo_name: Auvergne
    source_row: 4872
  - country_entry_id: FRA-SUBNAT-12
    survey_labels: 2-FR21
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR21
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR21
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR21
    geo_nvar: NAME_LATN
    geo_name: Champagne-Ardenne
    source_row: 4873
  - country_entry_id: FRA-SUBNAT-13
    survey_labels: 20-FR81
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR81
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR81
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR81
    geo_nvar: NAME_LATN
    geo_name: Languedoc-Roussillon
    source_row: 4874
  - country_entry_id: FRA-SUBNAT-14
    survey_labels: 21-FR82
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR82
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR82
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR82
    geo_nvar: NAME_LATN
    geo_name: "Provence-Alpes-C\xF4te d'Azur"
    source_row: 4875
  - country_entry_id: FRA-SUBNAT-15
    survey_labels: 22-FR83
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR83
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR83
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR83
    geo_nvar: NAME_LATN
    geo_name: Corse
    source_row: 4876
  - country_entry_id: FRA-SUBNAT-16
    survey_labels: 3-FR22
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR22
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR22
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR22
    geo_nvar: NAME_LATN
    geo_name: Picardie
    source_row: 4877
  - country_entry_id: FRA-SUBNAT-17
    survey_labels: 4-FR23
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR23
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR23
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR23
    geo_nvar: NAME_LATN
    geo_name: Haute-Normandie
    source_row: 4878
  - country_entry_id: FRA-SUBNAT-18
    survey_labels: 5-FR24
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR24
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR24
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR24
    geo_nvar: NAME_LATN
    geo_name: Centre
    source_row: 4879
  - country_entry_id: FRA-SUBNAT-19
    survey_labels: 6-FR25
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR25
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR25
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR25
    geo_nvar: NAME_LATN
    geo_name: Basse-Normandie
    source_row: 4880
  - country_entry_id: FRA-SUBNAT-20
    survey_labels: 7-FR26
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR26
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR26
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR26
    geo_nvar: NAME_LATN
    geo_name: Bourgogne
    source_row: 4881
  - country_entry_id: FRA-SUBNAT-21
    survey_labels: 8-FR30
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR30
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR30
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR30
    geo_nvar: NAME_LATN
    geo_name: Nord - Pas-de-Calais
    source_row: 4882
  - country_entry_id: FRA-SUBNAT-22
    survey_labels: 9-FR41
    survey_variables: subnatid
    gmd_subnatid1: FRA_2013_NUTS2_FR41
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2013_NUTS2_FR41
    geo_year: '2013'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR41
    geo_nvar: NAME_LATN
    geo_name: Lorraine
    source_row: 4883
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: null
    human_reviewed: false
    reviewer: null
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2021
  effective_to: null
  selectors: null
  value:
  - country_entry_id: FRA-SUBNAT-01
    survey_labels: 1-FR10
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FR10
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FR10
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FR10
    geo_nvar: NAME_LATN
    geo_name: Ile-de-France
    source_row: 5170
  - country_entry_id: FRA-SUBNAT-02
    survey_labels: 10-FRF2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRF2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRF2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRF2
    geo_nvar: NAME_LATN
    geo_name: Champagne-Ardenne
    source_row: 5171
  - country_entry_id: FRA-SUBNAT-03
    survey_labels: 11-FRF3
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRF3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRF3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRF3
    geo_nvar: NAME_LATN
    geo_name: Lorraine
    source_row: 5172
  - country_entry_id: FRA-SUBNAT-04
    survey_labels: 12-FRG0
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRG0
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRG0
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRG0
    geo_nvar: NAME_LATN
    geo_name: Pays de la Loire
    source_row: 5173
  - country_entry_id: FRA-SUBNAT-05
    survey_labels: 13-FRH0
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRH0
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRH0
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRH0
    geo_nvar: NAME_LATN
    geo_name: Bretagne
    source_row: 5174
  - country_entry_id: FRA-SUBNAT-06
    survey_labels: 14-FRI1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRI1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRI1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRI1
    geo_nvar: NAME_LATN
    geo_name: Aquitaine
    source_row: 5175
  - country_entry_id: FRA-SUBNAT-07
    survey_labels: 15-FRI2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRI2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRI2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRI2
    geo_nvar: NAME_LATN
    geo_name: Limousin
    source_row: 5176
  - country_entry_id: FRA-SUBNAT-08
    survey_labels: 16-FRI3
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRI3
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRI3
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRI3
    geo_nvar: NAME_LATN
    geo_name: Poitou-Charentes
    source_row: 5177
  - country_entry_id: FRA-SUBNAT-09
    survey_labels: 17-FRJ1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRJ1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRJ1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRJ1
    geo_nvar: NAME_LATN
    geo_name: Languedoc-Roussillon
    source_row: 5178
  - country_entry_id: FRA-SUBNAT-10
    survey_labels: 18-FRJ2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRJ2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRJ2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRJ2
    geo_nvar: NAME_LATN
    geo_name: "Midi-Pyr\xE9n\xE9es"
    source_row: 5179
  - country_entry_id: FRA-SUBNAT-11
    survey_labels: 19-FRK1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRK1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRK1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRK1
    geo_nvar: NAME_LATN
    geo_name: Auvergne
    source_row: 5180
  - country_entry_id: FRA-SUBNAT-12
    survey_labels: 2-FRB0
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRB0
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRB0
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRB0
    geo_nvar: NAME_LATN
    geo_name: "Centre \u2014 Val de Loire"
    source_row: 5181
  - country_entry_id: FRA-SUBNAT-13
    survey_labels: 20-FRK2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRK2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRK2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRK2
    geo_nvar: NAME_LATN
    geo_name: "Rh\xF4ne-Alpes"
    source_row: 5182
  - country_entry_id: FRA-SUBNAT-14
    survey_labels: 21-FRL0
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRL0
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRL0
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRL0
    geo_nvar: NAME_LATN
    geo_name: "Provence-Alpes-C\xF4te d\u2019Azur"
    source_row: 5183
  - country_entry_id: FRA-SUBNAT-15
    survey_labels: 22-FRM0
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRM0
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRM0
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRM0
    geo_nvar: NAME_LATN
    geo_name: Corse
    source_row: 5184
  - country_entry_id: FRA-SUBNAT-16
    survey_labels: 3-FRC1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRC1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRC1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRC1
    geo_nvar: NAME_LATN
    geo_name: Bourgogne
    source_row: 5185
  - country_entry_id: FRA-SUBNAT-17
    survey_labels: 4-FRC2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRC2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRC2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRC2
    geo_nvar: NAME_LATN
    geo_name: "Franche-Comt\xE9"
    source_row: 5186
  - country_entry_id: FRA-SUBNAT-18
    survey_labels: 5-FRD1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRD1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRD1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRD1
    geo_nvar: NAME_LATN
    geo_name: Basse-Normandie
    source_row: 5187
  - country_entry_id: FRA-SUBNAT-19
    survey_labels: 6-FRD2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRD2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRD2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRD2
    geo_nvar: NAME_LATN
    geo_name: Haute-Normandie
    source_row: 5188
  - country_entry_id: FRA-SUBNAT-20
    survey_labels: 7-FRE1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRE1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRE1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRE1
    geo_nvar: NAME_LATN
    geo_name: Nord-Pas de Calais
    source_row: 5189
  - country_entry_id: FRA-SUBNAT-21
    survey_labels: 8-FRE2
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRE2
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRE2
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRE2
    geo_nvar: NAME_LATN
    geo_name: Picardie
    source_row: 5190
  - country_entry_id: FRA-SUBNAT-22
    survey_labels: 9-FRF1
    survey_variables: subnatid
    gmd_subnatid1: FRA_2021_NUTS2_FRF1
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: true
    is_rep_subnat2: false
    is_rep_subnat3: false
    is_rep_subnat4: false
    representative_level: 1
    gmd_subnatidsurvey: FRA_2021_NUTS2_FRF1
    geo_year: '2021'
    geo_source: NUTS
    geo_level: '2'
    geo_idvar: NUTS_ID
    geo_id: FRF1
    geo_nvar: NAME_LATN
    geo_name: Alsace
    source_row: 5191
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
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

