# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_06.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 18:27:39 by frfrance          #+#    #+#              #
#    Updated: 2020/04/14 18:27:47 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


dic = {"sandwich" : {"ingrediants": ["Jambon", "Pain", "Fromage", "Tomate"],
					"type" : "Dejeuner",
					"time": 10},
		"cake" : {"ingrediants" : ["Farine", "Sucre", "Desert"],
				"type" : "Desert",
				"time" : 60},
		"salade" : {"ingrediants" : ["Avoat", "Roquette", "Tomates", "Epinard"],
				"type" : "dejeuner",
				"time" : 15},
		}

def	ft_home_print():
	print("\nPlease select an option by typing the corresponding number:")
	print("1: Ajouter une recette")
	print("2: Suprimer une recette")
	print("3: Afficher une recette")
	print("4: Afficher toute les recettes")
	print("5: Quitter")


def ft_ajout():
	print("\nQuelle est la recette que vous voulez ajouter ?")
	first = input()
	while first in dic:
		print("\nCette recette existe deja\nVoulez vous recomencer ?\n")
		print("1 : Oui\n2: Retour menu principal\n")
		first = input()
		if (first == "1"):
			print("\nQuelle est la recette que vous voulez ajouter ?")
			first = input()
		if (first == "2"):
			ft_home()
	print("\nQuelles sont les ingrediants de la recette ?")
	print("Merci de les espacer avec une virgule\n")
	second = input().split(",", -1)
	print("Quelle est le type de repas (dejeuner, gouter, ect...) ?")
	third = input()
	print("Combien de temps dure la recette (en minutes) ?")
	fourth = input()
	while fourth.isdigit() == False:
		print("Mettre une duree valide")
		fourth = input()
	dic[first] = {"ingrediants":second, "type":third, "time":fourth}
	print("\nVotre recette a bien ete rajoute\n")


def ft_supp():
	print("\nQuelle est la recette que vous voulez supprimer ?")
	a = input()
	while a not in dic:
		print("\nCette recette n'existe pas\nVoulez vous recomencer ?\n")
		print("1: Oui\n2: Retour menu principal\n")
		a = input()
		if (a == "1"):
			print("\nQuelle est la recette que vous voulez supprimer ?")
			a = input()
		if (a == "2"):
			ft_home()
	if (a in dic):
		print("\n",a.capitalize(), "a bien ete supprime\nVoulez vous en supprimer une autre?")
		del dic[a]


def ft_print_r():
	print("\nQuelle est la recette que vous voulez afficher ?")
	a = input()
	if (a not in dic):
		print("\nCette recette n'existe pas\nVoulez vous recomencer ?\n")
		print("1: Oui\n2: Retour menu principal\n")
		a = input()
		if (a == "1"):
			ft_print_r()
		if (a == "2"):
			ft_home()
	if (a in dic):
			print("\nIl faut ",dic[a]["ingrediants"])
			print("C'est un", dic[a]["type"])
			print("Dure : ",dic[a]["time"], "min\n")


def ft_print_all():
	print("\nVoila toute les recettes du livres\n")
	for recette in dic:
		print(recette.capitalize())


def	ft_home():
	ft_home_print()
	i = input()
	if (i.isdigit() == False or int(i) < 0 or int(i) > 5):
		print("\nErreur commande\n")
	if (i == "1"):
		ft_ajout()
	if (i == "2"):
		ft_supp()
	if (i == "3"):
		ft_print_r()
	if (i == "4"):
		ft_print_all()
	if (i == "5"):
		print("Fermeture du programme...")
		exit()
	ft_home()



ft_home()
