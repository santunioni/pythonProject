"""
Collections module - defaultdict

Collections -> High-performance Container DataTypes

defaultdict -> To create a default dict we need to assign a default value to it.
A lambda can be used as default value.
- In case there is a not attributed key in the dict,
the default value is automatically assigned to it.
- In case we try to access a non-existent key, the key is automatically
created with the default value.
"""

# import
from collections import defaultdict
print("\nSee the help for defaultdict:")
print(help(defaultdict), end="\n\n")
print("\nSee more methods from defaultdict:")
print(dir(defaultdict(lambda: 0)), end="\n\n")

new_default_dict = defaultdict(lambda: 0)
print(new_default_dict)
new_default_dict['Course'] = 'Programming in Python'
print(new_default_dict)
name_value = new_default_dict['Name']
print(new_default_dict)
new_default_dict['Name'] = 'Vinícius Vargas'
print(new_default_dict)
