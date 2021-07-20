# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "15-jul-2021"
__version__ = ""
__status__ = ""

"""
The map() function executes a specified function for each item in an iterable. 
The item is sent to the function as a parameter.
"""

x = map(lambda a: a * a, [1, 2, 3, 4, 5])
# output: [1, 4, 9, 16, 25]
print(list(x))


def sqr_f(a):
    return a * a


l = [6, 7, 8, 9, 10]
y = map(sqr_f, l)
# output: [36, 49, 64, 81, 100]
print(list(y))
