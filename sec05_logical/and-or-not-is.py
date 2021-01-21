"""
This are the logical operators
"""


def not_the_input(bool_variable):
    return not bool_variable


def are_the_same(entry_1, entry_2):
    # I will kept redundant parenthesis
    # for better understanding
    return (entry_1 is entry_2)


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


lista_1 = [1,2,4,124,2]
lista_2 = lista_1
print(are_the_same(lista_1, lista_2))


lista_1 = [1,2,4,124,2]
lista_2 = lista_1.copy()
print(are_the_same(lista_1, lista_2))
