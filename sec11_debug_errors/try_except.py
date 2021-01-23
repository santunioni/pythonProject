"""
The Try/Except block

We use the block Try/Except to treat errors that may occur in our code, preventing the final users to see unexpected \
error messages in our code. For us, developers, seeing errors is not a problem, because it helps us to identify \
failures in the code, but the final user don't want to see them.

- In other programming languages the block is called Try/Catch.

The simplest and general way to treat the error is:
try:
    //problematic execution
except:
    //what you must do in case the execution fails

- Treating errors in a generic way is not the best way. The best is to always treat specifically.
"""

# Example
try:
    geek()
except:
    print("Some problem occurred in the app. Please send this error message to your supporter")
print("\n")


# Example: treating a specific error
try:
    # len(1)  # if uncomment this line, a type error is raised, not treated in block except NameError
    geek()
except NameError:  # the error type in front of except treat this error specifically.
    # Other types will not be reported in this case
    print("You are using a unexistent function. Please call support.")
print("\n")


# Example: giving name to the error
try:
    geek()
except NameError as err:  # err = error_name. You can call it whatever you want
    print(f"The app returned the error: {err}")
# this will return the error: name 'geek' is not defined.
# it's not recommended because a cracker you known your code vulnerabilities.
# this type of error are stored in an protected log of the system, allowing devs to look at the erros.
print("\n")


# Example: we can perform several types of error treating in the same code
try:
    # len(5)
    # geek()
    print('Geek'[9])
except NameError as err:
    print(f"Returned NameError: {err}")
except TypeError as err:
    print(f"Returned TypeError: {err}")
except:
    print(f"An error occurred.")
print("\n")


# Example: using try/except in functions
def catch_value(_dict, _key):
    try:
        return _dict[_key]
    except NameError as err_Name:
        print("This key is not present in this dictionary.")
    except TypeError as err_Type:
        print("The first argument must be a dictionary.")


user_info = {'name': 'Vinicius'}
print(catch_value(1, 'name'))
print("\n")
