# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "21-may-2021"
__version__ = ""
__status__ = ""

"""
A few examples of Python dicts methods:
.clear(), 
.copy(), 
.fromkeys(), 
.get(), 
.items(), 
.keys(), 
.pop(key), 
.popitem(), 
.setdefault(), 
.update(key-elem), 
.values()
"""


from contextlib import suppress

my_dictionary_py = {
    'name': 'Guido',
    'surname': 'van Rossum',
    'year': 1991,
    'lang': 'Python',
}

my_dictionary_py_copy = my_dictionary_py.copy()

# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python'}
print(my_dictionary_py)
print(my_dictionary_py_copy)

my_dictionary_py_copy1 = dict(my_dictionary_py_copy)
my_dictionary_py_copy['year'] = 1990
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python'}
print(my_dictionary_py)
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1990, 'lang': 'Python'}
print(my_dictionary_py_copy)
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python'}
print(my_dictionary_py_copy1)

keys = 'a', 'b', 'c'
values = 1
my_dict_fromkeys = dict.fromkeys(keys, values)
# output: {'a': 1, 'b': 1, 'c': 1}
print(my_dict_fromkeys)
values = 1, 2, 3
my_dict_fromkeys1 = dict.fromkeys(keys, values)
# output: {'a': (1, 2, 3), 'b': (1, 2, 3), 'c': (1, 2, 3)}
print(my_dict_fromkeys1)
# default value is None
my_dict_fromkeys2 = dict.fromkeys(keys)
# output: {'a': None, 'b': None, 'c': None}
print(my_dict_fromkeys2)

# output: Guido
print(my_dictionary_py.get('name'))
# return a value if the specified key does not exist - default is None
# output: Guido
print(my_dictionary_py.get('lastname', 'Indefined'))

# returns a view object
# otput: dict_items([('name', 'Guido'), ('surname', 'van Rossum'), ('year', 1991), ('lang', 'Python')])
print(my_dictionary_py.items())
# for change values
my_items_mirror_py_copy = my_dictionary_py_copy.items()
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1990, 'lang': 'Python'}
print(my_dictionary_py_copy)
# output: dict_items([('name', 'Guido'), ('surname', 'van Rossum'), ('year', 1990), ('lang', 'Python')])
print(my_items_mirror_py_copy)
my_dictionary_py_copy['year'] = 1991
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python'}
print(my_dictionary_py_copy)
# output: dict_items([('name', 'Guido'), ('surname', 'van Rossum'), ('year', 1991), ('lang', 'Python')])
print(my_items_mirror_py_copy)

# same as .item() but for keys
print(my_dictionary_py.keys())
my_keys_mirror_py_copy = my_dictionary_py_copy.keys()
my_dictionary_py_copy['country'] = 'Netherlands'
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python', 'country': 'Netherlands'}
print(my_dictionary_py_copy)
# output: dict_keys(['name', 'surname', 'year', 'lang', 'country'])
print(my_keys_mirror_py_copy)

my_dictionary_py_copy.pop('country')
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'lang': 'Python'}
print(my_dictionary_py_copy)
# returns a value if key does not exist
# an error is raised if the value is not especified and the key is not found
# ERROR!
with suppress(KeyError):
    my_dictionary_py_copy.pop('country')
my_dictionary_py_copy.pop('country', False)

"""
The popitem() method removes the item that was last inserted into the dictionary. 
In versions before 3.7, the popitem() method removes a random item.
"""
my_dictionary_py_copy.popitem()
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991}
print(my_dictionary_py_copy)


##### setdafult

my_dictionary_py_copy.update({'country': 'Netherlands'})
# output: {'name': 'Guido', 'surname': 'van Rossum', 'year': 1991, 'country': 'Netherlands'}
print(my_dictionary_py_copy)

# same as .item() and .keys() but for values
print(my_dictionary_py.values())
my_values_mirror_py_copy = my_dictionary_py_copy.values()
my_dictionary_py_copy['surname'] = 'Van Rossum'
# output: dict_values(['Guido', 'Van Rossum', 1991, 'Netherlands'])
print(my_values_mirror_py_copy)
