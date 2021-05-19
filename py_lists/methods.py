# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "14-may-2021"
__version__ = ""
__status__ = ""

"""
A few examples of Python list methods:
.append(element), 
.clear(),
.copy(),
.count(element),
.extend(element),
.index(element), 
.insert(index, element), 
.pop(position), 
.pop(), 
.remove(element), 
.reverse(), 
.sort() 
***
.join()
"""


import copy
from contextlib import suppress

my_list_of_chars = ['a', 'b', 'c', 'd', 'z', 'e', 'f']

my_list_of_chars.append('g')
# output: ['a', 'b', 'c', 'd', 'z', 'e', 'f', 'g']
print(my_list_of_chars)

my_list_of_chars.clear()
# output: []
print(my_list_of_chars)

my_list_of_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'f', 'f', 'g', 'z']
# output: 3
print(my_list_of_chars.count('f'))

my_list_of_chars.extend(['x', 'y'])
# output: ['a', 'b', 'c', 'd', 'e', 'f', 'f', 'f', 'g', 'z', 'x', 'y']
print(my_list_of_chars)

# returns the index of the first element
# output: 5
print(my_list_of_chars.index('f'))

# ERROR! value is not in list
with suppress(ValueError):
    print(my_list_of_chars.index('ff'))

my_list_of_chars.insert(6, 'fff')
# output: ['a', 'b', 'c', 'd', 'e', 'f', 'fff', 'f', 'f', 'g', 'z', 'x', 'y']
print(my_list_of_chars)

""" method pop - LIFO """
my_list_of_chars.pop(7)
# output: ['a', 'b', 'c', 'd', 'e', 'f', 'fff', 'f', 'g', 'z', 'x', 'y']
print(my_list_of_chars)
my_list_of_chars.pop()
# output: ['a', 'b', 'c', 'd', 'e', 'f', 'fff', 'f', 'g', 'z', 'x']
print(my_list_of_chars)

my_list_of_chars.remove('a')
# output: ['b', 'c', 'd', 'e', 'f', 'fff', 'f', 'g', 'z', 'x']
print(my_list_of_chars)
# if teh item does not exist, throws an exception
with suppress(ValueError):
    my_list_of_chars.remove('u')

my_list_of_chars = ['ff', 'c', 'a', 'e', 'x', 'r', 'f', 'g', 'd', 'x']
my_list_of_chars.reverse()
# output: ['x', 'd', 'g', 'f', 'r', 'x', 'e', 'a', 'c', 'ff']
print(my_list_of_chars)

my_list_of_chars.sort()
# output: ['a', 'c', 'd', 'e', 'f', 'ff', 'g', 'r', 'x', 'x']
print(my_list_of_chars)

my_list_of_chars = ['a', 'b', 'c', 4, 'd']
# ERROR! '<' not supported between instances of 'str' and 'int'
with suppress(TypeError):
    my_list_of_chars.sort()


""" Copy of lists """
# # # # # # #
# ATTENTION #
# # # # # # #

my_list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8]

my_list_of_integers_meth_copy = my_list_of_integers.copy()

# Shallow copy
my_list_of_integers_shallow_copy = copy.copy(my_list_of_integers)
# Deep copy
my_list_of_integers_deep_copy = copy.deepcopy(my_list_of_integers)

my_list_of_integers_copy = list(my_list_of_integers)
my_list_of_integers_copy1 = my_list_of_integers[:]
my_list_of_integers_copy2 = [x for x in my_list_of_integers]

# copy of the list reference
my_list_of_integers_reference = my_list_of_integers

# output: [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list_of_integers)
print(my_list_of_integers_meth_copy)
print(my_list_of_integers_shallow_copy)
print(my_list_of_integers_deep_copy)
print(my_list_of_integers_copy)
print(my_list_of_integers_copy1)
print(my_list_of_integers_copy2)
print(my_list_of_integers_reference)


my_list_of_integers[2] = 333
# output: [1, 2, 333, 4, 5, 6, 7, 8]
print(my_list_of_integers)
# output: [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list_of_integers_meth_copy)
print(my_list_of_integers_shallow_copy)
print(my_list_of_integers_deep_copy)
print(my_list_of_integers_copy)
print(my_list_of_integers_copy1)
print(my_list_of_integers_copy2)
# output: [1, 2, 333, 4, 5, 6, 7, 8]
print(my_list_of_integers_reference)

""" METHDS FOR USE WITH LISTS """

""" JOIN """
my_list_of_chars = ['Hi', 'Python', '!!!']
# join elements using string as separator
# output: Hi_Python_!!!
print('_'.join(my_list_of_chars))

""" SUM """
my_sum_elements = sum(my_list_of_integers)
# output: 366
print(my_sum_elements)
my_sum_pair_elements = [
    sum(pair)
    for pair in zip(
        [1, 2, 3],
        [1, 2, 3],
    )
]
# output: [2, 4, 6]
print(my_sum_pair_elements)
