"""
Assertions

We use the reserved word 'assert' to check simple conditionals in Python tests

OBS: We can specify, optionally a second argument or a personalized error message.
OBS: The 'assert' can be used in any function or code, not only in tests.

ATTENTION: Be careful while using 'assert'. If a python program is executed with flag -O, no assert will be executed.
"""


def sum_positives(a, b):
    assert a > 0 and b > 0, 'Both numbers need to be positive'
    return a + b


try:
    print(sum_positives(1, -2))
except AssertionError:
    print("I can't sum negative number.")


def eat_fast_food(food):
    assert food in [
        'pizza',
        'ice-cream',
        'candy',
        'french fries',
        'hot dog'
    ], 'You must eat fast-food.'
    return f"I'm eating {food}"


print(eat_fast_food('hot dog'))


# CAREFUL USING ASSERT

def do_something_bad(user):
    assert user.is_adm, 'Only admins can do bad things!'
    destroy_system()
    return 'Good bye!'

# A simple python -O flag can ignore the is_adm check.
