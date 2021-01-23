"""
Raising our own erros

raise -> raise exceptions (errors)

OBS:
 - Raise is not a function. It is a reserved word, as well as def is.
 - when raise is called, the function is finalized.

Thin of raise as useful to create our own exceptions and error messages.

How to use: raise ErrorType('error message')
"""


# example
def coloring(text, color):
    allowed_colors = {'green', 'yellow', 'blue', 'white'}
    if type(text) is not str:
        raise TypeError('The text variable needs to be a string')
    if type(color) is not str:
        raise TypeError('The color variable needs to be a string')
    if color not in allowed_colors:
        raise ValueError(f'The color must be one of {allowed_colors}')

    print(f'The text {text} will be printed in {color} color')


coloring('Vinicius', 'black')

