# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex_07.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: frfrance <frfrance@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/16 11:09:05 by frfrance          #+#    #+#              #
#    Updated: 2020/04/17 21:58:13 by frfrance         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) != 3 or sys.argv[2].isdigit() == False:
	print("ERROR")
	exit()

str_ = sys.argv[1]
res = str_.translate(str.maketrans("","", string.punctuation))
a = len(res)
nb = int(sys.argv[2])
x = res.split(" ", -1)
list_ = []
for word in x:
	if (len(word) > nb):
		list_.append(word)
print(list_)




