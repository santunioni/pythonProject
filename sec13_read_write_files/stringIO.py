"""
StringI/O

In order to read or write a file in the operating system, you need permission.

StringIO -> Used to read and write files in volatile memory.
"""

# We should import the package
from io import StringIO

message = "This is a string message to write in the StringIO file in the volatile memory.\n"
file = StringIO(message)
# Now we can do whatever we want we the file.
print(file.read())
print("Where is the cursor? ")
print(file.read())

# we can write:
file.write("We can easily write more texts in the file.\n")

# we can move the cursor
file.seek(0)
file.write("_______\n")
file.seek(0)
print(file.read())
file.write("Python will always write to my file in insert mode. I must create the function myself if I want to append \
lines to the beginning.")
file.seek(0)
print(file.read())
