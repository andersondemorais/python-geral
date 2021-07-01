# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "14-jun-2021"
__version__ = ""
__status__ = ""

"""
Iterator: an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__()
"""


class Factorial:
    """class to implement an iterator of factorial numbers"""

    def __init__(self, max_number=0):
        self.max_number = max_number + 1

    def __iter__(self):
        self.number = 0
        self.result = 0
        return self

    def __next__(self):
        if self.number <= self.max_number:
            if self.number == 0:
                self.result = 1
            else:
                self.result *= self.number
            self.number += 1
            return self.result
        else:
            raise StopIteration


factorial = Factorial(15)
myit = iter(factorial)

for n, i in enumerate(myit):
    print('Factorial of {}: {}'.format(n, i))


class Factorial_1:
    """class to implement an iterator of factorial numbers"""

    def __init__(self, max_number=0):
        self.max_number = max_number

    def __iter__(self):
        self.result = 1

        for number in range(0, self.max_number + 2):
            if number == 0:
                self.result = 1
            else:
                self.result *= number
            yield self.result


factorial_1 = Factorial_1(5)
myit_1 = iter(factorial_1)

for n, i in enumerate(myit_1):
    print('Factorial of {}: {}'.format(n, i))
