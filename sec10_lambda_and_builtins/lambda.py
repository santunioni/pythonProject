"""
Lambda functions

Lambda functions are unnamed functions. They are anonymous.
"""

# Standard function in python:
from IPython.utils.tests.test_wildcard import y


def operation(x, y):
    return x ** y + y ** x


print(operation(3, 5))

# Lambda expression
lambda x, y: x ** y + y ** x

# How to use lambda? (unideal)
operation_lambda = lambda x, y: x ** y + y ** x
print(operation_lambda(3, 5))

# If I have to assign a lambda to
# a variable, why not using def?

# We can have lambda expressions with multiple entries
complete_name = lambda name, last_name: name.strip().title + ' ' + \
                                        last_name.strip().title()

# We can also have zero entry
love = lambda: 'How not to love Python? '
# and multiple
multiple = lambda *args: sum(args)

print(love())
print(multiple(1, 2, 3, 4, 5))


# WE MUST NOT ASSIGN LAMBDA FUNCTIONS. IT'S UGLY
# Other example: order authors by lastname
authors = ['Friedrich Hayek', 'Ayn Rand', 'Hans Hermamn Hoppe', 'Ludwig von Misses', 'Murray Rothbard']
print(authors)
# key in sort receives a function that takes the full_name, split it by ' '
# take the last name from the split version and take the key last
authors.sort(key=lambda full_name: full_name.split(' ')[-1].lower())
print(authors)


def quadratic_polinomial(a, b, c):
    """Return the function f(x) = a + b*x + c*x**2"""
    return lambda x: a + b*x + c*x**2


free_fall = quadratic_polinomial(0, 0, -10/2)


trajectory = [(_time, free_fall(_time)) for _time in range(0, 1000, 10)]
print(trajectory)


# We generally use lambda functions to filter and order data
