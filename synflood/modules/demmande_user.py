
class DemandeUtilisateur:
    def obtenir_informations(self):
        # Demander à l'utilisateur les informations nécessaires
        cible = input("Adresse cible : ")
        port = int(input("Port : "))
        nbrpaquet = int(input("Nombre de paquets : "))
        nbr_processus = int(input("Nombre de processus : "))
        return cible, port, nbrpaquet, nbr_processus

if __name__ == "__main__":
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus = demande_utilisateur.obtenir_informations()
    print(f"Cible : {cible}, Port : {port}, Nombre de paquets : {nbrpaquet}, Nombre de processus : {nbr_processus}")
