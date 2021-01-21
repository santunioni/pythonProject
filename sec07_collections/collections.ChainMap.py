"""
Collections module - ChainMap

Collections -> High-performance Container DataTypes

defaultdict -> To create a default dict we need to assign a default value to it.
A lambda can be used as default value.
- In case there is a not attributed key in the dict,
the default value is automatically assigned to it.
- In case we try to access a non-existent key, the key is automatically
created with the default value.
"""

# import
from collections import ChainMap

print("\nSee the help for ChainMap:")
print(help(ChainMap), end="\n\n")
print("\nSee more methods from ChainMap:")
print(dir(ChainMap()), end="\n\n")
