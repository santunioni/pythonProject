"""
Reversed

OBS: don't confuse with the function reverse() se found on lists/

Don't confuse with the function reverse() we already study in lists. The reverse() function works only with lists, \
while the reversed() function works with every iterable.

 - reversed() doesn't act on the argument as the sort() function does.
 - The reversed() function returns a reversed-iterator-object.

reverse(iterable, /)
 - /: this is an extra parameter which I don't know how to use
"""
from sys import getsizeof

numbers = [1, 42, 2, 51, 24, 2, 5412, 6, 76, 5, 786]
reversed_it = reversed(numbers)
print(numbers)
print(reversed_it)


print(f"""
- The size of the list is {getsizeof(numbers)} bytes
- The size of reversed is {getsizeof(reversed_it)} bytes

We known we can store the reversed object into a list. However what if I delete the original list? Let's see:""")

del numbers
reversed_list = list(reversed_it)
print(reversed_list)
print("Therefore the reversed object stores the values. I could think it only maps the ordering from the original list.")
