"""
Dictionaries
 
The Python dictionaries are known in other programming
languages as maps.
 
Dictionaries are collections of type key/value. They
don't have indexes.
 
Dictionaries are represented by braces (curly brackets) {}.

Keys and values are split by :
Any type or data can be keys or values

Where to use dictionaries: Imagine you have a e-commerce, where
the shopping cart is where we add products.
Shopping cart:
    Product_1:
        - nome:
        - amount:
        - unit_price:
    Product_2:
        - nome:
        - amount:
        - unit_price:

# This could be done with a list:
shopping_cart = []
product1 = (`Playstation 4`, 1, 230.00)
product2 = (`God of War 4`, 1, 230.00)
shopping_cart.append(product1)
shopping_cart.append(product2)
print(shopping_cart)
# The problem with this solution is we must known the indexes
# of all information inside the shopping_cart.
"""

# Most common creating dictionaries way:
countries_shortcut_1 = {42: 57, 'br': 'Brazil', 'us': 'United States', 'py': 'Paraguai'}


# Second way of creating dictionaries:
countries_shortcut_2 = dict(there_is_no_way='to_use_values_as_keys_here', br='Brazil', eua='United States', py='Paraguay')


################################################
# getting values from dictionaries
################################################

################################################
print("Annoying way to get elements:")
print(countries_shortcut_1[42])
print(countries_shortcut_2['there_is_no_way'])
# raise error for non-existent keys
################################################

################################################
print("Recommended way to get elements:")
print(countries_shortcut_1.get(42))
print(countries_shortcut_2.get("there_is_no_way"))
print("return None for non-existent keys:")
print(countries_shortcut_2.get("there_is_a_way"), end="\n \n")
################################################

################################################
################################################
################################################


print("Popping out entries with pop")
print(countries_shortcut_1.pop('br'))
if not countries_shortcut_1.get('br'):
    print("Brazil was popped out the dictionary.")

print("Popping out last entry with popitem")
print(countries_shortcut_1.popitem())
if not countries_shortcut_1.get('py'):
    print("Paraguay was popped out the dictionary.", end="\n \n")


print("Making Shallow Copy with dictionaries", end="\n \n")
countries_shortcut_1 = countries_shortcut_2.copy()


print("Extracting keys from dictionaries")
for _key in countries_shortcut_1.keys():
    print(_key, countries_shortcut_1.get(_key))
print("Extracting values from dictionaries", end="\n \n")
values = countries_shortcut_1.values()
for _key, _value in countries_shortcut_1.items():
    print(_key, _value)
print("\n")


print("Making Deep Copy with dictionaries")
countries_shortcut_1 = countries_shortcut_2
# adding new entry
countries_shortcut_1[71] = "Cabide"
print(countries_shortcut_1)
print(countries_shortcut_2)


# keys can be searched
print(71 in countries_shortcut_2)
print("Cabide" in countries_shortcut_2, end="\n \n")


# Non common ways to update entry. They return None
print(countries_shortcut_1.update({71: "Rodrigo"}), end="\n \n")
# this next line does nothing because key 72 don't exist
countries_shortcut_1.update({72: "Nobody"})


print("Let's construct a shopping cart for a e-commerce:")
shopping_cart = []

shopping_cart.append({'name': 'Playstation 4', 'amount': 1, 'unit_price': 230.00})
shopping_cart.append({'name': 'God of War 4', 'amount': 1, 'unit_price': 30.00})
print(shopping_cart, end="\n\n")


print("Unusual way to construct dictionaries:")
new_dict = {}.fromkeys(['us', 'br', 'ru', 'py'], "unknown")
# syntax: {}.fromkeys(iterable, every_key_value)
print(new_dict)


print("\nSee the help for dictionaries:")
print(help({'a': 2}), end="\n\n")

print("\nSee more methods from dictionaries:")
print(dir({'a': 2}), end="\n\n")
