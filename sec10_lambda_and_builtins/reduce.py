"""
Reduce

OBS: Since python 3+ the reduce() function is not built-in
Now we have to import and use the function from the functools module


Guido van Rossum: Use function reduce() if you really need it.
For almost every case, a for loop is more readable than reduce.


To understand reduce():
Imagine you have a data collection:
data = [a1, a2, a3, a4, a5, ..., aN]

You also have a function receiving two parameters:
de f(x, y):
    return something_with(x, y)

As map() and filter(), the function reduce() receives two parameters:
    one function and an iterable.

The function reduce() works in the following way:
 - Step 1: res1 = f(a1, a2)  # Apply the function f(a1, a2) in the first
two elements and store the return.
 - Step 2: res2 = f(res1, a2)  # Apply the function with the return from
step 1 and the next element a3.
 .
 .
 .
 - Step N: resN = f(res(N-1), aN)

result(data) = f(...f(f(f(f(a1, a2), a3), ..., aN)
"""

# How does it work in practice? Let's use to multiply every element from a list

from functools import reduce

data = [2, 4, 12, 6, 7, 9, 3, 6, 8, 324, 5, 78]
result = reduce(lambda x, y: x*y, data)
print(result)

# do the same thing using a loop
result = 1
for _data in data:
    result *= _data
print(result)

