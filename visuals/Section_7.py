import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc


from visuals.graphiques import plot_multi_stacked_bar
from visuals.graphiques import plot_side_graph

def section_7(data, output_path, file_name):

    fig = plt.figure(figsize=(7, 15))
    gs = fig.add_gridspec(2, 1, height_ratios=[1,5], hspace=0.3)

    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    plt.subplots_adjust(right=0.75)  # Espace pour légende


    question_1 = ['com_7']
    categories_1 = ["Oui", "Non", "Ne sait pas"]
    colors_1 = ["#baffc9", "#FAD9D6", "#e3e3ed"]
    y_ytick_1=["Des actions de communication\nsur les missions et action des CLPE sont-elles\nréalisées par les membres du CLPE ?"]
    plot_multi_stacked_bar(
        ax_1,
        data,
        question_1,
        title="",
        font_size=22,
        pad=5,
        categories=categories_1,
        colors=colors_1,
        yticklabels=y_ytick_1
    )

    fixed_order = [
        "Ne sait pas",
        "Les actions ne sont pas communiquées",
        "Auprès des agents internes aux membres du CLPE",
        "Autres influenceurs locaux",
        "Presses",
        "Usagers entreprises / Employeurs",
        "Usagers demandeurs d’emploi",
    ]
    color_palette = [
        '#e3e3ed', '#B5D8CC', '#FFDE8C', '#89d2f0',
        '#D9C7B8', '#e6aaba', '#E8C3E0'
    ]

    plot_side_graph(
        ax=ax_2,
        data=data,
        font_size=22,
        column_presented='result_7',
        fixed_order=fixed_order,
        color_palette=color_palette,
        title="Les résultats des actions menées par les CLPE sont communiqués aux...")



    fig.tight_layout()
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
