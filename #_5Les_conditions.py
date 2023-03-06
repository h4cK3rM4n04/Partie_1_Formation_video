#coding:utf-8

""" 

conditions multiples:	and (ET *)
						!= (différent de)
						or (OU +)
						in (DANS)
						not in (PAS DANS)


"""

identifiant = "00"
mot_de_passe = "h4"

user_id = input("Entrez votre identifiant:	")
user_pass = input("Entrez votre password:	")

if user_id != identifiant:
	print("Wrong password try again!!!")
else:
	print("Bravo votre mot de passe est confirmé!!!")


lettre = "yu"

if lettre in "aeyuio":
	print("votre lettre  est une voyelle")
else:
	print(None)
jeu_charge = 1


if not jeu_charge:
	print("Le jeu est chargé!!!")
else:
        print("Le jeu n'est pas chargé!!! la valeur est False!!!")

#	Teste si jeu_charge est True
x = 0

if x:
	print("Bonjour")
else:
	print("hey")