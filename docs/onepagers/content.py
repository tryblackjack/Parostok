"""Тексти одноаркушників Parostok (EN / FR / NL-BE).

Кожне твердження має джерело в docs/ktd/parostok-tulip/04_registr.yaml або
в профілі KARE (grantwriter_kare.zip). Заборонені твердження профілю
(guaranteed yield, proven results, independently verified, world's first)
і CONFLICTING_UNRESOLVED цифри («до +65 %», «у 2–4 рази») не використовуються.
«Certified» — лише в точному формулюванні сертифікатів EUTEST MD25127601
і ISO 13485 (8О139.СУЯ.14-25), без узагальнень.
Несуча частота не вказується (рішення власника 2026-10-21); суми не вказуються.
"""

CONTACT = "PE SPE “KARE” · Odesa, Ukraine · mwparostok@gmail.com · www.parostokmw.com"

SPECS = {
    "en": [("Power supply", "220 V (110 V version on request)"), ("Power consumption", "3.0–6.0 kW"),
           ("Throughput", "0.4–2.0 t/h"), ("Weight", "210 kg"),
           ("Dimensions", "70 × 90 × 206 cm"), ("Loading", "from the top")],
    "fr": [("Alimentation", "220 V (version 110 V sur demande)"), ("Puissance absorbée", "3,0–6,0 kW"),
           ("Débit", "0,4–2,0 t/h"), ("Poids", "210 kg"),
           ("Dimensions", "70 × 90 × 206 cm"), ("Chargement", "par le haut")],
    "nl": [("Voeding", "220 V (versie 110 V op aanvraag)"), ("Opgenomen vermogen", "3,0–6,0 kW"),
           ("Capaciteit", "0,4–2,0 t/u"), ("Gewicht", "210 kg"),
           ("Afmetingen", "70 × 90 × 206 cm"), ("Vullen", "langs boven")],
}

EQUIPMENT = {
    "en": {
        "lang": "en",
        "kicker": "Equipment",
        "title": "Chemical-free microwave seed treatment",
        "lead": "Parostok treats seed before sowing with a controlled microwave field. "
                "Dry process, no chemicals, no residues on the seed.",
        "caption": "New design (rendering). The specifications refer to the current production model.",
        "h_how": "How it works",
        "how": ["Seed flows continuously through a controlled microwave field.",
                "A library of treatment modes, built from earlier trials and test implementations, is kept in non-volatile memory; each crop and variety has its own mode.",
                "Treatment can be offered as a service or with the machine installed on site."],
        "h_specs": "Key specifications (current model)",
        "h_evidence": "Evidence to date",
        "evidence": [
            "<b>Independent laboratory, April 2026</b> (Plant Health Institute, Ukravit Science Park; commissioned by KARE; DSTU 4138-2002): "
            "36 corn seed samples from 6 lots, 5 modes — uniform root development, no signs of suppression.",
            "<b>Weaker seed gains most:</b> in the same test the lowest lot (86 % germination) gained 6.2 points, "
            "while lots at 90–92 % changed by −1.6 to +1.6 points.",
            "<b>Field, Poland 2024</b> (RSUW Głuchów, KWS Nataelo): 11.97 vs 10.34 t/ha (+15.7 %). "
            "Single plots without replication — indicative only.",
            "<b>Research since 2000</b> with Ukrainian research institutes: 24 crops in the 2000–2001 programme, "
            "replicated field trials on winter wheat.",
        ],
        "h_conf": "Conformity and quality",
        "conf": [
            "<b>Parostok KM:</b> technical file reviewed by EUTEST against the Machinery (2006/42/EC), Low Voltage (2014/35/EU) and EMC (2014/30/EU) directives — certificate of conformity MD25127601, valid until 14.03.2030 (voluntary review, not a notified-body procedure).",
            "<b>Manufacturer:</b> quality management system certified to EN ISO 13485:2016, certificate 8O139.СУЯ.14-25, valid until 26.02.2028.",
        ],
        "h_for": "For whom",
        "for": "Seed producers and processors, cooperatives and large farms — especially for seed lots "
               "below their germination standard.",
        "photo": "Laboratory germination test of the corn seed lots, April 2026.",
        "foot": "October 2026. Figures are the company’s own unless marked as independent.",
    },
    "fr": {
        "lang": "fr",
        "kicker": "Équipement",
        "title": "Traitement des semences par micro-ondes, sans chimie",
        "lead": "Parostok traite les semences avant le semis par un champ micro-ondes contrôlé. "
                "Procédé à sec, sans produits chimiques, sans résidus sur la semence.",
        "caption": "Nouveau design (rendu). Les caractéristiques concernent le modèle de production actuel.",
        "h_how": "Principe",
        "how": ["Les semences traversent en flux continu un champ micro-ondes contrôlé.",
                "Une bibliothèque de modes de traitement, issue d’essais et d’implantations pilotes antérieurs, est conservée en mémoire non volatile ; chaque culture et variété a son propre mode.",
                "Le traitement est proposé comme prestation de service ou avec la machine installée sur site."],
        "h_specs": "Caractéristiques principales (modèle actuel)",
        "h_evidence": "Résultats à ce jour",
        "evidence": [
            "<b>Laboratoire indépendant, avril 2026</b> (Plant Health Institute, Ukravit Science Park ; sur commande de KARE ; DSTU 4138-2002) : "
            "36 échantillons de semences de maïs issus de 6 lots, 5 modes — développement racinaire homogène, aucun signe d’inhibition.",
            "<b>Les semences faibles gagnent le plus :</b> dans ce même essai, le lot le plus faible (86 % de germination) a gagné "
            "6,2 points, tandis que les lots à 90–92 % ont varié de −1,6 à +1,6 point.",
            "<b>Champ, Pologne 2024</b> (RSUW Głuchów, KWS Nataelo) : 11,97 contre 10,34 t/ha (+15,7 %). "
            "Parcelles uniques sans répétition — résultat indicatif.",
            "<b>Recherche depuis 2000</b> avec des instituts de recherche ukrainiens : 24 cultures dans le programme 2000–2001, "
            "essais au champ répétés sur blé d’hiver.",
        ],
        "h_conf": "Conformité et qualité",
        "conf": [
            "<b>Parostok KM :</b> dossier technique examiné par EUTEST au regard des directives Machines (2006/42/CE), Basse tension (2014/35/UE) et CEM (2014/30/UE) — certificat de conformité MD25127601, valable jusqu’au 14.03.2030 (examen volontaire, hors procédure d’organisme notifié).",
            "<b>Fabricant :</b> système de management de la qualité certifié EN ISO 13485:2016, certificat 8O139.СУЯ.14-25, valable jusqu’au 26.02.2028.",
        ],
        "h_for": "Pour qui",
        "for": "Producteurs et conditionneurs de semences, coopératives et grandes exploitations — en particulier pour "
               "les lots de semences sous la norme de germination.",
        "photo": "Test de germination en laboratoire des lots de semences de maïs, avril 2026.",
        "foot": "Octobre 2026. Les chiffres sont ceux de l’entreprise, sauf mention « indépendant ».",
    },
    "nl": {
        "lang": "nl-BE",
        "kicker": "Uitrusting",
        "title": "Zaadbehandeling met microgolven, zonder chemie",
        "lead": "Parostok behandelt zaaizaad vóór het zaaien met een gecontroleerd microgolfveld. "
                "Droog proces, zonder chemicaliën, geen residu op het zaad.",
        "caption": "Nieuw ontwerp (rendering). De specificaties gelden voor het huidige productiemodel.",
        "h_how": "Werking",
        "how": ["Het zaad loopt in een continue stroom door een gecontroleerd microgolfveld.",
                "Een bibliotheek van behandelingsstanden, opgebouwd uit eerdere proeven en testimplementaties, staat in niet-vluchtig geheugen; elk gewas en elk ras heeft een eigen stand.",
                "De behandeling kan als dienst worden aangeboden of met de machine ter plaatse."],
        "h_specs": "Belangrijkste specificaties (huidig model)",
        "h_evidence": "Resultaten tot nu toe",
        "evidence": [
            "<b>Onafhankelijk laboratorium, april 2026</b> (Plant Health Institute, Ukravit Science Park; in opdracht van KARE; DSTU 4138-2002): "
            "36 stalen maïszaad uit 6 partijen, 5 standen — gelijkmatige wortelontwikkeling, geen tekenen van remming.",
            "<b>Zwakker zaad wint het meest:</b> in dezelfde test won de zwakste partij (86 % kieming) 6,2 punten, "
            "terwijl partijen van 90–92 % tussen −1,6 en +1,6 punten veranderden.",
            "<b>Veld, Polen 2024</b> (RSUW Głuchów, KWS Nataelo): 11,97 tegenover 10,34 t/ha (+15,7 %). "
            "Enkele percelen zonder herhaling — enkel indicatief.",
            "<b>Onderzoek sinds 2000</b> met Oekraïense onderzoeksinstituten: 24 gewassen in het programma 2000–2001, "
            "herhaalde veldproeven met wintertarwe.",
        ],
        "h_conf": "Conformiteit en kwaliteit",
        "conf": [
            "<b>Parostok KM:</b> technisch dossier door EUTEST getoetst aan de Machinerichtlijn (2006/42/EG), de Laagspanningsrichtlijn (2014/35/EU) en de EMC-richtlijn (2014/30/EU) — conformiteitscertificaat MD25127601, geldig tot 14.03.2030 (vrijwillige toetsing, geen procedure van een aangemelde instantie).",
            "<b>Fabrikant:</b> kwaliteitsmanagementsysteem gecertificeerd volgens EN ISO 13485:2016, certificaat 8O139.СУЯ.14-25, geldig tot 26.02.2028.",
        ],
        "h_for": "Voor wie",
        "for": "Zaadproducenten en -verwerkers, coöperaties en grote landbouwbedrijven — vooral voor zaadpartijen "
               "onder hun kiemnorm.",
        "photo": "Kiemtest in het laboratorium van de partijen maïszaad, april 2026.",
        "foot": "Oktober 2026. Cijfers zijn die van het bedrijf, tenzij als onafhankelijk aangeduid.",
    },
}

TULIP = {
    "en": {
        "lang": "en",
        "kicker": "Development partnership",
        "title": "Gentle microwave treatment of tulip bulbs",
        "lead": "Parostok builds on research into microwave seed treatment since 2000. Together with Belgian partners we "
                "propose to develop a dedicated machine for chemical-free treatment of living tulip bulbs — designed "
                "first of all not to harm the bulb.",
        "h_why": "Why a dedicated machine",
        "why": ["A tulip bulb (32–45 mm) is several times larger than the depth the microwave field penetrates (about 1 cm).",
                "In round objects of this size microwave heating can concentrate at the centre — exactly where the flower bud sits.",
                "Seed equipment therefore cannot simply be reused: bulbs need their own handling, dosing and control."],
        "h_design": "Design principles",
        "design": ["Single layer of rotating bulbs, no drops or impacts.",
                   "Dose delivered in sections, with equalisation zones in between.",
                   "<b>Hard limit: the bulb core never exceeds 42 °C.</b> Hot-water treatment above about 45 °C is considered harmful to tulip bulbs.",
                   "Optional low-heat pulsed mode.",
                   "Mode library in non-volatile memory; AI selects and adjusts the dose within the qualified limits — the 42 °C limit is held by independent interlocks that the AI cannot override.",
                   "Remote monitoring and control: the line can run fully autonomously.",
                   "Every batch logged: power, temperatures, recipe.",
                   "Easy-to-clean contact surfaces, so that disease is not carried between lots."],
        "h_status": "Where we stand",
        "status": "The effect of microwave treatment on tulip bulbs has not been demonstrated yet: we found no published "
                  "study on living tulip bulbs. The programme therefore starts with bud-safety and pilot forcing trials "
                  "against an untreated control, and stops if they show no benefit.",
        "h_plan": "Staged programme",
        "plan": [("1", "Bulb properties, bud-safety threshold, pilot forcing → go / no-go", "6–9 months"),
                 ("2", "Design and prototype machine (0.5 t/h)", "about 2 years"),
                 ("3", "Independent forcing and field trials", "one season")],
        "plan_total": "Evidence-based result expected in 2029–2030.",
        "h_seek": "What we are looking for in Belgium",
        "seek": ["Growers and forcers who can provide bulbs and forcing space for trials.",
                 "An independent research partner for the safety and forcing trials.",
                 "End users and co-funding partners for the prototype."],
        "h_line": "Concept of the line",
        "line": ["Crates", "Feeder", "Single layer", "Microwave section", "Equalisation", "× N sections", "Core check", "Crates"],
        "line_cap": "Functional diagram of the planned machine — not a drawing of an existing unit.",
        "h_specs": "Target specifications (prototype, draft)",
        "specs": [("Product", "living tulip bulbs, 10/11 – 12/+ cm"), ("Prototype throughput", "0.5 t/h (≈ 20 000 bulbs/h)"),
                  ("Generators", "4–12 × 1.5 kW modules"),
                  ("Bulb core temperature", "≤ 42 °C, hard limit"), ("Handling", "single layer, ≈ 1 m wide"),
                  ("Control", "mode library, AI, remote monitoring"), ("Power supply", "220 V (110 V version on request)"), ("Target compliance", "CE: (EU) 2023/1230, LVD, EMC")],
        "specs_note": "Values follow the draft technical specification and are fixed only after the bulb tests.",
        "foot": "October 2026. Target values are confirmed only after the bulb tests.",
    },
    "fr": {
        "lang": "fr",
        "kicker": "Partenariat de développement",
        "title": "Traitement doux des bulbes de tulipe par micro-ondes",
        "lead": "Parostok s’appuie sur des recherches en traitement des semences par micro-ondes menées depuis 2000. Avec des partenaires belges, nous "
                "proposons de développer une machine dédiée au traitement sans chimie des bulbes de tulipe vivants — "
                "conçue avant tout pour ne pas abîmer le bulbe.",
        "h_why": "Pourquoi une machine dédiée",
        "why": ["Un bulbe de tulipe (32–45 mm) est plusieurs fois plus grand que la profondeur de pénétration du champ micro-ondes (environ 1 cm).",
                "Dans des objets ronds de cette taille, le chauffage micro-ondes peut se concentrer au centre — là où se trouve le bourgeon floral.",
                "On ne peut donc pas simplement réutiliser l’équipement pour semences : les bulbes demandent leur propre manutention, dosage et contrôle."],
        "h_design": "Principes de conception",
        "design": ["Bulbes en une seule couche, en rotation, sans chute ni choc.",
                   "Dose appliquée par sections, avec des zones d’égalisation entre elles.",
                   "<b>Limite absolue : le cœur du bulbe ne dépasse jamais 42 °C.</b> Un traitement à l’eau chaude au-delà d’environ 45 °C est considéré comme nuisible aux bulbes de tulipe.",
                   "Mode pulsé à faible échauffement en option.",
                   "Bibliothèque de modes en mémoire non volatile ; l’IA choisit et ajuste la dose dans les limites qualifiées — la limite de 42 °C est tenue par des verrouillages indépendants que l’IA ne peut pas contourner.",
                   "Surveillance et commande à distance : la ligne peut fonctionner de manière entièrement autonome.",
                   "Chaque lot enregistré : puissance, températures, recette.",
                   "Surfaces de contact faciles à nettoyer, pour ne pas transmettre de maladies d’un lot à l’autre."],
        "h_status": "Où nous en sommes",
        "status": "L’effet du traitement micro-ondes sur les bulbes de tulipe n’est pas encore démontré : nous n’avons trouvé "
                  "aucune étude publiée sur des bulbes de tulipe vivants. Le programme commence donc par des essais de sécurité "
                  "du bourgeon et de forçage pilote face à un témoin non traité, et s’arrête s’ils ne montrent aucun bénéfice.",
        "h_plan": "Programme par étapes",
        "plan": [("1", "Propriétés des bulbes, seuil de sécurité du bourgeon, forçage pilote → décision go / no-go", "6–9 mois"),
                 ("2", "Conception et prototype de machine (0,5 t/h)", "environ 2 ans"),
                 ("3", "Essais indépendants de forçage et au champ", "une saison")],
        "plan_total": "Résultat fondé sur des preuves attendu en 2029–2030.",
        "h_seek": "Ce que nous recherchons en Belgique",
        "seek": ["Producteurs et forceurs pouvant fournir des bulbes et de l’espace de forçage pour les essais.",
                 "Un partenaire de recherche indépendant pour les essais de sécurité et de forçage.",
                 "Utilisateurs finaux et partenaires de cofinancement pour le prototype."],
        "h_line": "Concept de la ligne",
        "line": ["Caisses", "Alimentation", "Une couche", "Section micro-ondes", "Égalisation", "× N sections", "Contrôle du cœur", "Caisses"],
        "line_cap": "Schéma fonctionnel de la machine prévue — pas le dessin d’une machine existante.",
        "h_specs": "Caractéristiques visées (prototype, projet)",
        "specs": [("Produit", "bulbes de tulipe vivants, 10/11 – 12/+ cm"), ("Débit du prototype", "0,5 t/h (≈ 20 000 bulbes/h)"),
                  ("Générateurs", "4–12 modules de 1,5 kW"),
                  ("Température au cœur du bulbe", "≤ 42 °C, limite absolue"), ("Manutention", "une couche, ≈ 1 m de large"),
                  ("Commande", "bibliothèque de modes, IA, supervision à distance"), ("Alimentation", "220 V (version 110 V sur demande)"), ("Conformité visée", "CE : (UE) 2023/1230, BT, CEM")],
        "specs_note": "Valeurs issues du cahier des charges provisoire ; elles ne seront fixées qu’après les essais sur bulbes.",
        "foot": "Octobre 2026. Les valeurs visées ne seront confirmées qu’après les essais sur bulbes.",
    },
    "nl": {
        "lang": "nl-BE",
        "kicker": "Ontwikkelingspartnerschap",
        "title": "Zachte microgolfbehandeling van tulpenbollen",
        "lead": "Parostok bouwt voort op onderzoek naar zaadbehandeling met microgolven sinds 2000. Samen met Belgische partners willen "
                "we een specifieke machine ontwikkelen voor de behandeling zonder chemie van levende tulpenbollen — "
                "in de eerste plaats ontworpen om de bol niet te beschadigen.",
        "h_why": "Waarom een aparte machine",
        "why": ["Een tulpenbol (32–45 mm) is meerdere keren groter dan de indringdiepte van het microgolfveld (ongeveer 1 cm).",
                "In ronde objecten van deze grootte kan de microgolfopwarming zich in het midden concentreren — precies waar de bloemknop zit.",
                "Zaaduitrusting kan dus niet zomaar hergebruikt worden: bollen vragen een eigen aanvoer, dosering en controle."],
        "h_design": "Ontwerpprincipes",
        "design": ["Eén laag draaiende bollen, zonder vallen of stoten.",
                   "Dosis in secties, met egalisatiezones daartussen.",
                   "<b>Harde grens: de kern van de bol komt nooit boven 42 °C.</b> Warmwaterbehandeling boven ongeveer 45 °C wordt als schadelijk voor tulpenbollen beschouwd.",
                   "Optionele gepulste stand met weinig opwarming.",
                   "Bibliotheek van standen in niet-vluchtig geheugen; AI kiest en regelt de dosis binnen de gekwalificeerde grenzen — de grens van 42 °C wordt bewaakt door onafhankelijke vergrendelingen die de AI niet kan omzeilen.",
                   "Bewaking en bediening op afstand: de lijn kan volledig autonoom werken.",
                   "Elke partij geregistreerd: vermogen, temperaturen, recept.",
                   "Makkelijk te reinigen contactoppervlakken, zodat ziekten niet tussen partijen worden overgedragen."],
        "h_status": "Waar we staan",
        "status": "Het effect van microgolfbehandeling op tulpenbollen is nog niet aangetoond: we vonden geen gepubliceerde "
                  "studie over levende tulpenbollen. Het programma start daarom met proeven op de veiligheid van de bloemknop "
                  "en een proefbroei tegenover een onbehandelde controle, en stopt als die geen voordeel tonen.",
        "h_plan": "Gefaseerd programma",
        "plan": [("1", "Eigenschappen van de bollen, veiligheidsdrempel van de knop, proefbroei → go / no-go", "6–9 maanden"),
                 ("2", "Ontwerp en prototype van de machine (0,5 t/u)", "ongeveer 2 jaar"),
                 ("3", "Onafhankelijke broei- en veldproeven", "één seizoen")],
        "plan_total": "Onderbouwd resultaat verwacht in 2029–2030.",
        "h_seek": "Wat we in België zoeken",
        "seek": ["Telers en broeiers die bollen en broeiruimte voor de proeven kunnen leveren.",
                 "Een onafhankelijke onderzoekspartner voor de veiligheids- en broeiproeven.",
                 "Eindgebruikers en cofinancieringspartners voor het prototype."],
        "h_line": "Concept van de lijn",
        "line": ["Kisten", "Aanvoer", "Eén laag", "Microgolfsectie", "Egalisatie", "× N secties", "Kerncontrole", "Kisten"],
        "line_cap": "Functioneel schema van de geplande machine — geen tekening van een bestaande machine.",
        "h_specs": "Beoogde specificaties (prototype, ontwerp)",
        "specs": [("Product", "levende tulpenbollen, 10/11 – 12/+ cm"), ("Capaciteit prototype", "0,5 t/u (≈ 20 000 bollen/u)"),
                  ("Generatoren", "4–12 modules van 1,5 kW"),
                  ("Kerntemperatuur van de bol", "≤ 42 °C, harde grens"), ("Behandeling", "één laag, ≈ 1 m breed"),
                  ("Besturing", "standenbibliotheek, AI, bewaking op afstand"), ("Voeding", "220 V (versie 110 V op aanvraag)"), ("Beoogde conformiteit", "CE: (EU) 2023/1230, LS, EMC")],
        "specs_note": "Waarden volgen het ontwerp van het technisch lastenboek en worden pas na de proeven op bollen vastgelegd.",
        "foot": "Oktober 2026. Beoogde waarden worden pas na de proeven op bollen bevestigd.",
    },
}
