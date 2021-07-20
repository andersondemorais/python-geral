# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "20-jul-2021"
__version__ = ""
__status__ = ""

"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""

""" In Python a function is defined using the def keyword """


def my_function():
    print("Hello from a function")


""" 
In Python, functions are first-class objects. 
The functions can be passed around and used as arguments, 
just like any other object (string, int, float, list, and so on). 
"""


def hello(name):
    return f"Hello {name}"


def welcome(name):
    return f"Welcome to Python, {name}!"


def say_somethin(call_it):
    return call_it("Elvis")


print(hello('Joe'))
print(welcome('Joe'))

print(say_somethin(hello))
print(say_somethin(welcome))

""" Inner functions - functions inside other functions """


def parent():
    print("parent() function")

    def first_child():
        print("first_child() function")

    def second_child():
        print("second_child() function")

    second_child()
    first_child()


parent()

""" Returning functions from functions """


def parent(number):
    def first_child():
        return "First child"

    def second_child():
        return "Second child"

    def oldest_child():
        return "Oldest child"

    if number == 1:
        return first_child()
    elif number == 2:
        return second_child()
    else:
        # without parentheses
        # returning a reference to the function
        return oldest_child


print(parent(1))
print(parent(2))
print(parent(5))
