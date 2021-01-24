"""
Higher Order Functions (HOF)

What does HOF means?
 - When a programming language supports HOF, it's possible that a function can return another function. We can also \
 functions as arguments to pass to another functions. Also, we can define variables receiving functions.

In Python, the functions are First Class Citizen (FCC)
"""


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    return a/b


# the next line defines a Higher Order Function (HOF)
def calcular(a, b, operation):
    return operation(a, b)


print(calcular(2, 3, somar))
print(calcular(2, 3, diminuir))
print(calcular(2, 3, multiplicar))
print(calcular(2, 3, dividir))


print("""
We will now study nested functions (funções aninhadas)
 - Nested lists were analogous to matrices.
 - Nested functions are functions inside functions.
 """)
from random import choice


def cumprimento(pessoa):
    # This is a nested function
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa.title()


print(cumprimento('vinicius'))


def make_me_laugh():
    # The next line is a inner function
    def laugh():
        return choice(['hahahahahahah', 'kkkkkkkkkkkk', 'yayayayayaya', 'poskpokspooks', 'aeiaoaeioaeio'])
    # I am returning the laugh() function, not the laugh
    return laugh

laugh = make_me_laugh()
print(laugh())
