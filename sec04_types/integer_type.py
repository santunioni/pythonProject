"""
Numeric type
"""

print(1+2)
print(5/2)

# Integer part
print(int(5/2))
# Pythonic way
print(5//2)

# Modulo
print(5%2)

# Power
print(2**3)

# Underlines doesn't count in python numbers
number = 10_000_000_000
print(f"Look at this number: {number}")

# Beautiful syntax
print(f"This number {number} is {type(number)}")

# Using dir
print(dir(number))