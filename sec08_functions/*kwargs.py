"""
Understanding *args

- *kwargs is a dictionary off keywords arguments a function receives
but were not expected in the function. The extra parameters will be
stored in the dictionary kwargs. You can actually use any name besides
*kwargs, like *parameters for example. Then, the extra keyword parameters
are in the dictionary parameters.

By convention, the python community decided to use as *kwargs

But what is *kwargs?

The parameter *kwargs used in a function put all extra values \
informed by the caller as a dictionary called kwargs.
"""


# Example


def favorite_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person.title()} favorite color is {color.lower()}")


print("\nCompare the next two lines:")
favorite_colors(marcos='green', vinicius='yellow', leandro='black')

# the parameters aren't necessary
favorite_colors()


def special_greeting(**kwargs):
    print("")
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'You received a special Pythonic Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} 'Geek''!"
    return "I am not certain who you are ..."


print(special_greeting())
print(special_greeting(geek='Python'))

print("""
We can have in our functions (IN THIS ORDER):
 - Mandatory parameters
 - **args
 - Default parameters (not mandatory)
 - **kwargs
\n""")


def just_to_use_parameters(age, name, *args, single=False, **kwargs):
    print(f"{name.title()} is {age} years old.")
    print(args)
    if single:
        print("You are single!")
    else:
        print("You are married.")
    print(kwargs)


just_to_use_parameters(25, "Vinicius")
just_to_use_parameters(22, "Bianca", 22, 2412, 21, single=False)
just_to_use_parameters(5, 'Miguel', me='no', you='Go')
just_to_use_parameters(7, "Livia", 22, 2412, 21, java=False, python=True)


# Unpacking items (key: value) from dictionaries: **
def print_keys_values(**kwargs):
    print(kwargs)
    for _key, _value in kwargs.items():
        print(f"{_key.title()} is age {_value}.")


ages_sample = {'Vinicius': 25, 'Bianca': 23, 'Aparecida': 55, 'Bruno': 26}
print_keys_values(**ages_sample)
