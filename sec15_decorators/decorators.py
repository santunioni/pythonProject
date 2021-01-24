"""
Decorators

What are Decorators?
 - They are functions;
 - They wrap other functions and enhance their behaviour.
 - They are an example of Higher Order Functions;
 - They have own syntax, using '@' (Syntactic Sugar)


|-------------------------------------------------------|
|                  Function Decorator                   |
|                                                       |
|                                                       |
|           |--------------------------------|          |
|           |       Decorated Function       |          |
|           |--------------------------------|          |
|                                                       |
|-------------------------------------------------------|
"""


# Not recommended syntax: without Syntactic Sugar


def be_polite_decorator(function):
    def wrapper():
        print('It was a pleasure to meet you!')
        function()
        print('Have a good day!')

    return wrapper


def greetings():
    print('Welcome to Geek University')


# testing 1
decorated_greetings = be_polite_decorator(greetings)
print(decorated_greetings())

# the function be_polite_decorator() is a function decorator. It decorates the function greetings()
# the function greetings() is the function being decorated.

# we can also decorate the function greetings automatically by defining it as:
from functools import wraps


# this is a Decorator Function
def be_polite_decorator_2(function):
    # the wraps derogatory saves the function identity: __name__, __docstring__, etc...
    @wraps(function)
    def wrapper():
        print('It was a pleasure to meet you!')
        function()
        print('Have a good day!')

    return wrapper


# this function will be decorated
@be_polite_decorator_2  # this is a Decorator
def greetings_decorated():
    print('Welcome to Geek University')


print(greetings_decorated())
