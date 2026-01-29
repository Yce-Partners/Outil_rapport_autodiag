import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc



from visuals.graphiques import plot_multi_stacked_bar
from visuals.graphiques import plot_side_graph
def section_4(data, output_path, file_name):

    fig = plt.figure(figsize=(8, 15))
    gs = fig.add_gridspec(3, 1, height_ratios=[1, 1, 5], hspace=0.1)


    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])

    question_1 = ['pres_4']
    categories_1 = ["Présenté et compris", "Présenté mais non compris", "Non présenté", "Ne sait pas"]
    colors_1 = ["#F0E3FA", "#FFE8B4","#FAD9D6", "#e3e3ed"]
    y_ytick_1=["Le rôle d'appui de France\nTravail a-t-il été :"]
    plot_multi_stacked_bar(
        ax_1,
        data,
        question_1,
        title="",
        font_size=20,
        pad=10,
        categories=categories_1,
        colors=colors_1,
        yticklabels=y_ytick_1
    )

    question_2 = ['RPE_4']
    categories_2 = ["Oui", "Parfois", "Non", "Ne sait pas"]
    colors_2 = ["#baffc9", "#FFE8B4","#FAD9D6", "#e3e3ed"]
    y_ytick_2=["Les membres du CLPE utilisent-ils\nle tableau de bord du RPE"]
    plot_multi_stacked_bar(
        ax_2,
        data,
        question_2,
        title="",
        font_size=20,
        pad=10,
        categories=categories_2,
        colors=colors_2,
        yticklabels=y_ytick_2
    )



    fixed_order = [
        "Ne sait pas",
        "Autres outils spécifiques au territoire",
        "Dataemploi",
        "Mon portail pro",
        "Mes évènements Emploi (MEE)",
        "La plateforme de l'inclusion",
        "L'immersion facilitée",
        "Académie France Travail",
        "DORA",
    ]

    color_palette = [
        "#e3e3ed", '#d99ef0', '#F5A39E',
        '#B5EAD7', '#B5D8CC', '#FFDE8C', '#89d2f0',
        '#D9C7B8', '#e6aaba', '#E8C3E0'
    ]


    plot_side_graph(
        ax=ax_3,
        data=data,
        font_size=20,
        column_presented='Outils_4',
        column_used='Outils2_4',
        color_palette=color_palette,
        fixed_order=fixed_order,
        title='Autres outils présentés et utilisés')


    fig.tight_layout()
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
