class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False, marque="⛵"):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = marque

    
    @property
    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        else:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]
    
    def chevauche(self, autre):
        return any(pos in autre.positions for pos in self.positions)
    
    
    def coule(self, grille):
        return all(grille.matrice[l * grille.colonnes + c] in ["x", "💣"]
                for (l, c) in self.positions)

    
class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "⛴"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"