#initialisation de la variable continuer pour la boucle principale
continer = "o"
#definission des differente fonction pour l'addition, la soustraction,la division et la multiplication
def addition (a,b):
    return a+b

def soustraction(a,b):
    return a-b

def division(a,b):
    if (b==0):
        print("erreu un nombre n'est pas divisible par zero")
        return None
    else:
        return a/b

def multiplication(a,b):
    return a*b

#debut de la boucle principale de la calculatrice 

while(continer =="o"):
    # ici on demande d'entrer le premier nombre l'operation que l'on souhaite effectuer et le second nombre 

    a = float(input("entrer votre premeier nombre:"))
    op= input("entrer votre operation:")
    b= float(input("entrer votre second nombre:"))

    # ici en fonction de l'operation souhaiter on appel la fonctons correspondante

    if op =="+":
        resultat = addition(a,b)
    elif op=="-":
        resultat = soustraction(a,b)
    elif op=="*":
        resultat = multiplication(a,b)
    else:
        resultat = division(a,b)
    
    #on affiche le resultat

    print(resultat)
    
    #en fonction du choix de l'utilisateur on pourra relancer la calculatrice ou l'arrèter

    continer = input("voulez vous continuez (o/n):")
    if (continer!="o"):
        break
    