# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-may-2021"
__version__ = ""
__status__ = ""

"""
A few examples of Python using frozenset:
The frozenset() function returns an immutable frozenset object initialized 
with elements from the given iterable
Frozen sets can be used as keys in dictionary or as elements of another set

Methods:
.copy(), 
.difference(), 
.intersection(),.
symmetric_difference(),
.and(),
.union()
"""


from contextlib import suppress

# inicializing a frozenset
my_frozenset = frozenset([1, 2, 3, 4])

my_set_vowels = {'a', 'e', 'i', 'o', 'u'}
my_frozen_vowels = frozenset(my_set_vowels)

# output: {'o', 'e', 'u', 'i', 'a'}
print(my_set_vowels)
# output: frozenset({'o', 'a', 'e', 'u', 'i'})
print(my_frozen_vowels)

# ERROR! 'frozenset' object has no attribute 'add'
with suppress(AttributeError):
    my_frozen_vowels.add('z')

""" forzenset for dictionary """
my_dictionary = {'name': 'Guido', 'year': 1991, 'lang': 'Python'}
my_frozen_dict = frozenset(my_dictionary)

# output: frozenset({'year', 'lang', 'name'})
print(my_frozen_dict)
