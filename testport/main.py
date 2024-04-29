import asyncio
from modules.scan_synch import ScanSynch
from modules.scan_asynch import ScanASync
from modules.scan_thread import ScanThread

async def main():
    hote = input('Hote (localhost) : ')
    mode_scan = input('Mode de scan (synch/asynch/Thread) : ').lower()
    start_port = int(input('Port de départ : '))
    end_port = int(input('Port de fin : '))
    
    # Crée une liste de ports à scanner
    ports = range(start_port, end_port + 1)
    
    try:
        
        # Execution du scan en mode synchrone
        if mode_scan == 'synch':
            scann = ScanSynch(hote)
            port_ouvert = []
            # Ajout des ports dans la liste
            for port in ports:
                resultat = scann.scan(port)
                print('test du port %s' % port)
                # Verifier si le port est ouvert pour l'ajouter au tableau
                if resultat is not None and resultat[1]:
                    port_ouvert.append(resultat[0])

            print('Scan terminé')
            for port in port_ouvert:
                print('Port ouvert :', port)
        
        # Execution du scan en mode asynchrone
        elif mode_scan == 'asynch':
            scann = ScanASync(hote)

            # Liste pour stocker les futures de chaque scan asynchrone
            port_ouvert = []

            # Lancer les scans asynchrones pour chaque port
            for port in ports:
                print('test du port %s' % port)
                port_ouvert.append(scann.scan(port))

            # Attendre que tous les scans asynchrones soient terminés
            resultat = await asyncio.gather(*port_ouvert)

            # Afficher les résultats dans l'ordre
            print('Scan terminé')
            for port, status in resultat:
                if status:
                    print('Port ouvert :', port)
                else:
                    print('Port fermé :', port)

                
        elif mode_scan == 'thread':
            scann = ScanThread(hote)
            port_ouvert = []
            for port in ports:
                resultat = scann.scan(port)
                print('test du port %s' % port)
                # Verifier si le port est ouvert pour l'ajouter au tableau
                if resultat is not None and resultat[1]:
                    port_ouvert.append(resultat[0])        
            
        else:
            print('Mode de scan invalide.')
    except Exception as ex:
        print('Erreur %s dans la focntion main()' % ex)

if __name__ == '__main__':
    asyncio.run(main())
