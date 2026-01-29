# Outil_rapport_autodiag
Cette outil permet de créer des rapports d'auto_diagnostic à partir des réponses à un questionnaire sous format Excel (pour le cas exemple à partir d'un questionnaire EU survey). L'exemple dans ce projet est des rapports d'auto-diagnostic pour les CLPE, mais le code peut être réadapté pour créer des rapports pour d'autres types de questionnaire.

Ici, les CLPE sont les entités qui répondent à notre questionnaire.

Le fichier Outil_CLPE correspond à l'interface Tkinter. Il est possible de transformer ce fichier en exécutable pour rendre l'utilisation plus simple.

Outil_CLPE lance le fichier report_generator une fois que le bon format de fichier excel est importé. Ici, report_generator crée un PDF de synthèse par CLPE. Cette partie peut être modifié pour un prochain questionnaire.

Pour chaque loop par CLPE, report_generator appelle les fichiers visual_N dans visuals pour créer les graphiques matplotlib qui apparaissent dans le PDF. Visuals a les paramétrages qui sont ensuite intégrés dans graphiques.py. Pour chaque PDF, un score est calculé à partir des réponses fournies. Question_map associe un score à chaque réponse. Un score en pourcentage est calculé pour chaque thématique, est report_generator affiche les thématiques avec le moins bon score en premier et celles avec les meilleures scores en dernier.


Ainsi, ce code peut inspirer des futurs codeurs pour automatiser la génération de rapports de synthèse, en fonction de leurs besoins. Il faut notamment adapter les graphiques, le fichier question_map qui associe chaque question à une variable, notation_map, etc.


