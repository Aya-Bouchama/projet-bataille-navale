"""
User Story : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire
Actions :
1. créer une grille à 5 lignes et 8 colonnes
2. afficher la grille à l'écran
3. demander à l'utilisateur de rentrer deux coordonnées x et y
4. tirer à l'endroit indiqué sur la grille
5. retour en 2
"""



from src.grille import Grille  

def main():
    # 1. Créer une grille de 5 lignes et 8 colonnes
    ma_grille = Grille(5, 8)   # constructeur à coder dans grille.py

    while True:
        # 2. Afficher la grille
        ma_grille.afficher()   # méthode à coder dans Grille

        # 3. Demander à l’utilisateur des coordonnées
        print("Entrez les coordonnées (x y) : ")
        x, y = map(int, input().split())

        # 4. Tirer sur la grille
        resultat = ma_grille.tirer(x, y)   # méthode à coder dans Grille
        print("Résultat :", resultat)

        # 5. Retour en 2 (la boucle while reprend)


if __name__ == "__main__":
    main()
