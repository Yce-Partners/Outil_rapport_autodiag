import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
import gc


from visuals.graphiques import plot_multi_stacked_bar
from visuals.graphiques import plot_respondent_counts
from visuals.graphiques import plot_score_distribution


def section_2(data, output_path, file_name):


    
    fig = plt.figure(figsize=(9, 20))
    gs = fig.add_gridspec(6, 1, height_ratios=[1, 1, 1, 1,2,3], hspace=0.1)
    ax_1 = fig.add_subplot(gs[0])
    ax_2 = fig.add_subplot(gs[1])
    ax_3 = fig.add_subplot(gs[2])
    ax_4 = fig.add_subplot(gs[3])
    ax_5 = fig.add_subplot(gs[4])
    ax_6 = fig.add_subplot(gs[5])

    # Numéro 1: diagnostique territorial
    questions_1 = ['diag_2']
    categories_1 = ["Coconstruit","Formalisé", "Partagé", "Ne sait pas","Autres"]
    plot_respondent_counts(
        ax_1,
        data,
        questions_1,
        categories_1,
        font_size = 25,
        title="Un diagnostic territorial a-t-il été :"
    )

    # Numéro 2
    questions_2=['prev_diag_2']
    categories_2 = ["Oui plus d'une fois par an","Oui une fois par an","Non", "Ne sait pas"]
    colors_2 = ["#baffc9","#b5e3ea", "#ffd7d5",  "#e3e3ed"]
    y_yticklabels_2=["Est-il prévu d'actualiser\nce diagnostic ?"]

    plot_multi_stacked_bar(
        ax_2,
        data,
        questions_2,
        title="",
        font_size=25,
        pad=10,
        categories=categories_2,
        colors=colors_2,
        yticklabels=y_yticklabels_2
    )


    # Numéro 2
    questions_3=['Obj_2']
    categories_3 = ["Oui", "Non", "Ne sait pas"]
    colors_3= ["#baffc9", "#FAD9D6", "#e3e3ed"]
    y_yticklabels_3=["Connaissez vous les objectifs\nde la feuille de route fixés\npar le CLPE à court terme ?"]

    plot_multi_stacked_bar(
        ax_3,
        data,
        questions_3,
        title="",
        font_size=25,
        pad=10,
        categories=categories_3,
        colors=colors_3,
        yticklabels=y_yticklabels_3
    )





    # Question 4
    questions_4 = ['FDR_2']
    categories_4 = ["Coconstruite","Formalisée", "Partagée", "En cours d'élaboration", "Ne sait pas","Autres"]
    plot_respondent_counts(
        ax_4,
        data,
        questions_4,
        categories_4,
        font_size = 25,
        title="La feuille de route a été:"
    )

    # Questions 5 conf financeux
    questions_5=['finalite_2', 'Conf_fin_2',  'moyen_terme_2',]
    categories_5= ["Oui", "Non", "Ne sait pas"]
    colors_5= ["#baffc9", "#FAD9D6", "#e3e3ed"]
    y_yticklabels_5=["Connaissez-vous la finalité\nde la conférence des financeurs ?","La conférence des financeurs\na-t-elle été sollicitée ?",  "Avez-vous partagé une vision globale\nmoyen terme (ODS globale, maillage\ndes ODS…) ?"]
    plot_multi_stacked_bar(
        ax_5,
        data,
        questions_5,
        title="",
        font_size=25,
        pad=10,
        categories=categories_5,
        colors=colors_5,
        yticklabels=y_yticklabels_5
    )

    # Questions 6 fiche actions
    plot_score_distribution(
        ax_6,
        data['cb_2'],
        n_range=11,
        x_text = "",
        font_size= 25,
        label_pad=2,
        title="Nombre de fiches actions rédigées concrétisant\nles priorités communes à court terme",
        )



    # Adjust layout and save
    fig.tight_layout(pad=2.0)
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / file_name, dpi=300, bbox_inches='tight')
    plt.close(fig)
    gc.collect()
