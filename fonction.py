def addition(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        return nombre1 + nombre2
    except ValueError:
        print("Erreur")

    
def soustraction(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        return nombre1 - nombre2
    except ValueError:
        print("Erreur")
    

def multiplication(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        return nombre1 * nombre2
    except ValueError:
        print("Erreur")

def division(a,b):
    try:
        nombre1 = float(a)
        nombre2 = float(b)
        try:
            return nombre1 / nombre2
        except ZeroDivisionError:
            print("La division par zero n'est pas possible")
    except ValueError:
        print("Erreur")
    
    
print(addition(2,5))
print(soustraction(100,45))
print(multiplication(10,2))
division(4,0)