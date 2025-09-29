


from src.grille import Grille

def test_initialisation():
    g = Grille(3, 3)
    assert g.matrice == ["~"] * 9

def test_tirer():
    g = Grille(3, 3)
    g.tirer(1, 1) 
    index = 1 * g.colonnes + 1
    assert g.matrice[index] == "x"
