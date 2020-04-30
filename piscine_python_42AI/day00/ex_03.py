# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_03.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 14:42:22 by frfrance          #+#    #+#              #
#    Updated: 2020/04/13 16:13:29 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import string


def text_analyser(text=None):
	if text == None:
		print("What is the text to analyse?")
		text = input()
	punctuation = 0
	m = 0
	M = 0
	space = 0

	for c in text:

		if c in string.punctuation:
			punctuation += 1
		if c in string.ascii_lowercase:
			m += 1
		if c in string.ascii_uppercase:
			M += 1
		if c in string.whitespace:
			space += 1
	print("The text contains", len(text), "characters:")
	print("\n")
	print("-", M, "upper letters")
	print("\n")
	print("-", m, "lower letters")
	print("\n")
	print("-", punctuation, "punctuation marks")
	print("\n")
	print("-", space, "spaces")

# text_analyser(None if len(sys.argv) != 2 else sys.argv[1])
