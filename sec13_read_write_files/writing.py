"""
Writing in files

Obs: While open a file for reading, we can't write on it. only read. While opening a file for writing, we can't read \
it, only write in it.

OBS: When opening a file to write, the file is created. If the file already exists, it will be overwritten.
"""

with open("text.txt", 'w') as file:
    file.write("It's too easy to write in a file.\n")
    file.write("We can put the many lines we want.\n")
    file.write("As long we respect the write function receives only strings.\n")
    file.write("This mode of writing the file will overwrite it. You will lose previous texts.\n")

with open("text.txt", 'r') as file:
    # this mode will only read the fiel
    file.read()

try:
    with open("university.txt", 'x') as file:
        # this will open the file only if the file don't exist. If it exist, a error FileExistsError is raised.
        file.write("Content testing.")
except FileExistsError as err:
    print("Error raised: FileExistsError")

with open("text.txt", 'a') as file:  # a = append
    file.write("This will open the file for writing and write on it's last line if the file already exist.\n")
    file.write("If the file don't exist, a new file will be created.\n")
    file.write("With the append format, the content will be added only in the file final. We can't control the \
cursor.\n")

with open("text.txt", 'r+') as file:
    file.seek(0)
    file.write("Using seek() in this mode, we overwriting the previous characters.  \n")
    # if you want to write in the file beginning, you should use the seek() function.
