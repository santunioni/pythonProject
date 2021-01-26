"""
Polymorphism

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when \
a parent class reference is used to refer to a child class object. Any Java object that can pass more than one IS-A \
test is considered to be polymorphic.

When we implement a method in the child class which is present in the parent class, we are overriding the parent \
method. Overriding is the best representation of a polymorphism.
"""


class Animal(object):

    def __init__(self, name):
        self.__name = name

    def speak(self):
        raise NotImplementedError('The child classes need to implement this method.')

    def eat(self):
        return f'{self.__name} is eating.'


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f'{self._Animal__name} speaks: woof woof'


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f'{self._Animal__name} speaks: meow meow'


class Mouse(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self._Animal__name} doesn't speak."


# Testing
felix = Cat('Felix')
print(felix.eat())
print(felix.speak())

pluto = Dog('Pluto')
print(pluto.eat())
print(pluto.speak())

mikey = Mouse('Mikey')
print(mikey.speak())
print(mikey.eat())
