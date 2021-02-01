"""
Simpler debugger with f-strings
The new functionalities help to debug code with variable tracking.
"""

# New functionalities were added to f-strings:
print(f"My name is {(name := 'Vinicius')}, therefore call me {name} please.")

# Adding = after the variable will exhibit it's name and value:
geek: str = 'Geek University'
print(f"Check this: {geek=}")
print(f"Also check this: {geek.upper()[::-1]=}")
