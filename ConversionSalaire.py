
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
            ecart = float(salaire)*0.23
            net = float(salaire) - ecart
            net = str(net)
            print("Votre salaire sera d'environ " + net + ' euros net.' )
        except ValueError:
            print("Ce n'est pas un nombre!")

    if i == '2':
        salaire=input('Saisissez votre salaire:')
        try:
            float(salaire)
            ecart = float(salaire)*0.23
            net = float(salaire) + ecart
            net = str(net)
            print("Votre salaire sera d'environ " + net + ' euros brut.' )
        except ValueError:
            print("Ce n'est pas un nombre!")                    
    



