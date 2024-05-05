from datetime import datetime  
import os  

class Journal:
    def __init__(self):
        # Définition des chemins des dossiers et fichiers du journal
        self.journal_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "journal_evenement"))  # Chemin absolu du dossier journal_evenement
        self.attaque_folder = os.path.join(self.journal_folder, "attaque")  # Chemin du dossier des attaques
        self.recap_file = os.path.join(self.journal_folder, "recap_attaques.txt")  # Chemin du fichier de récapitulation des attaques
        self.create_folders()  # Appel de la méthode pour créer les dossiers nécessaires
        self.attaque_infos = []  # Initialisation d'une liste pour stocker des informations sur les attaques

    def create_folders(self):
        # Méthode pour créer les dossiers s'ils n'existent pas déjà
        if not os.path.exists(self.journal_folder):
            os.makedirs(self.journal_folder)  # Création du dossier journal_evenement s'il n'existe pas
            print(f"Dossier '{self.journal_folder}' créé avec succès.")
        else:
            print(f"Dossier '{self.journal_folder}' existe déjà.")

        if not os.path.exists(self.attaque_folder):
            os.makedirs(self.attaque_folder)  # Création du dossier attaque s'il n'existe pas
            print(f"Dossier '{self.attaque_folder}' créé avec succès.")
        else:
            print(f"Dossier '{self.attaque_folder}' existe déjà.")
            
        return os.path.exists(self.journal_folder) and os.path.exists(self.attaque_folder)  # Vérification de l'existence des dossiers

    def log_demande(self, cible, port, nbrpaquet, nbr_processus):
        # Méthode pour enregistrer une demande dans le journal
        now = datetime.now()  # Récupération de la date et l'heure actuelles
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")  # Formatage de la date et l'heure

        log_entry = f"Date/Heure : {timestamp}\n"  # Création de l'entrée de journal avec la date et l'heure
        log_entry += f"Cible : {cible}\n"  # Ajout de l'adresse cible
        log_entry += f"Port : {port}\n"  # Ajout du port
        log_entry += f"Nombre de paquets : {nbrpaquet}\n"  # Ajout du nombre de paquets
        log_entry += f"Nombre de processus : {nbr_processus}\n\n"  # Ajout du nombre de processus utilisés

        with open(self.recap_file, 'a') as f:
            f.write(log_entry)  # Écriture de l'entrée de journal dans le fichier de récapitulation

    def log_recap_attaque(self, cible, port, nbrpaquet, nbr_processus, messages):
        # Méthode pour enregistrer un récapitulatif d'attaque dans le journal
        attaque_file = os.path.join(self.attaque_folder, f"attaque_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")  # Chemin du fichier d'attaque

        with open(attaque_file, 'a') as f:  
            demande_info = f"Adresse cible: {cible}\n"  # Ajout de l'adresse cible
            demande_info += f"Port: {port}\n"  # Ajout du port
            demande_info += f"Nombre de paquets: {nbrpaquet}\n"  # Ajout du nombre de paquets
            demande_info += f"Nombre de processus: {nbr_processus}\n\n"  # Ajout du nombre de processus utilisés
            f.write(demande_info)  # Écriture des informations de la demande dans le fichier d'attaque
        
            for message in messages:
                f.write(message + '\n')  # Écriture des messages associés à l'attaque
