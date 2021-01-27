"""
Understanding iterators and iterables

Iterator ->
    - It's an object that can be iterated
    - The object returns a data, one element per time a function next() is called.

Iterable ->
    - One object that returns an iterator when method iter() is called on it.
"""

# Iterable examples: this is not iterator. The thing that for loop does is to transform
# iterables into iterators by calling the iter() function.
name = 'Geek University'
numbers = [number for number in range(10)]

# iterators are the thing that are iterated in for loops under the hood
# iterators have the next function, which is used under the hood by the for loop
name_it = iter(name)
for i in range(15):
    print(next(name_it))

