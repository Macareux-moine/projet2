from modules.scan_synch import ScanSynch

def main():
    hote = input('Hote (localhost) : ')
    ports = range(1, 20)
    scann = ScanSynch(hote)
    port_ouvert = []
    
    # Lance un scan sur tout les port
    for port in ports:
        print ("test du port %s " % port)
        resultat = scann.scan(port)
        if resultat is not None:
            port_ouvert.append(resultat)
    
    print ('scan terminéés')
    for port in port_ouvert:
        print ('port_ouvert : %s' % port)
        
    
if __name__ == '__main__':
    main()
