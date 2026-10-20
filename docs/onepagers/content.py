"""Тексти одноаркушників Parostok (EN / FR / NL-BE).

Кожне твердження має джерело в docs/ktd/parostok-tulip/04_registr.yaml або
в профілі KARE (grantwriter_kare.zip). Заборонені твердження профілю
(certified, guaranteed yield, proven results, independently verified,
world's first) і CONFLICTING_UNRESOLVED цифри («до +65 %», «у 2–4 рази»)
не використовуються.
"""

CONTACT = "PE SPE “KARE” · Odesa, Ukraine · mwparostok@gmail.com · www.parostokmw.com"

SPECS = {
    "en": [("Power supply", "110 / 220 V"), ("Power consumption", "3.0–6.0 kW"),
           ("Throughput", "0.4–2.0 t/h"), ("Weight", "210 kg"),
           ("Dimensions", "70 × 90 × 206 cm"), ("Loading", "from the top"),
           ("Microwave frequency", "2.45 GHz (ISM band)")],
    "fr": [("Alimentation", "110 / 220 V"), ("Puissance absorbée", "3,0–6,0 kW"),
           ("Débit", "0,4–2,0 t/h"), ("Poids", "210 kg"),
           ("Dimensions", "70 × 90 × 206 cm"), ("Chargement", "par le haut"),
           ("Fréquence micro-ondes", "2,45 GHz (bande ISM)")],
    "nl": [("Voeding", "110 / 220 V"), ("Opgenomen vermogen", "3,0–6,0 kW"),
           ("Capaciteit", "0,4–2,0 t/u"), ("Gewicht", "210 kg"),
           ("Afmetingen", "70 × 90 × 206 cm"), ("Vullen", "langs boven"),
           ("Microgolffrequentie", "2,45 GHz (ISM-band)")],
}

EQUIPMENT = {
    "en": {
        "lang": "en",
        "kicker": "Equipment",
        "title": "Chemical-free microwave seed treatment",
        "lead": "Parostok treats seed before sowing with a controlled 2.45 GHz microwave field. "
                "Dry process, no chemicals, no residues on the seed.",
        "caption": "New design (rendering). The specifications refer to the current production model.",
        "h_how": "How it works",
        "how": ["Seed flows continuously through a controlled microwave field.",
                "The dose is set by exposure time at fixed power; each crop and variety has its own mode.",
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
        "lead": "Parostok traite les semences avant le semis par un champ micro-ondes contrôlé de 2,45 GHz. "
                "Procédé à sec, sans produits chimiques, sans résidus sur la semence.",
        "caption": "Nouveau design (rendu). Les caractéristiques concernent le modèle de production actuel.",
        "h_how": "Principe",
        "how": ["Les semences traversent en flux continu un champ micro-ondes contrôlé.",
                "La dose est réglée par la durée d’exposition à puissance fixe ; chaque culture et variété a son propre mode.",
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
        "lead": "Parostok behandelt zaaizaad vóór het zaaien met een gecontroleerd microgolfveld van 2,45 GHz. "
                "Droog proces, zonder chemicaliën, geen residu op het zaad.",
        "caption": "Nieuw ontwerp (rendering). De specificaties gelden voor het huidige productiemodel.",
        "h_how": "Werking",
        "how": ["Het zaad loopt in een continue stroom door een gecontroleerd microgolfveld.",
                "De dosis wordt ingesteld via de blootstellingstijd bij vast vermogen; elk gewas en elk ras heeft een eigen stand.",
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
        "why": ["A tulip bulb (32–45 mm) is several times larger than the depth a 2.45 GHz field penetrates (about 1 cm).",
                "In round objects of this size microwave heating can concentrate at the centre — exactly where the flower bud sits.",
                "Seed equipment therefore cannot simply be reused: bulbs need their own handling, dosing and control."],
        "h_design": "Design principles",
        "design": ["Single layer of rotating bulbs, no drops or impacts.",
                   "Dose delivered in sections, with equalisation zones in between.",
                   "<b>Hard limit: the bulb core never exceeds 42 °C.</b> Hot-water treatment above about 45 °C is considered harmful to tulip bulbs.",
                   "Optional low-heat pulsed mode.",
                   "Every batch logged: power, temperatures, recipe.",
                   "Easy-to-clean contact surfaces, so that disease is not carried between lots."],
        "h_status": "Where we stand",
        "status": "The effect of microwave treatment on tulip bulbs has not been demonstrated yet: we found no published "
                  "study on living tulip bulbs. The programme therefore starts with bud-safety and pilot forcing trials "
                  "against an untreated control, and stops if they show no benefit.",
        "h_plan": "Staged programme",
        "plan": [("1", "Bulb properties, bud-safety threshold, pilot forcing → go / no-go", "6–9 months", "€21–74k"),
                 ("2", "Design and prototype machine (0.5 t/h)", "about 2 years", "after gate 1"),
                 ("3", "Independent forcing and field trials", "one season", "after phase 2")],
        "plan_total": "Indicative total: up to about €0.5 million. Evidence-based result expected in 2029–2030.",
        "h_seek": "What we are looking for in Belgium",
        "seek": ["Growers and forcers who can provide bulbs and forcing space for trials.",
                 "An independent research partner for the safety and forcing trials.",
                 "End users and co-funding partners for the prototype."],
        "h_line": "Concept of the line",
        "line": ["Crates", "Feeder", "Single layer", "Microwave section", "Equalisation", "× N sections", "Core check", "Crates"],
        "line_cap": "Functional diagram of the planned machine — not a drawing of an existing unit.",
        "h_specs": "Target specifications (prototype, draft)",
        "specs": [("Product", "living tulip bulbs, 10/11 – 12/+ cm"), ("Prototype throughput", "0.5 t/h (≈ 20 000 bulbs/h)"),
                  ("Microwave frequency", "2.45 GHz (ISM band)"), ("Generators", "4–12 × 1.5 kW modules"),
                  ("Bulb core temperature", "≤ 42 °C, hard limit"), ("Handling", "single layer, ≈ 1 m wide"),
                  ("Power supply", "3 × 400 V, 50 Hz"), ("Target compliance", "CE: (EU) 2023/1230, LVD, EMC")],
        "specs_note": "Values follow the draft technical specification and are fixed only after the bulb tests.",
        "foot": "October 2026. Estimates are indicative and not a commercial offer.",
    },
    "fr": {
        "lang": "fr",
        "kicker": "Partenariat de développement",
        "title": "Traitement doux des bulbes de tulipe par micro-ondes",
        "lead": "Parostok s’appuie sur des recherches en traitement des semences par micro-ondes menées depuis 2000. Avec des partenaires belges, nous "
                "proposons de développer une machine dédiée au traitement sans chimie des bulbes de tulipe vivants — "
                "conçue avant tout pour ne pas abîmer le bulbe.",
        "h_why": "Pourquoi une machine dédiée",
        "why": ["Un bulbe de tulipe (32–45 mm) est plusieurs fois plus grand que la profondeur de pénétration d’un champ de 2,45 GHz (environ 1 cm).",
                "Dans des objets ronds de cette taille, le chauffage micro-ondes peut se concentrer au centre — là où se trouve le bourgeon floral.",
                "On ne peut donc pas simplement réutiliser l’équipement pour semences : les bulbes demandent leur propre manutention, dosage et contrôle."],
        "h_design": "Principes de conception",
        "design": ["Bulbes en une seule couche, en rotation, sans chute ni choc.",
                   "Dose appliquée par sections, avec des zones d’égalisation entre elles.",
                   "<b>Limite absolue : le cœur du bulbe ne dépasse jamais 42 °C.</b> Un traitement à l’eau chaude au-delà d’environ 45 °C est considéré comme nuisible aux bulbes de tulipe.",
                   "Mode pulsé à faible échauffement en option.",
                   "Chaque lot enregistré : puissance, températures, recette.",
                   "Surfaces de contact faciles à nettoyer, pour ne pas transmettre de maladies d’un lot à l’autre."],
        "h_status": "Où nous en sommes",
        "status": "L’effet du traitement micro-ondes sur les bulbes de tulipe n’est pas encore démontré : nous n’avons trouvé "
                  "aucune étude publiée sur des bulbes de tulipe vivants. Le programme commence donc par des essais de sécurité "
                  "du bourgeon et de forçage pilote face à un témoin non traité, et s’arrête s’ils ne montrent aucun bénéfice.",
        "h_plan": "Programme par étapes",
        "plan": [("1", "Propriétés des bulbes, seuil de sécurité du bourgeon, forçage pilote → décision go / no-go", "6–9 mois", "21–74 k€"),
                 ("2", "Conception et prototype de machine (0,5 t/h)", "environ 2 ans", "après l’étape 1"),
                 ("3", "Essais indépendants de forçage et au champ", "une saison", "après l’étape 2")],
        "plan_total": "Total indicatif : jusqu’à environ 0,5 million €. Résultat fondé sur des preuves attendu en 2029–2030.",
        "h_seek": "Ce que nous recherchons en Belgique",
        "seek": ["Producteurs et forceurs pouvant fournir des bulbes et de l’espace de forçage pour les essais.",
                 "Un partenaire de recherche indépendant pour les essais de sécurité et de forçage.",
                 "Utilisateurs finaux et partenaires de cofinancement pour le prototype."],
        "h_line": "Concept de la ligne",
        "line": ["Caisses", "Alimentation", "Une couche", "Section micro-ondes", "Égalisation", "× N sections", "Contrôle du cœur", "Caisses"],
        "line_cap": "Schéma fonctionnel de la machine prévue — pas le dessin d’une machine existante.",
        "h_specs": "Caractéristiques visées (prototype, projet)",
        "specs": [("Produit", "bulbes de tulipe vivants, 10/11 – 12/+ cm"), ("Débit du prototype", "0,5 t/h (≈ 20 000 bulbes/h)"),
                  ("Fréquence micro-ondes", "2,45 GHz (bande ISM)"), ("Générateurs", "4–12 modules de 1,5 kW"),
                  ("Température au cœur du bulbe", "≤ 42 °C, limite absolue"), ("Manutention", "une couche, ≈ 1 m de large"),
                  ("Alimentation", "3 × 400 V, 50 Hz"), ("Conformité visée", "CE : (UE) 2023/1230, BT, CEM")],
        "specs_note": "Valeurs issues du cahier des charges provisoire ; elles ne seront fixées qu’après les essais sur bulbes.",
        "foot": "Octobre 2026. Les estimations sont indicatives et ne constituent pas une offre commerciale.",
    },
    "nl": {
        "lang": "nl-BE",
        "kicker": "Ontwikkelingspartnerschap",
        "title": "Zachte microgolfbehandeling van tulpenbollen",
        "lead": "Parostok bouwt voort op onderzoek naar zaadbehandeling met microgolven sinds 2000. Samen met Belgische partners willen "
                "we een specifieke machine ontwikkelen voor de behandeling zonder chemie van levende tulpenbollen — "
                "in de eerste plaats ontworpen om de bol niet te beschadigen.",
        "h_why": "Waarom een aparte machine",
        "why": ["Een tulpenbol (32–45 mm) is meerdere keren groter dan de indringdiepte van een veld van 2,45 GHz (ongeveer 1 cm).",
                "In ronde objecten van deze grootte kan de microgolfopwarming zich in het midden concentreren — precies waar de bloemknop zit.",
                "Zaaduitrusting kan dus niet zomaar hergebruikt worden: bollen vragen een eigen aanvoer, dosering en controle."],
        "h_design": "Ontwerpprincipes",
        "design": ["Eén laag draaiende bollen, zonder vallen of stoten.",
                   "Dosis in secties, met egalisatiezones daartussen.",
                   "<b>Harde grens: de kern van de bol komt nooit boven 42 °C.</b> Warmwaterbehandeling boven ongeveer 45 °C wordt als schadelijk voor tulpenbollen beschouwd.",
                   "Optionele gepulste stand met weinig opwarming.",
                   "Elke partij geregistreerd: vermogen, temperaturen, recept.",
                   "Makkelijk te reinigen contactoppervlakken, zodat ziekten niet tussen partijen worden overgedragen."],
        "h_status": "Waar we staan",
        "status": "Het effect van microgolfbehandeling op tulpenbollen is nog niet aangetoond: we vonden geen gepubliceerde "
                  "studie over levende tulpenbollen. Het programma start daarom met proeven op de veiligheid van de bloemknop "
                  "en een proefbroei tegenover een onbehandelde controle, en stopt als die geen voordeel tonen.",
        "h_plan": "Gefaseerd programma",
        "plan": [("1", "Eigenschappen van de bollen, veiligheidsdrempel van de knop, proefbroei → go / no-go", "6–9 maanden", "€ 21–74 k"),
                 ("2", "Ontwerp en prototype van de machine (0,5 t/u)", "ongeveer 2 jaar", "na fase 1"),
                 ("3", "Onafhankelijke broei- en veldproeven", "één seizoen", "na fase 2")],
        "plan_total": "Indicatief totaal: tot ongeveer € 0,5 miljoen. Onderbouwd resultaat verwacht in 2029–2030.",
        "h_seek": "Wat we in België zoeken",
        "seek": ["Telers en broeiers die bollen en broeiruimte voor de proeven kunnen leveren.",
                 "Een onafhankelijke onderzoekspartner voor de veiligheids- en broeiproeven.",
                 "Eindgebruikers en cofinancieringspartners voor het prototype."],
        "h_line": "Concept van de lijn",
        "line": ["Kisten", "Aanvoer", "Eén laag", "Microgolfsectie", "Egalisatie", "× N secties", "Kerncontrole", "Kisten"],
        "line_cap": "Functioneel schema van de geplande machine — geen tekening van een bestaande machine.",
        "h_specs": "Beoogde specificaties (prototype, ontwerp)",
        "specs": [("Product", "levende tulpenbollen, 10/11 – 12/+ cm"), ("Capaciteit prototype", "0,5 t/u (≈ 20 000 bollen/u)"),
                  ("Microgolffrequentie", "2,45 GHz (ISM-band)"), ("Generatoren", "4–12 modules van 1,5 kW"),
                  ("Kerntemperatuur van de bol", "≤ 42 °C, harde grens"), ("Behandeling", "één laag, ≈ 1 m breed"),
                  ("Voeding", "3 × 400 V, 50 Hz"), ("Beoogde conformiteit", "CE: (EU) 2023/1230, LS, EMC")],
        "specs_note": "Waarden volgen het ontwerp van het technisch lastenboek en worden pas na de proeven op bollen vastgelegd.",
        "foot": "Oktober 2026. Ramingen zijn indicatief en geen commercieel aanbod.",
    },
}
