import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc


from visuals.graphiques import plot_multi_stacked_bar
from visuals.graphiques import plot_score_distribution
from visuals.graphiques import plot_side_graph

def section_5(data, output_path, file_name):





    fig = plt.figure(figsize=(5, 27))
    gs = fig.add_gridspec(7, 1, height_ratios=[10,10, 26,6,4, 3, 6], hspace=0.4)

    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])
    ax_4 = fig.add_subplot(gs[3])
    ax_5 = fig.add_subplot(gs[4])
    ax_6 = fig.add_subplot(gs[5])
    ax_7 = fig.add_subplot(gs[6])

    plot_score_distribution(
        ax_1,
        data['freq_5'],
        n_range=11,
        x_text = "",
        font_size= 18,
        label_pad=2,
        title="Combien de fois par an votre CLPE se réunit-il en format plénier?\n-Nombre de répondants par réponse\nDe 0 à 10 fois par an",
        )

    plot_score_distribution(
        ax_2,
        data['freq2_5'],
        n_range=11,
        x_text = "",
        font_size=18,
        label_pad=2,
        title="Combien de comités techniques sont organisés par an ?\n-Nombre de répondants par réponse\nDe 0 à 10 fois par an",
        )


        #Partie 3
    question_multi_3 = ['Method_5','Method_im_5', 'amont_5', 'collabo_5', 'CR_5','obj_5', 'method_5']
    y_ytick_multi_3= [
        "La méthodologie de travail mise\nen place au sein du CLPE \npermet-elle de modifier la coopération ?",
        "La méthodologie de travail mise\nen place au sein du CLPE\nfavorise-elle la coopération\nau service de l'impact ?",
        "Des ordres du jour des CLPE\nsont-ils préparés en amont ?",
        "Les ordres du jour sont-ils\npréparés en collaboration ?",
        "Les comptes rendus des réunions\nsont-ils rédigés et diffusés ?",
        "Les orientations sont-elles\nobjectivées à partir de constats partagés\net d'indicateurs de résultats ?",
        "Dans le cadre des comités techniques,\nune méthode structurée et participative\nest-elle mise en œuvre ?",
    ]
    categories_multi_3 = ["Systématiquement", "Quelques fois", "Jamais", "Ne sait pas"]
    colors_multi_3 = ["#baffc9", "#FFE8B4", "#FAD9D6", "#e3e3ed"]
    plot_multi_stacked_bar(
        ax_3,
        data,
        question_multi_3,
        title="",
        font_size=18,
        pad=5,
        categories=categories_multi_3,
        colors=colors_multi_3,
        yticklabels=y_ytick_multi_3
    )

    #Partie 4
    question_multi_4 = ['actif_5']
    y_ytick_multi_4  = ["L'engagement actif de\ntous est-il encouragé ?"]
    categories_multi_4 = ["Oui, les membres participent à\ndes groupes de travail spécifiques", "Oui, les membres sont en responsabilité\nde groupes de travail spécifiques", "Non", "Ne sait pas"]
    colors_multi_4 = ["#C9D7F0", "#D7E9D2", "#FAD9D6", "#e3e3ed"]

    plot_multi_stacked_bar(
        ax_4,
        data,
        question_multi_4,
        title="",
        font_size=18,
        pad=5,
        categories=categories_multi_4,
        colors=colors_multi_4,
        yticklabels=y_ytick_multi_4
    )




    #Partie 5
    question_multi_5 = ['contri_5']
    y_ytick_multi_5 = ["Les contributions de chacun et\nles actions menées sont-elles\ncommuniquées et valorisées ?"]
    categories_multi_5 = ["Oui systématiquement", "Oui régulièrement", "Parfois", "Jamais", "Ne sait pas"]
    colors_multi_5 = ["#baffc9","#D7E9D2", "#FFE8B4","#FAD9D6", "#e3e3ed"]

    plot_multi_stacked_bar(
        ax_5,
        data,
        question_multi_5,
        title="",
        font_size=18,
        pad=5,
        categories=categories_multi_5,
        colors=colors_multi_5,
        yticklabels=y_ytick_multi_5
    )

    #Partie 6
    question_multi_6 = ['FA_5']
    y_ytick_multi_6 = [
        "Les fiches actions sont-elles\nsystématiquement saisies sur\nle tableau de bord du RPE"
    ]
    categories_multi_6 = ["Oui", "Non", "Ne sait pas"]
    colors_multi_6 = ["#baffc9", "#FAD9D6", "#e3e3ed"]
    plot_multi_stacked_bar(
        ax_6,
        data,
        question_multi_6,
        title="",
        font_size=18,
        pad=5,
        categories=categories_multi_6,
        colors=colors_multi_6,
        yticklabels=y_ytick_multi_6
    )

    #Partie 7

    fixed_order = [
        "Ne sait pas",
        "Pas d’organisation définie",
        "Les membres à tour de rôle",
        "DDETS",
        "France Travail",
        "Les porteurs de l'action",
    ]

    color_palette = [
        "#e3e3ed", '#B5EAD7', '#B5D8CC', '#FFDE8C', '#89d2f0',
        '#D9C7B8', '#e6aaba', '#E8C3E0'
    ]


    plot_side_graph(
        ax=ax_7,
        data=data,
        font_size=18,
        column_presented='Qui_5',
        color_palette=color_palette,
        fixed_order=fixed_order,
        title='Qui saisit les fiches actions')



    fig.tight_layout(pad=2.0)
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
