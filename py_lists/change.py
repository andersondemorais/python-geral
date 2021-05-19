# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2020"
__email__ = ""
__date__ = "13-may-2021"
__version__ = ""
__status__ = ""

"""
Add and change elements
"""


from contextlib import suppress


""" Change elements """
# Correcting mistake values in a list
my_list_of_chars = ['a', 'b', 'c', 'z', 'e', 'f']

# change the 4th element
my_list_of_chars[3] = 'd'
print(my_list_of_chars[3])

# change a sequence of elements
my_list_of_chars[1:3] = ['B', 'C']
# output: ['a', 'B', 'C', 'z', 'e', 'f']
print(my_list_of_chars)


""" Appending and Extending lists """
# method append
my_list_of_chars.append(5)
# output: ['a', 'B', 'C', 'd', 'e', 'f', 5]
print(my_list_of_chars)
my_list_of_chars.append([1, 2])
# output: ['a', 'B', 'C', 'd', 'e', 'f', 5, [1, 2]]
print(my_list_of_chars)

# ERROR! append() and extend() take exactly one argument
with suppress(TypeError):
    my_list_of_chars.append(2, 5)
    my_list_of_chars.append([1, 2], 5)
    my_list_of_chars.extend(16, 'v')
    my_list_of_chars.extend([16, 2], 'v')

# method extend
my_list_of_chars.extend([56, -19])
# output: ['a', 'B', 'C', 'd', 'e', 'f', 5, [1, 2], 56, -19]
print(my_list_of_chars)
my_list_of_chars.extend([True])
# output: ['a', 'B', 'C', 'd', 'e', 'f', 5, [1, 2], 56, -19, True]
print(my_list_of_chars)

# # # # # # #
# ATTENTION #
# # # # # # #
my_list_of_chars.extend('new')
# output: ['a', 'B', 'C', 'd', 'e', 'f', 5, [1, 2], 'n', 'e', 'w']
print(my_list_of_chars)
my_list_of_chars.extend(['again'])
# output: ['a', 'B', 'C', 'd', 'e', 'f', 5, [1, 2], 'n', 'e', 'w', 'again']
print(my_list_of_chars)

""" Using maths operators """
my_list_of_chars = ['a', 'b', 'c']
my_list_of_chars2 = [1, 2, 3, 4]

# output: ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
print(3 * my_list_of_chars)

my_list_of_chars += ['d', 'e']
# output: ['a', 'b', 'c', 'd', 'e']
print(my_list_of_chars)

my_list_combined = my_list_of_chars + my_list_of_chars2
# output: ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4]
print(my_list_combined)

# split a string into a list
my_list_of_chars = list('Python')
# otput: ['P', 'y', 't', 'h', 'o', 'n']
print(my_list_of_chars)
