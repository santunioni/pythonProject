"""
This are the logical operators
"""


def not_the_input(bool_variable):
    return not bool_variable


def compare_two_bools(bool_1, bool_2):
    # I will kept redundant parenthesis
    # for better understanding
    return (bool_1 is bool_2)


def or_function(bool_1, bool_2):
    if bool_1 or bool_2:
        return "Ok"
    else:
        return "Not Ok"


def and_function(bool_1, bool_2):
    if bool_1 and bool_2: return "Ok"
    else: return "Not Ok"


print(f"The variables {True} and {False} are {type(True)}")


active = True
# Pythonic way
if not active:
    print("Please activate your account.")
else:
    print("Welcome user!")
# or
if active is True:
    print("Welcome user!")
else:
    print("Please activate your account.")


