"""
POO - Inheritance

The Inheritance idea is to reuse code and also to extend our classes.

OBS: with inheritance we can create other classes (the kids) from existing classes (the parents).

Imagine we have two entities:

Client:
    - name
    - last_name
    - ssn
    - income

Employee:
    - name
    - last_name
    - ssn
    - registry

OBS: when a Class (child) inherit from Class (parent), the child inherit every methods and attributes from the parent.
The parent Class is known as:
    - Super Class  --> super()
    - Mother Class
    - Father Class
    - Parent Class
    - Base Class
    - Generic Class
The child Class is known as:
    - Sub Class
    - Child Class
    - Specific Class


"""


# class Client:
#
#     def __init__(self, name, last_name, ssn, income):
#         self.__name = name
#         self.__last_name = last_name
#         self.__ssn = ssn
#         self.__income = income
#
#     def full_name(self):
#         return f'{self.__name} {self.__last_name}'
#
#
# class Employee:
#
#     def __init__(self, name, last_name, ssn, registry):
#         self.__name = name
#         self.__last_name = last_name
#         self.__ssn = ssn
#         self.__registry = registry
#
#     def full_name(self):
#         return f'{self.__name} {self.__last_name}'
#
#
# client_angelina = Client('Angelina', 'Jolie', '123.123.12', 5000)
# employee_felicity = Client('Felicity', 'Jones', '654.654.80', 1234)
#
# print(client_angelina.full_name())
# print(employee_felicity.full_name())

print("""Repeating the same attributes for two nearly identical Classes is wast of time coding. WWe can use \
inheritances to create another Class from the parent class, inheriting the methods and attributes.
When different Classes are repeating code, we should ask: is there any entity general enough that encapsulates the \
attributes and methods common to those Classes? """)


class Person:

    def __init__(self, name, last_name, ssn):
        self.__name = name
        self.__last_name = last_name
        self.__ssn = ssn

    def full_name(self):
        return f'{self.__name} {self.__last_name}'


print("Now comes inheritance, by saying to the following Classes they are both person:")


class Client(Person):

    def __init__(self, name, last_name, ssn, income):
        """This class will inherit the attributes name, last_name and assn from the Class person. We use the \
        constructor method Person.__init__ to access the class Person constructor. The specific attributes come last \
        as parameter. However, it's more common to use the super().__init__ function instead of calling the parent \
        Class by it's name. """
        Person.__init__(self, name, last_name, ssn)
        self.__income = income


class Employee(Person):

    def __init__(self, name, last_name, ssn, registry):
        """This class will inherit the attributes name, last_name and assn from the Class person. We use the function \
        super() to access the class Person constructor. The specific attributes come last as parameter."""
        super().__init__(name, last_name, ssn)
        self.__registry = registry

    def full_name(self):
        """OOP - Overriding Classes
        The ability of a subclass to override a method allows a class to inherit from a superclass whose behavior is \
        "close enough" and then to modify behavior as needed. The overriding method has the same name, number and type of \
        parameters, and return type as the method that it overrides."""
        return f"Employee: {self.__registry} | Name: {self._Person__name}"


client_angelina = Client('Angelina', 'Jolie', '123.123.12', 5000)
employee_felicity = Employee('Felicity', 'Jones', '654.654.80', 1234)

print(client_angelina.full_name())
print(employee_felicity.full_name())

print(client_angelina.__dict__)
print(employee_felicity.__dict__)

print(help(Employee.full_name))
