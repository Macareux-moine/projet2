import socket
import threading

class ScanThread:
    def __init__(self, hote):
        self.hote = hote
        self.ports_ouvert = []

    def scan_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            resultat = s.connect_ex((self.hote, port))
            if resultat == 0:
                self.ports_ouvert.append(port)
            s.close()
        except Exception as ex:
            print("Erreur %s dans le scan_port" % ex)

    def scan_range(self, port_debut, port_fin):
        try:
            threads = []
            for port in range(port_debut, port_fin + 1):
                thread = threading.Thread(target=self.scan_port, args=(port,))
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join()
                
            return threads  # Retourner la liste des threads
        except Exception as ex:
            print("Erreur %s dans le scan_range" % ex)



    def port_ouvert(self):
        if self.ports_ouvert:
            print("Ports ouvert : ")
            for port in self.ports_ouvert:
                print(f"Le port {port} est ouvert ")
        else:
            print("Aucun port ouvert trouvé")
