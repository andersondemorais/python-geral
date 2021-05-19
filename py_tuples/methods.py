# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "19-may-2021"
__version__ = ""
__status__ = ""

"""
A few examples of Python list methods:
.count(element),
.index(element)
***
.join()
sum()
"""


from contextlib import suppress

my_tuple_of_chars = ('a', 'b', 'c', 'd', 'e', 'f', 'f', 'f', 'g', 'z')
# output: 3
print(my_tuple_of_chars.count('f'))

# returns the index of the first element
# output: 5
print(my_tuple_of_chars.index('f'))

# ERROR! value is not in list
with suppress(ValueError):
    print(my_tuple_of_chars.index('ff'))

""" unpacking tuple """
number1, number2 = (10, 20)
# output: 10
print(number1)
# output: 20
print(number2)
number1, number2 = 33, 77
# output: 33
print(number1)
# output: 77
print(number2)
number1, number2 = number2, number1
# output: 77
print(number1)
# output: 33
print(number2)

number1, number3, *other = (192, 210, 100, 0.5)
# output: 192
print(number1)
# output: 210
print(number3)
# output: [100, 0.5]
print(other)

# it can only use the * operator once on the left-hand side
# ERROR! two starred expressions in assignment
# number1, number2, *number3, *number4 = (192, 210, 100, 0.5)

""" merging tuples """
my_tuple_1 = ('a', 'b', 'c')
my_tuple_2 = ('x', 'y', 'z')
my_tuple_3 = (*my_tuple_2, *my_tuple_1)
# output: ('x', 'y', 'z', 'a', 'b', 'c')
print(my_tuple_3)

""" ZIP """
my_tuple_1 = ('a', 'b', 'c')
my_tuple_2 = (1, 2, 3)
my_tuple_3 = (True, True, False)
my_tuple_of_chars_zip = tuple(zip(my_tuple_1, my_tuple_2, my_tuple_3))
# output: (('a', 1, True), ('b', 2, True), ('c', 3, False))
print(my_tuple_of_chars_zip)

""" SUM """
# output: 6
print(sum(my_tuple_2))

""" JOIN """
# output: a\b\c
print('\\'.join(my_tuple_1))
