"""
New types were introduced in python3.8:

- Liberal type
- Union
- Final
- Typed dictionaries
- Protocols

This types help us with type hinting. Remember: python is and always will be a dynamically typed language. Types hints \
are only hints for developers. Those hints can help when running the conde with MyPy.
"""
from typing import Literal


# Literal type:
def compute_v1(math_operation: str, num1: int, num2: int) -> int:
    if math_operation == '+':
        return num1 + num2
    elif math_operation == '-':
        return num1 - num2
    else:
        raise ValueError(f'Invalid operation {math_operation!r}')


# Only the first two will work
print(compute_v1('+', 6, 4))
print(compute_v1('-', 10, 2))
# print(compute_v1('*', 5, 2))


def compute_v2(math_operation: Literal['+', '-'], num1: int, num2: int) -> int:
    if math_operation == '+':
        return num1 + num2
    elif math_operation == '-':
        return num1 - num2
    else:
        raise ValueError(f'Invalid operation {math_operation!r}')


# Only the first two will work
print(compute_v2('+', 6, 4))
print(compute_v2('-', 10, 2))
# print(compute_v2('*', 5, 2))


from typing import Union
# This module Union packs different types.


from typing import Final
# The module is used for defining constants.
NAME: Final = 'Geek'
NAME = 'University'  # this will accuse error when running with MyPy
print(NAME)

# We also have a decorator called final.
# With this decorator, no other Class should extend the marked Class.
from typing import final


@final
class Person:
    pass


class Student(Person):
    pass

    @final
    def study(self):
        print('I am studying.')


class Intern(Student):
    pass

    def study(self):
        print('Studying and interning ...')


# Typed Dictionaries
from typing import TypedDict

class PythonCourse(TypedDict):
    version: str
    update: int


geek = PythonCourse(version='3.8.5', update=2020)
print(geek)

another_course = PythonCourse(something='go', thing=True)
print(another_course)


# Protocols: related to duck typing.
# protocols define a class which is used to check the type of objects based on duck typing.
from typing import Protocol


class Course(Protocol):
    title: str

    def __init__(self):
        Course.title = ""

# ...