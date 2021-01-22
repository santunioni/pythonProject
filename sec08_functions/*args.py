"""
Understanding *args

- *args is a tuple off arguments a function receives but were
not expected in the function. The extra parameters will be
stored in the tuple args. You can actually use any name besides
*args, like *numbers. Then, the extra parameters are storage in
the tuple numbers.

By convention, the python community decided to define it as *args

But what is *args?

The parameter *args used in a function put all extra values \
informed by the caller as a tuple called args.
"""


# Examples

def sum_all_numbers(num1, num2, num3):
    return num1 + num2 + num3


# The next line becomes TypeError if number
# of parameters is different than three 3,
# be the number greater or lesser
print(sum_all_numbers(1, 2, 4))


# The next solution is beautiful

def really_sum_all_numbers(num=None, *args):
    if not num:
        raise TypeError("Please provide at least one parameter.")
    return num + sum(args)


def really_sum_all_numbers2(*args):
    if len(args) < 1:
        raise TypeError("Please provide at least one parameter.")
    return sum(args)


print(really_sum_all_numbers(1, 2, 3, 1, 2, 4, 1, 2))
print(really_sum_all_numbers(1, 1, 12, 4, 12))
print(really_sum_all_numbers2(1, 1, 12, 4, 12))

# Unpacking
num_list = [1, 1, 12, 4, 12]
num_set = {1, 1, 12, 4, 12}
num_tuple = (1, 1, 12, 4, 12)
print('The big number got by unpacking is:', +
      really_sum_all_numbers2(*num_list, *num_set, *num_tuple))
# it is not possible to use *args with dictionaries. We need *kwargs


really_sum_all_numbers2()
