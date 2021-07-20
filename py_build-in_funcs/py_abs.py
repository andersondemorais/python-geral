# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "15-jul-2021"
__version__ = ""
__status__ = ""

"""
The abs() function returns the absolute value of the specified number.
Complex number: Python uses the symbol 1j for √-1 rather than the symbol i.
"""

x = abs(-12)
# output: 12
print(x)
y = abs(4 + 2j)
# output: 4.47213595499958
print(y)
# output: 2.0
print(abs(2j))
# output: 1.0
print(abs(1j))
