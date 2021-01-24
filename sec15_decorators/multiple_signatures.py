"""
Decorators with different signatures

A function signature is represented by it's return, name and entry parameters.
"""


# remembering

# this is a decorator function
def yel(function):
    """The parameter name will be imported automatically when this function is called \
    as a decorator. """

    def raise_volume(name):
        return function(name).upper()

    return raise_volume


# this function will be decorated
@yel
# this is a decorator that instead of executing greetings,
# execute yel, with greetings as parameter
def greetings(name):
    return f"Hello, I am {name}"


# This function will be decorated
@yel
# This is a decorator that instead of executing demand,
# execute yel, with demand as parameter
def demand(main_course, side_dish):
    return f"Hello, I'd like a {main_course} with {side_dish}, please."


# This function will bug the code when called because it needs two parameters
# but the function decorating it receives functions with only one parameter.


print(greetings('Angelina'))

# The next line will break the code because the decorator function accept only one parameter.
# print(demand('filet steak', 'french fries'))

print("""
To solve the problema of multiple arguments going to a decorator function that \
accepts only one argument, we usa a software design patter called Decorator Patter. \
In this case we use the *args and **kwargs arguments to the decorator function. \
Therefore let's change the function yel: """)


# this is a decorator function
def yel_decorator_patter(function):
    def raise_volume(*args, **kwargs):
        return function(*args, **kwargs).upper()

    return raise_volume


# This function will be decorated
@yel_decorator_patter
# This is a decorator that instead of executing demand,
# execute yel, with demand as parameter
def demand_decorator_patter(main_course, side_dish):
    return f"Hello, I'd like a {main_course} with {side_dish}, please."


# This function will bug the code when called because it needs two parameters
# but the function decorating it receives functions with only one parameter.


print(demand_decorator_patter('filet steak', 'french fries'))

# We can also have decorator with arguments (they need an entry parameter)


# decorator function:
def verify_first_argument(value_to_verify):
    """This is a decorator that will receive a value to be a function and a value \
    to be verified. If the function have the first argument equals the verified value, \
    the decorator will return the function itself. If the first argument is different \
    to the verified value, the decorator will print a message saying to choose the right value."""

    def receive_the_function(function):
        """When the function is passed as parameters, it's arguments are waiting to be assigned \
        to an intern function, where in this case they are automatically  stored as the *args and \
        **kwargs variables because the function check_the_argument_received assigns them this way
        """

        @wraps(function)  # this decorator will preserve the function metadata
        def check_the_argument_received(*args, **kwargs):
            if args and args[0] != value_to_verify:
                return f'Incorrect value! First argument needs to be {value_to_verify}'
            else:
                return function(*args, **kwargs)

        return check_the_argument_received

    return receive_the_function


@verify_first_argument('pizza')
def favorite_food(*args):
    print(args)


# We are forcing the first argument of the next function to be 10
# In case it's not 10, the message inside the decorator function
# will be returned.
@verify_first_argument(10)
def soma_10(num1, num2):
    return num1 + num2


print(favorite_food('rice', 'hamburger', 'strogonoff'))

sum_to_10 = 21
print(f"10 + {sum_to_10} = {soma_10(11, sum_to_10)}")
