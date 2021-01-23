"""
Debugging code with PDB: Python Debugger

The first computer problem that happened in history was because a bug invaded one giant computer.
That's the story of words bug and debug.

OBS: the use of print() to debug code is a bad practice, because now there are many better practices.
 - There exist more professional ways to perform debugging. In python we can debug code with several IDE's,
like PyCharm or Virtual Studio Code. Another way is using the built-in Python Debugger, not tied to any IDE.
"""

print("""
To use the PyCharm debugger, mark break points in the code by clicking next to the line number. \
A red flag will appear next to the line number. When the code gets executed by clicking in the bug, \
the interpreter will stop before the break points.
""")

# # Doing the PyCharm way
# def quotient_wrong(int_1, int_2):
#     _quotient = int_1//int_2
#     _remainder = int_1 - _quotient*int_2
#     return f"The quotient between {int_1} and {int_2} is {_quotient} and remainder {_remainder}"
#
#
# quotient_wrong(7, 0)

print("""\n
To use Python Debugger, we need to import the library pdb, and then use the function set_trace().
The pdb commands are:
 - l: list where we are in the code.
 - n: go to next line
 - p: print variable
 - c: continue the code - end the debugger
 """)

# # Example 1
# import pdb
# name = 'Angelina'
# last_name = 'Jolie'
# pdb.set_trace()  # this will mark the next line as a break point
# full_name = name + ' ' + last_name
# course = 'Python programming: essentials'
# final = full_name + ' is practicing ' + course
# print(final)


# # Example 2
# name = 'Angelina'
# last_name = 'Jolie'
# import pdb; pdb.set_trace()  # this will mark the next line as a break point
# full_name = name + ' ' + last_name
# course = 'Python programming: essentials'
# final = full_name + ' is practicing ' + course
# print(final)
# # why using this second format instead of the first? the pdb module will be imported
# # only in developing stage of the function. Therefore, it's easier to remember you are
# # importing some unnecessary module when you see it acting in your code.


# Example 3
# from python 3.7 until now, it's not mandatory to import the pdb module anymore. The
# debugger was built in the python console using the function breakpoint().
name = 'Angelina'
last_name = 'Jolie'
breakpoint()  # this will mark the next line as a break point
full_name = name + ' ' + last_name
course = 'Python programming: essentials'
final = full_name + ' is practicing ' + course
print(final)


# OBS: be careful with conflict between variable names and pdb commands.
# Example:
def soma(l, n, p, c):
    breakpoint()
    return sum(l, n, p, c)


soma(1, 2, 3, 5)
# this will bug the code because the variable names have the same name as pdb commands
