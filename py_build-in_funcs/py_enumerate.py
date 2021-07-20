# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "15-jul-2021"
__version__ = ""
__status__ = ""

"""
The enumerate() function takes a collection and returns it as an enumerate object.
The enumerate() function adds a counter as the key of the enumerate object.
"""

x = enumerate(['C++', 'Python', 'PHP'])
# output: [(0, 'C++'), (1, 'Python'), (2, 'PHP')]
print(list(x))

l = ('Django', 'Flask', 'Laravel')
y = enumerate(l)
# output: [(0, 'Django'), (1, 'Flask'), (2, 'Laravel')]
print(list(y))

l1 = ['using', 'parameter', 'start', 'at', '4']
z = enumerate(l1, 4)
# output: [(4, 'using'), (5, 'parameter'), (6, 'start'), (7, 'at'), (8, '4')]
print(list(z))
