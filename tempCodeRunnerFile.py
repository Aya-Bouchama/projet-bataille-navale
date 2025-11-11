 # Vérifie si ce bateau est coulé
            if bateau_touche and bateau_touche.coule(grille_joueur):
                bateaux_coules += 1
                print(f"🔥 {bateau_touche.__class__.__name__.upper()} COULÉ ! 🔥")
                for pos_y, pos_x in bateau_touche.positions:
                    idx = pos_y * grille_joueur.colonnes + pos_x
                    grille_joueur.matrice[idx] = bateau_touche.marque
