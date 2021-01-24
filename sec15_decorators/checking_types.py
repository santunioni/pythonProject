"""
Forcing data type to functions with decorators

In Python we don't specify data types to variables. The variable can be assigned any type in any part of the code. \
Therefore, we may want to force datatype to our functions inputs in order to prevent errors from happening. The \
functions may broke the code if receiving other type than the one requested in the input.
"""
from functools import wraps


def force_type(*wanted_types):
    def receives_function(entry_function):
        @wraps(entry_function)
        def checker_function(*args, **kwargs):
            new_args = []
            for arg, wanted_type in zip(args, wanted_types):
                # if type(arg) is not wanted_type:
                #     raise TypeError
                new_args.append(wanted_type(arg))
            return entry_function(*new_args, **kwargs)
        return checker_function
    return receives_function


@force_type(str, int)
def repeat_message(msg, x_times):
    for time in range(x_times):
        print(msg, end=' ')


repeat_message('Oi', '20')


