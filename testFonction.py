# Les tests de nos différentes fonctions

# Importation de notre fichier 'fonction.py' contenant nos fonctions
import fonction

# Tests pour l'Addition
def test_addition():
   # Cas 1 : test avec des nombres réels positifs
    exemple1 = 12.5
    exemple2 = 10
    oracle = 22.5
    try:
        assert fonction.addition(exemple1, exemple2) == oracle
        print("Test du cas 1 validé.")
    except AssertionError:
        print("Test du cas 1 échoué.")
    
    # Cas 2 : test avec des nombres réels négatifs
    exemple1 = -5
    exemple2 = -12.5
    oracle = -17.5
    try:
        assert fonction.addition(exemple1, exemple2) == oracle
        print("Test du cas 1 validé.")
    except AssertionError:
        print("Test du cas 1 échoué.")
    
    # Cas 3 : test avec un nombre positif et un nombre négatif
    exemple1 = 25
    exemple2 = -4.5
    oracle = 20.5
    try:
        assert fonction.addition(exemple1, exemple2) == oracle
        print("Test du cas 1 validé.")
    except AssertionError:
        print("Test du cas 1 échoué.")

    # Cas 4 : test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    
    try:
        fonction.addition(exemple1, exemple2)
    except ValueError:
        print("Test du cas 4 validé.")
    else:
        print("Test du cas 4 échoué.")

# Appel de la fonction 'test_addition'
test_addition()
print("\n")

# Tests pour la Soustraction
def test_soustraction():
    # Cas 1: test avec des nombres réels
    exemple1 = 12.5
    exemple2 = 10
    oracle = 2.5
    try:
        assert fonction.soustraction(exemple1, exemple2) == oracle
        print("Test du cas 1 validé.")
    except AssertionError:
        print("Test du cas 1 échoué.")
    
    # Cas 2: test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    try:
        fonction.soustraction(exemple1, exemple2)
    except ValueError:
        print("Test du cas 2 validé.")
    else:
        print("Test du cas 2 échoué.")

# Appel de la fonction 'test_soustraction'
test_soustraction()
print("\n")

# Tests pour la Multiplication
def test_multiplication():
    # Cas 1: test avec les nombres réels
    exemple1 = 12.5
    exemple2 = 10
    oracle = 125
    try:
        assert fonction.multiplication(exemple1, exemple2) == oracle
        print("Test du cas 1 de la multiplication validé.")
    except AssertionError:
        print("Test du cas 1 de la multiplication échoué.")
    
    # Cas 2: test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    try:
        fonction.multiplication(exemple1, exemple2)
    except ValueError:
        print("Test du cas 2 de la multiplication validé.")
    else:
        print("Test du cas 2 de la multiplication échoué.")

# Appel de la fonction 'test_multiplication'
test_multiplication()
print("\n")

# Tests pour la Division
def test_division():
    # Cas 1: test avec deux (02) nombres réels
    exemple1 = 12.5
    exemple2 = 10
    oracle = 1.25
    try:
        assert fonction.division(exemple1, exemple2) == oracle
        print("Test du cas 1 de la division validé.")
    except AssertionError:
        print("Test du cas 1 de la division échoué.")
    
    # Cas 2: test avec un nombre réél et '0'
    exemple1 = 20
    exemple2 = 0
    try:
        fonction.division(exemple1, exemple2)
    except ValueError:
        print("Test du cas 2 de la division validé.")
    else:
        print("Test du cas 2 de la division échoué.")

    # Cas 3: test avec une chaine et un nombre réel
    exemple1 = ""
    exemple2 = 12
    try:
        fonction.division(exemple1, exemple2)
    except ValueError:
        print("Test du cas 3 de la division validé.")
    else:
        print("Test du cas 3 de la division échoué.")

# Appel de la fonction 'test_division'
test_division()
print("\n")