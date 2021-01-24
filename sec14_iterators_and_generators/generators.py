"""
Generators

 - Generators are one kind of Iterators.

 OBS: The opposite isn't true. Not every iterator is a generator.

 Info:
  - Generators may be created by generator functions.
  - generator functions use the reserved word yield
  - Generators can be created with generator expressions

Difference between functions and generating functions:

-----------------------------------------------------------------------------
|     Functions                      |  Generator Functions                 |
-----------------------------------------------------------------------------
|     they use return                |  use yield                           |
|     can return only once           |  can yield multiple times            |
|     always return a value          |  always return a generator           |
-----------------------------------------------------------------------------
"""
# generator expression example
gen_exp = (number for number in range(10))
print(gen_exp)


# Generator function example
def count_to(max_value):
    counter = 1
    while counter < max_value + 1:
        # the yield command returns the value counter
        # and waits for the next function to be called
        yield counter
        counter += 1
# OBS: a generator function isn't a generator, it will return a generator


# the next line will use a generator function to create a generator
gen = count_to(10)
print(gen)
# the for loop will print in steps of 2 because both the for and the print calls the next() function
for number in gen:
    print(next(gen))


# testing memory and speed of generators compared to lists
def make_fib_gen(max_index):
    fib_number_1 = 0
    fib_number_2 = 1
    yield fib_number_1 + fib_number_2
    counter = 1
    while counter < max_index:
        fib_number = fib_number_1 + fib_number_2
        yield fib_number
        fib_number_1 = fib_number_2
        fib_number_2 = fib_number
        counter += 1


def make_fib_list(max_index):
    nums = []
    a, b = 0, 1
    counter = 1
    while counter < max_index:
        nums.append(b)
        a, b = b, a + b
        counter += 1
    return nums


from sys import getsizeof
fib_gen = make_fib_gen(100000)
fib_list = list(fib_gen)
print(
    f"""
    Let's compare sizes in memory of list and generator:
     - the list is size {getsizeof(fib_list)} bytes.
     - the generator is size {getsizeof(fib_gen)} bytes.
     - the generator size \
is {round(100 * getsizeof(fib_gen) / getsizeof(fib_list), 2)}% \
the list size.

     The difference is absurd for larger sets.
     Use generators instead of comprehension always as possible.""")

input()


# Now we will compare the time for both functions to create the generator and the list
import time
index_number = 100000
gen_initial = time.time()
fib_gen = make_fib_gen(index_number)
gen_final = time.time()
delta_gen = gen_final - gen_initial
list_initial = time.time()
fib_list = make_fib_list(index_number)
list_final = time.time()
delta_list = list_final - list_initial
print(
    f"""\n\n
    Let's compare speeds between creating a fibonacci list and a fibonacci generator:
     - the list took {delta_list} seconds.
     - the generator took {delta_gen} seconds.
     - the time to create the generator \
is {round(100 * delta_gen / delta_list, 3)}% \
the time to create the list.

     The difference is absurd for larger sets.
     Use generators instead of comprehension always as possible.""")
