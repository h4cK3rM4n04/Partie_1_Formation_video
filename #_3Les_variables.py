#coding:utf-8

"""Une variable: pas de caractères spéciaux, espaces-accents,
underscore

type standars:	entier numérique (int)
				nombre flottant (float)
				chaine de caractère (str)
				booléen (bool)

"""

age_personne = 16
nbr_flottant = 2313.12
booleens = True and False #opération *(and)
booll = True or False #opération (+)

print("âge de la personne\t", age_personne,
	"\n", "Ex de nbr flottant\t",nbr_flottant,
	"\n", "Ex de booléen\t",booleens, "\n", "Booléens 2", booll)

#méthode .format()

print("Je vous montre des information {}, et puis {}".format(age_personne, nbr_flottant))

player_name = input("Entrez un chiffre de votre choix:	")

#Caster une donnée = changer son type

Bool_value = True and False
print(int(Bool_value))