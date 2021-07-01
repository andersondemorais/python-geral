# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-may-2021"
__version__ = ""
__status__ = ""

"""
A few examples of Python set methods:
.add(element),
.clear(),
.copy(),
.discart(element),
.pop(),
.remove()
*
.union(),
.intersection(),
.difference(),
.symmetric_difference(),
.isubset(),
.issuperset(),
.isdisjoint(),
***
.join()
sum()
"""

my_set_of_integers = {1, 2, 3, 4, 5}
my_set_of_chars = {'a', 'b', 'c', 'x', 'y', 'z'}

my_set_of_integers.add(-3)
# output: {1, 2, 3, 4, 5, -3}
print(my_set_of_integers)

# does not raise an error if element not found
my_set_of_chars.discard('a')
print(my_set_of_chars)

# removes a random item from the set
# raises an error if set is empty
my_set_of_integers.pop()
# output:
print(my_set_of_integers)

my_set_of_chars.clear()
# output: set()
print(my_set_of_chars)

""" union(|), intersection(&), difference(-), symmetric_difference(^) """
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}

my_set3 = my_set1.union(my_set2)
my_set31 = my_set1 | my_set2
# output: {1, 2, 3, 4, 5}
print(my_set3)
print(my_set31)

my_set4 = my_set1.intersection(my_set2)
my_set41 = my_set1 & my_set2
# output: {3}
print(my_set4)
print(my_set41)

my_set5 = my_set1.difference(my_set2)
my_set51 = my_set1 - my_set2
# output: {1, 2}
print(my_set5)
print(my_set51)

my_set6 = my_set1.symmetric_difference(my_set2)
my_set61 = my_set1 ^ my_set2
# output: {1, 2, 4, 5}
print(my_set6)
print(my_set61)

# output: False
print(my_set1.issubset(my_set2))
# output: False
print(my_set1.issuperset(my_set2))
# returns True if two sets have a null intersection
# output: False
print(my_set1.isdisjoint(my_set2))

""" SUM """
my_set_of_integers_sum = {1, 2, 3, 4, 5}
# output: 15
print(sum(my_set_of_integers_sum))

""" JOIN """
my_set_of_chars = {'P', 'y', 't', 'h', 'o', 'n', '3', 'x'}
# output: o-t-n-h-3-x-P-y, n-3-y-h-t-x-P-o, ... unordered elements
print('-'.join(my_set_of_chars))
