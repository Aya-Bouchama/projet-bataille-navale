from src.bateau import Bateau
from src.grille import Grille

def test_creation_bateau_obligatoire():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False

def test_creation_bateau_facultatif():
    b = Bateau(1, 1, 3, True)
    assert b.ligne == 1
    assert b.colonne == 1
    assert b.longueur == 3
    assert b.vertical is True
    
def test_positions_horizontales():
    b = Bateau(2, 3, longueur=3)
    assert b.positions == [(2, 3), (2, 4), (2, 5)]

def test_positions_verticales():
    b = Bateau(2, 3, longueur=3, vertical=True)
    assert b.positions == [(2, 3), (3, 3), (4, 3)]


def test_bateau_coule():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    
    g.ajoute(b)
    assert b.coule(g) is False
    
    g.tirer(1, 0)
    assert b.coule(g) is False
    
    g.tirer(1, 1)
    assert b.coule(g) is True