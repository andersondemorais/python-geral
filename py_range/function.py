# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "21-may-2021"
__version__ = ""
__status__ = ""

"""
Creating ranges in Python:
RANGE: inmutable, sequence, subscriptable
variable = range(1,10)
range(ST, E, SP) -> STart(number to start the counter), 
End(number(not included) to end the counter), 
SteP(skips during counting - optional)
"""


from random import randint

my_range1 = range(1, 5)
# output: range(1, 5)
print(my_range1)

my_range2 = range(50, 60, 2)
# output: range(50, 60, 2)
print(my_range2)

""" 
Accessing elements
"""
# output: 3
print(my_range1[2])
# output: 54
print(my_range2[2])

my_sum_range1 = 0
for _ in my_range1:
    my_sum_range1 += _
# output: 10
print(my_sum_range1)

my_sum_range2 = 0
for _ in my_range2:
    my_sum_range2 += _
# output: 270
print(my_sum_range2)

my_sum = 0
for _ in range(-5, 17):
    my_sum += _
# output: 121
print(my_sum)

my_sum = 0
for _ in range(-28, 275, 4):
    my_sum += _
# output: 9272
print(my_sum)

rand_num = randint(1, 10)
if rand_num in my_range1:
    print(rand_num)
