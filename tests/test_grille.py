


from src.grille import Grille
from src.bateau import Bateau

def test_initialisation():
    g = Grille(3, 3)
    assert g.matrice == ["~"] * 9

def test_tirer():
    g = Grille(3, 3)
    g.tirer(1, 1) 
    index = 1 * g.colonnes + 1
    assert g.matrice[index] == "x"
    
    
def test_str_grille():
    g = Grille(2, 3)
    attendu = "~~~\n~~~"
    assert str(g) == attendu

    g.tirer(1, 1)
    attendu = "~~~\n~x~"
    assert str(g) == attendu
    
    
def test_ajoute_bateau_ok():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.matrice == ['~', '~', '~', '⛵', '⛵', '~']
    

def test_ajoute_bateau_depasse():
    g = Grille(2, 3)

    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    assert g.matrice == ['~', '~', '~', '~', '~', '~']

    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.matrice == ['~', '~', '~', '~', '~', '~']