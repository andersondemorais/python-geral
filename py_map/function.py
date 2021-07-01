# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "21-may-2021"
__version__ = ""
__status__ = ""

"""
maps
"""


def upper_case(word: str) -> str:
    return word.upper()


my_map = map(upper_case, ('python', 'c', 'cpp', 'php'))
# convert map to list
# output: ['PYTHON', 'C', 'CPP', 'PHP']
print(list(my_map))

# with lambda
my_map1 = map(lambda x: 2 ** x, [1, 2, 3, 4, 5])
# output: [2, 4, 8, 16, 32]
print(list(my_map1))

# alphabet letters/ lowercase
my_alphabet_lower = list(map(chr, range(97, 123)))
print(my_alphabet_lower)
# uppercase
my_alphabet_upper = list(map(upper_case, my_alphabet_lower))
print(my_alphabet_upper)
