

class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "~"  
        self.matrice = [self.vide] * (lignes * colonnes)

    def afficher(self):
        for l in range(self.lignes):
            ligne = self.matrice[l * self.colonnes:(l + 1) * self.colonnes]
            print(" ".join(ligne))

    def tirer(self, ligne, colonne):
        index = ligne * self.colonnes + colonne
        self.matrice[index] = "x"

