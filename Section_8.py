import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc



from visuals.graphiques import plot_multi_stacked_bar
from visuals.graphiques import plot_side_graph


def section_8(data, output_path, file_name):

    fig = plt.figure(figsize=(5, 12))
    gs = fig.add_gridspec(3, 1, height_ratios=[1, 8, 8], hspace=0.5)

    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])


    question_1 = ['outils_8']
    categories_1 = ["Oui", "Non", "Ne sait pas"]
    colors_1 = ["#baffc9", "#FAD9D6", "#e3e3ed"]
    y_ytick_1=["Des outils collaboratifs sont mis\nen place au sein du CLPE"]
    plot_multi_stacked_bar(
        ax_1,
        data,
        question_1,
        title="",
        font_size=14,
        pad=5,
        categories=categories_1,
        colors=colors_1,
        yticklabels=y_ytick_1
    )




    fixed_order_1 = [
        "Gestion de la relation client (CRM)",  "Tableaux blanc virtuels","Prise de notes collaboratives","Partage de documents",  "Gestion de projet",  "Visioconférence","Messagerie instantannée"
    ]
    fixed_order_2 = [
         "Ne sait pas","Autre", "Google Drive","Trello",  "Zoom", "Google Workspace","La Place", "Resana", "Teams",
    ]


    color_palette_1 = [
        '#d99ef0', '#F5A39E',
        '#B5EAD7', '#B5D8CC', '#FFDE8C', '#89d2f0',
        '#D9C7B8', '#e6aaba', '#E8C3E0'
    ]

    color_palette_2 = [
        '#e3e3ed', '#B5D8CC', '#FFDE8C', '#89d2f0',
        '#D9C7B8', '#e6aaba', '#E8C3E0'
    ]



    plot_side_graph(
        ax=ax_2,
        data=data,
        font_size=14,
        column_presented='utilisation_8',
        fixed_order=fixed_order_1,
        color_palette=color_palette_1,
        title="Utilisation des outils collaboratifs au sein du CLPE")

    plot_side_graph(
        ax=ax_3,
        data=data,
        font_size=14,
        column_presented='platform_8',
        fixed_order=fixed_order_2,
        color_palette=color_palette_2,
        title="Plateformes collaboratives les plus utilisées")

    fig.tight_layout()
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
