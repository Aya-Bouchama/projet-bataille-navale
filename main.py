import random

from src.grille import Grille
from src.bateau  import PorteAvion, Croiseur, Torpilleur, SousMarin


def debut_jeu():

    grille = Grille(lignes=8, colonnes=10)

    flotte = [
        PorteAvion(0, 0),
        Croiseur(0, 0),
        Torpilleur(0, 0),
        SousMarin(0, 0)
    ]

    bateaux_places = []

    for bateau in flotte:
        placement_valide = False
        while not placement_valide:
            
            bateau.vertical = random.choice([True, False])

            if bateau.vertical:
                bateau.ligne = random.randint(0, grille.lignes - bateau.longueur)
                bateau.colonne = random.randint(0, grille.colonnes - 1)
            else:
                bateau.ligne = random.randint(0, grille.lignes - 1)
                bateau.colonne = random.randint(0, grille.colonnes - bateau.longueur)

            chevauchement = any(pos in autre.positions for autre in bateaux_places for pos in bateau.positions)

            if not chevauchement:
                placement_valide = True
                grille.ajoute(bateau)
                bateaux_places.append(bateau)

    return grille, bateaux_places


def main():
    grille_jeu, flotte = debut_jeu()
    grille_joueur = Grille(grille_jeu.lignes, grille_jeu.colonnes)

    nombre_coups = 0
    bateaux_coules = 0

    print("--- véerification de la solution ---")
    grille_jeu.afficher()
    print("-" * 30)

    while bateaux_coules < len(flotte):
        print("\n--- GRILLE DU JOUEUR ---")
        grille_joueur.afficher()

        while True:
            try:
                entree = input("\nEntrez les coordonnées du tir (colonne,ligne ex: 3,5) : ")
                x_str, y_str = entree.split(',')
                x, y = int(x_str.strip()), int(y_str.strip())
                
                if not (0 <= x < grille_joueur.colonnes and 0 <= y < grille_joueur.lignes):
                    print("⚠️ Coordonnées hors de la grille.")
                    continue

                index = y * grille_joueur.colonnes + x

                if grille_joueur.matrice[index] != grille_joueur.vide:
                    print("⚠️ Vous avez déjà tiré ici.")
                    continue

                break
            except ValueError:
                print("Erreur : format invalide. Exemple : 4,2")

        nombre_coups += 1

        index_solution = y * grille_jeu.colonnes + x
        case_solution = grille_jeu.matrice[index_solution]

        if case_solution not in [grille_jeu.vide, "x", "💣"]:
            print("\n💣 TOUCHÉ ! 💣")
            grille_joueur.matrice[index] = "💣"

            bateau_touche = next((b for b in flotte if (y, x) in b.positions), None)

            if bateau_touche and bateau_touche.coule(grille_joueur):
                bateaux_coules += 1
                print(f"🔥 {bateau_touche.__class__.__name__.upper()} COULÉ ! 🔥")
                for pos_y, pos_x in bateau_touche.positions:
                    idx = pos_y * grille_joueur.colonnes + pos_x
                    grille_joueur.matrice[idx] = bateau_touche.marque

        else:
            print("\n🌊 Dans l’eau ! Raté.")
            grille_joueur.matrice[index] = "x"

    print("🚢 Mission accomplie, Capitaine !")
    print(f"Toute la flotte ennemie a été coulée en {nombre_coups} tirs.")

    print("\nGrille finale :")
    grille_joueur.afficher()


if __name__ == "__main__":
    main()
