"""
Working with built-in modules

_________________________
|Python|Built-in modules|
-------------------------
"""

# Using alias (shortcuts) for functions
# from random import *  # IMPORT ALL FUNCTIONS FROM MODULE TO THE CURRENT PATH
from random import choice as choose_between, random as rdm

print(choose_between([1, 2]))
print(rdm())

# We use to put several imports from a given module as a tuple
from random import (
    choice,
    random,
    shuffle,
    choices,
    randint
)

print(choice([1, 2]))

import math
print(math.pi)
