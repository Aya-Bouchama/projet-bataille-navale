class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
    
    
    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]
    
    def chevauche(self, autre):
        return any(pos in autre.positions for pos in self.positions)
    
    
    def coule(self, grille):
        return all(grille.matrice[l * grille.colonnes + c] == "x" for (l, c) in self.positions)