"""
# Correto

texto: str

# Incorreto
texto:str
texto : str

# Correto
) -> str
)->str
) ->str

# Correto
alinhamento: bool = True

# Incorreto
alinhamento:bool=True
alinhamento : bool = True
alinhamento : bool=True
alinhamento: bool= True
"""

import math


def circle_perimeter(raio: float) -> float:
    return 2 * math.pi * raio


print("The function circle_perimeter annotation is: ", circle_perimeter.__annotations__, end="\n\n")


# More examples: Specifying parameter types
nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print(nome)
print(peso)
print(ativo)
print("")

print("Current annotations: ", __annotations__, end="\n\n")


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Geek University', idade=37, peso=69.5)
print("An object from Class Pessoa have the dictionary: ", p.__dict__, end="\n\n")

# Classes don't have annotations
# print(p.__annotations__)

print("The method andar of the object from Pessoas have dict: ", p.andar.__annotations__, end="\n\n")

print("The constructor method of the object from Pessoa have annotations: ", p.__init__.__annotations__)
