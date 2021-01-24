"""
File system and browsing

In order to manipulate files in the OS, we need to import the module os.
"""

import os

print("\nThe function os.getcwd() will get the absolute working directory: ")
absolute_path = os.getcwd()
print(absolute_path)

print("\nWe change directory with the os.chdir() command:", end=' ')
os.chdir('..')
print(os.getcwd())
print("\nWe can go to root:", end=' ')
os.chdir('/')
print(os.getcwd())
print("\nCome back to working directory:", end=' ')
os.chdir(absolute_path)
print(os.getcwd())

print("\nWe can check if some the directory is absolute or relative:", end=' ')
print(os.path.isabs('~/Dropbox'))

print("\nWe can identify the operating system with os module:", end=' ')
print(os.name)
print("Now with more details: ", os.uname())

import sys
print("Print only the platform: ", sys.platform)

print("""
What if I want to directory inside my current work directory?
""")
new_directory = os.path.join(os.getcwd(), 'new_directory', 'geek', 'university')
os.makedirs(new_directory, exist_ok=True)
# the os.mkdir() command will not make all directories I want in this tree

print("I am currently at: ", os.getcwd())
print("\nI can also print files in directory with the os.listdir(): ", os.listdir())

print("\n We can list files and directories with more details with os.scandir():")
scanner = os.scandir()
files = list(scanner)  # the os.scandir() function returns an iterator.
print(files)

print("\nNow see the dir for DirEntry type: ", dir(files[0]))
print("Let's see what inode is: ", files[0].inode())
print("Let's see what is_dir is: ", files[0].is_dir())
print("Let's see what is_file is: ", files[0].is_file())
print("Let's see what is_symlink is: ", files[0].is_symlink())
print("Let's see what stat is: ", files[0].stat())
print("Let's see what path is: ", files[0].path)

# OBS: we must close the scanner after running the function scandir().
scanner.close()
