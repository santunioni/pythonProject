"""
Reading files

We use the built-in function open() to read files in python.

open() -> in the simplest way to use the function we use a single parameter as entry, in this case it is the
file name. This functions returns a _io.TextIOWrapper which is the object we work in the code. This object
is only on volatile memories.

https://docs.python.org/3/library/functions.html#open

# OBS: By default the open function opens the file only for reading. The file should exist, or the function
will raise the error FileNotFoundError.
"""

# Example: default mode = 'r' (reading only)
file = open('text.txt')
print(file)
print(type(file))


# to read the file content after it's opening we should use the built-in function read()
reader = file.read()
print(type(reader))
print(reader)
# Python closes the file after first reading
# Python using a resource called cursor to work with files. This cursor works like a cursor while we are writing
# Python reads only text positioned after the cursor. In order to read the text again, the file should be opened again
print(file.read())
print(dir(file))
