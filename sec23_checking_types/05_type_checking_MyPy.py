"""
MyPy
Mypy type checks programs that have type annotations conforming to PEP 484. Getting started is easy if you know \
Python. The aim is to support almost all Python language constructs in mypy.

Installing mypy: pip install mypy

Instead of executing the codee with Python, we use mypy command in terminal.

05_type_checking_MyPy.py:31: error: Argument "align" to "head" has incompatible type "str"; expected "bool"
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
conditional = False
if conditional:
    print(head('geek university', align='geek'))


# To fix problem we can use type checking tools, which will loop for declared types in our functions,
# methods and classes, and check if all variables passed to they are the correct type.

# The Python program will lose a bit of performance with type hinting.
