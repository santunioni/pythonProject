"""
Dictionary Comprehension
"""

# Syntax
# iterable =
# {_key: _value for _value in iterable}

# Example
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
numbers_squared = {_key: _value**2 for _key, _value in numbers.items()}
print(numbers_squared)

# transform list to dictionary with their square area
numbers_list = [12, 41, 12, 51, 124, 51, 12, 1, 4, 3, 68, 234]
numbers_squared = {_number: _number**2 for _number in numbers_list}
print(numbers_squared)

# even or odd
even_odd = {_number: ('odd' if _number % 2 else 'even') for _number in numbers_list}
print(even_odd)
