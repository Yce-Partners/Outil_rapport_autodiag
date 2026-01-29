import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc

from visuals.graphiques import plot_multi_stacked_bar

def section_6(data, output_path, file_name):



    fig = plt.figure(figsize=(5, 14))
    gs = fig.add_gridspec(5, 1, height_ratios=[1,1, 1,2,1], hspace=0.5)
    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])
    ax_4 = fig.add_subplot(gs[3])
    ax_5 = fig.add_subplot(gs[4])




    question_1 = ['appr_6']
    categories_1 = ["Oui et le sujet a été abordé en profondeur", "Oui et le sujet a été abordé partiellement", "Non pas encore", "Non et ce n’est pas prévu pour le moment", "Ne sait pas"]
    colors_1 = ["#baffc9","#b5e3ea","#FFE8B4", "#FAD9D6", "#e3e3ed"]
    y_ytick_1=["L’appropriation des indicateurs\ndu tableau de bord a-t-elle fait\nl’objet de séance(s) collaborative(s) ?"]
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

    question_2 = ['pour_vous_6']
    categories_2 = ["Oui", "Non", "Ne sait pas"]
    colors_2 = ["#baffc9", "#FAD9D6", "#e3e3ed"]
    y_ytick_2=["Pour vous, la différence entre les\nrésultats des actions et l’impact\ndes actions est-elle claire ?"]
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

    question_3 = ['ind_6']
    categories_3 = ["Oui pour toutes les actions", "Oui pour quelques-unes des actions","Non",  "Ne sait pas"]
    colors_3 = ["#baffc9","#FFE8B4", "#FAD9D6", "#e3e3ed"]
    y_ytick_3=["Des indicateurs de performance\nspécifiques à chaque action menée ont-ils\nété établis pour mesurer les résultats ?"]
    plot_multi_stacked_bar(
        ax_3,
        data,
        question_3,
        title="",
        font_size=20,
        pad=10,
        categories=categories_3,
        colors=colors_3,
        yticklabels=y_ytick_3
    )



    question_4 = ['analyse_6', 'eval_6',]
    categories_4 = ["Oui plusieurs fois par an", "Oui une fois par an", "Non", "Ne sait pas"]
    colors_4 = ["#baffc9","#FFE8B4", "#FAD9D6","#e3e3ed"]
    y_ytick_4=[ "Menez-vous une analyse des effets\nou résultats des actions mises en œuvre ?", "Évaluez-vous l’impact des\nactions mises en œuvre ?",]
    plot_multi_stacked_bar(
        ax_4,
        data,
        question_4,
        title="",
        font_size=20,
        pad=10,
        categories=categories_4,
        colors=colors_4,
        yticklabels=y_ytick_4
    )

    question_5 = ['result_6']
    categories_5 = ["Systématiquement", "Parfois", "Jamais", "Ne sait pas"]
    colors_5 = ["#baffc9","#FFE8B4", "#FAD9D6", "#e3e3ed"]
    y_ytick_5=["Réinterrogez-vous la mobilisation\ndes moyens au regard des\nrésultats obtenus ?"]
    plot_multi_stacked_bar(
        ax_5,
        data,
        question_5,
        title="",
        font_size=20,
        pad=10,
        categories=categories_5,
        colors=colors_5,
        yticklabels=y_ytick_5
    )


    fig.tight_layout()
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
