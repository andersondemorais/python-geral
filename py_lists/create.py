# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2020"
__email__ = ""
__date__ = "13-may-2021"
__version__ = ""
__status__ = ""

"""
Creating lists in Python
LIST: mutable, sequence, indexed, subscriptable, multiple(allows equal elem - duplicate)
variable = [elem1, elem2, elem3, ..., elemN]
constructor: variable = list((elem1, elem2, elem3, ..., elemN))
"""


from contextlib import suppress

my_list_default_mode = []
my_list_with_constructor = list(())

# list of the same type
my_list_of_integers = [1, 2, 3, 4, 5]
my_list_of_chars = ['a', 'b', 'c', 'z', 'f', '7']
my_list_of_strings = ['Python', 'Django', 'Flask', 'PHP']

# lists can have mixed data
my_list_mixed = [1, 'a', 'x', True]

# lists can also have another list as an item
my_list_nested = [1.5, ['a', 'b', 'c'], -300]

""" 
Accessing elements
"""
# output: Python
print(my_list_of_strings[0])
# output: Django
print(my_list_of_strings[1])
# output: Flask
print(my_list_of_strings[2])
# output: PHP
print(my_list_of_strings[3])

# Nested list
# output: 1.5
print(my_list_nested[0])
# output: b
print(my_list_nested[1][1])
# output: -300
print(my_list_nested[2])

# ERROR! List indices must be integers or slices, not float
with suppress(TypeError):
    print(my_list_nested[1.5])

""" Negative indices """
# list my_list_of_chars: lenght = 6 -> 6 elements
#  0  |  1  |  2  |  3  |  4  |  5
# 'a' | 'b' | 'c' | 'z' | 'f' | '7'
# -6  | -5  | -4  | -3  | -2  | -1

# output: b
print(my_list_of_chars[-5])

# indices between the elements
#  0  |  1  |  2  |  3  |  4  |  5  |
#  | 'a' | 'b' | 'c' | 'z' | 'f' | '7'
# -6  | -5  | -4  | -3  | -2  | -1  |

# elements 2nd to 4th - output: ['b', 'c', 'z']
print(my_list_of_chars[1:4])
# elements begining to 4th - output: ['a', 'b', 'c', 'z']
print(my_list_of_chars[:-2])
print(my_list_of_chars[:4])
# elements 2nd to end - output: ['b', 'c', 'z', 'f', '7']
print(my_list_of_chars[-5:])
print(my_list_of_chars[1:])
# elements beginning to end
print(my_list_of_chars[:])
