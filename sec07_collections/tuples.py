"""
Tuples

Tuples are almost like lists

There are two basic differences:
    - Tuples are represented by parenthesis () instead of []
    - Tuples cannot change. Never. They are immutable.
    - Every operation on a tuple returns a new tuple.
"""

tuple_1 = (12, 12, 41, 24, 12, 41)
print(tuple_1)
tuple_2 = tuple(sorted(tuple_1))
print(tuple_2)


# We don't need parenthesis to define tuple
# with multiple entries
tuple_3 = 1, 2, 12, 41251, 2, 12, 341, 2, 1421, 2
print(f"The object tuple_3 is {type(tuple_3)}")


# Watch out for single element tuples
# Tuples are defined by the comma,
# not by parenthesis ().
number_1 = 12412
number_2 = (12342)
tuple_4 = number_1,
print(f"""The objects number_1 and number_2 are
 {type(number_1)} and {type(number_2)}, 
while tuple_4 is {type(tuple_4)}""")
print("This is a tuple: ", tuple_4)


# Unpacking tuples
tuple_5 = "Geek University", "Python programming: essentials"
escola, curso = tuple_5

tuple_6 = tuple("New entry added")
print(f"The text 'New entry added' have {tuple_6.count('e')} letters e.")


print("\nSee the help for tuples:")
print(help(("a", 2)), end="\n\n")

print("\nSee more methods from tuples:")
print(dir(("a", 2)), end="\n\n")
