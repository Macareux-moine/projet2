import multiprocessing


class DemandeUtilisateur:
    def obtenir_informations(self):
        # Demander à l'utilisateur les informations nécessaires
        cible = input("Adresse cible : ") # demande a utilisateur, la cible
        port = int(input("Port : ")) #obliger avoir un int(input) pour avoir un entier sinon bloucle infini entre synflod_multi et demande_user
        nbrpaquet = int(input("Nombre de paquets : ")) # demande a utilisateur le nbr de paquet a envoyer
        max_processus_possible = multiprocessing.cpu_count() 
        print("Nombre de processus max de votre machine. ", max_processus_possible)
        print("ATTENTION: Mettre plus pourrais ralentir le processus et de ralentissement de votre machine: \n")
        nbr_processus = int(input("Nombre de processus : ")) # Si le nombre de processeur ne permet pas avoir un compte complet par exemple 10 paquet pour 4 proceseur, on perdra 2 paquet.
        return cible, port, nbrpaquet, nbr_processus

if __name__ == "__main__":
    demande_utilisateur = DemandeUtilisateur()
    cible, port, nbrpaquet, nbr_processus= demande_utilisateur.obtenir_informations()
    print(f"Cible : {cible}, Port : {port}, Nombre de paquets : {nbrpaquet}, Nombre de processus : {nbr_processus}")

 #\
