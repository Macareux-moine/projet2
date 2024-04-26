import socket

class ScanSynch:
    def __init__(self, hote):
        self.hote = hote

    # Creation d'une socket et tentative de connection au port donné
    def scan(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((self.hote, port))
                return port, True
        except (socket.error, socket.timeout, ConnectionRefusedError):
            return port, False