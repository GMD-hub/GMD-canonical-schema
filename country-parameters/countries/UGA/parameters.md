---
country_id: CTY-UGA
iso3: UGA
schema_version: '0.2'
status: draft
country_name: UGA
parameters:
- parameter_id: PARAM-EDU-LEVEL-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: UGA-EDU-01
    national_label_en: Early childhood education (pre-primary)
    national_label_local: Early childhood education (pre-primary)
    entry_age: 3
    duration_years: 3
    isced_level: '0'
    isced_label: ISCED 0 Early childhood education
    gmd_educat4_target: no_education
    gmd_educat5_target: no_education
    gmd_educat7_target: none
    source_row: 7
  - country_entry_id: UGA-EDU-02
    national_label_en: Primary
    national_label_local: Primary
    entry_age: 6
    duration_years: 7
    isced_level: '1'
    isced_label: ISCED 1 Primary
    gmd_educat4_target: primary
    gmd_educat5_target: primary_incomplete
    gmd_educat7_target: primary_incomplete
    source_row: 8
  - country_entry_id: UGA-EDU-03
    national_label_en: Lower secondary (O' level)
    national_label_local: Lower secondary (O' level)
    entry_age: 13
    duration_years: 4
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 9
  - country_entry_id: UGA-EDU-04
    national_label_en: Post-primary, (vocational)
    national_label_local: Post-primary, (vocational)
    entry_age: 13
    duration_years: 3
    isced_level: '2'
    isced_label: ISCED 2 Lower secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: lower_secondary
    gmd_educat7_target: lower_secondary_complete
    source_row: 10
  - country_entry_id: UGA-EDU-05
    national_label_en: Upper secondary (A' level)
    national_label_local: Upper secondary (A' level)
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 11
  - country_entry_id: UGA-EDU-06
    national_label_en: Upper secondary (other, e.g. Business, Technical Vocational
      Education and Training (BTVET) and Primary Teachers Colleges programmes)
    national_label_local: Upper secondary (other, e.g. Business, Technical Vocational
      Education and Training (BTVET) and Primary Teachers Colleges programmes)
    entry_age: 17
    duration_years: 2
    isced_level: '3'
    isced_label: ISCED 3 Upper secondary
    gmd_educat4_target: secondary
    gmd_educat5_target: upper_secondary
    gmd_educat7_target: upper_secondary_complete
    source_row: 12
  - country_entry_id: UGA-EDU-07
    national_label_en: Diploma programmes (After UACE)
    national_label_local: Diploma programmes (After UACE)
    entry_age: 19
    duration_years: 2
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 13
  - country_entry_id: UGA-EDU-08
    national_label_en: Diploma programmes (After certificate 2)
    national_label_local: Diploma programmes (After certificate 2)
    entry_age: 19
    duration_years: 3
    isced_level: '5'
    isced_label: ISCED 5 Short-cycle tertiary
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 14
  - country_entry_id: UGA-EDU-09
    national_label_en: Bachelor's degree programme
    national_label_local: Bachelor's degree programme
    entry_age: 19
    duration_years: 4
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 15
  - country_entry_id: UGA-EDU-10
    national_label_en: long Bachelor's degree programme
    national_label_local: Long Bachelor's degree programme
    entry_age: 19
    duration_years: 5
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 16
  - country_entry_id: UGA-EDU-11
    national_label_en: Postgraduate studies
    national_label_local: Postgraduate studies
    entry_age: 22
    duration_years: 1
    isced_level: '6'
    isced_label: ISCED 6 Bachelor or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 17
  - country_entry_id: UGA-EDU-12
    national_label_en: Master's degree
    national_label_local: Master's degree
    entry_age: 22
    duration_years: 2
    isced_level: '7'
    isced_label: ISCED 7 Master or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 18
  - country_entry_id: UGA-EDU-13
    national_label_en: Doctoral studies
    national_label_local: Doctoral studies
    entry_age: 24
    duration_years: 3
    isced_level: '8'
    isced_label: ISCED 8 Doctoral or equivalent
    gmd_educat4_target: tertiary
    gmd_educat5_target: tertiary
    gmd_educat7_target: tertiary
    source_row: 19
  provenance:
    source: extraction\10_source\country-parameters-inputs\ISCED\ISCED_2011_Mapping_Uganda.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-GEO-GMD-CROSSWALK
  effective_from: 2024
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: UGA-SUBNAT-01
    survey_labels: 1 - Central | 1 – Central
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: UGA_2024_GAUL1_1675
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UGA_2024_GAUL1_1675
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '1675'
    geo_nvar: gaul1_name
    geo_name: Central
    source_row: 17100
  - country_entry_id: UGA-SUBNAT-02
    survey_labels: 2 - Eastern | 2 – Eastern
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: UGA_2024_GAUL1_1676
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UGA_2024_GAUL1_1676
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '1676'
    geo_nvar: gaul1_name
    geo_name: Eastern
    source_row: 17101
  - country_entry_id: UGA-SUBNAT-03
    survey_labels: 3 - Northern | 3 – Northern
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: UGA_2024_GAUL1_1677
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UGA_2024_GAUL1_1677
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '1677'
    geo_nvar: gaul1_name
    geo_name: Northern
    source_row: 17102
  - country_entry_id: UGA-SUBNAT-04
    survey_labels: 4 - Western | 4 – Western
    survey_variables: subnatid | subnatid1
    gmd_subnatid1: UGA_2024_GAUL1_1678
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: yes
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 1
    gmd_subnatidsurvey: UGA_2024_GAUL1_1678
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '1'
    geo_idvar: gaul1_code
    geo_id: '1678'
    geo_nvar: gaul1_name
    geo_name: Western
    source_row: 17103
  - country_entry_id: UGA-SUBNAT-05
    survey_labels: 0 - Kampala | 1 - KAMPALA | 1 - Kampala
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAUL2_106253
    geo_year: '2024'
    geo_source: GAUL
    geo_level: '2'
    geo_idvar: gaul2_code
    geo_id: '106253'
    geo_nvar: gaul2_name
    geo_name: Kampala
    source_row: 17120
  - country_entry_id: UGA-SUBNAT-06
    survey_labels: 1 - Central1 | 2 - Buganda South
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_1
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '1'
    geo_nvar: gaul2_name
    geo_name: Bukomansimbi & Butambala & Buvuma & Gomba & Kalangala & Kalungu & Kyotera
      & Lwengo & Lyantonde & Masaka & Mpigi & Rakai & Ssembabule
    source_row: 17121
  - country_entry_id: UGA-SUBNAT-07
    survey_labels: 10 - West Nile | 11 - West Nile
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_10
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '10'
    geo_nvar: gaul2_name
    geo_name: Adjumani & Arua & Koboko & Madi Okollo & Maracha & Moyo & Nebbi & Obongi
      & Pakwach & Yumbe & Zombo
    source_row: 17122
  - country_entry_id: UGA-SUBNAT-08
    survey_labels: 11 - Bunyoro | 12 - Bunyoro
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_11
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '11'
    geo_nvar: gaul2_name
    geo_name: Buliisa & Hoima & Kagadi & Kakumiro & Kibaale & Kikuube & Kiryandongo
      & Masindi
    source_row: 17123
  - country_entry_id: UGA-SUBNAT-09
    survey_labels: 12 - Tooro | 13 - Tooro | 13 - Toro
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_12
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '12'
    geo_nvar: gaul2_name
    geo_name: Bundibugyo & Bunyangabu & Kabarole & Kamwenge & Kasese & Kitagwenda
      & Kyegegwa & Kyenjojo & Ntoroko
    source_row: 17124
  - country_entry_id: UGA-SUBNAT-10
    survey_labels: 13 - Ankole | 14 - Ankole
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_13
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '13'
    geo_nvar: gaul2_name
    geo_name: Buhweju & Bushenyi & Ibanda & Isingiro & Kazo & Kiruhura & Mbarara &
      Mitooma & Ntungamo & Rubirizi & Rwampara & Sheema
    source_row: 17125
  - country_entry_id: UGA-SUBNAT-11
    survey_labels: 14 - Kigezi | 15 - Kigezi
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_14
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '14'
    geo_nvar: gaul2_name
    geo_name: Kabale & Kanungu & Kisoro & Rubanda & Rukiga & Rukungiri
    source_row: 17126
  - country_entry_id: UGA-SUBNAT-12
    survey_labels: 2 - Central2 | 3 - Buganda North
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_2
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '2'
    geo_nvar: gaul2_name
    geo_name: Buikwe & Kassanda & Kayunga & Kiboga & Kyankwanzi & Luwero & Mityana
      & Mubende & Mukono & Nakaseke & Nakasongola & Wakiso
    source_row: 17127
  - country_entry_id: UGA-SUBNAT-13
    survey_labels: 3 - Busoga | 4 - Busoga
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_3
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '3'
    geo_nvar: gaul2_name
    geo_name: Bugweri & Buyende & Iganga & Jinja & Kaliro & Kamuli & Luuka & Mayuge
      & Namayingo & Namutumba
    source_row: 17128
  - country_entry_id: UGA-SUBNAT-14
    survey_labels: 4 - Bukedi | 5 - Bukedi
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_4
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '4'
    geo_nvar: gaul2_name
    geo_name: Budaka & Busia & Butaleja & Butebo & Kibuku & Pallisa & Tororo
    source_row: 17129
  - country_entry_id: UGA-SUBNAT-15
    survey_labels: 5 - Bugishu | 6 - Elgon
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_5
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '5'
    geo_nvar: gaul2_name
    geo_name: Bududa & Bulambuli & Kapchorwa & Kween & Manafwa & Mbale & Namisindwa
      & Sironko
    source_row: 17130
  - country_entry_id: UGA-SUBNAT-16
    survey_labels: 6 - Teso | 7 - Teso
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_6
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '6'
    geo_nvar: gaul2_name
    geo_name: Amuria & Bukedea & Kaberamaido & Kalaki & Kapelebyong & Katakwi & Kumi
      & Ngora & Serere & Soroti
    source_row: 17131
  - country_entry_id: UGA-SUBNAT-17
    survey_labels: 7 - Karamoja | 8 - Karamoja
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_7
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '7'
    geo_nvar: gaul2_name
    geo_name: Abim & Amudat & Kaabong & Karenga & Kotido & Moroto & Nabilatuk & Nakapiripirit
      & Napak
    source_row: 17132
  - country_entry_id: UGA-SUBNAT-18
    survey_labels: 8 - Lango | 9 - Lango
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_8
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '8'
    geo_nvar: gaul2_name
    geo_name: Alebtong & Amolatar & Apac & Dokolo & Kole & Kwania & Lira & Otuke &
      Oyam
    source_row: 17133
  - country_entry_id: UGA-SUBNAT-19
    survey_labels: 10 - Acholi | 9 - Acholi
    survey_variables: subnatidsurvey
    gmd_subnatid1: ''
    gmd_subnatid2: ''
    gmd_subnatid3: ''
    gmd_subnatid4: ''
    is_rep_subnat1: no
    is_rep_subnat2: no
    is_rep_subnat3: no
    is_rep_subnat4: no
    representative_level: 0
    gmd_subnatidsurvey: UGA_2024_GAULx_9
    geo_year: '2024'
    geo_source: GAUL
    geo_level: x
    geo_idvar: sample
    geo_id: '9'
    geo_nvar: gaul2_name
    geo_name: Agago & Amuru & Gulu & Kitgum & Lamwo & Nwoya & Omoro & Pader
    source_row: 17134
  provenance:
    source: extraction\10_source\country-parameters-inputs\GEO\Sub_nat_gmd.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: UGA-SAN-01
    source_category_code: 8_composting
    national_label_en: 8. composting
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: UGA-SAN-02
    source_category_code: 8_composting_toilet
    national_label_en: 8. Composting toilet
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: UGA-SAN-03
    source_category_code: composting_toilet
    national_label_en: Composting toilet
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: UGA-SAN-04
    source_category_code: composting_toilet_ecosan
    national_label_en: composting toilet / ecosan
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: UGA-SAN-05
    source_category_code: ecosan_compost_toilet
    national_label_en: Ecosan (compost toilet)
    national_label_local: Composting toilets
    jmp_classification: Composting toilets
    jmp_id: composting_toilets
    gmd_target: composting
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 128
  - country_entry_id: UGA-SAN-06
    source_category_code: 3_flush_pour_flush_toilets_connected_to_elsewhere
    national_label_en: '3. Flush/pour flush toilets connected to: Elsewhere'
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: UGA-SAN-07
    source_category_code: 3_flush_elsewhere
    national_label_en: 3. flush_elsewhere
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: UGA-SAN-08
    source_category_code: flush_to_open_drain
    national_label_en: Flush To Open Drain
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: UGA-SAN-09
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: UGA-SAN-10
    source_category_code: flush_pour_flush_not_to_sewer_septic_tank
    national_label_en: Flush/ pour flush not to sewer/septic tank
    national_label_local: to elsewhere
    jmp_classification: Flush and pour flush > to elsewhere
    jmp_id: flush_and_pour_flush.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 65
  - country_entry_id: UGA-SAN-11
    source_category_code: 1_flush_pour_flush_toilets_connected_to_piped_sewer_system
    national_label_en: '1. Flush/pour flush toilets connected to: Piped sewer system'
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: UGA-SAN-12
    source_category_code: 1_flush_sewer
    national_label_en: 1. flush_sewer
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: UGA-SAN-13
    source_category_code: flush_to_piped_sewer_system
    national_label_en: flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: UGA-SAN-14
    source_category_code: flush_toilet_to_piped_sewer_system
    national_label_en: Flush toilet to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: UGA-SAN-15
    source_category_code: flush_pour_flush_to_piped_sewer_system
    national_label_en: Flush/pour flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush and pour flush > to piped sewer system
    jmp_id: flush_and_pour_flush.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: UGA-SAN-16
    source_category_code: 13_flush_pour_flush_toilets_connected_to_pit_latrine
    national_label_en: '13. Flush/pour flush toilets connected to: Pit Latrine'
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: UGA-SAN-17
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: UGA-SAN-18
    source_category_code: flushed_toilet_to_pit_latrine
    national_label_en: Flushed toilet to pit latrine
    national_label_local: to pit
    jmp_classification: Flush and pour flush > to pit
    jmp_id: flush_and_pour_flush.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 63
  - country_entry_id: UGA-SAN-19
    source_category_code: 2_flush_pour_flush_toilets_connected_to_septic_tank
    national_label_en: '2. Flush/pour flush toilets connected to: Septic tank'
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: UGA-SAN-20
    source_category_code: 2_flush_septic
    national_label_en: 2. flush_septic
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: UGA-SAN-21
    source_category_code: flush_to_septic_tank
    national_label_en: flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: UGA-SAN-22
    source_category_code: flush_pour_flush_to_septic_tank_or_pit_latrine
    national_label_en: Flush/ pour flush to septic tank or pit latrine
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: UGA-SAN-23
    source_category_code: flushed_toilet_to_septic_tank
    national_label_en: Flushed toilet to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush and pour flush > to septic tank
    jmp_id: flush_and_pour_flush.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 62
  - country_entry_id: UGA-SAN-24
    source_category_code: 4_flush_pour_flush_toilets_connected_to_unknown_not_sure_do_not_know
    national_label_en: '4. Flush/pour flush toilets connected to: Unknown / Not sure
      / Do not know'
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: UGA-SAN-25
    source_category_code: 4_flush_unknown
    national_label_en: 4. flush_unknown
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: UGA-SAN-26
    source_category_code: flush_to_dk_where
    national_label_en: Flush To DK Where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: UGA-SAN-27
    source_category_code: flush_don_t_know_where
    national_label_en: flush, don't know where
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: UGA-SAN-28
    source_category_code: flush_pour_flush_to_unknown
    national_label_en: Flush/pour flush to unknown
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush and pour flush > to unknown place/ not sure/DK
    jmp_id: flush_and_pour_flush.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 64
  - country_entry_id: UGA-SAN-29
    source_category_code: flush_or_pour_flush_toilet
    national_label_en: Flush or pour flush toilet
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-SAN-30
    source_category_code: flush_toilet
    national_label_en: Flush Toilet
    national_label_local: Flush/toilets
    jmp_classification: Flush/toilets
    jmp_id: flush_toilets
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-SAN-31
    source_category_code: flush_toilet_owned
    national_label_en: Flush Toilet (Owned)
    national_label_local: Private flush/toilet
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: UGA-SAN-32
    source_category_code: flush_toilet_private
    national_label_en: Flush toilet private
    national_label_local: Private flush/toilet
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: UGA-SAN-33
    source_category_code: own_flush_toilet
    national_label_en: Own flush toilet
    national_label_local: Private flush/toilet
    jmp_classification: Flush/toilets > Private flush/toilet
    jmp_id: flush_toilets.private_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 72
  - country_entry_id: UGA-SAN-34
    source_category_code: flush_toilet_shared
    national_label_en: Flush Toilet (Shared)
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: UGA-SAN-35
    source_category_code: flush_toilet_shared
    national_label_en: Flush toilet shared
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: UGA-SAN-36
    source_category_code: shared_flush_toilet
    national_label_en: Shared flush toilet
    national_label_local: Public/shared flush/toilet
    jmp_classification: Flush/toilets > Public/shared flush/toilet
    jmp_id: flush_toilets.public_shared_flush_toilet
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 78
  - country_entry_id: UGA-SAN-37
    source_category_code: flush_to_somewhere_else
    national_label_en: flush to somewhere else
    national_label_local: to elsewhere
    jmp_classification: Flush/toilets > to elsewhere
    jmp_id: flush_toilets.to_elsewhere
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: UGA-SAN-38
    source_category_code: flush_to_piped_sewer_system
    national_label_en: Flush to piped sewer system
    national_label_local: to piped sewer system
    jmp_classification: Flush/toilets > to piped sewer system
    jmp_id: flush_toilets.to_piped_sewer_system
    gmd_target: flush_sewer
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: UGA-SAN-39
    source_category_code: flush_to_pit_latrine
    national_label_en: flush to pit latrine
    national_label_local: to pit
    jmp_classification: Flush/toilets > to pit
    jmp_id: flush_toilets.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: UGA-SAN-40
    source_category_code: flush_to_septic_tank
    national_label_en: flush to septic tank
    national_label_local: to septic tank
    jmp_classification: Flush/toilets > to septic tank
    jmp_id: flush_toilets.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 68
  - country_entry_id: UGA-SAN-41
    source_category_code: has_a_flush_toilet
    national_label_en: has a flush toilet
    national_label_local: to unknown place/ not sure/DK
    jmp_classification: Flush/toilets > to unknown place/ not sure/DK
    jmp_id: flush_toilets.to_unknown_place_not_sure_dk
    gmd_target: flush_elsewhere
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-SAN-42
    source_category_code: latrine_pit
    national_label_en: Latrine, Pit
    national_label_local: Dry latrines
    jmp_classification: Latrines > Dry latrines
    jmp_id: latrines.dry_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: no
    shared_flag: no
    source_row: 103
  - country_entry_id: UGA-SAN-43
    source_category_code: pit_latrine
    national_label_en: Pit latrine
    national_label_local: Dry latrines
    jmp_classification: Latrines > Dry latrines
    jmp_id: latrines.dry_latrines
    gmd_target: ''
    gmd_spans: vip|pit_slab|pit_noslab|hanging|bucket|other
    improved_flag: no
    shared_flag: no
    source_row: 103
  - country_entry_id: UGA-SAN-44
    source_category_code: 9_bucket
    national_label_en: 9. bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: UGA-SAN-45
    source_category_code: bucket_toilet
    national_label_en: Bucket toilet
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: UGA-SAN-46
    source_category_code: bucket_pot
    national_label_en: Bucket/pot
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: UGA-SAN-47
    source_category_code: pan_bucket
    national_label_en: Pan/bucket
    national_label_local: Bucket latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Bucket latrine
    jmp_id: latrines.dry_latrines.improved_latrines.bucket_latrine
    gmd_target: bucket
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 110
  - country_entry_id: UGA-SAN-48
    source_category_code: 10_hanging
    national_label_en: 10. hanging
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: UGA-SAN-49
    source_category_code: 10_hanging_toilet_hanging_latrine
    national_label_en: 10. Hanging toilet /Hanging latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: UGA-SAN-50
    source_category_code: hanging_toilet
    national_label_en: Hanging toilet
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: UGA-SAN-51
    source_category_code: hanging_toilet_hanging_latrine
    national_label_en: Hanging Toilet/Hanging Latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: UGA-SAN-52
    source_category_code: hanging_toilet_latrine
    national_label_en: hanging toilet/latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 109
  - country_entry_id: UGA-SAN-53
    source_category_code: 11_other
    national_label_en: 11. other
    national_label_local: Other
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: UGA-SAN-54
    source_category_code: covered_pit_latrine_no_slab
    national_label_en: Covered pit latrine no slab
    national_label_local: Other
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: UGA-SAN-55
    source_category_code: uncovered_pit_latrine_with_a_slab
    national_label_en: Uncovered Pit Latrine with a slab
    national_label_local: Other
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: UGA-SAN-56
    source_category_code: uncovered_pit_latrine_with_slab
    national_label_en: uncovered pit latrine with slab
    national_label_local: Other
    jmp_classification: Latrines > Dry latrines > Improved latrines > Other
    jmp_id: latrines.dry_latrines.improved_latrines.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 111
  - country_entry_id: UGA-SAN-57
    source_category_code: 6_pit_latrine_with_slab
    national_label_en: 6. Pit latrine with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-58
    source_category_code: 6_pit_with_slab
    national_label_en: 6. pit_with_slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-59
    source_category_code: covered_pit_latrine_with_slab
    national_label_en: covered pit latrine - with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-60
    source_category_code: covered_pit_latrine_with_a_slab
    national_label_en: Covered Pit Latrine with a slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-61
    source_category_code: covered_pit_latrine_with_slab
    national_label_en: covered pit latrine with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-62
    source_category_code: covered_uncovered_pit_latrine_with_slab
    national_label_en: Covered/uncovered pit latrine with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-63
    source_category_code: pit_latrine_with_slab
    national_label_en: Pit latrine with slab
    national_label_local: Pit latrine with slab/covered latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      with slab/covered latrine
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_with_slab_covered_latrine
    gmd_target: pit_slab
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-SAN-64
    source_category_code: 7_pit_latrine_without_slab_open_pit
    national_label_en: 7. Pit latrine without slab  / open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-65
    source_category_code: 7_pit_no_slab
    national_label_en: 7. pit_no_slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-66
    source_category_code: covered_uncovered_pit_latrine_without_a_slab
    national_label_en: Covered + Uncovered Pit Latrine without a slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-67
    source_category_code: covered_pit_latrine_without_slab_open_pit
    national_label_en: covered pit latrine - without slab / open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-68
    source_category_code: covered_pit_latrine_without_slab
    national_label_en: Covered Pit latrine without slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-69
    source_category_code: covered_uncovered_pit_latrine_without_slab
    national_label_en: Covered/uncovered pit latrine without slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-70
    source_category_code: pit_latrine_uncovered
    national_label_en: Pit Latrine (Uncovered)
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-71
    source_category_code: pit_latrine_without_slab
    national_label_en: Pit latrine without slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-72
    source_category_code: pit_latrine_without_slab_bucket_toilet
    national_label_en: Pit latrine without slab/bucket toilet
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-73
    source_category_code: pit_latrine_without_slab_open_pit
    national_label_en: Pit latrine without slab/open pit
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-74
    source_category_code: uncovered_pit_latrine
    national_label_en: Uncovered pit latrine
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-75
    source_category_code: uncovered_pit_latrine_with_slab_without_slab
    national_label_en: Uncovered pit latrine (with slab/without slab)
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-76
    source_category_code: uncovered_pit_latrine_no_slab
    national_label_en: uncovered pit latrine no slab
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Improved latrines > Pit latrine
      without slab/open pit
    jmp_id: latrines.dry_latrines.improved_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 108
  - country_entry_id: UGA-SAN-77
    source_category_code: covered_pit_latrine_with_slab_without_slab
    national_label_en: Covered pit latrine (with slab/without slab)
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-SAN-78
    source_category_code: covered_pit_latrine_no_slab
    national_label_en: covered pit latrine no slab
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-SAN-79
    source_category_code: pit_latrine
    national_label_en: Pit Latrine
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-SAN-80
    source_category_code: pit_latrine_covered
    national_label_en: Pit Latrine (Covered)
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-SAN-81
    source_category_code: traditional_pit_toilet
    national_label_en: Traditional pit toilet
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-SAN-82
    source_category_code: uncovered_pit_latrine_with_slab
    national_label_en: Uncovered pit latrine with slab
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.improved_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-SAN-83
    source_category_code: 5_ventilated_improved_pit_latrine
    national_label_en: 5. Ventilated improved pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-84
    source_category_code: 5_vip
    national_label_en: 5. vip
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-85
    source_category_code: ventilated_improved_pit_vip_latrine
    national_label_en: Ventilated improved pit (VIP) latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-86
    source_category_code: ventilated_improved_pit_latrine
    national_label_en: Ventilated improved pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-87
    source_category_code: ventilated_improved_pit_latrine_vip
    national_label_en: Ventilated Improved Pit Latrine (VIP)
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-88
    source_category_code: ventilated_pit_latrine
    national_label_en: Ventilated pit latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-89
    source_category_code: vip
    national_label_en: VIP
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-90
    source_category_code: vip_latrine
    national_label_en: VIP latrine
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Improved latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.improved_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 105
  - country_entry_id: UGA-SAN-91
    source_category_code: 10_hanging_toilet_hanging_latrine
    national_label_en: 10. Hanging toilet /Hanging latrine
    national_label_local: Hanging toilet/hanging latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Hanging toilet/hanging
      latrine
    jmp_id: latrines.dry_latrines.private_latrines.hanging_toilet_hanging_latrine
    gmd_target: hanging
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 117
  - country_entry_id: UGA-SAN-92
    source_category_code: uncovered_pit_latrine
    national_label_en: Uncovered pit latrine
    national_label_local: Pit latrine without slab/open pit
    jmp_classification: Latrines > Dry latrines > Private Latrines > Pit latrine without
      slab/open pit
    jmp_id: latrines.dry_latrines.private_latrines.pit_latrine_without_slab_open_pit
    gmd_target: pit_noslab
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 116
  - country_entry_id: UGA-SAN-93
    source_category_code: covered_pit_latrine_private
    national_label_en: Covered pit latrine - Private
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: UGA-SAN-94
    source_category_code: covered_pit_latrine_private
    national_label_en: Covered pit latrine private
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Traditional latrine
    jmp_id: latrines.dry_latrines.private_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: no
    source_row: 115
  - country_entry_id: UGA-SAN-95
    source_category_code: covered_vip_latrine_private
    national_label_en: Covered VIP latrine - Private
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 113
  - country_entry_id: UGA-SAN-96
    source_category_code: vip_latrine_private
    national_label_en: VIP latrine private
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 113
  - country_entry_id: UGA-SAN-97
    source_category_code: vip_private
    national_label_en: VIP PRIVATE
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Private Latrines > Ventilated Improved
      Pit latrine
    jmp_id: latrines.dry_latrines.private_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 113
  - country_entry_id: UGA-SAN-98
    source_category_code: covered_pit_latrine_shared
    national_label_en: Covered pit latrine - Shared
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: UGA-SAN-99
    source_category_code: covered_pit_latrine_shared
    national_label_en: Covered pit latrine shared
    national_label_local: Traditional latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Traditional
      latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.traditional_latrine
    gmd_target: ''
    gmd_spans: pit_slab|pit_noslab
    improved_flag: no
    shared_flag: yes
    source_row: 123
  - country_entry_id: UGA-SAN-100
    source_category_code: covered_vip_latrine_shared
    national_label_en: Covered VIP latrine - Shared
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 121
  - country_entry_id: UGA-SAN-101
    source_category_code: vip_latrine_shared
    national_label_en: VIP latrine shared
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 121
  - country_entry_id: UGA-SAN-102
    source_category_code: vip_shared
    national_label_en: VIP SHARED
    national_label_local: Ventilated Improved Pit latrine
    jmp_classification: Latrines > Dry latrines > Public/shared Latrines > Ventilated
      Improved Pit latrine
    jmp_id: latrines.dry_latrines.public_shared_latrines.ventilated_improved_pit_latrine
    gmd_target: vip
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 121
  - country_entry_id: UGA-SAN-103
    source_category_code: flush_toilet_pour
    national_label_en: Flush Toilet (pour)
    national_label_local: Pour flush latrines
    jmp_classification: Latrines > Pour flush latrines
    jmp_id: latrines.pour_flush_latrines
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 85
  - country_entry_id: UGA-SAN-104
    source_category_code: flush_toilet_private
    national_label_en: Flush toilet (private)
    national_label_local: Private pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Private pour flush latrine
    jmp_id: latrines.pour_flush_latrines.private_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: no
    source_row: 91
  - country_entry_id: UGA-SAN-105
    source_category_code: flush_toilet_shared
    national_label_en: Flush toilet (shared)
    national_label_local: Public/shared pour flush latrine
    jmp_classification: Latrines > Pour flush latrines > Public/shared pour flush
      latrine
    jmp_id: latrines.pour_flush_latrines.public_shared_pour_flush_latrine
    gmd_target: ''
    gmd_spans: flush_sewer|flush_septic|flush_pit|flush_elsewhere
    improved_flag: no
    shared_flag: yes
    source_row: 97
  - country_entry_id: UGA-SAN-106
    source_category_code: 12_bush
    national_label_en: 12. bush
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-107
    source_category_code: 12_no_facility_bush_field
    national_label_en: 12. No facility / bush / field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-108
    source_category_code: bush
    national_label_en: Bush
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-109
    source_category_code: bush_no_toilet
    national_label_en: Bush/No toilet
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-110
    source_category_code: no_facility
    national_label_en: No Facility
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-111
    source_category_code: no_facility_bush_field
    national_label_en: No facility, bush, field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-112
    source_category_code: no_facility_bush
    national_label_en: No facility/ bush
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-113
    source_category_code: no_facility_bush_polythene_bags_bucket
    national_label_en: No facility/bush/ polythene bags/ bucket
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-114
    source_category_code: no_facility_bush_polythene_bags_bucket_etc
    national_label_en: No facility/bush/ polythene bags/ bucket/ etc.
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-115
    source_category_code: no_facility_bush_field
    national_label_en: No facility/bush/field
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-116
    source_category_code: no_facility_bush_field_polythene
    national_label_en: No Facility/Bush/Field/Polythene
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-117
    source_category_code: no_facility_bush_polythene_bags_bucket
    national_label_en: No facility/Bush/Polythene bags/Bucket
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-118
    source_category_code: no_latrine
    national_label_en: No latrine
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-119
    source_category_code: no_toilet_bush
    national_label_en: No toilet (bush)
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-120
    source_category_code: non_pas_disponible
    national_label_en: Non, pas disponible
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-121
    source_category_code: open_defecation
    national_label_en: Open defecation
    national_label_local: No facility, bush, field
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: UGA-SAN-122
    source_category_code: community_latrines
    national_label_en: Community latrines
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: UGA-SAN-123
    source_category_code: flush_bio_digester_biofil
    national_label_en: Flush, bio-digester (biofil)
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: UGA-SAN-124
    source_category_code: uncovered_pit_latrine_with_slab
    national_label_en: uncovered pit latrine - with slab
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: UGA-SAN-125
    source_category_code: uncovered_pit_latrine_with_slab
    national_label_en: Uncovered Pit latrine with slab
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  - country_entry_id: UGA-SAN-126
    source_category_code: ecosan
    national_label_en: Ecosan
    national_label_local: Other
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 133
  - country_entry_id: UGA-SAN-127
    source_category_code: 11_other
    national_label_en: 11. Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: UGA-SAN-128
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: UGA-SAN-129
    source_category_code: other_specify
    national_label_en: Other (specify)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: UGA-SAN-130
    source_category_code: other_unimproved_we_don_t_know_the_type_of_facilities
    national_label_en: Other unimproved (we don't know the type of facilities)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: UGA-SAN-131
    source_category_code: uncovered_pit_latrine_without_slab
    national_label_en: Uncovered Pit latrine without slab
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 136
  - country_entry_id: UGA-SAN-132
    source_category_code: method_unknown
    national_label_en: Method unknown
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  - country_entry_id: UGA-SAN-133
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  - country_entry_id: UGA-SAN-134
    source_category_code: other_specify
    national_label_en: Other (specify)
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  - country_entry_id: UGA-SAN-135
    source_category_code: uncovered_pit_latrine_without_slab
    national_label_en: uncovered pit latrine - without slab
    national_label_local: Other
    jmp_classification: Other unimproved > Other
    jmp_id: other_unimproved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 137
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_UGA_Uganda_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: UGA-WAS-01
    source_category_code: spring
    national_label_en: Spring
    national_label_local: All springs
    jmp_classification: Ground water > All springs
    jmp_id: ground_water.all_springs
    gmd_target: ''
    gmd_spans: protected_spring|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 74
  - country_entry_id: UGA-WAS-02
    source_category_code: 5_protected_spring
    national_label_en: 5. Protected spring
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: UGA-WAS-03
    source_category_code: 7_water_from_spring_protected_spring
    national_label_en: '7. Water from Spring: Protected Spring'
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: UGA-WAS-04
    source_category_code: protected_spring
    national_label_en: Protected Spring
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: UGA-WAS-05
    source_category_code: protected_spring_closed
    national_label_en: Protected spring (closed)
    national_label_local: Protected spring
    jmp_classification: Ground water > Protected spring
    jmp_id: ground_water.protected_spring
    gmd_target: protected_spring
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 78
  - country_entry_id: UGA-WAS-06
    source_category_code: 4_protected_well
    national_label_en: 4. Protected well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-07
    source_category_code: 5_dug_well_protected_well
    national_label_en: '5. Dug Well: Protected Well'
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-08
    source_category_code: dug_well_protected
    national_label_en: 'Dug Well: Protected'
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-09
    source_category_code: protected_dug_well
    national_label_en: Protected dug well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-10
    source_category_code: protected_dug_well_closed_or_with_handpump
    national_label_en: Protected dug well (closed) or with handpump
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-11
    source_category_code: protected_well
    national_label_en: Protected well
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-12
    source_category_code: protected_well_spring
    national_label_en: Protected well / spring
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-13
    source_category_code: protected_well_spring
    national_label_en: protected well/spring
    national_label_local: Protected well
    jmp_classification: Ground water > Protected well
    jmp_id: ground_water.protected_well
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 66
  - country_entry_id: UGA-WAS-14
    source_category_code: protected_well_spring
    national_label_en: Protected Well/Spring
    national_label_local: Other
    jmp_classification: Ground water > Protected well > Other
    jmp_id: ground_water.protected_well.other
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 69
  - country_entry_id: UGA-WAS-15
    source_category_code: protected_well_in_yard_compound
    national_label_en: protected well in yard/ compound
    national_label_local: Private
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: UGA-WAS-16
    source_category_code: protected_well_in_yard_plot
    national_label_en: Protected well in yard/plot
    national_label_local: Private
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: UGA-WAS-17
    source_category_code: protected_well_spring_in_yard_plot
    national_label_en: Protected well/spring in yard/plot
    national_label_local: Private
    jmp_classification: Ground water > Protected well > Private
    jmp_id: ground_water.protected_well.private
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 67
  - country_entry_id: UGA-WAS-18
    source_category_code: protected_public_well
    national_label_en: Protected public well
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: UGA-WAS-19
    source_category_code: protected_public_well_spring
    national_label_en: Protected public well/spring
    national_label_local: Public
    jmp_classification: Ground water > Protected well > Public
    jmp_id: ground_water.protected_well.public
    gmd_target: protected_well
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 68
  - country_entry_id: UGA-WAS-20
    source_category_code: protected_dug_wells_springs
    national_label_en: Protected dug wells/springs
    national_label_local: Protected wells or springs
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: UGA-WAS-21
    source_category_code: protected_well_spring
    national_label_en: Protected well/spring
    national_label_local: Protected wells or springs
    jmp_classification: Ground water > Protected wells or springs
    jmp_id: ground_water.protected_wells_or_springs
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 46
  - country_entry_id: UGA-WAS-22
    source_category_code: protected_well_spring
    national_label_en: Protected well/spring
    national_label_local: Other
    jmp_classification: Ground water > Protected wells or springs > Other
    jmp_id: ground_water.protected_wells_or_springs.other
    gmd_target: ''
    gmd_spans: protected_well|protected_spring
    improved_flag: yes
    shared_flag: no
    source_row: 49
  - country_entry_id: UGA-WAS-23
    source_category_code: well
    national_label_en: Well
    national_label_local: Traditional wells
    jmp_classification: Ground water > Traditional wells
    jmp_id: ground_water.traditional_wells
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 62
  - country_entry_id: UGA-WAS-24
    source_category_code: well_in_residence
    national_label_en: Well in Residence
    national_label_local: Private
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: UGA-WAS-25
    source_category_code: well_tube_well_for_personal_use
    national_label_en: Well/tube-well for personal use
    national_label_local: Private
    jmp_classification: Ground water > Traditional wells > Private
    jmp_id: ground_water.traditional_wells.private
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: no
    source_row: 63
  - country_entry_id: UGA-WAS-26
    source_category_code: public_well
    national_label_en: Public Well
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 64
  - country_entry_id: UGA-WAS-27
    source_category_code: public_private_well_tube_well_sharing
    national_label_en: Public/private well/tube well (sharing)
    national_label_local: Public
    jmp_classification: Ground water > Traditional wells > Public
    jmp_id: ground_water.traditional_wells.public
    gmd_target: ''
    gmd_spans: protected_well|unprotected_well
    improved_flag: no
    shared_flag: yes
    source_row: 64
  - country_entry_id: UGA-WAS-28
    source_category_code: 3_tubewell_bore_hole
    national_label_en: 3. Tubewell/bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-29
    source_category_code: 4_tube_well_or_borehole
    national_label_en: 4. Tube well or borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-30
    source_category_code: bore_hole
    national_label_en: bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-31
    source_category_code: bore_hole
    national_label_en: Bore-hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-32
    source_category_code: borehole
    national_label_en: Borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-33
    source_category_code: borehole_with_handpump_pump
    national_label_en: Borehole (with handpump/pump)
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-34
    source_category_code: tube_well_or_borehole
    national_label_en: tube well or borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-35
    source_category_code: tubewell_or_borehole
    national_label_en: Tubewell or borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-36
    source_category_code: tubewell_borehole
    national_label_en: Tubewell, borehole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-37
    source_category_code: tubewell_bore_hole
    national_label_en: Tubewell/bore hole
    national_label_local: Tubewell, borehole
    jmp_classification: Ground water > Tubewell, borehole
    jmp_id: ground_water.tubewell_borehole
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 58
  - country_entry_id: UGA-WAS-38
    source_category_code: bore_hole
    national_label_en: Bore-hole
    national_label_local: Other
    jmp_classification: Ground water > Tubewell, borehole > Other
    jmp_id: ground_water.tubewell_borehole.other
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 61
  - country_entry_id: UGA-WAS-39
    source_category_code: borehole_in_yard_plot
    national_label_en: Borehole in yard / plot
    national_label_local: Private
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 59
  - country_entry_id: UGA-WAS-40
    source_category_code: borehole_in_yard_plot
    national_label_en: Borehole in yard/plot
    national_label_local: Private
    jmp_classification: Ground water > Tubewell, borehole > Private
    jmp_id: ground_water.tubewell_borehole.private
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 59
  - country_entry_id: UGA-WAS-41
    source_category_code: public_borehole
    national_label_en: Public borehole
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 60
  - country_entry_id: UGA-WAS-42
    source_category_code: public_pump
    national_label_en: Public pump
    national_label_local: Public
    jmp_classification: Ground water > Tubewell, borehole > Public
    jmp_id: ground_water.tubewell_borehole.public
    gmd_target: borehole
    gmd_spans: ''
    improved_flag: yes
    shared_flag: yes
    source_row: 60
  - country_entry_id: UGA-WAS-43
    source_category_code: 8_water_from_spring_unprotected_spring
    national_label_en: '8. Water from Spring: Unprotected Spring'
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: UGA-WAS-44
    source_category_code: 9_unprotected_spring
    national_label_en: 9. Unprotected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: UGA-WAS-45
    source_category_code: protected_spring
    national_label_en: Protected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: UGA-WAS-46
    source_category_code: unprotected_spring
    national_label_en: unprotected spring
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: UGA-WAS-47
    source_category_code: unprotected_spring_open
    national_label_en: Unprotected spring (open)
    national_label_local: Unprotected spring
    jmp_classification: Ground water > Unprotected spring
    jmp_id: ground_water.unprotected_spring
    gmd_target: unprotected_spring
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 82
  - country_entry_id: UGA-WAS-48
    source_category_code: 6_dug_well_unprotected_well
    national_label_en: '6. Dug Well: Unprotected Well'
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-49
    source_category_code: 8_unprotected_well
    national_label_en: 8. Unprotected well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-50
    source_category_code: dug_well_unprotected
    national_label_en: 'Dug Well: Unprotected'
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-51
    source_category_code: unprotected_dug_well
    national_label_en: Unprotected dug well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-52
    source_category_code: unprotected_dug_well_open
    national_label_en: Unprotected dug well (open)
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-53
    source_category_code: unprotected_well
    national_label_en: Unprotected well
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-54
    source_category_code: unprotected_well_spring
    national_label_en: Unprotected well / spring
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-55
    source_category_code: unprotected_well_spring
    national_label_en: unprotected well/spring
    national_label_local: Unprotected well
    jmp_classification: Ground water > Unprotected well
    jmp_id: ground_water.unprotected_well
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 70
  - country_entry_id: UGA-WAS-56
    source_category_code: unprotected_well_spring
    national_label_en: Unprotected Well/Spring
    national_label_local: Other
    jmp_classification: Ground water > Unprotected well > Other
    jmp_id: ground_water.unprotected_well.other
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 73
  - country_entry_id: UGA-WAS-57
    source_category_code: open_well_in_yard_compound
    national_label_en: open well in yard/compound
    national_label_local: Private
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: UGA-WAS-58
    source_category_code: open_well_in_yeard_plot
    national_label_en: Open well in yeard/plot
    national_label_local: Private
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: UGA-WAS-59
    source_category_code: unprotected_well_spring_in_yard_plot
    national_label_en: Unprotected well/spring in yard/plot
    national_label_local: Private
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: UGA-WAS-60
    source_category_code: well
    national_label_en: Well
    national_label_local: Private
    jmp_classification: Ground water > Unprotected well > Private
    jmp_id: ground_water.unprotected_well.private
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 71
  - country_entry_id: UGA-WAS-61
    source_category_code: open_public_well
    national_label_en: Open public well
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: UGA-WAS-62
    source_category_code: unprotected_public_well_spring
    national_label_en: Unprotected public well/spring
    national_label_local: Public
    jmp_classification: Ground water > Unprotected well > Public
    jmp_id: ground_water.unprotected_well.public
    gmd_target: unprotected_well
    gmd_spans: ''
    improved_flag: no
    shared_flag: yes
    source_row: 72
  - country_entry_id: UGA-WAS-63
    source_category_code: unprotected_dug_wells_springs
    national_label_en: Unprotected dug wells/springs
    national_label_local: Unprotected wells or springs
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: UGA-WAS-64
    source_category_code: unprotected_well_spring
    national_label_en: Unprotected well/spring
    national_label_local: Unprotected wells or springs
    jmp_classification: Ground water > Unprotected wells or springs
    jmp_id: ground_water.unprotected_wells_or_springs
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 50
  - country_entry_id: UGA-WAS-65
    source_category_code: unprotected_well_spring
    national_label_en: Unprotected well/spring
    national_label_local: Other
    jmp_classification: Ground water > Unprotected wells or springs > Other
    jmp_id: ground_water.unprotected_wells_or_springs.other
    gmd_target: ''
    gmd_spans: unprotected_well|unprotected_spring
    improved_flag: no
    shared_flag: no
    source_row: 53
  - country_entry_id: UGA-WAS-66
    source_category_code: 10_tanker_truck_cart_with_small_tank
    national_label_en: 10. Tanker truck/cart with small tank
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-67
    source_category_code: 11_cart_with_small_tank
    national_label_en: 11. Cart with Small Tank
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-68
    source_category_code: 15_bicycle_with_jerrycans
    national_label_en: 15. Bicycle with jerrycans
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-69
    source_category_code: bicycle_with_jerrycans
    national_label_en: bicycle with jerrycans
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-70
    source_category_code: cart_with_small_tank
    national_label_en: Cart with small tank
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-71
    source_category_code: purchased_from_a_cart_with_a_small_tank_or_drum
    national_label_en: Purchased from a cart with a small tank or drum
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-72
    source_category_code: vendor_cart_with_small_tank
    national_label_en: 'Vendor: Cart with small tank'
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-73
    source_category_code: water_truck
    national_label_en: Water truck
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-74
    source_category_code: water_vendor
    national_label_en: Water vendor
    national_label_local: Cart with small tank/drum
    jmp_classification: Other improved sources > Cart with small tank/drum
    jmp_id: other_improved_sources.cart_with_small_tank_drum
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 101
  - country_entry_id: UGA-WAS-75
    source_category_code: gravity_flow_scheme
    national_label_en: Gravity Flow Scheme
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: UGA-WAS-76
    source_category_code: tap_boreholes_protected_wells_and_springs
    national_label_en: Tap, boreholes, protected wells and springs
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: UGA-WAS-77
    source_category_code: vendor
    national_label_en: Vendor
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 103
  - country_entry_id: UGA-WAS-78
    source_category_code: gravity_flow_scheme
    national_label_en: Gravity flow scheme
    national_label_local: Other
    jmp_classification: Other improved sources > Other
    jmp_id: other_improved_sources.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 104
  - country_entry_id: UGA-WAS-79
    source_category_code: 10_tanker_truck
    national_label_en: 10. Tanker Truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-80
    source_category_code: purchased_from_a_tanker_truck
    national_label_en: Purchased from a tanker truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-81
    source_category_code: tanker_truck
    national_label_en: Tanker truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-82
    source_category_code: tanker_truck_provided
    national_label_en: Tanker truck provided
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-83
    source_category_code: tanker_truck_vendor
    national_label_en: Tanker truck, vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-84
    source_category_code: tanker_truck_cart_with_small_tank_drum
    national_label_en: Tanker truck/cart with small tank/drum
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-85
    source_category_code: vendor_tanker_truck
    national_label_en: Vendor/Tanker Truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-86
    source_category_code: water_truck_tanker_service
    national_label_en: Water truck/tanker service
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-87
    source_category_code: water_truck_water_vendor
    national_label_en: Water Truck/water vendor
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-88
    source_category_code: water_selling_cart_or_truck
    national_label_en: Water-selling cart or truck
    national_label_local: Tanker truck provided
    jmp_classification: Other improved sources > Tanker truck provided
    jmp_id: other_improved_sources.tanker_truck_provided
    gmd_target: tanker
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 102
  - country_entry_id: UGA-WAS-89
    source_category_code: 96_other
    national_label_en: 96. Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-WAS-90
    source_category_code: open_water_sources
    national_label_en: Open water sources
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-WAS-91
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-WAS-92
    source_category_code: other_specify
    national_label_en: Other (specify)
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-WAS-93
    source_category_code: others
    national_label_en: Others
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-WAS-94
    source_category_code: source_unknown
    national_label_en: Source unknown
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: UGA-WAS-95
    source_category_code: other
    national_label_en: Other
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-WAS-96
    source_category_code: other_specify
    national_label_en: Other (specify)
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-WAS-97
    source_category_code: other_unknown_source
    national_label_en: Other + Unknown Source
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-WAS-98
    source_category_code: refused_don_t_know
    national_label_en: Refused + Don't know
    national_label_local: Other
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other#2
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 107
  - country_entry_id: UGA-WAS-99
    source_category_code: 13_bottled_water
    national_label_en: 13. Bottled Water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: UGA-WAS-100
    source_category_code: 7_bottled_improved_and_unimproved
    national_label_en: 7. Bottled (Improved and unimproved)
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: UGA-WAS-101
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: UGA-WAS-102
    source_category_code: bottled_water_with_improved_source
    national_label_en: Bottled water with improved source
    national_label_local: Bottled water
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: UGA-WAS-103
    source_category_code: 12_sachet
    national_label_en: 12. Sachet
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: UGA-WAS-104
    source_category_code: 14_sachet_water
    national_label_en: 14. Sachet Water
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: UGA-WAS-105
    source_category_code: bottled_water
    national_label_en: Bottled Water
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: UGA-WAS-106
    source_category_code: bottled_water_without_improved_source
    national_label_en: Bottled water without improved source
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: UGA-WAS-107
    source_category_code: sachet_water
    national_label_en: Sachet water
    national_label_local: Sachet water
    jmp_classification: Packaged water > Sachet water
    jmp_id: packaged_water.sachet_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 91
  - country_entry_id: UGA-WAS-108
    source_category_code: 6_rainwater
    national_label_en: 6. Rainwater
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: UGA-WAS-109
    source_category_code: 9_rainwater
    national_label_en: 9. Rainwater
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: UGA-WAS-110
    source_category_code: rain_water
    national_label_en: Rain Water
    national_label_local: Rainwater
    jmp_classification: Rainwater
    jmp_id: rainwater
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 86
  - country_entry_id: UGA-WAS-111
    source_category_code: rain_water
    national_label_en: Rain Water
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: UGA-WAS-112
    source_category_code: rainwater
    national_label_en: Rainwater
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: UGA-WAS-113
    source_category_code: rainwater_collection
    national_label_en: Rainwater collection
    national_label_local: Covered cistern/tank
    jmp_classification: Rainwater > Covered cistern/tank
    jmp_id: rainwater.covered_cistern_tank
    gmd_target: rainwater
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 87
  - country_entry_id: UGA-WAS-114
    source_category_code: 11_surface_water
    national_label_en: 11. Surface water
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-115
    source_category_code: 12_surface_water
    national_label_en: 12. Surface water
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-116
    source_category_code: river_stream_lake
    national_label_en: River / stream / lake
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-117
    source_category_code: river_or_steam
    national_label_en: River or steam
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-118
    source_category_code: river_stream_lake_pond
    national_label_en: River, stream, lake, pond
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-119
    source_category_code: river_steam_lake_pond
    national_label_en: river,steam, lake,pond
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-120
    source_category_code: river_stream_lake
    national_label_en: River/ Stream/ Lake
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-121
    source_category_code: river_dam_lake_ponds_stream_canal_irrigation_channel
    national_label_en: River/dam/lake/ponds/stream/canal/irrigation channel
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-122
    source_category_code: river_lake_spring_etc
    national_label_en: River/lake/spring etc.
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-123
    source_category_code: river_lake_stream_other_specify_including_neighbours
    national_label_en: River/Lake/Stream & (Other Specify including neighbours)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-124
    source_category_code: river_stream_lake
    national_label_en: River/stream/lake
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-125
    source_category_code: surface_water
    national_label_en: Surface water
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-126
    source_category_code: surface_water_pond_river_stream
    national_label_en: Surface water (pond/river/stream)
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-127
    source_category_code: surface_water_like_a_river_dam_lake_pond_stream_canal_or_irrigation_channel
    national_label_en: Surface water, like a river, dam, lake, pond, stream, canal
      or irrigation channel
    national_label_local: Surface water
    jmp_classification: Surface water
    jmp_id: surface_water
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 92
  - country_entry_id: UGA-WAS-128
    source_category_code: dam
    national_label_en: Dam
    national_label_local: Dam
    jmp_classification: Surface water > Dam
    jmp_id: surface_water.dam
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 95
  - country_entry_id: UGA-WAS-129
    source_category_code: pond_lake
    national_label_en: Pond/lake
    national_label_local: Lake
    jmp_classification: Surface water > Lake
    jmp_id: surface_water.lake
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 94
  - country_entry_id: UGA-WAS-130
    source_category_code: pond_lake
    national_label_en: Pond/Lake
    national_label_local: Pond
    jmp_classification: Surface water > Pond
    jmp_id: surface_water.pond
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 96
  - country_entry_id: UGA-WAS-131
    source_category_code: river_lake_spring
    national_label_en: River, lake, spring
    national_label_local: River
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: UGA-WAS-132
    source_category_code: river_stream_lake_pond
    national_label_en: River, stream, lake, pond
    national_label_local: River
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: UGA-WAS-133
    source_category_code: river_stream
    national_label_en: River/Stream
    national_label_local: River
    jmp_classification: Surface water > River
    jmp_id: surface_water.river
    gmd_target: surface
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 93
  - country_entry_id: UGA-WAS-134
    source_category_code: 16_piped_water_piped_to_neighbor
    national_label_en: '16. Piped water: piped to neighbor'
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: UGA-WAS-135
    source_category_code: gravity_flow_scheme
    national_label_en: gravity flow scheme
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: UGA-WAS-136
    source_category_code: gravity_flow_schemes
    national_label_en: Gravity flow schemes
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: UGA-WAS-137
    source_category_code: piped_to_neighbor
    national_label_en: piped to neighbor
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: UGA-WAS-138
    source_category_code: tap_piped_water
    national_label_en: Tap/Piped Water
    national_label_local: Other
    jmp_classification: Tap water > Other
    jmp_id: tap_water.other
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 42
  - country_entry_id: UGA-WAS-139
    source_category_code: private_connected_to_pipeline
    national_label_en: private connected to pipeline
    national_label_local: Piped on premises
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  - country_entry_id: UGA-WAS-140
    source_category_code: 1_piped_into_dwelling_yard
    national_label_en: 1. Piped into dwelling/yard
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-141
    source_category_code: 1_piped_water_piped_into_dwelling_indoor
    national_label_en: '1. Piped Water: Piped into dwelling/indoor'
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-142
    source_category_code: indoor_tap
    national_label_en: Indoor tap
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-143
    source_category_code: piped_in_dwelling
    national_label_en: Piped in Dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-144
    source_category_code: piped_into_dwelling
    national_label_en: Piped into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-145
    source_category_code: piped_into_residence
    national_label_en: Piped into residence
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-146
    source_category_code: piped_water_into_dwelling
    national_label_en: Piped water into dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-147
    source_category_code: piped_water_into_dwelling_yard_or_plot
    national_label_en: Piped water into dwelling, yard or plot
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-148
    source_category_code: piped_water_into_the_dwelling
    national_label_en: Piped water into the dwelling
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-149
    source_category_code: private_connection_to_pipeline
    national_label_en: Private connection to pipeline
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-150
    source_category_code: private_connection_to_pipeline_tap
    national_label_en: Private connection to pipeline (Tap)
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-151
    source_category_code: private_faucet_or_tap
    national_label_en: Private faucet or tap
    national_label_local: Piped water into dwelling
    jmp_classification: Tap water > Piped on premises > Piped water into dwelling
    jmp_id: tap_water.piped_on_premises.piped_water_into_dwelling
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 39
  - country_entry_id: UGA-WAS-152
    source_category_code: 2_piped_water_pipe_to_yard_plot
    national_label_en: '2. Piped Water: Pipe to yard/plot'
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-153
    source_category_code: piped_into_yard
    national_label_en: Piped into yard
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-154
    source_category_code: piped_into_yard_plot
    national_label_en: Piped into yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-155
    source_category_code: piped_outside_dwelling
    national_label_en: Piped outside Dwelling
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-156
    source_category_code: piped_to_yard_plot
    national_label_en: piped to yard/plot
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-157
    source_category_code: piped_water_into_yard
    national_label_en: Piped water into yard
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-158
    source_category_code: piped_water_into_yard_plot_or_compound
    national_label_en: Piped water into yard, plot or compound
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-159
    source_category_code: piped_water_to_the_yard
    national_label_en: Piped water to the yard
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-160
    source_category_code: private_within_building_sharing_tap
    national_label_en: Private within building sharing tap
    national_label_local: Piped water to yard/plot
    jmp_classification: Tap water > Piped on premises > Piped water to yard/plot
    jmp_id: tap_water.piped_on_premises.piped_water_to_yard_plot
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 40
  - country_entry_id: UGA-WAS-161
    source_category_code: 2_public_tap_standpipe
    national_label_en: 2. Public tap/standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-162
    source_category_code: 3_piped_water_public_tap_standpipe
    national_label_en: '3. Piped Water: Public tap/standpipe'
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-163
    source_category_code: private_or_public_tap_outside_the_building
    national_label_en: Private or public tap outside the building
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-164
    source_category_code: public_tap
    national_label_en: Public tap
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-165
    source_category_code: public_tap_or_standpipe
    national_label_en: Public tap or standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-166
    source_category_code: public_tap_standpipe
    national_label_en: Public tap, standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-167
    source_category_code: public_tap_standpipe
    national_label_en: public tap/standpipe
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  - country_entry_id: UGA-WAS-168
    source_category_code: public_taps
    national_label_en: public taps
    national_label_local: Public tap, standpipe
    jmp_classification: Tap water > Public tap, standpipe
    jmp_id: tap_water.public_tap_standpipe
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 41
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_UGA_Uganda_0.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

