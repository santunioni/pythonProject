"""
Function documentation with docstrings: docstrings are strings like this one.

The docstring after defining a function() will appear when calling help(function)

OBS: We can get a function documentation with the property .__doc__

"""


import math


print(help(print))


def say_hello(optional_arg=True):
    """This a simple function that says Hello! in your console."""
    return 'Hello!'


def exponential(x, base=math.e):
    """This is a function that returns the number base to the power x
    :param x: Numeric type parameter that will be the power
    :param base: Numeric type parameter that will be the base. If not provided then base=EulerNumber
    :return: The result of base**x
    """
    if base == math.e:
        return math.exp(x)
    return base**x


say_hello_docstring = say_hello.__doc__
print("_________________________________________\n \
The say_hello() function docstring: ")
print(say_hello_docstring)
