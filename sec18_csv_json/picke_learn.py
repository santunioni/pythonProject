"""
Knowing Pickle

The Piclke module task is to perform the following processes:
    - Binarization -> Python Object
    - Python Object -> Binarization

These processes are called serialization/deserialization, respectively.

OBS: The Pickle module isn't safe against malicious data. Therefore we must only work with private Pickle files.

"""

import pickle


class Animal:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def eat(self):
        print(f"{self.__name} is eating...")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(f"{self.name}, the cat: meow meow meow ... ")


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name}, the cat: woof woof woof ... ")


# Writing pickle files:
# felix = Cat('Felix')
# pluto = Dog('Pluto')
# with open('animals.pickle', 'wb') as file:
#    pickle.dump((felix, pluto), file)

# Reading pickle files:
with open('animals.pickle', 'rb') as file:
    (cat, dog) = pickle.load(file)

    print(f"The cat is called {cat.name}")
    cat.meow()
    print(f"The cat type is {type(cat)}")
    print(f"The dog is called {dog.name}")
    dog.bark()
    print(f"The dog type is {type(dog)}")
