"""
Collections module - OrderedDict

Collections -> High-performance Container DataTypes

OrderedDict -> Dictionary that remembers insertion order
"""

# import
from collections import OrderedDict
print("\nSee the help for OrderedDict:")
print(help(OrderedDict), end="\n\n")
print("\nSee more methods from OrderedDict:")
print(dir(OrderedDict()), end="\n\n")

# new_default_dict = defaultdict(lambda: 0)
# print(new_default_dict)
# new_default_dict['Course'] = 'Programming in Python'
# print(new_default_dict)
# name_value = new_default_dict['Name']
# print(new_default_dict)
# new_default_dict['Name'] = 'Vinícius Vargas'
# print(new_default_dict)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)

o_dict1 = OrderedDict({"a": 1, "b": 2})
o_dict2 = OrderedDict({"b": 2, "a": 1})
print(o_dict1 == o_dict2)
