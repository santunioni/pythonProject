"""
Defining functions:

- Functions are small pieces of code which perform specific
tasks.
- A function may receive entries, but not necessarily.

OBS: if you are writing very complex and lengthy functions, your code is ugly, unreadable and perhaps
unmaintainable. Try to reformulate your code looking for simpler and smaller functions.

Why to create functions? DRY - Don't repeat yourself
"""
import math


def function(parameter_1,  # first argument
             parameter_2,  # second argument
             optional='default_value'  # default arguments (always last)
             ):
    # returning is optional. Functions without
    # return always return None
    return parameter_1 + parameter_2 + optional


# Naming parameters
def name_complete(first_name, last_name):
    return f'Your complete name is {first_name} {last_name}'


print(name_complete('Vinicius', 'Vargas'))


# The difference between parameters and arguments:
# - Parameters are variables declared in the function definition.
# - Arguments are data passed to the function for execution.
def useless_function(parameter_1, parameter_2):
    return f'{parameter_1} + {parameter_2}'


useless_function(parameter_2='argument_2', parameter_1='argument_1')


def exp_function(x, base=math.e):
    if base != math.e:
        return base ** x
    return math.exp(x)


print(exp_function(1, base=10.0))


# functions can be passed as parameters to other functions
def summation(number_1, number_2):
    return number_1 + number_2


def subtraction(number_1, number_2):
    return number_1 - number_2


def multiplication(number_1, number_2):
    return number_1 * number_2


def operation(number_1, number_2, func=multiplication):
    return func(number_1, number_2)


print(operation(4, 4, summation))

# Scope
global_variable_1 = "I am the first global variable. "
global_variable_2 = "I am the second global variable. "
print("\nText inside the function: ")


def check_scope(change=False):
    global global_variable_1

    global_variable_1 = "I, the first, changed inside the function. "
    global_variable_2 = "I, the second, changed inside the function. "
    global_variable_3 = "I am a third variable initialized inside the function."

    def inside_function():
        # nonlocal variables are one level up variables
        nonlocal global_variable_3
        global_variable_3 = "I, the third, changed inside the second-level function. "

    if change:
        inside_function()

    print(global_variable_1 + global_variable_2 + global_variable_3)


check_scope(change=False)
print("\nText outside the function: ")
print(global_variable_1 + global_variable_2)
