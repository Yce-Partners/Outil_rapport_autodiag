import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc


from visuals.graphiques import plot_multi_stacked_bar

def section_9(data, output_path, file_name) :

    fig = plt.figure(figsize=(10, 8))
    gs = fig.add_gridspec(3, 1, hspace=0.2)
    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])


    question_1= ['proc_9']
    categories_1 = ["Systématiquement", "Parfois", "Jamais", "Ne sait pas"]
    colors_1 = ["#baffc9", "#FFE8B4", "#FAD9D6", "#e3e3ed"]
    y_ytick_1=["Des retours d'expériences sont-ils mis en\nplace pour identifier les points à améliorer ?"]
    plot_multi_stacked_bar(
        ax_1,
        data,
        question_1,
        title="",
        font_size=24,
        pad=10,
        categories=categories_1,
        colors=colors_1,
        yticklabels=y_ytick_1
    )
    question_2= ['form_9']
    categories_2 = ["Oui","Non, mais c'est prévu","Non", "Ne sait pas"]
    colors_2= ["#baffc9", "#FFE8B4", "#FAD9D6", "#e3e3ed"]
    y_ytick_2=["Des actions de montée en compétences pour les\nmembres des CLPE sont-elles proposées ?"]
    plot_multi_stacked_bar(
        ax_2,
        data,
        question_2,
        title="",
        font_size=24,
        pad=10,
        categories=categories_2,
        colors=colors_2,
        yticklabels=y_ytick_2
    )

    question_3= ['SPEL_9']
    categories_3 = ["Oui","Non", "Ne sait pas"]
    colors_3= ["#baffc9", "#FAD9D6", "#e3e3ed"]
    y_ytick_3=["Avez-vous l'impression d'avoir engagé une\ntransformation du SPEL en CLPE ?"]
    plot_multi_stacked_bar(
        ax_3,
        data,
        question_3,
        title="",
        font_size=24,
        pad=10,
        categories=categories_3,
        colors=colors_3,
        yticklabels=y_ytick_3
    )


    fig.tight_layout()
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
