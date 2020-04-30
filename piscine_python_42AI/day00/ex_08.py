# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_08.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 12:43:26 by frfrance          #+#    #+#              #
#    Updated: 2020/04/20 15:02:02 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys
# This is the dictonary that i'll use later on
alpha = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
		'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
		'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
		'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
		'Y':'-.--', 'Z':'--..', ' ': ' '}
# Here I check if I recieved an argumenet
if (len(sys.argv) != 2):
	print("<a-zA-Z string>")
	exit()
word = sys.argv[1]
# Here I check if the len of my argument is upper than 0
if (len(word) == 0):
	print("<a-zA-Z string>")
	exit()
# Here I check the content of my arguments
for c in word.upper():
	if (c not in string.ascii_uppercase and c != ' '):
		print("<a-zA-Z string>")
		exit()
# Here i print every chararcter from the argument
# with the corresponding morse code in the dictionary
for c in word.upper():
	print(alpha[c], end = '')
# Final '\n'
print("")

