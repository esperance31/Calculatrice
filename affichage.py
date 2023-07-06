import fonction

#Répéter ces étapes jusqu'à ce que l'utilisateur décide de quitter l'application
boucle = 1
while (boucle == 1):
    
    #Demander à l'utilisateur de saisir le premier nombre.
    nombre1 = input("Entrer le premier nombre : \n")

    #Demander à l'utilisateur de saisir le deuxieme nombre.
    nombre2 = input("Entrer le deuxieme nombre : \n")

    #Afficher un menu proposant les opérations disponibles.
    
    print("----------Bienvenue sur la calculatrice----------")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    #Demander à l'utilisateur de choisir une opération en saisissant le numéro correspondant.
    
    choix = int(input("Choisissez une opération : "))

    #En fonction du choix de l'utilisateur, effectuer l'opération appropriée et afficher le résultat.


    if (choix == 1):
        if (nombre1.isdigit() and nombre2.isdigit()):
            resultat = fonction.addition(nombre1,nombre2)
            print("L'addition de",nombre1," et de ",nombre2,"est:", resultat)
        else:
            fonction.addition(nombre1,nombre2)
    elif (choix == 2):
        if (nombre1.isdigit() and nombre2.isdigit()):
            resultat = fonction.soustraction(nombre1,nombre2)
            print("La soustraction de",nombre1," et de ",nombre2,"est:", resultat)
        else:
            fonction.soustraction(nombre1,nombre2)
    elif (choix == 3):
        if (nombre1.isdigit() and nombre2.isdigit()):
            resultat = fonction.multiplication(nombre1,nombre2)
            print("La multiplication de",nombre1," et de ",nombre2,"est:", resultat)
        else:
            fonction.multiplication(nombre1,nombre2)
    elif (choix == 4):
        if (nombre1.isdigit() and nombre2.isdigit()  ):
            if (nombre2!=0): 
                resultat = fonction.division(nombre1,nombre2)
                print("La division de",nombre1," et de ",nombre2,"est:", resultat)
        else:
            fonction.division(nombre1,nombre2)
    else:
        print("Entrer un numero entre 1 et 4")
        
    boucle = int(input("Voulez vous effectuer une autre operation? Si oui taper 1 ou tout autre saisie pour quittez  :"))
