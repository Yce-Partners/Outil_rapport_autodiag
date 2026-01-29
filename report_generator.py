import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt


import numpy as np
from matplotlib.ticker import MaxNLocator
from datetime import datetime
import matplotlib.font_manager as fm
from pathlib import Path
import tempfile
import shutil
from matplotlib.colors import LinearSegmentedColormap
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.colors import HexColor, Color
from reportlab.graphics.shapes import Drawing, Line
from PIL import Image
import gc
import os
import sys


# ---importer les fonction---
from question_map import question_map
from visuals.Section_1 import section_1
from visuals.Section_2 import section_2
from visuals.Section_3 import section_3
from visuals.Section_4 import section_4
from visuals.Section_5 import section_5
from visuals.Section_6 import section_6
from visuals.Section_7 import section_7
from visuals.Section_8 import section_8
from visuals.Section_9 import section_9

from Notation_map import section_schemes, section_max_scores, calculate_section_score
from Notation_map import SECTION_NOTES



def process_excel_file(excel_file_path):
    try:

        df = pd.read_excel(excel_file_path, skiprows=3)
        df["A quel CLPE êtes-vous rattaché ?"] = df.filter(like="A quel CLPE êtes-vous rattaché ?").bfill(axis=1).iloc[:, 0]
        df.rename(columns=question_map, inplace=True)

        if getattr(sys, 'frozen', False):
            # en compiled executable
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        logo_path = os.path.join(base_path, "Logo.png")
        logo_path_FT = os.path.join(base_path, "Logo_FT.png")

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        output_folder_path = Path(f"Résultats_{timestamp}")
        output_folder_path.mkdir(parents=True, exist_ok=True)


        ##traitements des variables
        df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
        df["fluidite_1"] = df["fluidite_1"].str.replace(",", "", regex=False )
        df['cb_2'] = df['cb_2'].replace({'10 et plus': 10, 'Ne sait pas': -1})
        df['cb_2'] = df['cb_2'].astype(str)
        df["diag_2"] = df["diag_2"].str.replace(
            r"\bAucune des réponses précédentes\b",
            "Autres",
            regex=True ,
        )
        df["FDR_2"] = df["FDR_2"].str.replace("’", "'", regex=False )
        df["FDR_2"] = df["FDR_2"].str.replace(
            r"\bAucune des réponses précédentes\b",
            "Autres",
            regex=True ,
        )
        df["prev_diag_2"] = df["prev_diag_2"].str.replace(",", "", regex=False )
        df["consult_3"] = df["consult_3"].str.replace(",", "", regex=False )
        df["consult_3"] = df["consult_3"].str.replace(
            r"\bOui auprès des demandeurs d’emplois ou de leurs représentants\b",
            "Oui auprès des demandeurs\nd’emplois ou de leurs représentants",
            regex=True
        )
        df["consult_3"] = df["consult_3"].str.replace(
            r"\bOui auprès des employeurs et des demandeurs d’emplois ou de leurs représentants\b",
            "Oui auprès des employeurs et des\ndemandeurs d’emplois ou\nde leurs représentants",
            regex=True
        )
        df["Outils_4"] = df["Outils_4"].str.replace(
            r"\bDORA, outil d’aide à la prescription de services d’insertion\b",
            "DORA",
            regex=True
        )
        df["Outils2_4"] = df["Outils2_4"].str.replace(
            r"\bDORA, outil d’aide à la prescription de services d’insertion\b",
            "DORA",
            regex=True
        )
        df["actif_5"] = df["actif_5"].str.replace(
            r"\bOui, les membres participent à des groupes de travail spécifiques\b",
            "Oui, les membres participent à\ndes groupes de travail spécifiques",
            regex=True
        )
        df["actif_5"] = df["actif_5"].str.replace(
            r"\bOui, les membres sont en responsabilité de groupes de travail spécifiques\b",
            "Oui, les membres sont en responsabilité\nde groupes de travail spécifiques",
            regex=True
        )
        df["Qui_5"] = df["Qui_5"].astype(str).str.replace(r"Direction.*DDETS.*", "DDETS", regex=True, case=False)
        df['freq_5'] = df['freq_5'].replace({'Ne sait pas': -1} )
        df['freq_5'] =df['freq_5'] .apply(str)
        df['freq2_5'] = df['freq2_5'].replace({'Ne sait pas': -1} )
        df['freq2_5'] =df['freq2_5'] .apply(str)
        df["eval_6"] = df["eval_6"].apply(lambda x: str(x).replace(",", "") )
        df["analyse_6"] = df["analyse_6"].apply(lambda x: str(x).replace(",", "") )
        df["ind_6"] = df["ind_6"].apply(lambda x: str(x).replace(",", "") )
        df["appr_6"] = df["appr_6"].apply(lambda x: str(x).replace(",", "") )


        #Génération des fichiers
        def generate_pdf_report(df_subset, region_name=None, department_name=None, clpe_name=None):
            print(f"Le code traite le PDF : {clpe_name}")
            clpe_name=clpe_name.replace("/", "_")
            clpe_name=clpe_name.replace("?", "_")
            scope = clpe_name

            output_pdf_path = output_folder_path / f"Rapport_{scope}.pdf"

            with tempfile.TemporaryDirectory() as temp_dir:
                image_folder = Path(temp_dir)
                #Création des visuels
                file_names = {
                    'sect_1': "Thematique_1.png",
                    'sect_2': "Thematique_2.png",
                    'sect_3': "Thematique_3.png",
                    'sect_4': "Thematique_4.png",
                    'sect_5': "Thematique_5.png",
                    'sect_6': "Thematique_6.png",
                    'sect_7': "Thematique_7.png",
                    'sect_8': "Thematique_8.png",
                    'sect_9': "Thematique_9.png"
                    }
                section_1(df_subset, image_folder, file_names['sect_1'])
                section_2(df_subset, image_folder, file_names['sect_2'])
                section_3(df_subset, image_folder, file_names['sect_3'])
                section_4(df_subset, image_folder, file_names['sect_4'])
                section_5(df_subset, image_folder, file_names['sect_5'])
                section_6(df_subset, image_folder, file_names['sect_6'])
                section_7(df_subset, image_folder, file_names['sect_7'])
                section_8(df_subset, image_folder, file_names['sect_8'])
                section_9(df_subset, image_folder, file_names['sect_9'])


                #création du pdf
                name_file=f"Rapport_{scope}.pdf"
                c = canvas.Canvas(str(output_pdf_path))

                titre = f"Réponses {scope}"

                c.setFont("Helvetica-Bold", 15)
                c.drawString(20, 810, titre)


                def draw_image_preserving_ratio(canvas, image_path, x, y, target_width):
                    with Image.open(image_path) as img:
                        orig_width, orig_height = img.size
                        aspect_ratio = orig_height / orig_width
                        target_height = target_width * aspect_ratio
                        canvas.drawImage(str(image_path), x=x, y=y, width=target_width, height=target_height, preserveAspectRatio=True, mask='auto')

                # pour rajouter du text
                styles = getSampleStyleSheet()
                style = styles["Normal"]
                style.fontName = "Times-Roman"
                style.fontSize = 11
                style.leading = 12
                style.leftIndent = 20
                style.rightIndent = 20
                style.firstLineIndent = 0
                style.alignment = 0

                # premier paragraphe
                first_para_text = f"Vous trouverez dans ce document la synthèse des réponses des membres du CLPE ''{scope}''."

                # Second
                second_para_text = """
                    Loin d'être un simple bilan, cette synthèse constitue une opportunité précieuse
                    d'évaluer collectivement la maturité de notre coopération. Les indices de collaboration
                    qui émergent de cette évaluation nous offriront une vision claire des leviers sur
                    lesquels agir pour progresser ensemble. Ce processus itératif nous permettra d'ajuster
                    nos approches, d'affiner nos méthodes et de construire une dynamique de partenariat
                    toujours plus performante.
                """
                c.setFont("Times-Bold", 10)
                c.setFillColor("#000000")



                # Mettre ces paragraphes sur le pdf
                first_para = Paragraph(first_para_text, style)
                second_para = Paragraph(second_para_text, style)

                first_para.wrapOn(c, 530, 800)
                first_para.drawOn(c, 15, 780)

                second_para.wrapOn(c, 530, 800)
                second_para.drawOn(c, 15, 720)



                c.drawString(35, 700, f"Nombre de répondants au questionnaire: {len(df_subset)}")
                c.drawString(35,690, f"Période de réponse au questionnaire : du {df['date'].min().strftime('%d/%m/%Y')} au {df['date'].max().strftime('%d/%m/%Y')}")
                c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                page_number_text = f"Page {c.getPageNumber()}"
                c.setFont("Times-Roman", 10)
                c.drawCentredString(297, 20, page_number_text)



                c.setStrokeColor("#5C0F38")
                c.setLineWidth(3)
                c.setFont("Times-Roman", 12)
                c.setFillColor("#5C0F38")
                c.drawString(30, 670, "Thématique 1: Installation du CLPE")
                c.line(10, 665, 575, 665)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_1'], x=70, y=440, target_width=470)

                #Thématique 2
                c.setFont("Times-Roman", 12)
                c.drawString(30, 430, "Thématique 2: Les objectifs et missions du CLPE")
                c.line(10, 425, 575, 425)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_2'], x=50, y=40, target_width=470)

                c.showPage()

                c.setStrokeColor("#5C0F38")
                c.setLineWidth(3)
                c.setFont("Times-Roman", 12)
                c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                page_number_text = f"Page {c.getPageNumber()}"
                c.setFont("Times-Roman", 10)
                c.drawCentredString(297, 20, page_number_text)




                #Thématique 3
                c.setFont("Times-Roman", 12)
                c.drawString(30, 780, "Thématique 3: L’engagement des parties prenantes au sein du CLPE")
                c.line(10, 775, 575, 775)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_3'], x=40, y=450, target_width=530) #Obj et mission




                c.drawString(30, 420, "Thématique 4: Le rôle de France Travail dans le cadre de sa mission d’appui à la mise en œuvre du RPE")
                c.line(10, 415, 555, 415)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_4'], x=50, y=30, target_width=500) #création FT

                c.showPage()
                c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                page_number_text = f"Page {c.getPageNumber()}"
                c.setFont("Times-Roman", 10)
                c.drawCentredString(297, 20, page_number_text)
                c.setFont("Times-Roman", 12)     # Regular font
                c.setFillColor("#5C0F38")
                c.setLineWidth(3)



                c.drawString(30, 780, "Thématique 5: Les méthodes de travail du CLPE")
                c.line(10, 775, 575, 775)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_5'], x=50, y=30, target_width=510) #Orga méthodo


                c.showPage()
                c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                page_number_text = f"Page {c.getPageNumber()}"
                c.setFont("Times-Roman", 10)
                c.drawCentredString(297, 20, page_number_text)
                c.setFont("Times-Roman", 12)     # Regular font
                c.setFillColor("#5C0F38")
                c.setLineWidth(3)


                c.drawString(30, 780, "Thématique 6: Culture du résultat au sein du CLPE - évaluation et indicateurs de suivi et de résultats")
                c.line(10, 775, 575, 775)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_6'], x=55, y=430,target_width=500)



                c.drawString(30, 410, "Thématique 7: Communication des missions du CLPE et actions menées")
                c.line(10, 405, 575, 405)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_7'], x=20, y=30, target_width=430)

                c.showPage()
                c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                page_number_text = f"Page {c.getPageNumber()}"
                c.setFont("Times-Roman", 10)
                c.drawCentredString(297, 20, page_number_text)
                c.setFont("Times-Roman", 12)
                c.setFillColor("#5C0F38")
                c.setLineWidth(3)

                c.setFont("Times-Roman", 12)
                c.drawString(30, 780, "Thématique 8: Le recours aux outils collaboratifs pour la mise en œuvre de la collaboration au sein du CLPE")
                c.line(10, 775, 575, 775)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_8'], x=70, y=330, target_width=400)


                c.setFont("Times-Roman", 12)
                c.drawString(30, 280, "Thématique 9: L'adaptation et l'amélioration continue au sein du CLPE")
                c.line(10, 275, 575, 275)
                draw_image_preserving_ratio(c, image_folder/file_names['sect_9'], x=30, y=90, target_width=520) #Orga méthodo map


                c.showPage()


                #CONCLUSION
                c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                page_number_text = f"Page {c.getPageNumber()}"
                c.setFont("Times-Roman", 10)
                c.drawCentredString(297, 20, page_number_text)
                c.setFillColor("#5C0F38")
                c.setStrokeColor("#5C0F38")
                c.setLineWidth(3)

                c.setFont("Times-Roman", 12)
                c.drawString(30, 800, "Conclusion")
                c.line(10, 795, 575, 795)
                #Définition de la forme
                styles = {
                    'section_header': ParagraphStyle(
                        'SectionHeader',
                        fontName='Helvetica-Bold',
                        fontSize=10,
                        leading=12,
                        textColor=colors.HexColor('#5C0F38'),
                        spaceAfter=2*mm
                    ),
                    'recommendation': ParagraphStyle(
                        'Recommendation',
                        fontName='Helvetica',
                        fontSize=10,
                        leading=12,
                        spaceAfter=4*mm,
                        leftIndent=0,
                        alignment=TA_LEFT,
                        wordWrap='CJK'  #pour revenir à la ligne
                    )
                }

                SECTION_TITLES = {
                    "1": "Recommandations Thématique 1: Installation du CLPE ",
                    "2": "Recommandations Thématique 2: Les objectifs et missions du CLPE",
                    "3": "Recommandations Thématique 3: L'engagement des parties prenantes au sein du CLPE",
                    "4": "Recommandations Thématique 4: Le rôle de France Travail dans le cadre de sa mission d'appui à la mise en œuvre du RPE",
                    "5": "Recommandations Thématique 5: Les méthodes de travail du CLPE",
                    "6": "Recommandations Thématique 6: Culture du résultat au sein du CLPE - évaluation et indicateurs de suivi et de résultats",
                    "7": "Recommandations Thématique 7: Communication des missions du CLPE et actions menées",
                    "8": "Recommandations Thématique 8: Recours aux outils collaboratifs au sein du CLPE",
                    "9": "Recommandations Thématique 9: L'adaptation et l'amélioration continue au sein du CLPE"
                }

                # Calcul des scores par thématiques
                section_scores = {f"Section_{i}": calculate_section_score(df_subset, f"Section_{i}", 'percentage')
                                 for i in range(1, 10)}

                # Faire en sorte que la thématique 6 compte 2 fois plus que les autres
                weighted_for_sorting = {
                    section: (score / 2) if section == "Section_6" else score
                    for section, score in section_scores.items()
                }

                # Trier du moins bon score en premier au meilleur
                all_sections_sorted = sorted(weighted_for_sorting.items(), key=lambda x: x[1])


                y_position = 780
                left_margin = 40
                bottom_margin = 50  #

                def add_header_footer(c):

                    c.drawImage(logo_path, x=550, y=800, width=30, height=34)
                    c.drawImage(logo_path_FT, x=480, y=800, width=60, height=27)
                    page_number_text = f"Page {c.getPageNumber()}"
                    c.setFont("Times-Roman", 10)
                    c.drawCentredString(297, 20, page_number_text)

                # Text d'intro avec recommandations
                intro_text = Paragraph(
                    "Les réponses agrégées de cet auto diagnostic ont permis d'identifier les points forts et les axes d'amélioration du fonctionnement de votre CLPE. Vous trouverez ci-dessous des recommandations d'amélioration. Les thématiques sont classées par ordre de priorité: de celle à améliorer en priorité jusqu'à celle qui est le point le plus fort de votre CLPE.",
                    styles['recommendation']
                )

                #Mettre le texte d'intro sur le pdf
                intro_w, intro_h = intro_text.wrap(540, 600)
                if y_position - intro_h < bottom_margin:
                    c.showPage()
                    add_header_footer(c)
                    y_position = 750

                intro_text.drawOn(c, left_margin, y_position - intro_h)
                y_position -= intro_h + 15  # Espace suite à l'intro

                # Mettre chaque recommandation de telle sorte qu'elles ne se superposent pas.
                for section, score in all_sections_sorted:
                    section_num = section.split('_')[1]
                    section_title = SECTION_TITLES.get(section_num, f"Thématique {section_num}")

                    # Créer le header et paragraphe
                    section_header = Paragraph(section_title, styles['section_header'])
                    recommendation = Paragraph(
                        SECTION_NOTES.get(section, "Aucune recommandation spécifique disponible."),
                        styles['recommendation']
                    )

                    # Calculer la hauteur nécessaire pour cette section
                    header_w, header_h = section_header.wrap(540, y_position)
                    rec_w, rec_h = recommendation.wrap(540, y_position - header_h - 10)  # prendre en compte le header + espace

                    total_section_height = header_h + rec_h + 15  # hauteur header + hauter content + espace

                    # vérifier que tout rentre dans la page
                    if y_position - total_section_height < bottom_margin:
                        # Sinon créer une nouvelle page
                        c.showPage()
                        add_header_footer(c)
                        y_position = 750


                        header_w, header_h = section_header.wrap(540, y_position)
                        rec_w, rec_h = recommendation.wrap(540, y_position - header_h - 10)


                    section_header.drawOn(c, left_margin, y_position - header_h)
                    y_position -= header_h + 5

                    # Mettre texte
                    recommendation.drawOn(c, left_margin, y_position - rec_h)
                    y_position -= rec_h + 10


                c.save()
                #Nettoyage de la mémoire
                plt.close('all')
                gc.collect()

        for clpe_name, clpe_df in df.groupby('clpe'):
            generate_pdf_report(
                clpe_df,
                clpe_name=clpe_name)
        return True
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return False
