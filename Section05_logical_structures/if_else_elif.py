"""
These are the logical structures
"""


# This is how the elif works:
number = float(input("Please type a number here: "))
if number < 0:
    print(f"The number {number} is negative.")
elif number == 0:
    print(f"The number {number} vanishes.")
else:
    print(f"The number {number} is positive.")
