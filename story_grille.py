from src.grille import Grille  

def main():
    ma_grille = Grille(5, 8)

    while True:
        print(ma_grille)
        print("Entrez les coordonnées (ligne colonne) : ")
        ligne, colonne = map(int, input().split())
        ma_grille.tirer(ligne, colonne)

if __name__ == "__main__":
    main()
