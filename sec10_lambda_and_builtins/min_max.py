"""
Min e Max
min() -> return the minimum from an iterable
max() -> return the maximum from an iterable
a function can be used as key to probe the minimum
"""

# example: the minimum will be 0 when weighted by x**2
numbers = range(-10, 10, 1)
print(min(numbers, key=lambda x: x**2))

# example: will the maximum be 10 or 100?
print(max(numbers, key=lambda x: x**2))
# the maximum is -10, this means it returns the
# iterable value, not the function applied to it
# the function chose -10 instead of 10 because it
# gets only the first in this case.

# if provided an empty list, returns the default key
print(max(range(0), default="This iterable is empty"))
