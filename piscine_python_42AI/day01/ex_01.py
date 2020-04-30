# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_01.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/21 21:23:02 by frfrance          #+#    #+#              #
#    Updated: 2020/04/21 21:47:40 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



# class Stark:

# 	def __init__(self, first_name=None, is_alive=True):
# 		self.family_name = "stark"
# 		self.house_words = "winter is coming"

# class Child:

class Personne:
	"""Classe représentant une personne"""
	def __init__(self, nom):
		"""Constructeur de notre classe"""
		self.nom = nom
		self.prenom = "Martin"
	def __str__(self):
		"""Méthode appelée lors d'une conversion de l'objet en chaîne"""
		return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
	"""Classe définissant un agent spécial.
	Elle hérite de la classe Personne"""

	def __init__(self, nom, matricule):
		"""Un agent se définit par son nom et son matricule"""
		self.nom = nom
		self.matricule = matricule
	def __str__(self):
		"""Méthode appelée lors d'une conversion de l'objet en chaîne"""
		return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

	def	print_str(self):
		print(self.__str__())
