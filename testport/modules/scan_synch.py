import socket

class ScanSynch:  # Définition d'une classe ScanSynch pour effectuer des scans de ports synchrones
    def __init__(self, hote):
        self.hote = hote 

    # Méthode pour scanner un port donné
    def scan(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Création d'une socket TCP
                s.settimeout(1)
                s.connect((self.hote, port))  # Tentative de connexion au port spécifié
                return port, True  # Si la connexion est réussie, retourner le port et True
        except (socket.error, socket.timeout, ConnectionRefusedError):  # Gestion des exceptions pour les erreurs de connexion
            return port, False  # Si la connexion échoue, retourner le port et False
