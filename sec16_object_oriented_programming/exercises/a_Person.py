class Person:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def height(self):
        return self.__height

    @age.setter
    def age(self, age):
        self.__age = age

    @height.setter
    def height(self, height):
        self.__height = height

    def data(self):
        return f"name: {self.__name}, age: {self.__age}, height: {self.__height}"


myself = Person('Vinicius Vargas', 24, 1.78)
myself.age += 1
print(myself.data())
