# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "14-may-2021"
__version__ = ""
__status__ = ""

"""
Deleting lists/elements in Python
"""


from contextlib import suppress

my_list_of_chars = ['a', 'b', 'c', 'd', 'z', 'e', 'f']

del my_list_of_chars[4]
# output: ['a', 'b', 'c', 'd', 'e', 'f']
print(my_list_of_chars)

# delete multiple elements
del my_list_of_chars[1:4]
# output: ['a', 'e', 'f']
print(my_list_of_chars)

# delete the list
del my_list_of_chars
# ERROR! list is not defined
with suppress(NameError):
    print(my_list_of_chars)

""" Remove and Pop """
my_list_of_chars = ['a', 'b', 'c', 'd', 'z', 'e', 'f']

# remove the given item
my_list_of_chars.remove('a')
# output: ['b', 'c', 'd', 'z', 'e', 'f']
print(my_list_of_chars)
# if teh item does not exist, throws an exception
with suppress(ValueError):
    my_list_of_chars.remove('u')

# pop() method removes and returns the last item if the index is not provided
my_list_of_chars.pop(3)
# output: ['b', 'c', 'd', 'e', 'f']
print(my_list_of_chars)
my_list_of_chars.pop()
# output: ['b', 'c', 'd', 'e']
print(my_list_of_chars)

""" Clear """
# to empty a list
my_list_of_chars.clear()
# output = []
print(my_list_of_chars)

""" other ways """
my_list_of_chars = ['a', 'b', 'c', 'd', 'z', 'e', 'f']

# delete a slice of the list
my_list_of_chars[2:5] = []
# output: ['a', 'b', 'e', 'f']
print(my_list_of_chars)

# to empty a list
my_list_of_chars = []
# output: []
print(my_list_of_chars)
