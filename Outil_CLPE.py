import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os
import sys

class ExcelImportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Outil de synthèse des résultats d'autodiagnostic des CLPE")
        self.root.geometry("700x600")

        # Palette
        self.colors = {
            "primary": "#DBE3FF",    # Bleu claire
            "secondary": "#F0E3FA",  # Violet
            "accent1": "#FCE5F2",    # Rose
            "accent2": "#FAD9D6",    # Corail
            "accent3": "#FFF0C7",    # Jaune
            "text": "#2C3E50",       # Bleu gris
            "button": "#5C6BC0",     # Couleur boutton
            "button_text": "white"   # Text du bouton
        }

        # Configurer la racine
        self.root.configure(bg=self.colors["primary"])

        self.excel_file_path = None

        self.create_widgets()



        #TOUT CE QUI EST FORME
    def create_widgets(self):
        # Main avec pad
        main_container = tk.Frame(self.root, bg=self.colors["primary"], padx=20, pady=20)
        main_container.pack(fill=tk.BOTH, expand=True)

        # Titre
        title_label = tk.Label(main_container,
                              text="Outil de synthèse des résultats d'autodiagnostic des CLPE",
                              font=("Arial", 17, "bold"),
                              fg=self.colors["text"],
                              bg=self.colors["primary"])
        title_label.pack(pady=(0, 20))

        # intro
        explanation_frame = tk.Frame(main_container, bg=self.colors["secondary"], padx=15, pady=15, relief=tk.RAISED, bd=1)
        explanation_frame.pack(fill=tk.X, pady=(0, 20))

        # Text explicatif
        explanation_text = """Cet outil vous permet d'obtenir un/des rapport(s) d'analyse automatique des résultats de l'autodiagnostic renseignés sur la plateform EUSurvey.

Procédure :
1. Importez le fichier Excel contenant les réponses au formulaire à partir d'EUSurvey
2. Cliquez sur 'Lancer l'analyse' pour générer le/les rapport(s)
3. Retrouvez vos rapports PDF dans un dossier "Résultats" avec horodatage
Les rapports incluent une analyse détaillée par thématique et des recommandations hierarchisées dans une démarche d'amélioration continue."""

        explanation_label = tk.Label(explanation_frame,
                                    text=explanation_text,
                                    font=("Arial", 10),
                                    justify=tk.LEFT,
                                    fg=self.colors["text"],
                                    bg=self.colors["secondary"],
                                    wraplength=600)
        explanation_label.pack()

        # chemin des fichier
        self.file_path_label = tk.Label(main_container,
                                       text="Aucun fichier sélectionné",
                                       font=("Arial", 9),
                                       fg=self.colors["text"],
                                       bg=self.colors["primary"],
                                       wraplength=500)
        self.file_path_label.pack(pady=(0, 15))

        button_frame = tk.Frame(main_container, bg=self.colors["primary"], height=50)
        button_frame.pack(fill=tk.X, pady=(0, 15))

        # Import
        import_btn = tk.Button(button_frame,
                      text="Importer le fichier Excel",
                      command=self.import_excel,
                      bg=self.colors["button"],
                      fg=self.colors["button_text"],
                      font=("Arial", 11, "bold"),
                      padx=15,
                      pady=8,
                      relief=tk.RAISED,
                      bd=2)
        import_btn.place(relx=0.3, rely=0.5, anchor='center')

        # Lancer l'analyse
        self.run_btn = tk.Button(button_frame,
                                text="Lancer l'analyse",
                                command=self.run_analysis,
                                state=tk.DISABLED,
                                bg=self.colors["button"],
                                fg=self.colors["button_text"],
                                font=("Arial", 11, "bold"),
                                padx=15,
                                pady=8,
                                relief=tk.RAISED,
                                bd=2)
        self.run_btn.place(relx=0.7, rely=0.5, anchor='center')
        # Progression
        progress_frame = tk.Frame(main_container, bg=self.colors["primary"])
        progress_frame.pack(fill=tk.X, pady=(0, 15))

        #bar de progression
        self.progress = ttk.Progressbar(progress_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(0, 10))

        # Label de status
        self.status_label = tk.Label(main_container,
                                    text=" ",
                                    font=("Arial", 10),
                                    fg=self.colors["text"],
                                    bg=self.colors["primary"],  # Match main background
                                    wraplength=500,
                                    padx=10,
                                    pady=5)
        self.status_label.pack(fill=tk.X, pady=(0, 15))
    def import_excel(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionner le fichier Excel",
            filetypes=[("Fichiers Excel", "*.xlsx"), ("Tous les fichiers", "*.*")]
        )

        if file_path:
            self.excel_file_path = file_path
            self.file_path_label.config(text=f"Fichier sélectionné: {os.path.basename(file_path)}")

            try:
                # Essayer de lire le fichier pour s'assurer qu'il est valide
                import pandas as pd
                test_df = pd.read_excel(file_path, skiprows=3, nrows=5)
                self.run_btn.config(state=tk.NORMAL)
                self.status_label.config(text="Fichier chargé avec succès. Cliquez sur 'Lancer l'analyse' pour continuer.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de lire le fichier Excel: {str(e)}")
                self.status_label.config(text="Erreur lors du chargement du fichier.")


    #Analyse en cours
    def run_analysis(self):
        if not self.excel_file_path:
            messagebox.showwarning("Attention", "Veuillez d'abord sélectionner un fichier Excel.")
            return

        self.run_btn.config(state=tk.DISABLED)
        self.progress.start(10)
        self.status_label.config(text="Traitement en cours... Cette opération peut prendre quelques minutes.")

        thread = threading.Thread(target=self.process_data)
        thread.daemon = True
        thread.start()

    def process_data(self):
        try:
            # Traitement excel
            from report_generator import process_excel_file
            success = process_excel_file(self.excel_file_path)
            # UI mis à jour en fonction du chemin
            if success:
                self.root.after(0, self.on_processing_complete)
            else:
                self.root.after(0, lambda: self.on_processing_error("Échec du traitement du fichier Excel."))

        except Exception as e:
            error_message = str(e)
            self.root.after(0, lambda: self.on_processing_error(error_message))

    def on_processing_complete(self):
        self.progress.stop()
        self.run_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Analyse terminée avec succès! Les rapports ont été générés.")
        messagebox.showinfo("Succès", "Analyse terminée avec succès! Les rapports ont été générés.")

    def on_processing_error(self, error_msg):
        self.progress.stop()
        self.run_btn.config(state=tk.NORMAL)
        self.status_label.config(text=f"Erreur: {error_msg}")
        messagebox.showerror("Erreur", f"Une erreur s'est produite lors du traitement:\n{error_msg}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelImportApp(root)
    root.mainloop()
