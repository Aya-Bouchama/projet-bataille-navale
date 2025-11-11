import random
from src.grille import Grille
from src.bateau import PorteAvion, Croiseur, Torpilleur, SousMarin


def placer_bateaux_aleatoirement(grille: Grille):
    
    types_bateaux = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    bateaux_places = []

    for TypeBateau in types_bateaux:
        placements_valides = []

       
        for ligne in range(grille.lignes):
            for colonne in range(grille.colonnes):
                for vertical in [True, False]:
                    b = TypeBateau(ligne, colonne, vertical)

                   
                    if any(l >= grille.lignes or c >= grille.colonnes for (l, c) in b.positions):
                        continue  

              
                    if any(b.chevauche(existant) for existant in bateaux_places):
                        continue 

                  
                    placements_valides.append(b)

      
        if not placements_valides:
            raise ValueError(f" Impossible de placer {TypeBateau.__name__}")

        
        bateau_choisi = random.choice(placements_valides)

        
        grille.ajoute(bateau_choisi)
        bateaux_places.append(bateau_choisi)

    return bateaux_places


def main():
    
    print("=== ⚓ Bataille navale : Placement des bateaux ===")
    grille = Grille(8, 10)

 
    bateaux = placer_bateaux_aleatoirement(grille)
    print(" Tous les bateaux ont été placés aléatoirement !")

    
    print(grille)

if __name__ == "__main__":
    main()
