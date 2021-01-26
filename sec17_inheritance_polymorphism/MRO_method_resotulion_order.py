"""
MRO -> Method resolution order

MRO is the ordering of parents methods execution.

In Python, we can check the MRO in two ways:
    - By the class property __mro__
    - By the method mro()
    - By help()
"""


class Animal:

    def __init__(self, name):
        self.__name = name

    def sounds(self, sound):
        return f'The {self.__name} does {sound}'

    def greet(self):
        return f"Hello, I am {self.__name}"


class Aquatic(Animal):

    def __init__(self, name):
        super().__init__(name)

    def swing(self):
        return f"{self._Animal__name} is swimming."

    def greet(self):
        return f"I am {self._Animal__name} from the sea."


class Land(Animal):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return f"{self._Animal__name} is walking."

    def greet(self):
        return f"I am {self._Animal__name} from land."


class Penguin(Aquatic, Land):

    def __init__(self, name):
        super().__init__(name)


"""
Penguin(Aquatic, Land): I am Tux from the sea.

Penguin(Land, Aquatic): I am Tux from land.
"""
