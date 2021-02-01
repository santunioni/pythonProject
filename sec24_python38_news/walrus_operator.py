"""
WALRUS
:=

This operator allows to ASSIGN AND RETURN value in one line.

This is the main change in python 3.8.
"""

# Before this change we were forced to do this:
name1 = "Geek university"
print(name1)

# Now we can do this:
print(name2 := "Geek University")

# More examples:

# Python <= 3.7
cesta1 = []
fruta = input("Informe a fruta: ")
while fruta != 'jaca':
    cesta1.append(fruta)
    fruta = input("Informe a fruta: ")
# Now with Python >= 3.8
cesta2 = []
while (fruta := input("Informe a fruta: ")) != 'jaca':
    cesta2.append(fruta)

print("Primeira cesta: ", cesta1)
print("Primeira cesta: ", cesta2)
