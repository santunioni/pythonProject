"""
Positional-only arguments

This resource is present in Python for a long time in built-ins functions, however we couldn't use in our own functions.


The arguments before / are set as positional-only arguments:
# >>> help(float)
# class float(object)
#  |  float(x=0, /)
#  |
#  |  Convert a string or number to a floating point number, if possible.


In this case we can never call the function this way:
float(value='67.3')
"""


# With Python 3.8 we can create:
def greetings_v1(name):
    return f'Hello, {name}.'


# Both these prints will work:
print(greetings_v1('Vinicius'))
print(greetings_v1(name='Geek'))


# Now we define the function with positional-only arguments.
def greetings_v2(name, /):
    return f'Hello, {name}.'


# Only the first print will work:
print(greetings_v2('Vinicius'))
# print(greetings_v2(name='Geek'))


# Now mixing positional-only and other arguments:
def greetings_v3(name, /, message):
    return f'{message} {name}'


print(greetings_v3('Vinicius', message='From the mixed arguments: Hello, '))
print(greetings_v3('Vinicius', 'From the mixed arguments: Hello, '))


"""
We can also do the opposite: we can forbid arguments from being passed positionally:
"""


def greetings_v4(message, /, *, name):
    return f'Hello, {name}'


# Only the first print will work:
print(greetings_v4("From the positional-forbidden arguments: ", name='Vinicius'))
# print(greetings_v4(message="From the positional-forbidden arguments: ", name='Vinicius'))
# print(greetings_v4(message="From the positional-forbidden arguments: ", 'Vinicius'))
# print(greetings_v4("From the positional-forbidden arguments: ", 'Vinicius'))


# Parameters between / and * are have the passing methods optional:
def greetings_v5(name, /, message1="Hello", *, message2):
    return f'{message1}, {name.title()}. {message2}'


# Only the first two will work:
print(greetings_v5("vinicius", message2="Have a nice day!"))
print(greetings_v5("vinicius", message1="How are you", message2="Have a nice day!"))
# print(greetings_v5("vinicius", message1="How are you", "Have a nice day!"))
# The last didn't work because message2 is forbidden to be positional.
