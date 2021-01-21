"""
None type

The python None type represents the type without any Type
It is known as a empty type, but type-without-type is
a more appropriated name.

- Always None, not none.

When do we use None?
- We can use when we want to initialize a variable
without type, before receiving a final value.
"""

numbers = None

print(numbers)
print(type(numbers))


if not None:
    print("""The None type is always False
    when checked as boolean.""")
else:
    "This block will never run"


print("\nSee the help for None:")
print(help(None), end="\n\n")

print("\nSee more methods from None:")
print(dir(None), end="\n\n")

