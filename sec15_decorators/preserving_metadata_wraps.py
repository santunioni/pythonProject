"""
Preserving metadata with wraps

What are metadata?
 - They are data intrinsic to files. In our functions they are intrinsic to functions, like name, args type, etc.

What are wraps?
 - They are functions that envelop (that wrap) other functions or elements. The wrapping is useful for several purposes.
 - Our decorator functions are examples of wraps.

Why preserve metadata in wraps?
 - Metadata losses can occur when a function is wrapped by another function used as decorator.
 - It's important to keep your original function metadata to preserve it's name and other properties \
 because sometimes those properties are important.
"""

# First: let's see the problems that arise when we don't preserve our decorated function metadata
from functools import wraps


def decorator_function(entry_function):
    """This function receives another function, designed as entry_function, \
    and wraps it by more code with some functionality."""

    # @wraps(entry_function)
    def login(*args, **kwargs):
        """I am the inner function that receives the arguments from the entry_function, make something with them, \
add more code between the entry_function execution and call it after I did whatever I want to do before. I can also \
continuing performing the tasks I want after I call the function."""
        print(f"You are called the function named as: {entry_function.__name}")
        print(f"Here it is the function doc string: {entry_function.__doc__}")
        return entry_function(*args, **kwargs)

    return login


@decorator_function
def summing(a, b):
    """This function will simply sum two numbers (a and b) entered as my inputs."""
    return a + b


print(f"\nThe function summing name now is: {summing.__name__}")
print(f"The function summing docstring now is: {summing.__doc__}")

print("""\n\n\
There is a problem: the function summing lost it metadata and absorbed the wrapping function metadata. We want to \
keep our function metadata, therefore we add to the decorator function the decorator @wraps(entry_function) \
where the argument entry_function is the function the decorator is tasked to decorate. This will pass the function \
metadata to the decorator, therefore they become accessible. Let's change the decorator function defined above to: \n"""
      )


def decorator_function(entry_function):
    """This function receives another function, designed as entry_function, \
    and wraps it by more code with some functionality."""

    @wraps(entry_function)
    def login(*args, **kwargs):
        """I am the inner function that receives the arguments from the entry_function, make something with them, \
add more code between the entry_function execution and call it after I did whatever I want to do before. I can also \
continuing performing the tasks I want after I call the function."""
        print(f"You are called the function named as: {entry_function.__name}")
        print(f"Here it is the function doc string: {entry_function.__doc__}")
        return entry_function(*args, **kwargs)

    return login


print("And we must define the summing function again.\n")


@decorator_function
def summing(a, b):
    """This function will simply sum two numbers (a and b) entered as my inputs."""
    return a + b


print(f"The function summing name now is: {summing.__name__}")
print(f"The function summing docstring now is: {summing.__doc__}")
