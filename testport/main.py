import asyncio
from modules.scan_synch import ScanSynch
from modules.scan_asynch import ScanASync

async def main():
    hote = input('Hote (localhost) : ')
    mode_scan = input('Mode de scan (synch/asynch) : ').lower()
    port_debut = int(input('Port de départ : '))
    port_fin = int(input('Port de fin : '))
    
    # Crée une liste de ports à scanner
    ports = range(port_debut, port_fin + 1)
    
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

        # Exécute le scan de manière asynchrone pour chaque port
        port_ouvert = []
        for port in ports:
            resultat = await scann.scan(port)
            print('test du port %s' % port)
            # Verifier si le port est ouvert pour l'ajouter au tableau
            if resultat is not None and resultat[1]:
                port_ouvert.append(resultat[0])

        print('Scan terminé')
        for port in port_ouvert:
            print('Port ouvert :', port)
    else:
        print('Mode de scan invalide.')

if __name__ == '__main__':
    asyncio.run(main())
