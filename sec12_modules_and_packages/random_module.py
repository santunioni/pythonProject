"""
The random module: it is integrated to the python package.

- In Python, modules are another Python files, built by some other developer, that we can use to make our work more agile.
- Modules are built into packages, which can be shared between the Python community.

random module --> possesses several functions to work with random numbers generating.

BE CAREFUL: If you have a file in the directory you are importing some module, and the file have the same name as the \
module, Python will prefer to import your file instead of the module.
"""

# Importing the entire module, all functions, attributes, classes and properties are imported.
# You may want to import only the function or class you want to use. Import entire modules only
# if you known that the module is small. If you known exactly what functions you will use, import
# only the ones needed.
import random
print(random.random())

# importing a specific function from the module
from random import choice as choice
print(choice((1, 23, 42, 1, 6)))  # pseudo-random choice between the iterable options

from random import uniform as choose_between
print(choose_between(3, 10))  # pseudo-random in [3, 10)

from random import randint
print(randint(1, 10))  # pseudo-random number in [1, 11]

from random import shuffle
# this function will shuffle your data. example:
naipes = {'copas', 'ouros', 'espadas', 'paus'}
cartas = {*[str(number) for number in range(1, 11)], 'Valete', 'Dama', "Rei"}
baralho = [f'{carta} de {naipe}' for carta in cartas for naipe in naipes]
print("\nSeu baralho é: ", baralho)
shuffle(baralho)
print("\nSeu baralho embaralhado é: ", baralho)
