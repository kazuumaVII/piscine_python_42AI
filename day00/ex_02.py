# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_02.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 14:05:17 by frfrance          #+#    #+#              #
#    Updated: 2020/04/13 14:39:50 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2:
	print("error")
	exit()
if len(sys.argv) == 1:
	exit()
if sys.argv[1].isdigit() == False:
	print("error.")
	exit()

n = sys.argv[1]
if int(n) == 0:
	print("I'm Zero.")
elif int(n) % 2 == 0:
	print("I'm Even")
else:
	print("I'm Odd")
