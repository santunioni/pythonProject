"""
Collections module - namedtuple

Collections -> High-performance Container DataTypes

namedtuple -> Tuples where we specify names and parameters
"""

# import
from collections import namedtuple

print("\nSee the help for NamedTuple:")
print(help(namedtuple), end="\n\n")
print("\nSee more methods from NamedTuple:")
print(dir(namedtuple('typename', 'field_names')), end="\n\n")

# Example
dog = namedtuple('dog', 'age breed name')
# or
dog = namedtuple('dog', 'age, breed, name')
# or (the last is the clearest to understand)
dog = namedtuple('dog', ['age', 'breed', 'name'])
print(dog)

ray = dog(age=2, name='Ray', breed='Chown-Chown')
print(ray)


print(ray[2])  # name
print(ray.name)  # name
print(ray[2] is ray.name)

# after created, the tuple have the methods of
# traditional tuples, plus the ones created
print(dir(ray))
