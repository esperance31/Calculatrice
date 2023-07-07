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
    print("5. Puissance")


    

    #En fonction du choix de l'utilisateur, effectuer l'opération appropriée et afficher le résultat.

    #Demander à l'utilisateur de choisir une opération en saisissant le numéro correspondant.
    
    choix = int(input("Choisissez une opération : "))
    if (choix == 1):
        if (isinstance(nombre1,float) and isinstance(nombre2,float )):
            print(fonction.addition(nombre1,nombre2))
        else:
            resultat = fonction.addition(nombre1,nombre2)
            print("L'addition de" + nombre1 + " et de " + nombre2 + "est:" + str(resultat))
    elif (choix == 2):
        if (isinstance(nombre1,float) and isinstance(nombre2,float )):
            resultat = fonction.soustraction(nombre1,nombre2)
            print("La soustraction de",nombre1," et de ",nombre2,"est:", resultat)
        else:
            print(fonction.soustraction(nombre1,nombre2))
    elif (choix == 3):
        if (isinstance(nombre1,float) and isinstance(nombre2,float )):
            resultat = fonction.multiplication(nombre1,nombre2)
            print("La multiplication de",nombre1," et de ",nombre2,"est:", resultat)
        else:
            print(fonction.multiplication(nombre1,nombre2))
    elif (choix == 4):
        if (isinstance(nombre1,float) and isinstance(nombre2,float )):
            if (nombre2==0.0): 
                fonction.division(nombre1,nombre2)
            else:
                resultat = fonction.division(nombre1,nombre2)
                print("La division de",nombre1," et de ",nombre2,"est:", str(resultat))
        else:
            print(fonction.division(nombre1,nombre2))
    elif(choix == 5):
        if (isinstance(nombre1,float) and isinstance(nombre2,float )):
            resultat = fonction.puissance(nombre1,nombre2)
            print("La puissanse de",nombre1," par ",nombre2,"est:", resultat)
        else:
            print(fonction.puissance(nombre1,nombre2))
    else:
        print("Entrer un numero entre 1 et 5 :")
        
    boucle = float(input("Voulez vous effectuer une autre operation? Si oui taper 1 ou tout autre saisie pour quittez  :"))
