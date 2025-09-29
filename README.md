# Projet Bataille Navale 

##  Description

Ce projet est une implémentation en **Python** du jeu de **Bataille Navale**.  
Contrairement au jeu classique à deux joueurs, nous développons ici une **interface pour un seul joueur**.  

Le joueur dispose d’une grille et peut tirer sur des cases pour tenter de toucher et de couler les navires adverses.  


##  Installation

1. Cloner ce dépôt :
   ```bash
   git clone https://github.com/Aya-Bouchama/projet-bataille-navale.git
   cd projet-bataille-navale
   ```

2. Créer un environnement virtuel et l’activer :

   - **Sous Windows PowerShell** :
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **Sous Linux / Mac** :
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

##  Exécution du jeu

Lancer le jeu avec :
```bash
python main.py
```

## Lancer les tests

Exécuter tous les tests unitaires avec :

```bash
pytest
```