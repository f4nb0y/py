# Imports
from os import getcwd
import numpy as np
from matplotlib.pyplot import plot as plt
from time import *

# Built-ins
bytes
float
int
list
map
object
str
tuple

# Classes
class Hello:
    def __init__(self, x):
        self.name = x

    def selfprint(self):
        print("hello my name is ", self.name)

    def testprint(self):
        print(1*2, 2+3, 4 % 5, 8-4, 9/4, 23//4)

# Decorators
class Decorators:
    @classmethod
    def decoratorsTest(self):
        pass

# Lists
a = [1, 2, 3, 4, 5]
a.sort()
print(a[1:3])
print(a[:4])
print(a[2])
print(a[2:])

# Dicts
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Strings
'single-quote'
"double-quote"
"""triple double-quote"""
'''triple single-quote'''
r'raw'
'escape\n'
'\04'  # octal
'\xFF'  # hex
'\u1111'  # unicode character

# Numbers
1  # Integral
1L
1.0  # Float
.1
1+2j  # Complex

# Singletons
True
False
None

# Lambda
def x2(n):
    lambda n: n/7

# If / Else
if 1 > 2:
    print("yes")
elif 4 > 5:
    print("maybe")
else:
    print("no")

# Loops
i = 5
while(i > 0):
    print(i)
    i -= 1

for x in range(1, 20, 2):
    print(x)

# Exceptions
raise SyntaxError
