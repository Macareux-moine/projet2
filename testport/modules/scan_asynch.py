import asyncio

class ScanASync:  # Définition d'une classe ScanASync pour effectuer des scans de ports asynchrones
    def __init__(self, host):
        self.host = host

    async def scan(self, port):  # Méthode asynchrone pour scanner un port donné
        try:
            lecture, ecriture = await asyncio.open_connection(self.host, port) # Ouvre une connexion asynchrone au port donné
            ecriture.close()  # Fermeture du canal d'écriture
            await ecriture.wait_closed()  # Attente de la fermeture complète de la connexion /!\ crée des errurs si ce n'est pas entierement fermé
            return port, True  # Si la connexion réussit, retourner le numéro de port et True
        except (asyncio.TimeoutError, ConnectionRefusedError):  # Gestion des exceptions pour les erreurs de connexion
            return port, False  # Si la connexion échoue, retourner le numéro de port et False
