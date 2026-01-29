import pandas as pd

section_schemes = {

    #Thématique 1
    "Section_1":{
        "local_officials_1": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0},
        "internal_rules_1": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0
            },
        "instances_gov_1": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0
            },
        "fluidite_1": {
            "Oui": 1,
            "Oui mais elle n'est pas fluide": 0.5,
            "Non": 0,
            "Ne sait pas": 0},
        "asc_1": {
            0: 0,
            1: 0.2,
            2: 0.4,
            3: 0.6,
            4: 0.8,
            5: 1,
            },
    },

    "Section_2":{
        "diag_2": {
            "Coconstruit": 0.5,
            "Formalisé": 0.5,
            "Partagé": 0.5,
            "Autres": 0,
            "Ne sait pas": 0,
        },
        "prev_diag_2": {

            "Oui plus d'une fois par an": 1,
            "Oui une fois par an": 0.5,
            "Ne sait pas": 0,
            "Non": 0,
        },
        "Obj_2": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,
        },

        "obj_const_2": {
            "Coconstruit": 0.5,
            "Formalisé": 0.5,
            "Partagé": 0.5,
            "Autres": 0,
            "Ne sait pas": 0,
        },

        "FDR_2": {
            "Coconstruite": 0.5,
            "Formalisée": 0.5,
            "Partagée": 0.5,
            "En cours d'élaboration": 0.5,
            "Autres": 0,
            "Ne sait pas": 0,
        },

        "cb_2": {
            "0": 0,
            "1": 1,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 0.5,
            "6": 0.5,
            "7": 0.5,
            "8": 0.5,
            "9": 0.5,
            "10": 0.5,
            "-1": 0,
        },

        "finalite_2": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,
            },
        "Conf_fin_2": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,
            },
        "moyen_terme_2": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,
            },
    },

    "Section_3":{
        "Impli_3": {
            "Ne sait pas": 0,
            "Non": 0,
            "Parfois": 0.4,
            "Régulièrement": 0.6,
            "Souvent": 0.8,
            "Toujours": 1,
            },

        "Particip_3":{
            "Tous les élus sont présents": 1,
            "Les élus sont présents à tour de rôle": 0.5,
            "Les élus se font représenter": 0.2,
            "L’organisation de la participation des élus n’est pas figée": 0,
            "Ne sait pas": 0,
        },

        "consult_3": {
            "Oui auprès des employeurs ou de leurs représentants": 0.5,
            "Oui auprès des demandeurs\nd’emplois ou de leurs représentants": 0.5,
            "Oui auprès des employeurs et des\ndemandeurs d’emplois ou\nde leurs représentants":1,
            "Non pas pour le moment mais c'est envisagé": 0.2,
            "Non et ce n'est pas prévu": 0,
            "Ne sait pas": 0,
        },
        },

    "Section_4":{
        "pres_4": {
            "Ne sait pas": 0,
            "Non présenté": 0,
            "Présenté mais non compris": 0.5,
            "Présenté et compris": 1,
        },
        "RPE_4": {
            "Ne sait pas": 0,
            "Non": 0,
            "Parfois": 0.5,
            "Oui": 1,
        },
        "Outils_4": {

        },
        "Outils2_4": {

        },

    },
    "Section_5":{
        "Method_5": {
            "Ne sait pas": 0,
            "Jamais": 0,
            "Quelques fois": 0.5,
            "Systématiquement": 1,
        },
        "Method_im_5": {
            "Ne sait pas": 0,
            "Jamais": 0,
            "Quelques fois": 0.5,
            "Systématiquement": 1,
        },
        "amont_5": {
            "Ne sait pas": 0,
            "Jamais": 0,
            "Quelques fois": 0.5,
            "Systématiquement": 1,
        },

        "freq_5": {
            "0": 0,
            "1": 1,
            "2": 1,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 1,
            "7": 1,
            "8": 1,
            "9": 1,
            "10": 1,
            "-1": 0,
        },

        "freq2_5": {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 1,
            "4": 1,
            "5": 1,
            "6": 1,
            "7": 1,
            "8": 1,
            "9": 1,
            "10": 1,
            "-1": 0,
        },

        "CR_5": {
            "Ne sait pas": 0,
            "Jamais": 0,
            "Quelques fois": 0.2,
            "Systématiquement": 1,
        },

        "FA_5": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,
        },
        "Qui_5": {
            "Les porteurs de l'action": 0.3,
            "France Travail": 0.3,
            "DDETS": 0.3,
            "Les membres à tour de rôle": 0.3,
            "Pas d’organisation définie": 0,
            "Ne sait pas": 0,
        },

        "obj_5": {
            "Ne sait pas": 0,
            "Jamais": 0,
            "Quelques fois": 0.2,
            "Systématiquement": 1,
        },

        "method_5": {
            "Ne sait pas": 0,
            "Jamais": 0,
            "Quelques fois": 0.2,
            "Systématiquement": 1,
        },
        "actif_5": {
            "Oui, les membres participent à\ndes groupes de travail spécifiques": 1,
            "Oui, les membres sont en responsabilité\nde groupes de travail spécifiques": 1,
            "Non": 0,
            "Ne sait pas": 0,},

        "contri_5": {
            "Oui systématiquement": 1,
            "Oui régulièrement": 0.8,
            "Parfois": 0.2,
            "Jamais": 0,
            "Ne sait pas": 0,},

    },
    "Section_6":{
        "appr_6": {
            "Oui et le sujet a été abordé en profondeur": 1,
            "Oui et le sujet a été abordé partiellement": 0.5,
            "Non pas encore": 0,
            "Non et ce n’est pas prévu pour le moment": 0,
            "Ne sait pas": 0,},

        "pour_vous_6": {
            "Non": 0,
            "Oui": 1,
            "Ne sait pas": 0,},


        "ind_6": {
            "Non": 0,
            "Oui pour quelques-unes des actions": 0.5,
            "Oui pour toutes les actions": 1,
            "Ne sait pas": 0,},
        "analyse_6": {
            "Non": 0,
            "Oui une fois par an": 0.5,
            "Oui plusieurs fois par an": 1,
            "Ne sait pas": 0,},

        "eval_6": {
            "Non": 0,
            "Oui une fois par an": 0.5,
            "Oui plusieurs fois par an": 1,
            "Ne sait pas": 0,},

        "result_6": {
            "Jamais": 0,
            "Parfois": 0.5,
            "Systématiquement": 1,
            "Ne sait pas": 0,},

    },

    "Section_7":{
        "com_7": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,},

        "result_7": {
            "Usagers demandeurs d’emploi": 0.2,
            "Usagers entreprises / Employeurs": 0.2,
            "Presses": 0.2,
            "Autres influenceurs locaux": 0.2,
            "Auprès des agents internes aux membres du CLPE": 0.2,
            "Les actions ne sont pas communiquées": 0,
            "Ne sait pas": 0,
            },
        },

    "Section_8":{
        "outils_8": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0,},
        "utilisation_8": {
        },
        "platform_8": {

            },
    },

    "Section_9":{
        "proc_9": {
            "Systématiquement": 1,
            "Parfois": 0.5,
            "Jamais": 0,
            },

        "form_9": {
            "Oui": 1,
            "Non, mais c'est prévu": 0.5,
            "Non": 0,
            "Ne sait pas": 0,     },

        "SPEL_9": {
            "Oui": 1,
            "Non": 0,
            "Ne sait pas": 0, 
        },
    },
}

# Score maximal pour chaque section
section_max_scores = {
    "Section_1": 5,
    "Section_2": 9.5,
    "Section_3": 3,
    "Section_4": 4,
    "Section_5": 13.2,
    "Section_6": 6,
    "Section_7": 2,
    "Section_8": 3,
    "Section_9": 3
}

SECTION_NOTES = {
    "Section_1": """
        Pour rappel, l’organisation des CLPE découle du décret du 18 juin 2024, pris en application de la Loi pour le Plein Emploi : <br/>
        •	Des représentants de l’État, de la région et du département doivent être nommés par le préfet de département ;<br/>
        •	Un représentant de chacun des établissements publics de coopération intercommunale dotés d'une fiscalité propre ou des établissements publics territoriaux doivent être nommés par le préfet du département sur proposition de leurs présidents ;<br/>
        •	Des représentants des communes et de leurs groupements doivent être nommés par le préfet de département sur proposition de l'association des maires du département ;<br/>
        •	Le directeur départemental de l'opérateur France Travail ou son représentant, les présidents des missions locales du Territoire ou leurs représentants et les présidents des organismes de placement spécialisé dans l'insertion professionnelle des personnes en situation de handicap du territoire ou leurs représentants doivent être intégrés dans la gouvernance des CLPE.<br/>
        <br/>
        Il est recommandé :<br/>
        •	D’associer un maximum les élus locaux nommés par le préfet de département dans la gouvernance, à toutes démarches relatives aux missions des CLPE.<br/>
        •	De veiller à l’invitation et à la présence des élus concernés aux instances du CLPE.<br/>
        •	De s’assurer que l’ensemble des membres du RPE soient invités, présents et actifs dans les instances.<br/>
        •	D’encourager la co-construction d'un règlement intérieur avec la participation des membres du CLPE et l'appui des co-présidents.<br/>
        •	De veiller à ce que les autres instances de gouvernance relatives à l’emploi sur le territoire ne subsistent pas (le CLPE a vocation à se substituer à l’ensemble des instances de gouvernance pour l’emploi qui existaient sur le territoire.)<br/>
        •	De veiller à ce que la réunion plénière avec l’ensemble des présidents des comités locaux pour l’emploi et des acteurs mobilisés en faveur de l’insertion et de l’emploi se tienne à minima une fois par an.<br/>
        •	De réunir au minimum trois fois par an les comités techniques.<br/>
        •	De s’assurer que l’articulation entre le CLPE et le CDPE auquel il est rattaché soit fluide : les informations importantes doivent être partagées de part et d’autre ainsi qu’avec l’ensemble des acteurs locaux pour l’emploi. Les priorités du CDPE et du CLPE doivent être partagées dans une logique circulaire afin d’être prises en compte dans les feuilles de route de chacun des comités.<br/>



    """,


    "Section_2": """
        Les objectifs fixés par le CLPE doivent être coconstruits avec l’ensemble des membres du CLPE, en tenant compte des besoins du territoire, des champs d’intervention des Comités Territoriaux Pour l’Emploi et des priorités du Comité National Pour l’Emploi.<br/>
        <br/>
        Ils doivent être formalisés dans une feuille de route, mise à disposition de tous afin de pouvoir s’y référer à n’importe quel moment si nécessaire. Ces objectifs coconstruits doivent également être partagés avec les membres participant ponctuellement au CLPE. La feuille de route peut, par exemple, être (re)présentée lors d’une réunion spécifique.<br/>
        <br/>
        La réalisation de cette feuille de route se base sur un diagnostic coconstruit et partagé également par les membres du CLPE ainsi qu’avec tout acteur local jugé pertinent. Ce diagnostic permet d’identifier collectivement les besoins du territoire. Il est nécessaire qu’il soit actualisé au moins une fois par an. <br/>
        <br/>
        De cette feuille de route, 2 ou 3 actions prioritaires maximum doivent être identifiées et rédigées en fiches actions. Il convient d’identifier des responsables et des parties prenantes qui auront la charge de leur mise en œuvre à court terme. Des outils sont mis à disposition par France Travail pour faciliter cette mise en œuvre. Il est également préconisé de partager une vision à moyen terme avec les membres du CLPE (identification de synergies à développer, évolution éventuelle de la complémentarité des offres de service, amélioration de l’organisation, anticipation des défis à venir, scénarios prospectifs, réussites collectives attendues…).
    """,

    "Section_3": """
        Chaque membre participant aux instances ou actions du CLPE détient une expertise complémentaire de celle des autres. C’est la raison pour laquelle chacun, en tenant compte de son rôle et du périmètre d’intervention, doit être engagé et se sentir impliqué dans les missions et actions du CLPE. Il est nécessaire que chacun puisse s’exprimer lors des réunions et/ou comités techniques, que chacun ait accès et reçoive les informations.<br/>
        <br/>
        De la même manière, il est préconisé la participation de l’ensemble des membres aux processus d’aide à la décision. En parallèle, il est recommandé d’organiser des écoutes participatives auprès des demandeurs d’emplois et des employeurs afin de recueillir leurs avis et besoins et de les intégrer dans les décisions prises par le CLPE. Ces consultations permettent d’aligner l’engagement des membres du CLPE sur les besoins du territoire et de maintenir une cohérence d’ensemble.

    """,

    "Section_4": """
        Pour rappel, France Travail joue un rôle d’appui à la gouvernance des CLPE. Dans ce cadre, France Travail est chargé de faciliter la coopération entre tous les acteurs du réseau pour l'emploi, de participer à la circulation de l’information, d'ajuster les dispositifs d'accompagnement en fonction des résultats obtenus et des retours des usagers, de mettre en place des formations et des outils adaptés pour les conseillers et les professionnels de l'emploi... Le rôle de France Travail doit impérativement avoir été présenté, compris et rappelé régulièrement notamment si de nouveaux participants au CLPE intègrent la démarche. Cette présentation peut faire l’objet, par exemple, d’un point à l’ordre du jour d’une instance. De nombreux outils France Travail sont mis à disposition pour faciliter la collaboration entre parties prenantes du CLPE, pour partager des données du territoire, pour mettre en œuvre et piloter des actions. Le CLPE est donc invité à s’emparer de ces ressources disponibles. Ces outils et ressources doivent également faire l’objet de présentation ciblée auprès des membres du CLPE.
    """,

    "Section_5": """
        La méthodologie de travail mise en œuvre au sein du CLPE doit permettre de favoriser la coopération. Il est recommandé que les ordres du jour soient préparés en amont de la réunion en recensant les besoins des participants puis envoyés quelques jours avant l’instance afin que chacun puisse en prendre connaissance. Les comptes rendus des réunions doivent systématiquement être diffusés aux membres du CLPE.<br/>
        <br/>
        Il est conseillé que les décisions prises au sein de la gouvernance puissent être objectivées et soutenues par des faits concrets et indicateurs partagés. Il est également recommandé d’organiser à minima 1 CLPE par an et 3 comités techniques par an. <br/>
        <br/>
        Une méthode de travail structurée et participative facilite également la mise en action et la culture du résultat au sein des comités techniques. Il est conseillé de la décrire en collaboration avec les membres du CLPE puis de la mettre à disposition afin que chacun puisse s’y référer. Chacun des membres est encouragé à s’engager activement en participant à des groupes de travail spécifiques et / ou en étant en responsabilité d’un ou plusieurs groupes de travail. Il est vivement recommandé de communiquer et de valoriser les contributions réalisées par chacun des membres.

    """,

    "Section_6": """
        La réalisation de points de pilotage contribue à construire une culture du résultat, favorise une meilleure compréhension des données, participe à mobiliser l'engagement de tous et in fine permettent de mener des actions à impact sur le territoire au bénéfice des usagers. Par ailleurs, le partage des résultats ne doit pas être un simple reporting, mais une opportunité d'apprendre des succès et des échecs, d'identifier les bonnes pratiques et de décider collectivement des ajustements nécessaires pour les actions futures. Il est donc souhaitable que ce partage se fasse de façon ludique et participative afin de rendre les résultats accessibles et sources d’inspiration pour tous.<br/>
        <br/>
        Les indicateurs du tableau de bord et l’analyse des résultats doivent faire l’objet, à minima, d’une séance collaborative avec les membres du CLPE afin de s’assurer que l’ensemble des membres du CLPE ait connaissance des indicateurs existants et pertinents à suivre au regard des actions mises en œuvre et des objectifs du CLPE. Cela permet également d’analyser collectivement les écarts constatés, d’identifier les succès et défis à relever, les axes et actions à ajuster. <br/>
        <br/>
        Des indicateurs de performance doivent donc être définis au préalable pour chacune des actions prioritaires afin d’en mesurer les résultats. L’impact des actions prioritaires mises en œuvre doit régulièrement être évalué grâce au suivi des indicateurs de performance. <br/>
        <br/>
        Il peut être facilitant de formaliser un processus rapide d'évaluation en définissant des étapes claires pour chaque évaluation : collecte des données, analyse, identification des écarts, définition des actions correctives. Les résultats de l’évaluation doivent être partagés avec toutes les parties prenantes du CLPE. Désigner et former des personnes clés au sein de chaque partie prenante du CLPE pour qu'elles deviennent des référentes sur l'utilisation et l'interprétation des tableaux de bord peut être proposé.
    """,

    "Section_7": """
        Afin de renforcer l’engagement des membres du CLPE et de mobiliser d’autres acteurs du territoire, il peut être intéressant de mener des actions de communication sur les missions portées par le CLPE sur son territoire, a minima auprès du grand public et auprès des influenceurs économiques : par exemples, un rapport annuel communiqué sur les sites internet des membres du CLPE, des communications sur les réseaux sociaux pour mettre en lumière ce qui est réalisé, des actions ciblées de communication auprès d’un public en particulier via les agences ou antennes des membres du CLPE, etc.
    """,

    "Section_8": """
    Les outils collaboratifs sont des supports et vecteurs d’information essentiels qui s’imposent rapidement dans un cadre collaboratif. <br/>
    <br/>
    Pour améliorer la collaboration et la performance, il est recommandé d’identifier les défis de collaboration et les besoins des participants au CLPE (gain de temps, centralisation, transparence et harmonisation des informations partagées en temps réel, coproduction de supports en ligne, chat, gestion de projets et de planifications, renforcement de la cohésion, accélération de la prise de décision). Il est judicieux de capitaliser également sur l’existant : habitudes de travail, plateformes collaboratives déjà utilisées et accessibles à tous, personnes identifiées comme ressources sur l’utilisation du digital…. <br/>
    <br/>
    Il est préférable de mettre en place progressivement l’utilisation d’outils adhoc et d’accompagner une montée en compétences ajustée aux besoins et aux niveaux de maitrise technique des membres. Il est recommandé de prioriser les usages à fort impact comme le partage de documents, la coproduction de documents partagés et la visioconférence.
    """,

    "Section_9": """
    Pour amener les membres du CLPE à s'inscrire dans un processus d'amélioration continue, il est essentiel de créer un cadre qui encourage la transparence, l'apprentissage mutuel et l'action collective. Il est suggéré de souligner les gains potentiels de l’amélioration continue en termes d'efficacité, de qualité des résultats, de réduction des frictions, et de renforcement de la confiance mutuelle.<br/>
    <br/>
    Il est conseillé de s’accorder sur des modalités de retours d’expériences pour aider les membres du CLPE à identifier les points à améliorer dans la gouvernance mais aussi dans la mise en œuvre des actions prioritaires.<br/>
    <br/>
    L'amélioration continue implique de pouvoir identifier les réussites puis de les valoriser. Il est donc conseillé d’identifier les problèmes et les dysfonctionnements et d’encourager en parallèle une culture où l'erreur est vue comme une opportunité d'apprendre.<br/>
    <br/>
    Pour qu'elle soit efficace, l'amélioration continue doit être organisée et régulière : lors de bilans d’actions et lors d’instance CLPE, il est intéressant de prévoir dans l’ordre du jour un point dédié pour analyser ce qui a bien fonctionné, ce qui aurait pu être amélioré, et pourquoi. Il est possible d’utiliser, en les adaptant si besoin, des méthodes d’échanges telles que «Start, Stop, Continue » ou « Mad, Sad, Glad ». Au-delà des rétrospectives finales, prévoir des moments plus courts et fréquents pour faire le point sur les actions en cours et ajuster rapidement. Il est utile de noter les problèmes identifiés, les solutions proposées et les actions décidées. Cela permet de suivre les progrès et d'éviter de reproduire les mêmes erreurs. Un outil collaboratif de gestion de projet peut être très utile ici.
    """,
}




def calculate_section_score(df, section_name, return_type='both'):
        section_rules = section_schemes.get(section_name, {})
        total_score = 0
        total_possible = 0
        n_respondents = len(df)
        print("numéro de respondents is", n_respondents)

        # Multi-choix avec addition classique
        multi_value_columns = [
            "obj_const_2", "diag_2", "FDR_2",
            "actif_5", "result_7", "comment_8", "platform_8"
        ]

        # Colonnes à scoring par palier
        outils_palier_columns_4 = ["Outils_4", "Outils2_4"]
        def score_outils_palier_4(x):
            if pd.isna(x) or str(x).strip() == "":
                return 0
            options = [
                opt.strip()
                for opt in str(x).split(';')
                if opt.strip()!= 'Ne sait pas'
            ]
            n = len(options)
            if n == 0:
                return 0
            elif n == 1:
                return 0.3
            elif 2 <= n <= 5:
                return 0.5
            else:
                return 1

        outils_palier_columns_8_1 = ["utilisation_8"]
        def score_outils_palier_8_1(x):
            if pd.isna(x) or str(x).strip() == "":
                return 0

            options = [
                opt.strip()
                for opt in str(x).split(';')
                if opt.strip()!= 'Ne sait pas'
            ]

            n = len(options)

            if n == 0:
                return 0
            elif n == 1:
                return 0.2
            elif n == 2:
                return 0.5
            elif n==3:
                return 0.8
            else:
                return 1
        outils_palier_columns_8_2 = ["platform_8"]
        def score_outils_palier_8_2(x):
            if pd.isna(x) or str(x).strip() == "":
                return 0

            options = [
                opt.strip()
                for opt in str(x).split(';')
                if opt.strip()!= 'Ne sait pas'
            ]

            n = len(options)

            if n == 0:
                return 0
            elif 1 <= n <= 2:
                return 1
            else:
                return 0.5

        for column, rule in section_rules.items():
            if column not in df.columns:
                continue

            #  Outils par palier
            if column in outils_palier_columns_4:
                scores = df[column].apply(score_outils_palier_4)
                max_per_row = 1

            elif column in outils_palier_columns_8_1:
                scores = df[column].apply(score_outils_palier_8_1)
                max_per_row = 1
            elif column in outils_palier_columns_8_2:
                scores = df[column].apply(score_outils_palier_8_2)
                max_per_row = 1

            # multi-choix additif
            elif column in multi_value_columns:
                scores = df[column].apply(
                    lambda x: sum(
                        rule.get(option.strip(), 0)
                        for option in str(x).split(';')
                        if option.strip() in rule
                    )
                )
                max_per_row = sum(rule.values())

            #  : règle fonction
            elif callable(rule):
                scores = df[column].apply(rule)
                max_per_row = 1

            #  mapping simple
            elif isinstance(rule, dict):
                scores = df[column].map(rule).fillna(0).astype(float)
                max_per_row = max(rule.values()) if rule else 0

            else:
                continue

            print(
                f"Column '{column}': {scores.sum()} points "
                f"(max possible: {max_per_row * n_respondents})"
            )

            total_score += scores.sum()
            total_possible += max_per_row * n_respondents

        if n_respondents > 0 and total_possible > 0:
            raw_score = total_score / n_respondents
            max_score = section_max_scores.get(
                section_name,
                total_possible / n_respondents
            )
            percentage = (raw_score / max_score) * 100 if max_score > 0 else 0
            print("Pourcentage", percentage)

            if return_type == 'percentage':
                return percentage
            elif return_type == 'raw':
                return raw_score
            elif return_type == 'both':
                return raw_score, percentage
            else:
                raise ValueError("return_type must be 'percentage', 'raw', or 'both'")

        return 0 if return_type != 'both' else (0, 0)
