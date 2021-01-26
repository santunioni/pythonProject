"""
OOP - The super() method

The method super() refers to super Class (also called Mother, Father or Parent)
"""


class Animal:

    def __init__(self, name, species):
        self.__name = name
        self.__species = name

    def sounds(self, sound):
        print(f'The {self.__name} does {sound}')


class Cat(Animal):
    """This is not the recommended way to create inheritance"""
    def __init__(self, name, species, race):
        Animal.__init__(self, name, species)
        self.__race = race


class Monkey(Animal):
    """This is the recommended way to create inheritance"""
    def __init__(self, name, species, race):
        super().__init__(name, species)
        self.__race = race


felix = Cat('Felix', 'Feline', 'Angorá')
felix.sounds('meow')
