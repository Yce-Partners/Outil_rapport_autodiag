import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc




from visuals.graphiques import plot_multi_stacked_bar

def section_3(data, output_path, file_name):


    fig = plt.figure(figsize=(8,15))
    gs = fig.add_gridspec(3, 1,  hspace=0.3)

    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])

    question_1 = ['Impli_3']
    categories_1 = ["Toujours", "Souvent", "Régulièrement", "Parfois", "Non", "Ne sait pas"]
    colors_1 = ["#baffc9","#D7E9D2", "#FFE8B4", "#71abd7","#FAD9D6", "#e3e3ed"]
    y_yticklabels_1=["Est-ce que les acteurs\nnommés ou leurs\nreprésentants sont parties\nprenantes et impliquées\ndans les instances ?"]
    plot_multi_stacked_bar(
        ax_1,
        data,
        question_1,
        title="",
        font_size=26,
        pad=5,
        categories=categories_1,
        colors=colors_1,
        yticklabels=y_yticklabels_1
    )

    question_2 = ['Particip_3']
    categories_2 = ["Tous les élus sont présents", "Les élus sont présents à tour de rôle", "Les élus se font représenter", "L’organisation de la participation des élus n’est pas figée", "Ne sait pas"]
    colors_2 = ["#71abd7", "#b0a1ed", "#ebabc2", "#ebc9ab", "#e3e3ed"]
    y_yticklabels_2=["Comment s’organise\nla participation des\nélus au CLPE ?"]
    plot_multi_stacked_bar(
        ax_2,
        data,
        question_2,
        title="",
        font_size=26,
        pad=5,
        categories=categories_2,
        colors=colors_2,
        yticklabels=y_yticklabels_2
    )


    question_3 = ['consult_3']
    categories_3 = ["Oui auprès des employeurs ou de leurs représentants", "Oui auprès des demandeurs\nd’emplois ou de leurs représentants", "Oui auprès des employeurs et des\ndemandeurs d’emplois ou\nde leurs représentants", "Non pas pour le moment mais c'est envisagé", "Non et ce n'est pas prévu", "Ne sait pas"]
    colors_3 = ["#FFE8B4", "#D7E9D2", "#baffc9","#71abd7","#FAD9D6", "#e3e3ed"]
    y_yticklabels_3=["Des consultations\nont-elles été menées auprès\ndes usagers pour recueillir\ndes avis et besoins ?"]
    plot_multi_stacked_bar(
        ax_3,
        data,
        question_3,
        title="",
        font_size=26,
        pad=5,
        categories=categories_3,
        colors=colors_3,
        yticklabels=y_yticklabels_3
    )



    fig.tight_layout()
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
