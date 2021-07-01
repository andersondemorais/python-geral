# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "19-may-2021"
__version__ = ""
__status__ = ""

"""
Creating tuples in Python
TUPLE: inmutable, sequence, indexed, subscriptable, multiple(allows equal elem - duplicate)
variable = (elem1, elem2, elem3, ..., elemN)
constructor: variable = tuple((elem1, elem2, elem3, ..., elemN))
"""


from contextlib import suppress

my_tuple_defaul_mode = ()
my_tuple_with_constructor = tuple(())

# tuple of the same type
my_tuple_of_integers = (1, 2, 3, 4, 5)
my_tuple_of_chars = ('a', 'b', 'c', 'z', 'f', '7')
my_tuple_of_strings = ('Python', 'Django', 'Flask', 'PHP')

# tuples can have mixed data
my_tuple_mixed = (1, 'a', 'x', True)

# tuples can also have another tuple as an item
my_tuple_nested = (1.5, ('a', 'b', 'c'), -300)

""" 
Accessing elements
"""
# output: Python
print(my_tuple_of_strings[0])
# output: Django
print(my_tuple_of_strings[1])
# output: Flask
print(my_tuple_of_strings[2])
# output: PHP
print(my_tuple_of_strings[3])

# Nested tuple
# output: 1.5
print(my_tuple_nested[0])
# output: b
print(my_tuple_nested[1][1])
# output: -300
print(my_tuple_nested[2])

# ERROR! tuple indices must be integers or slices, not float
with suppress(TypeError):
    print(my_tuple_nested[1.5])

""" Negative indices """
# tuple my_tuple_of_chars: lenght = 6 -> 6 elements
#  0  |  1  |  2  |  3  |  4  |  5
# 'a' | 'b' | 'c' | 'z' | 'f' | '7'
# -6  | -5  | -4  | -3  | -2  | -1

# output: b
print(my_tuple_of_chars[-5])

# indices between the elements
#  0  |  1  |  2  |  3  |  4  |  5  |
#  | 'a' | 'b' | 'c' | 'z' | 'f' | '7'
# -6  | -5  | -4  | -3  | -2  | -1  |

# elements 2nd to 4th - output: ['b', 'c', 'z']
print(my_tuple_of_chars[1:4])
# elements begining to 4th - output: ['a', 'b', 'c', 'z']
print(my_tuple_of_chars[:-2])
print(my_tuple_of_chars[:4])
# elements 2nd to end - output: ['b', 'c', 'z', 'f', '7']
print(my_tuple_of_chars[-5:])
print(my_tuple_of_chars[1:])
# elements beginning to end
print(my_tuple_of_chars[:])

""" STEPS """
# : is called slicing and has the format [start:end:step]
# elements beginning to end - only every 2-nd element
# output: ['a', 'c', 'f']
print(my_tuple_of_chars[::2])
