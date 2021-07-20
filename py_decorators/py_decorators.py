# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "15-jul-2021"
__version__ = ""
__status__ = ""

"""
Simple decorator
"""


def decorator_d(func):
    def wrap():
        print('Before call function')
        func()
        print('After call function')

    return wrap


def say_hello():
    print('Hello Python')


my_dec = decorator_d(say_hello)
my_dec()

""" Syntactic Sugar - pie syntax """
# The following example does the exact same thing as the first decorator


def decorator_d1(func):
    def wrap():
        print('Before call function')
        func()
        print('After call function')

    return wrap


@decorator_d1
def say_hello1():
    print('Hello Python')


say_hello1()
