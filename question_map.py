# question_mapping.py
question_map = {

    # AVANT DE COMMENCER
    "A quel CLPE êtes-vous rattaché ?": "clpe",
    "Indiquez la date.": "date",

    # Concernant l’installation de votre CLPE
    "Des élus locaux ont-ils été nommés dans la co-présidence ?": "local_officials_1",
    "Existe-il un Règlement Intérieur précisant le fonctionnement du CLPE ?" : "internal_rules_1",
    "Le CLPE est-il la seule instance de gouvernance des politiques de l'emploi sur le territoire ?": "instances_gov_1",
    "L’articulation entre les comités locaux et les comités départementaux existe-elle ?": "fluidite_1",
    "Sur une échelle de 0 (pas d’ascendance) à 5 (ascendance très fluide), comment qualifierez-vous l’ascendance entre le niveau local et le niveau départemental ? Par ascendance, on entend dans ce contexte le flux d'informations et d'actions mises en œuvre qui partent d'un niveau local pour atteindre un niveau supérieur (départemental) afin d'être examinées et prises en compte dans des décisions plus larges.": "asc_1",
    #--------------------------------------

    # 2    CONCERNANT LES OBJECTIFS ET MISSIONS DE VOTRE CLPE
    "Un diagnostic territorial a-t-il été :": "diag_2",
    "Est-il prévu d’actualiser ce diagnostic ?": "prev_diag_2",
    "Connaissez-vous les objectifs de la feuille de route fixés par le CLPE à court terme ?": "Obj_2",
    "La feuille de route a-t-elle été ?": "FDR_2",
    "Combien de fiches action concrétisant les priorités communes à court terme ont été rédigées (une fiche action identifie un objectif pour l’ensemble des acteurs afin de répondre à une problématique du territoire, précise le rôle de chacun dans la mise en œuvre et les indicateurs de suivi associés) ?": "cb_2",
    "Connaissez-vous la finalité de la conférence des financeurs des comités territoriaux pour l’emploi, créée au niveau des CDPE (Art. L5311-10 du code du Travail) ?": "finalite_2",
    "La conférence des financeurs des comités territoriaux pour l’emploi a-t-elle été sollicitée ?" : "Conf_fin_2",
    "Avez-vous partagé une vision globale moyen terme (Offre de Service globale, maillage des Offre de Service, convergence des SI, expertise sectorielle commune…) ?": "moyen_terme_2",


    #--------------------------------------
    # 3    CONCERNANT L'ENGAGEMENT DES PARTIES PRENANTES AU SEIN DE VOTRE CLPE
    "Est-ce que les acteurs nommés ou leurs représentants sont parties prenantes et impliquées dans les instances ?":"Impli_3",
    "Comment s’organise la participation des élus au CLPE ?": "Particip_3",
    "Des consultations ont-elles été menées auprès des usagers pour recueillir des avis et besoins ?": "consult_3",

    #--------------------------------------
    # 4    Concernant le rôle de France Travail dans le cadre de sa mission d’appui à la mise en œuvre du RPE

    "Le rôle d'appui de France Travail a-t-il été présenté ?": "pres_4",
    "Les membres du CLPE utilisent-ils le tableau de bord du réseau pour l'emploi ?": "RPE_4",
    "Quels sont les autres outils qui ont été présentés aux membres du CLPE ?": "Outils_4",
    "Quels autres outils utilisez-vous ?": "Outils2_4",


    #--------------------------------------
    # 5    Concernant les  méthodes de travail de votre CLPE
    "La méthodologie de travail mise en place au sein du CLPE permet-elle de modifier la coopération ?": "Method_5",
    "La méthodologie de travail mise en place au sein du CLPE favorise-t-elle la coopération au service de l’impact ?": "Method_im_5",


    "Des ordres du jour des CLPE sont-ils préparés en amont ?": "amont_5",
    "Les ordres du jour sont-ils préparés en collaboration ?": "collabo_5",


    "Combien de fois par an votre CLPE se réunit-il en format plénier ?": "freq_5",
    "Combien de comités techniques ou groupes de travail sont organisés par an ?": "freq2_5",

    "Les comptes rendus des réunions sont-ils rédigés et diffusés ?": "CR_5",
    "Les fiches actions sont-elles systématiquement saisies sur le tableau de bord du Réseau pour l’emploi ?": "FA_5",
    "Qui saisit les fiches actions ?": "Qui_5",
    "Les orientations sont-elles objectivées à partir de constats partagés et d'indicateurs de résultats ?": "obj_5",
    "Dans le cadre des comités techniques (préparations des instances, suivis des feuilles de route ou actions, commissions spécifiques sur publics spécifiques par exemple), une méthode structurée et participative est-elle mise en œuvre, permettant la mobilisation des acteurs au service des résultats ?": "method_5",
    "L'engagement actif de tous est-il encouragé ?": "actif_5",
    "Les contributions de chacun et les actions menées sont-elles communiquées et valorisées ?": "contri_5",

    #--------------------------------------
    # 6    Concernant la culture du résultat au sein de votre CLPE : évaluation et indicateurs de suivi et de résultats
    "L’appropriation des indicateurs du tableau de bord a-t-elle fait l’objet de séance(s) collaborative(s) ?": "appr_6",
    "Pour vous, la différence entre les résultats des actions et l’impact des actions est-elle claire ?": "pour_vous_6",
    "Des indicateurs de performance spécifiques à chaque action menée ont-ils été établis pour mesurer les résultats ?": "ind_6",
    "Menez-vous une analyse des effets ou résultats des actions mises en œuvre ?": "analyse_6",
    "Évaluez-vous l’impact des actions mises en œuvre ?": "eval_6",
    "Réinterrogez-vous la mobilisation des moyens au regard des résultats obtenus ?": "result_6",


    #--------------------------------------
    # 7    Concernant la communication et la sensibilisation de votre CLPE
    "De manière générale, des actions de communication sur les missions et/ou actions des CLPE sont-elles réalisées par les membres du CLPE ?": "com_7",
    "Les résultats des actions menées par les CLPE sont-ils communiqués aux ... ?": "result_7",


    #--------------------------------------
    # 8   Recours aux outils collaboratifs
    "Des outils collaboratifs ont-ils été mis en place au sein du CLPE ?": "outils_8",
    "Si oui, pour quelles utilisations ?": "utilisation_8",
    "Quelles sont les plateformes collaboratives que vous utilisez le plus ?":"platform_8",


    #--------------------------------------
    # 9 Concernant l'adaptation et l'amélioration continue au sein de votre CLPE
    "Des retours d'expériences sont-ils mis en place pour identifier les points à améliorer ?": "proc_9",
    "Des actions de montées en compétences pour les membres des CLPE sont-elles proposées ?": "form_9",
    "Avez-vous l’impression d’avoir engagé une transformation du Service Public pour l’Emploi Local (SPEL) en CLPE ?": "SPEL_9",
}
