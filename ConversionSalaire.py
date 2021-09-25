
print('Bonjour !')
print("1.Calculer mon salaire net")
print("2.Calculer mon salaire brut")

i = input("Choisissez 1 ou 2: ")
if i not in ['1', '2']:
    print("Choix incorrect !")
else:
    if i == '1' : 
        salaire=input('Saisissez votre salaire:')
        try:
            float(salaire)
            ecartNonCadre = float(salaire)*0.22
            netNonCadre = float(salaire) - ecartNonCadre
            netNonCadre = str(netNonCadre)
            ecartCadre = float(salaire)*0.25
            netCadre = float(salaire) - ecartCadre
            netCadre = str(netCadre)
            print("Votre salaire sera d'environ " + netNonCadre + " euros net si vous n'êtes pas cadre." )
            print("Votre salaire sera d'environ " + netCadre + " euros net si vous êtes cadre." )
        except ValueError:
            print("Ce n'est pas un nombre!")

    if i == '2':
        salaire=input('Saisissez votre salaire:')
        try:
            float(salaire)
            brutNonCadre = float(salaire)/0.78
            brutNonCadre = str(brutNonCadre)
            brutCadre = float(salaire)/0.75
            brutCadre = str(brutCadre)
            print("Votre salaire sera d'environ " + brutNonCadre + " euros net si vous n'êtes pas cadre." )
            print("Votre salaire sera d'environ " + brutCadre + " euros net si vous êtes cadre." )
        except ValueError:
            print("Ce n'est pas un nombre!")        



