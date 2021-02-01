"""
This is a formal solution to impose static types variables to Python.
We can define the parameter types that a function receive and specify the return type.
PEP 484 -> Python3.5
"""


# This is a function receiving only a string, returning also a string.
def greet(name: str) -> str:
    return f'Hello, {name}'


print(greet('Geek'))


def head(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, '#')


print(head('geek university'))
print(head('geek university', align=False))

# Even using the type hinting, the function still receives wrong parameters:
print(head('geek university', align='geek'))

# To fix problem we can use type checking tools, which will loop for declared types in our functions,
# methods and classes, and check if all variables passed to they are the correct type.
