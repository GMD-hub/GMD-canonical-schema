---
country_id: CTY-WLF
iso3: WLF
schema_version: '0.2'
status: draft
country_name: WLF
parameters:
- parameter_id: PARAM-WASH-SANITATION-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: WLF-SAN-01
    source_category_code: wc_interieur_et_pas_fosse_septique
    national_label_en: WC interieur et pas fosse septique
    national_label_local: reliée aux latrine
    jmp_classification: Flush/toilets > Private flush/toilet > to pit
    jmp_id: flush_toilets.private_flush_toilet.to_pit
    gmd_target: flush_pit
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 75
  - country_entry_id: WLF-SAN-02
    source_category_code: wc_interieur_et_fosse_septique
    national_label_en: WC interieur et fosse septique
    national_label_local: reliée a fosse septique
    jmp_classification: Flush/toilets > Private flush/toilet > to septic tank
    jmp_id: flush_toilets.private_flush_toilet.to_septic_tank
    gmd_target: flush_septic
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 74
  - country_entry_id: WLF-SAN-03
    source_category_code: pas_de_system
    national_label_en: Pas de system
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: WLF-SAN-04
    source_category_code: pas_wc_interieur_et_pas_fosse_septique
    national_label_en: pas WC interieur et pas fosse septique
    national_label_local: Pas de toilette/nature/plein air
    jmp_classification: No facility, bush, field
    jmp_id: no_facility_bush_field
    gmd_target: open
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 134
  - country_entry_id: WLF-SAN-05
    source_category_code: systeme_d_assainnissement_des_eaux_usees
    national_label_en: |-
      système d'assainnissement des
      eaux usées
    national_label_local: Autre
    jmp_classification: Other improved > Other
    jmp_id: other_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 132
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_WLF_Wallis_and_Futuna_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
- parameter_id: PARAM-WASH-WATER-CROSSWALK
  effective_from: ~
  effective_to: ~
  selectors: ~
  value:
  - country_entry_id: WLF-WAS-01
    source_category_code: autre
    national_label_en: Autre
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: WLF-WAS-02
    source_category_code: other
    national_label_en: Other
    national_label_local: Autre
    jmp_classification: Other non-improved > Other
    jmp_id: other_non_improved.other
    gmd_target: other
    gmd_spans: ''
    improved_flag: no
    shared_flag: no
    source_row: 106
  - country_entry_id: WLF-WAS-03
    source_category_code: bottled_water
    national_label_en: Bottled water
    national_label_local: Eau en bouteille
    jmp_classification: Packaged water > Bottled water
    jmp_id: packaged_water.bottled_water
    gmd_target: bottled
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 90
  - country_entry_id: WLF-WAS-04
    source_category_code: reseau_public
    national_label_en: Reseau public
    national_label_local: Connexions maison
    jmp_classification: Tap water > Piped on premises
    jmp_id: tap_water.piped_on_premises
    gmd_target: piped
    gmd_spans: ''
    improved_flag: yes
    shared_flag: no
    source_row: 38
  provenance:
    source: extraction\10_source\country-parameters-inputs\JMP\JMP_2025_WLF_Wallis_and_Futuna_1.xlsx
    verified_on: ~
    human_reviewed: no
    reviewer: ~
---

