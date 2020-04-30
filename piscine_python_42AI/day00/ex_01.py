# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/13 11:14:58 by frfrance          #+#    #+#              #
#    Updated: 2020/04/13 14:04:39 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = 0
delet_arg = sys.argv[1:]

for arg in delet_arg[::-1]:
	if i > 0 and i < len(arg):
		print(" ", end = "")
	i +=1
	print(arg[::-1].swapcase(), end = "")
