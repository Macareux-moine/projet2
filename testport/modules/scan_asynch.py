import asyncio

class ScanASync:
    def __init__(self, host):
        self.host = host

    async def scan(self, port):
        try:
            # Ouvre une connexion asynchrone au port donné
            lecture, ecriture = await asyncio.open_connection(self.host, port)
            ecriture.close()  # Ferme la connexion
            return port, True  # Si la connexion réussit, le port est ouvert
        except (asyncio.TimeoutError, ConnectionRefusedError):
            return port, False  # Si la connexion échoue, le port est fermé
