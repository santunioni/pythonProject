"""
Like the dictionaries, sets are represented by {}.
The difference is they store values without keys.

- Sets have no duplicate elements
- Set elements are not ordered
- Elements can't be accessed by indexes.

Set's are good to store elements in which we don't
care about ordering.
"""

"""Set's can be used as values to dictionaries. For example:."""
fruits_to_sell = {"bananas", "apples", "pineapples", "watermelons"}
grains_to_sell = {"rice", "beans", "corn", "soy"}
available_products = {'fruits': fruits_to_sell, 'grains': grains_to_sell}

print("Unusual way to define set:")
topics_to_study_1 = set({'quantum mechanics', 'electromagnetism', \
                         'mechanics', 'quantum mechanics'})

print("Usual way to define set:")
topics_to_study_2 = {'quantum mechanics', 'electromagnetism',
                     'classical mechanics', 'thermodynamics', 'quantum mechanics',
                     'algebra', 'calculus', 'statistical mechanics'}

print("""Set's don't store equal values twice:""")
print(topics_to_study_2)

print("See the intersection between two sets as another set")
print(topics_to_study_1.intersection(topics_to_study_2))

print("""Update the set with the intersection with a second set (return = None)""")
print(topics_to_study_1.intersection_update(topics_to_study_2))
print("""The new set is:""")
print(topics_to_study_1)

for _element in topics_to_study_1:
    print(f"The element {_element} is in both sets.")

print("Adding and removing: ")
topics_to_study_1.add('statistical mechanics')
topics_to_study_1.add('calculus')
topics_to_study_1.add('algebra')
print("""For removing, the remove method returns None,
while the pop method returns the value popped. Both methods
 return KeyError if the value is not found.""")
# topics_to_study_1.remove('geometry')
# topics_to_study_1.pop('geometry')
print("""The method discard doesn't return KeyError if
value is not found. This method also return None.""")
print(topics_to_study_1.discard('calculus'))
print(topics_to_study_1.discard('geometry'))


sets_math_methods = {'difference', 'intersection', 'isdisjoint',
                     'issubset', 'issuperset',
                     'symmetric_difference', 'union'}


print("\nSee the help for sets:")
print(help({"a", 2}), end="\n\n")

print("\nSee more methods from sets:")
print(dir({"a", 2}), end="\n\n")
