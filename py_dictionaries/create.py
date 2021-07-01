# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "21-may-2021"
__version__ = ""
__status__ = ""

"""
Creating dictionaries in Python:
DICTIONARY: mutable, indexed, subscriptable, unordered, unique key(does not allow repeated key)
variable = {'key1': elem1, 'key2': elem2, 'key3': elem3, ...}
constructor: variable = dict(key1 = elem1, key2 = elem2, key3 = elem3, ...) -> key is declared as a var
"""


from contextlib import suppress

my_dictionay_default_mode = {'a': 'aaa'}
my_dictionay_with_constructor = dict(a='aaa')

my_dictionary_py = {
    'name': 'Guido',
    'surname': 'van Rossum',
    'year': 1991,
    'lang': 'Python',
}
my_dictionary_c = dict(
    name='Dennis',
    surname='Ritchie',
    year=1972,
    lang='C',
)

# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python'}
print(my_dictionary_py)
# output: {'name': 'Dennis', 'surname': 'Ritchie', 'year': 1972, 'lang': 'C'}
print(my_dictionary_c)

# dictionaries can also have another dictionary as an item
my_dictionary_langs = {
    'lang_c': my_dictionary_c,
    'lang_py': my_dictionary_py,
    'lang_cpp': {
        'name': 'Bjarne',
        'surname': 'Stroustrup',
        'year': 1979,
        'lang': 'CPP',
    },
    'lang_php': {
        'name': 'Rasmus',
        'surname': 'Lerdorf',
        'year': 1995,
        'lang': 'PHP',
    },
}

# output:
# {'lang_c': {'name': 'Dennis', 'surname': 'Ritchie', 'year': 1972, 'lang': 'C'}, 'lang_py': {...
print(my_dictionary_langs)


""" 
Accessing elements
"""
# output: 1991
print(my_dictionary_py['year'])
# output: {'name': 'Rasmus', 'surname': 'Lerdorf', 'year': 1995, 'lang': 'PHP'}
print(my_dictionary_langs['lang_php'])
# output: Stroustrup
print(my_dictionary_langs['lang_cpp']['surname'])

# ERROR! keys do n0t exist
with suppress(KeyError):
    print(my_dictionary_langs[0])
    print(my_dictionary_langs[1])
