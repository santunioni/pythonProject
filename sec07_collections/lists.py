"""
Lists

Lists in Python are the analogue to vectors/matrices from other languages.
The advantages from other languages is LISTS HAVE DYNAMIC SIZE AND TYPE.
   - Lists can support entries in different types.

In languages as Java or C: Arrays
   - Size and types are fixed when array are declared.

In Python: Lists
   - Lists have dynamic size and type
   - The computer memory is the only limitation
   - They are represented in brackets []
   - Lists have indexed elements, as Arrays from other languages have
   (contrary to dictionaries)
"""

miscellaneous_list = ["bananas", 123, True, 2 > 40,
                      3.1415, "A long string"]
print(miscellaneous_list)

print(type(miscellaneous_list))
print(list("Hi. I am Goku!"))


# You can search for objects in lists
fruit = input("What fruit do you want? ")
if (fruit in miscellaneous_list) is True:
    print(f"Here are your {fruit}.")
else:
    print(f"We don't have {fruit} here, sorry.")


# We can easily print a list
number_list = [12, 4, 1, 23, 13, 12, 123, 1, 35, 123, 12, 361, 2]
print(number_list)

# I will sort the list and print again
number_list.sort()
print(number_list)

# Sorting also work with characters list
my_name = list("Vinícius Vargas")
my_name.sort()
print(my_name)

# We can easily count occurrences in list
number_of_i = my_name.count("i")
print(f"Your name have {number_of_i} letters i.")

# Append elements to lists
my_name = "Vinícius Vargas"
first_name, last_name = my_name.split()
middle_name = "Sant Unioni Ângelo"
full_name = [first_name, *middle_name.split()]
full_name.append(last_name)
print(full_name)

# What if we want to convert the list to string again?
full_name = ' '.join(full_name)
print(full_name)

lista = []
# We can also extend the list
# the extend() method takes exactly one argument
# which in this case is a list
lista.extend(["a", "c", "b"])
# the argument must be an iterable


# We can remove an element from list
index = -1
lista.pop(index)


# We can take a index of an object inside list
lista = ["apple", "banana", "mellon", "pineapple"]
print(f"The mellon is in the index {lista.index('mellon')}")
# .index() systax:  list.index(search_for, from, to)


# let's use slice now. the syntax is: list1a[inicio:fim:passo]
print(number_list)
inicio, fim = 0, len(number_list)-1
print(number_list[::-1])


# Make a list into a tuple
lista = [12, 45, 1, 2, 51, 2, 13, 24, 124, 1, "a"]
tupla = tuple(lista)
print(tupla)
# this doesn't work: tupla.__add__("maçã")
print(tupla)

# ########################################################
# Copying a list into another: Shallow Copy and Deep Copy
lista1 = [1, 3, 1245, "Some entry", 12, 12]
print(lista1)

# ########################################################
# This is a Shallow Copy. It is the same as lista2 = lista1
lista2 = lista1.copy()
lista2.append("New entry added")

# Comparing both, we see lista2 was added while lista1 was not
print(lista1)
print(lista2)

# #########################################################
# This is Deep Copy. This copy also receives the memory address of the list
lista2 = lista1
lista2.append("New entry added")

# Comparing both, we see both lists was added the new entry
print(lista1)
print(lista2)
# #########################################################


# This is a Shallow Copy
lista2 = lista1 + []
lista2.append("New entry added")
print(lista1)
print(lista2)


print("\n\nUnpacking lists, compare the following two prints:")
lista = [123, 2312, 124, 1243, 554, "end"]
print(lista)
print(*lista)


print("\nSee the help for lists:")
print(help([]), end="\n\n")

print("\nSee more methods from lists:")
print(dir([]), end="\n\n")
