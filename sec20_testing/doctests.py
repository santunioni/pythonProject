"""
Doctests

We can create documentation for our functions that works like tests.

The tests will run with:
python -m doctest -v module_name.py
"""


def summing(a, b):
    """Sum the numbers a and b
    # the nexline is a doctest
    >>> summing(1, 2)
    3

    >>> summing(4, -6)
    -2
    """
    return a + b


"""
Another example, now using TDD: Test Driven Development
"""


def double(values):
    """Doubles the values in a list.

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([0])
    [0]

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    """

    return [value*2 for value in values]


# Unexpected error: inside doctests python don't recognize double quotes, only simple quote.
def say_hi():
    """Say hi

    >>> say_hi()
    'hi'
    """
    return """hi"""


# Another weird case of failure
def true():
    """Return True

    >>> true()
    True
    """
    return True


