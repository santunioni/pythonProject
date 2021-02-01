"""
Duck typing:
It's related to Python dynamic typing.

The variable type is less important that the methods defining it.
"""


class CisneNegro:

    def __len__(self):
        return 42


book = CisneNegro()
print(len(book))

# The len methods works for all three variables below:
nome = 'Geek University'
lista = [12, 34, 55, 49]
dicio = {"carlos": 12, "vanessa": 34, "joana": 49}
# Therefore those objects are similar in some way: they are all containers
# This define duck-typing, if an object walks, swings and 'fly' like a duck, probably it's is a duck.

print(len(nome))
print(len(lista))
print(len(dicio))

# The next variables doesn't have len method, therefore they are different.
idade = 42
peso = 81.4

print(len(idade))
