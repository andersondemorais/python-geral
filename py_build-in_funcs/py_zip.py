# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "15-jul-2021"
__version__ = ""
__status__ = ""

"""
The zip() function returns a zip object, which is an iterator of tuples 
where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, 
the iterator with the least items decides the length of the new iterator.
"""

x = zip(['A', 'B', 'C', 'D'], [1, 2, 3, 4])
# output: [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
print(list(x))

l1 = ['X', 'Y', 'W', 'Z']
l2 = [6, 7, 8, 9]
y = zip(l1, l2)
# output: [('X', 6), ('Y', 7), ('W', 8), ('Z', 9)]
print(list(y))

z = zip((1, 2, 3, 4, 5), (6, 7, 8, 9))
# output: [(1, 6), (2, 7), (3, 8), (4, 9)]
print(list(z))
