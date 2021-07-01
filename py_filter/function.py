# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "21-may-2021"
__version__ = ""
__status__ = ""

"""
filter
"""


from random import randint


def even(number: int):
    return number % 2 == 0


def lt_zero(number: int):
    return number > 0


even_numbers = filter(even, range(1, 100))
print(list(even_numbers))

lt_zero_numbers = filter(lt_zero, [randint(-50, 50) for x in range(20)])
print(list(lt_zero_numbers))

sqrt_numbers = map(lambda x: 2 ** x, filter(even, range(1, 20)))
print(list(sqrt_numbers))
