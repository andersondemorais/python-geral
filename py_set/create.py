# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-may-2021"
__version__ = ""
__status__ = ""

"""
Creating sets in Python: unordered collection of unique elements
SET: mutable, unordered, *NOT subscriptable, unique(does *NOT allow equal elem - duplicate)
variable = {elem1, elem2, elem3, ..., elemN}
constructor: variable = set((elem1, elem2, elem3, ..., elemN))
"""


from contextlib import suppress

my_set_default_mode = {}
my_set_with_constructor = set(())

# set of the same type
my_set_of_integers = {1, 2, 3, 4, 5}
my_set_of_chars = {'a', 'b', 'c', 'z', 'f', '7'}
my_set_of_strings = {'Python', 'Django', 'Flask', 'PHP'}

# sets can have mixed data
my_set_mixed = {1, 'a', 'x', True}

# sets can not have another set, t-l-d as an item
# ERROR! unhashable type: 'set'
with suppress(TypeError):
    my_set_nested = {1.5, {'a', 'b', 'c'}, -300}

""" remove duplicates in lists """
my_list_of_chars = ['a', 'b', 'c', 'a', 'f', 7]
my_set_of_chars = set(my_list_of_chars)

# output: ['a', 'b', 'c', 'a', 'f', 7]
print(my_list_of_chars)
# output: {'f', 'a', 7, 'c', 'b'}
print(my_set_of_chars)
