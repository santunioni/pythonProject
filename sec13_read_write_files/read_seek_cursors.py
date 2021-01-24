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
reader = file.read(30)
# the read function can be limited by the amount of characters you want to read/
print(type(reader))
print(reader)
# Python closes the file after first reading
# Python using a resource called cursor to work with files. This cursor works like a cursor while we are writing
# Python reads only text positioned after the cursor. In order to read the text again, the file should be opened again
print(file.read())
print(dir(file))

print("""
Seek and Cursors

seek() --> Its used to move the cursor around the file
""")

file = open("text.txt")
print(file.read())

print("\n"+"""
The cursor is in the file end. We need to move it: The seek function is used to move the cursor around the file. \
The parameter it receives indicates where in the file we want to place the cursor. The number is the character number.
""")
file.seek(0)
print(file.read())

print("\n"+"""
There is also the function readline() which reads the file line by line.
""")
file.seek(0)
print(file.readline())

print("\n"+"""
The readlines() functions reads the amount of lines you want and put the result in a list of strings.
""")
file.seek(0)
print(file.readlines())
# how many lines there are in my file?
file.seek(0)
len(file.readlines())

print("\n"+"""
OBS: When the file is opened by the function open(), a streaming connection is made with your program. \
When you are done using the file, you must close it calling the function close(). \
""")
# open the file
file = open("text.txt")
# work on the file
print(file.read())
# close the file
file.close()
# check if the file is closed:
print(f"Is the file closed? {file.closed}.")
