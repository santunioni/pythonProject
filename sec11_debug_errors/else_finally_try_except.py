"""
Try / Except / Else / Finally

As you advance in programming experience you will identify better the possible errors that must be treated in your code

Tips for where to treat erros:
 - Every data-entry to the program must be error-treated.

OBS: The user job is to destroy your system
"""

# This is a sequencial execution. The else block is executed only if no errors occur.
try:
    input_number = input("Tell me an integer number (floats will be rounded towards 0): ")
    input_number = int(float(input_number))
except ValueError:
    print("You didn't type a number. ")
else:
    print(f"You typed number {input_number}")


# using Finally
# finally is generally used to close or deallocate resources: del input_number
try:
    input_number = input("Tell me an integer number (floats will be rounded towards 0): ")
    input_number = int(float(input_number))
except ValueError:
    print("You didn't type a number. ")
else:
    print(f"You typed number {input_number}")
finally:
    print("The finally block will always be executed, no matter if no errors occur.")
    del input_number

print('\nThe try/except block ended\n\n')


# Exercise: a function that returns quotient of two integers .
# This is wrong because you are treating the error in the input.
# The error must be treated in the function, because you are responsible
# for your function behavior. You are treating only the division by zero error,
# which is insufficient.

def quotient_wrong(int_1, int_2):
    try:
        _quotient = int_1//int_2
        _remainder = int_1 - _quotient*int_2
        return f"The quotient between {int_1} and {int_2} is {_quotient} and remainder {_remainder}"
    except ZeroDivisionError:
        print("You can not divide by zero. Insert a valid number.")


print("Let's divide two integer numbers.")
try:
    numerator = int(input("Insert the numerator: "))
except ValueError:
    print("You must type an integer number.")
else:
    try:
        denominator = int(input("Insert the denominator: "))
    except ValueError:
        print("You must type an integer number.")
    else:
        print(quotient_wrong(numerator, denominator))
finally:
    del numerator, denominator


# Exercise: a function that returns quotient of two integers .
# This is the correct way to do because now the erros are treated inside the functon.
def quotient_correct(_numerator, _denominator):
    try:
        num, dem = int(_numerator), int(_denominator)
        quo = num // dem
        rem = num - quo*dem
    except ValueError:
        return "You must enter two integer numbers to the function quotient_correct."
    except ZeroDivisionError:
        return "Sorry, but I don't know how to divide by zero."
    else:
        return f"The quotient is {quo} and remainder {rem}."


print("Let's divide two integer numbers.")
num1 = input('Type the numerator: ')
num2 = input('Type the denominator: ')
print(f"{quotient_correct(num1, num2)}")


# Example: semi-generic way to treat erros. Do it in a suscint way.
# this is also correct.
def quotient_correct(_numerator, _denominator):
    try:
        num, dem = int(_numerator), int(_denominator)
        quo = num // dem
        rem = num - quo*dem
    except (ValueError, ZeroDivisionError) as err:
        return f"The error following error occurred: {err}"
    else:
        return f"The quotient is {quo} and remainder {rem}."


print("Let's divide two integer numbers.")
num1 = input('Type the numerator: ')
num2 = input('Type the denominator: ')
print(f"{quotient_correct(num1, num2)}")
