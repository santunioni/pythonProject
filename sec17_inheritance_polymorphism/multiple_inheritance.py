"""
OOP - Multiple Inheritance

In Java, a class can have only one parent.

In Python, a single class can have multiple parents, inheriting all methods and attributes from all parent classes.

Multiple inheritance can be done two ways:
    - By direct multi derivation
    - By indirect multi derivation


# Example 1 - Direct Multiderivation
class Base1:
    pass
class Base2:
    pass
class MultiDerivation(Base1, Base2):
    pass
# Example 2 - Indirect Multiderivation
class Esab1:
    pass
class Esab2(Esab1):
    pass
class NoitaviredItlum(Esab2):
    pass


OBS: There is no difference between direct and indirect inheritance.
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


class Penguin(Land, Aquatic):

    def __init__(self, name):
        super().__init__(name)


# testing
baleia = Aquatic('Wally')
print(baleia.swing())
print(baleia.greet())

bear = Land('Xi Jinping')
print(bear.walk())
print(bear.greet())

tux = Penguin('Tux')
print(tux.swing())
print(tux.walk())
"""What greet() method will be penguin inherit? From the Land or from the Aquatic? When there are conflicting methods \
from parents we should decide which to choose. This is called Method Resolution Order. The penguin is inheriting the \
method from the first parent Class, which in this case is Aquatic."""
print(tux.greet())

print(f"Is Tux an instance of Penguin? {isinstance(tux, Penguin)}")
print(f"Is Tux an instance of Aquatic? {isinstance(tux, Aquatic)}")
print(f"Is Tux an instance of Land? {isinstance(tux, Land)}")
print(f"Is Tux an instance of Animal? {isinstance(tux, Animal)}")
print(f"Is Tux an object? {isinstance(tux, object)}")
