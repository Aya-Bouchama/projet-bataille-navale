import random
import os
import sys

from src.grille import Grille
from src.bateau import PorteAvion, Croiseur, Torpilleur, SousMarin


sys.stdout.reconfigure(encoding='utf-8')

# 🎨 Codes couleurs ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def debut_jeu():
    """Création de la grille et placement aléatoire des bateaux."""
    grille = Grille(lignes=8, colonnes=10)
    flotte = [PorteAvion(0, 0), Croiseur(0, 0), Torpilleur(0, 0), SousMarin(0, 0)]
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

            chevauchement = any(
                pos in autre.positions for autre in bateaux_places for pos in bateau.positions
            )

            if not chevauchement:
                placement_valide = True
                grille.ajoute(bateau)
                bateaux_places.append(bateau)

    return grille, bateaux_places


def afficher_grille(grille: Grille):

    print(f"{CYAN}    " + " ".join([str(i) for i in range(grille.colonnes)]) + RESET)
    print("   " + "-" * (2 * grille.colonnes))

    for i in range(grille.lignes):
        ligne = f"{CYAN}{i}{RESET} | "
        for j in range(grille.colonnes):
            case = grille.matrice[i * grille.colonnes + j]
            if case == "~":
                ligne += WHITE + "~ " + RESET
            elif case == "x":
                ligne += BLUE + "x " + RESET
            elif case == "💣":
                ligne += RED + "💣 " + RESET
            else:
                ligne += YELLOW + f"{case} " + RESET
        print(ligne)
    print()


def main():
   
    clear()
    print(f"{BLUE}╔══════════════════════════════════════╗{RESET}")
    print(f"{BLUE}║{RESET}     🌊  BATAILLE NAVALE  🚢      {BLUE}║{RESET}")
    print(f"{BLUE}╚══════════════════════════════════════╝{RESET}\n")

    grille_jeu, flotte = debut_jeu()
    grille_joueur = Grille(grille_jeu.lignes, grille_jeu.colonnes)

    nombre_coups = 0
    bateaux_coules = 0

   
    reponse = input("Afficher la solution (mode test) ? (o/n) : ").lower()
    solution_visible = reponse.startswith("o")

    if solution_visible:
        print("\n🔍 Grille solution :")
        afficher_grille(grille_jeu)

  
    while bateaux_coules < len(flotte):
        print(f"{YELLOW}\n--- Grille du joueur ---{RESET}")
        afficher_grille(grille_joueur)

        
        entree = input(" Entrez les coordonnées (colonne,ligne) : ")
        try:
            x_str, y_str = entree.split(',')
            x, y = int(x_str.strip()), int(y_str.strip())
        except Exception:
            print(f"{RED}⚠️ Format invalide. Exemple : 4,2{RESET}")
            continue

        
        if not (0 <= x < grille_joueur.colonnes and 0 <= y < grille_joueur.lignes):
            print(f"{RED}🧭 Coordonnées hors de la grille !{RESET}")
            continue

        index = y * grille_joueur.colonnes + x
        if grille_joueur.matrice[index] != grille_joueur.vide:
            print(f"{YELLOW}⚠️ Déjà tiré ici !{RESET}")
            continue

        nombre_coups += 1
        case_solution = grille_jeu.matrice[index]

        if case_solution not in [grille_jeu.vide, "x", "💣"]:
            grille_joueur.matrice[index] = "💣"
            print(f"{GREEN}💥 Touché !{RESET}")
            bateau_touche = next((b for b in flotte if (y, x) in b.positions), None)

            if bateau_touche and bateau_touche.coule(grille_joueur):
                bateaux_coules += 1
                print(f"{RED}🔥 {bateau_touche.__class__.__name__.upper()} COULÉ ! 🔥{RESET}")
                for pos_y, pos_x in bateau_touche.positions:
                    idx = pos_y * grille_joueur.colonnes + pos_x
                    grille_joueur.matrice[idx] = bateau_touche.marque
        else:
            grille_joueur.matrice[index] = "x"
            print(f"{CYAN}🌊 Dans l’eau...{RESET}")

   
    clear()
    print(f"{GREEN}🏁 Mission accomplie, Capitaine !{RESET}")
    afficher_grille(grille_joueur)
    print(f"{GREEN}Toute la flotte ennemie a été coulée en {nombre_coups} tirs !{RESET}\n")


if __name__ == "__main__":
    main()
