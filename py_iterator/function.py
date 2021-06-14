# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__copyright__ = "Copyright 2021"
__email__ = ""
__date__ = "14-jun-2021"
__version__ = ""
__status__ = ""

"""
Iterator: an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__()

Some useful built-in functions that accept iterables as arguments:
- list, tuple, dict, set: construct a list, tuple, dictionary, or set, respectively, from the contents of an iterable
- sum: sum the contents of an iterable.
- sorted: return a list of the sorted contents of an interable
- any: returns True and ends the iteration immediately if bool(item) was True for any item in the iterable.
- all: returns True only if bool(item) was True for all items in the iterable.
- max: return the largest value in an iterable.
- min: return the smallest value in an iterable.
The __iter__() method returns the iterator object itself. 
Use the next() function to manually iterate through all the items of an iterator.
"""

from contextlib import suppress

my_tuple = ('Python', 'PHP', 'C', 'C++', 'Lisp')
myit = iter(my_tuple)

# output: Python
print(myit.__next__())
# output: PHP
print(next(myit))
# output: C
print(next(myit))
# output: C++
print(myit.__next__())
# output: Lisp
print(next(myit))

# ERROR! end of iterator
with suppress(StopIteration):
    print(next(myit))

my_string = 'Django'
myit = iter(my_string)

# output: D
print(next(myit))
# output: j
print(next(myit))
# output: a
print(next(myit))
# output: n
print(next(myit))
# output: g
print(next(myit))
# output: o
print(next(myit))

""" looping through an iterator """
my_tuple = ('Network', 'Link', 'Internet', 'Transport', 'Application')
my_string = '127.0.0.1'

for i in my_tuple:
    print(i)
for i in my_string:
    print(i)

myit = my_tuple.__iter__()
while True:
    try:
        print(next(myit), end='')
    except StopIteration:
        print()
        break
    else:
        print(end=' - ')
