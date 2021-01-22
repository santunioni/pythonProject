"""
List Comprehension

- With list comprehension we can build new lists with data processed from an iterable.

# Syntax:
"""

# Basic example
numbers = [12, 3, 124, 12, 4, 125, 23, 65, 98, 0]


def square(_number):
    return _number ** 2


squared_numbers = [square(number) for number in numbers]


# String example: Return a list with all letters Capital
name = 'Vinicius Vargas'

print([_char.upper() for _char in name])


# Putting list to CapitalCase
friends = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
friends = [_friend.capitalize() for _friend in friends]
print(friends)


# Checking if it's even or odd (if in comprehension)
numbers = range(1, 101)
evens = [_even for _even in numbers if _even % 2 == 0]
odds = [_odds for _odds in numbers if _odds % 2 == 1]
print(evens, '\n', odds)


# Refactoring the code above:
# In Python the integer 0 is equivalent to bool False
evens = [_even for _even in numbers if not _even % 2]
# In Python integers != 0 are equivalent to bool True
odds = [_odds for _odds in numbers if _odds % 2]
print(evens, '\n', odds)


# Now I ill use the if else in list comprehension. I am dividing even numbers
# by 2 and turning odd numbers into 0.
res = [_number//2 if _number % 2 == 0 else 0 for _number in numbers]
print(res)


# Perform repetitive actions
def some_iterable():
    return range(10)


def do_something(_dummy):
    print(f"I print {_dummy}.")


iterable = some_iterable()
condition = False
[do_something(dummy) for dummy in iterable if dummy]
[do_something(dummy) if condition else print(0) for dummy in iterable]
