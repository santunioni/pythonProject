"""
Generators (generator expression)

In previous classes we studied:
 - List Comprehension
 - Dictionary Comprehension
 - Set Comprehension

We didnt study:
 - Tuple Comprehension
because they are actually called generators.
"""

"In the last class we saw:"
names = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
initials_are_C_list = [name[0] == 'C' for name in names]
print(all(initials_are_C_list))

print("""
We could use generators instead of lists []. Instead of making a list of \
booleans if initial is C, we put the booleans in a generator. A generator \
is also an iterable object, with the advantages of lower memory usage. \
The generator also destroys itself after usage
""")
initials_are_C_generator = (name[0] == 'C' for name in names)
print(initials_are_C_generator)
# this is a generator, not a list comprehension.
# As the function all() receives an iterable, not necessarily a list:
print(all(initials_are_C_generator))
# or put it directly in the all() function.
print(all(name[0] == 'C' for name in names))


# Let's see the memory size for both comprehension and generator
from sys import getsizeof

print(
    f"""
    Let's compare sizes of list and generator:
     - the list is size {getsizeof(initials_are_C_list)} bytes
     - the generator is size {getsizeof(initials_are_C_generator)} bytes
     - the relative size of both \
is {100*getsizeof(initials_are_C_generator)/getsizeof(initials_are_C_list)}%
     
     The difference is absurd for larger sets.
     Use generators instead of comprehension always as possible.""")
