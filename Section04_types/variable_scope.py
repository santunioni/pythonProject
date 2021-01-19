"""
Variables scope

We must learn where the variable are recognized in the program:
- Global variables;
- Local variables;

To declare variables:
variable_name = variable_value

Python is a dynamic type language. The type comes with the value.
"""


number = 42
print(number)
print(type(number))


# this is not possible in C and Java
number = "Geek"
print(number)
print(type(number))


existent1 = "I was defined outside, so I exist everywhere."


def useless_function():
    """This function will teach me about
    global and local variables."""
    non_existent = "I don't exist outside."
    global existent2
    existent2 = "I was defined inside, but I also exist everywhere."
    return None


print(existent1)
useless_function()
print(existent2)


if(True):
    existent3 = """I was defined in a conditional, so
    if it's True (which it is) I also exist everywhere"""


print(existent3)


# The next line bugs the script because the
# variable don't exist here.
print(non_existent)
