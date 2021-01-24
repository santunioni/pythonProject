print("""
The WITH block

How to work with files:

 1 - Open the file
 2 - Work in the file
 3 - Close the file
 
The with block is used to create a context of work where resources used are closed after the block ends.
""")

# the with block closes the files automatically after ending
# this is the pythonic way to work with the files

with open('text.txt') as file:
    print(file.readlines())
    print(f" Is the file open inside the with? {not file.closed}")
print(f" Is the file open outside the with? {not file.closed}")
