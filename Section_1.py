import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc


from visuals.graphiques import plot_multi_stacked_bar
from visuals.graphiques import plot_score_distribution


def section_1(data, output_path, file_name):


    fig = plt.figure(figsize=(16,7))
    gs = fig.add_gridspec(2, 3, height_ratios=[2, 1], wspace=1.3, hspace=0.3)

    ax_1 = fig.add_subplot(gs[0, 0])
    ax_2 = fig.add_subplot(gs[1, 0:1])
    ax_right = fig.add_subplot(gs[0, 1:2])


    #premier graphique
    question_multi_1 = ['local_officials_1', 'internal_rules_1','instances_gov_1']
    y_ytick_multi_1 = [
        "Des élus locaux ont-ils\nété nommés dans la\nco-présidence ? ",
        "Existe-il un Règlement\nIntérieur précisant le\nfonctionnement du CLPE ? ",
        "Le CLPE est-il la seule\ninstance de gouvernance\ndes politiques de l’emploi\nsur le territoire ?",
    ]

    categories_multi_1 = ["Oui", "Non", "Ne sait pas"]
    colors_multi_1 = ["#baffc9", "#FAD9D6", "#e3e3ed"]

    #deuxième graphique
    plot_multi_stacked_bar(
        ax_1,
        data,
        question_multi_1,
        title="",
        font_size=16,
        pad=10,
        categories=categories_multi_1,
        colors=colors_multi_1,
        yticklabels=y_ytick_multi_1
    )

    question_multi_2 = ['fluidite_1']
    y_ytick_multi_2 = [
        "L’articulation entre les\ncomités locaux et les comités\ndépartementaux existe-elle ?",
    ]

    categories_multi_2 = ["Oui", "Oui mais elle n'est pas fluide","Non", "Ne sait pas"]
    colors_multi_2 = ["#baffc9", "#FFDE8C", "#FAD9D6","#e3e3ed"]
    plot_multi_stacked_bar(
        ax_2,
        data,
        question_multi_2,
        title="",
        font_size=16,
        pad=10,
        categories=categories_multi_2,
        colors=colors_multi_2,
        yticklabels=y_ytick_multi_2
    )


    #trosième graphique

    plot_score_distribution(
        ax_right,
        data['asc_1'],
        n_range=6,
        x_text = "Score de 0 (pas d’ascendance)\nà 5 (ascendance très fluide)",
        font_size= 16,
        label_pad=2,
        title="Comment qualifierez-vous l’ascendance entre le niveau\nlocal et le niveau départemental ?\nNombre de répondants par score",
        )



    fig.tight_layout(pad=2.0)
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
