# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_00.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 18:06:50 by frfrance          #+#    #+#              #
#    Updated: 2020/04/21 21:17:28 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime

class Recette:

	def __init__(self, name, lvl, time, ingrediant, description, type_):
		self.name = name
		self.lvl = lvl
		self.time = time
		self.ing = ingrediant
		self.des = description
		self.type = type_
		self.verif_value()
		self.verif_type()

	def __str__(self):
		return "Nom recette : {}\nNiveau : {}\nDure : {}min\nIngrediant : {} \
				\nDescription : {}\nType : {}".format(self.name, self.lvl, \
				self.time, self.ing, self.des, self.type)

	def verif_type(self):
		if (type(self.ing) != list):
			raise TypeError("La valeur 'ingrediant' doit etre de type list\n")
		if (type(self.lvl) != int or type(self.time) != int):
			raise TypeError("Les valeurs 'lvl' et 'time' doivent etre des entier\n")
		if (type(self.name) != str or type(self.des) != str or \
				type(self.type) != str):
			raise TypeError("Les valeurs 'name' ingrediant' 'description' 'types' doivent \
					 etre des chaine de caractere\n")

	def verif_value(self):
		if (not self.name or not self.lvl or not self.time or not self.ing \
				or not self.type):
				print("Valeur manquante\n")
				exit()

	def	print_str(self):
		print(self.__str__())

class Book:

	def __init__(self, name_b):
		self.name = name_b
		self.date = datetime.date.today()
		self.lst_ = {}

	def get_recipe_by_name(self, name):
		for key, value in self.lst_.items():
			if key== name:
				print(key, value)

	def add_recipe_type(self, type_):
		for key, value in book1.lst_.items():
			if value["type"] == type_:
				print(key, "est de type", type_)

	def	add_recipe(self, recipe):
		self.lst_[recipe.name] = {"lvl" : recipe.lvl, "time" : recipe.time, "ingrediant" : \
			recipe.ing, "description" : recipe.des, "type" : recipe.type}
		print(recipe.name, "a ete ajouter")
		print(self.date)



if __name__ == "__main__":
	recette_1 = Recette("nutella", 5, 10, ["noisette", "huilde de palme", "cacao"], \
				"", "gouter")
	recette_2 = Recette("tiramisu", 2, 30, ["creme", "mascarpone", "chocolat"], \
				"miam miam", "gouter")
	book1 = Book("book_1")
	book2 = Book("book_2")
