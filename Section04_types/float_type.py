"""
Float type
"""

valor1, valor2 = 1, 44

print(f'The variable {valor1} is {type(valor1)}')

tuple1 = valor1, valor2
print(f'The variable {tuple1} is {type(tuple1)}')


# We can also work with complex numbers
complex_variable = valor1*1.0+valor2*1j
print(f'The variable {complex_variable} is {type(complex_variable)}')
print("The methods available are:")
print(dir(complex_variable))

print(complex_variable/complex_variable.conjugate())
