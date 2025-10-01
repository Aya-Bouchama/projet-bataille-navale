from src.bateau import Bateau

class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "~"  
        self.matrice = [self.vide] * (lignes * colonnes)

    def __str__(self):
        lignes = []
        for l in range(self.lignes):
            ligne = self.matrice[l * self.colonnes:(l + 1) * self.colonnes]
            lignes.append("".join(ligne))
        return "\n".join(lignes)

    def afficher(self):
        print(self.__str__())

    def tirer(self, ligne, colonne, touche="x"):
        index = ligne * self.colonnes + colonne
        self.matrice[index] = touche
        
    
    def ajoute(self, bateau: Bateau):
        for (l, c) in bateau.positions:
            if not (0 <= l < self.lignes and 0 <= c < self.colonnes):
                return False
       
        for (l, c) in bateau.positions:
            index = l * self.colonnes + c
            self.matrice[index] = "⛵"
        return True



