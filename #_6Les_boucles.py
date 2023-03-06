#coding:utf-8

for x in range(1):
	print("Jésus est grand!!!")

cpt = 0
while cpt < 1:
	print("Le compteur augmente")
	cpt += 1

lauch_game = 1

while lauch_game:
	var_1 = int(input("Entrez un nombre:	"))
	vari_2 = int(input("Entrez un deuxième nombre:	"))
	if (var_1 + vari_2) > 10:
		lauch_game = 0
	print("fin de la partie")

x = 1

while x:
	v = input("Entrez votre mot de passe:	")
	if v == "01":
		print("Très bien vous avez trouvé le mot de passe")
		break
	elif v == "123":
		print("Vous avez entré le code secret pour quitter")
		break

	else:
		print("Wrong pass")
		continue
