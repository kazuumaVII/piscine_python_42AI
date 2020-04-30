# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_04.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 16:13:44 by frfrance          #+#    #+#              #
#    Updated: 2020/04/16 11:29:16 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_error():

	if len(sys.argv) < 3:
		print("Usage: python operations.py <number1> <number2> \nExample:\n\tpython operations.py 10 3")
		exit()
	if len(sys.argv) > 3 :
		print("InputError: too many arguments")
		exit()
	if sys.argv[1].isdigit() == False or sys.argv[2].isdigit == False:
		print("InputError: only numbers")
		exit()



def ft_calcul(a, b):
	ad = a + b
	moin = a - b
	multi = a * b
	div = "ERROR: (div by zero)" if a == 0 or b == 0 else a / b
	modulo = "ERROR: (modulo by zero)" if a == 0 or b == 0 else a % b
	return ad, moin, multi, div, modulo

ft_error()
t = ft_calcul(int(sys.argv[1]), int(sys.argv[2]))


print("Sum:	     ", t[0])
print("Difference:  ", t[1])
print("Product:     ", t[2])
print("Quotient:    ", t[3])
print("Remainder:   ", t[4])




