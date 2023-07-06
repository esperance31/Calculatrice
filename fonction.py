def addition(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        return nombre1 + nombre2
    except ValueError:
        return "Erreur de saisie"

    
def soustraction(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        return nombre1 - nombre2
    except ValueError:
        return "Erreur de saisie"
    

def multiplication(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        return nombre1 * nombre2
    except ValueError:
        return "Erreur de saisie"

def division(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        try:
            return nombre1 / nombre2
        except ZeroDivisionError:
            "La division par zero n'est pas possible"
    except ValueError:
        return "Erreur de saisie"
    
    
