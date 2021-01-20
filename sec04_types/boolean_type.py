"""
Boolean type

Comes from Boolean algebra, created by George Boole

only two constants: True or False
"""


def invert(bool_variable):
    return not bool_variable


def or_function(bool_1, bool_2):
    if bool_1 or bool_2:
        return "Ok"
    else:
        return "Not Ok"


def and_function(bool_1, bool_2):
    if bool_1 and bool_2: return "Ok"
    else: return "Not Ok"


print(f"The variables {True} and {False} are {type(True)}")
