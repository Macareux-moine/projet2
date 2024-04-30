import socket
import threading

class ScanThread:  # Définition d'une classe ScanThread pour effectuer des scans de ports
    def __init__(self, hote): 
        self.hote = hote  
        self.ports_ouvert = [] 

    def scan_port(self, port):  # Méthode pour scanner un port donné
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            s.settimeout(1)  
            resultat = s.connect_ex((self.hote, port))
            if resultat == 0:  # Si la connexion est réussie (port ouvert)
                self.ports_ouvert.append(port)  # Ajout du port à la liste des ports ouverts
            s.close()
        except Exception as ex:  # Gestion des exceptions
            print("Erreur %s dans le scan_port" % ex)

    def scan_range(self, port_debut, port_fin):  # Méthode pour scanner une plage de ports
        try:
            threads = []
            for port in range(port_debut, port_fin + 1):  # Boucle pour chaque port dans la plage spécifiée
                thread = threading.Thread(target=self.scan_port, args=(port,))  # Création d'un thread pour scanner le port actuel
                threads.append(thread)
                thread.start()
            
            for thread in threads:  # Boucle pour attendre que tous les threads se terminent
                thread.join()
                
            return threads
        except Exception as ex:  # Gestion des exceptions
            print("Erreur %s dans le scan_range" % ex)

    def port_ouvert(self):  # Méthode pour afficher les ports ouverts
        if self.ports_ouvert:  # Si des ports sont ouverts
            print("Ports ouverts : ")
            for port in self.ports_ouvert:  # Boucle pour chaque port ouvert
                print(f"Le port {port} est ouvert ")  # Affichage du port ouvert
        else:  # Si aucun port n'est ouvert
            print("Aucun port ouvert trouvé")  # Affichage d'un message indiquant qu'aucun port n'est ouvert
