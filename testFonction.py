# Les tests de nos différentes fonctions

# Importation de notre fichier 'fonction.py' contenant nos fonctions
import fonction

# Tests pour l'Addition
def test_addition():
   # Cas 1 : test avec des nombres réels positifs
    exemple1 = 12.5
    exemple2 = 10
    oracle = 22.5
    assert fonction.addition(exemple1, exemple2) == oracle
        
    
    # Cas 2 : test avec des nombres réels négatifs
    exemple1 = -5
    exemple2 = -12.5
    oracle = -17.5
    assert fonction.addition(exemple1, exemple2) == oracle
    
    
    # Cas 3 : test avec un nombre positif et un nombre négatif
    exemple1 = 25
    exemple2 = -4.5
    oracle = 20.5
    assert fonction.addition(exemple1, exemple2) == oracle
    

    # Cas 4 : test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    fonction.addition(exemple1, exemple2)
    

# Appel de la fonction 'test_addition'
test_addition()
print("\n")

# Tests pour la Soustraction
def test_soustraction():
    # Cas 1: test avec des nombres réels
    exemple1 = 12.5
    exemple2 = 10
    oracle = 2.5
    assert fonction.soustraction(exemple1, exemple2) == oracle
   
    
    # Cas 2: test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    fonction.soustraction(exemple1, exemple2)
 

 # Tests pour la Multiplication
def test_multiplication():
    # Cas 1: test avec les nombres réels
    exemple1 = 12.5
    exemple2 = 10
    oracle = 125
    assert fonction.multiplication(exemple1, exemple2) == oracle
    
    # Cas 2: test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    fonction.multiplication(exemple1, exemple2)


# Tests pour la Division
def test_division():
    # Cas 1: test avec deux (02) nombres réels
    exemple1 = 12.5
    exemple2 = 10
    oracle = 1.25
    assert fonction.division(exemple1, exemple2) == oracle

    # Cas 2: test avec un nombre réél et '0'
    exemple1 = 20
    exemple2 = 0
    fonction.division(exemple1, exemple2)

    # Cas 3: test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    fonction.division(exemple1, exemple2)
