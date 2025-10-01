from src.bateau import Bateau

def main():
    print("User Story : chevauchement")

    
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(2, 4, longueur=2)
    print("Chevauchement attendu :", b1.chevauche(b2))  


    b3 = Bateau(0, 0, longueur=2)
    b4 = Bateau(1, 0, longueur=2, vertical=True)
    print("Chevauchement attendu :", b3.chevauche(b4))  

if __name__ == "__main__":
    main()
