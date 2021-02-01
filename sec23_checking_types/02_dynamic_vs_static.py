"""
Python uses dynamic typing, which is related with how Python uses memory, storing the values uniquely in heap memory, \
mapping they to variables stored in stack memory.
"""

age = 42
print(type(age))

# we can reallocate another type to the variable
age = 'Quarenta e dois'
print(type(age))

# The problem with dynamic type is:
conditional = False
if conditional:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41
# If the conditional is set to False, We can compile the code without any errors.

print(resultado)

# In programs with static type, the error would emerge while compiling the code.
# The compiler wouldn't even read the code
