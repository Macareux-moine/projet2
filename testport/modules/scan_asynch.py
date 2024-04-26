import asyncio

class ScanASync:
    def __init__(self, host):
        self.host = host

    async def scan(self, port):
        try:
            # Ouvre une connexion asynchrone au port donné
            lecture, ecriture = await asyncio.open_connection(self.host, port)
            ecriture.close()
            await ecriture.wait_closed()  # /!\ si c'est pas fermé ça crée des erreurs 
            return port, True 
        except (asyncio.TimeoutError, ConnectionRefusedError):
            return port, False
