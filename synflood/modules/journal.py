# le but est de compte le nbr de paaquet syn envoyer avec la mise en place dans un log et avec les information source, traget.from datetime import datetime
import os
from threading import Lock  # Importez le verrou


lock = Lock() # obligatoire sinon il n'y avais par exemple pour 10 ip en 2 processus, que 5 info qui etait copie, probleme du a la tentative ecriture en meme temp ans le fichier 

class Journal:
    def __init__(self):
        self.journal_folder = "./journal_evenement"
        self.attaque_folder = os.path.join(self.journal_folder, "attaque")
        self.recap_file = os.path.join(self.journal_folder, "recap_attaques.txt")
        self.create_folders()
        self.attaque_infos = []

    def create_folders(self):
        if not os.path.exists(self.journal_folder):
            os.makedirs(self.journal_folder)
            print(f"Dossier '{self.journal_folder}' créé avec succès.")
        else:
            print(f"Dossier '{self.journal_folder}' existe déjà.")

        if not os.path.exists(self.attaque_folder):
            os.makedirs(self.attaque_folder)
            print(f"Dossier '{self.attaque_folder}' créé avec succès.")
        else:
            print(f"Dossier '{self.attaque_folder}' existe déjà.")
            
        return os.path.exists(self.journal_folder) and os.path.exists(self.attaque_folder)

    def log_demande(self, cible, port, nbrpaquet, nbr_processus):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

        log_entry = f"Date/Heure : {timestamp}\n"
        log_entry += f"Cible : {cible}\n"
        log_entry += f"Port : {port}\n"
        log_entry += f"Nombre de paquets : {nbrpaquet}\n"
        log_entry += f"Nombre de processus : {nbr_processus}\n\n"

        with open(self.recap_file, 'a') as f:
            f.write(log_entry)

    def log_recap_attaque(self, cible, port, nbrpaquet, nbr_processus, messages):
        attaque_file = os.path.join(self.attaque_folder, f"attaque_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
        
        with lock:
            with open(attaque_file, 'a') as f:  
                demande_info = f"Adresse cible: {cible}\n"
                demande_info += f"Port: {port}\n"
                demande_info += f"Nombre de paquets: {nbrpaquet}\n"
                demande_info += f"Nombre de processus: {nbr_processus}\n\n"
                f.write(demande_info)
        
                for message in messages:
                    f.write(message + '\n')
