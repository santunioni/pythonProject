import os

print("""
How to manipulate files with Python
""")
print(f"\n1 - Does the file/directory exist?")
print(f"  Does text.txt exist? {os.path.exists('text.txt')}")
print(f"  Does directory geek/university exist? {os.path.exists('geek/univeersity')}")
print(f"  Does directory /opt/ exist? {os.path.exists('/opt')}")


print(f"\n2 - How to create a file?")
open('test.file', 'w').close()  # this will erase the file if it already exists
open('test.file', 'a').close()  # this will append to a file if it already exists
with open('test.file', 'a') as file:
    pass
# the best way is (the directory should already exist):
try:
    os.mknod('new_directory/test.file')
except FileExistsError as err:
    print(f"The error ({err}) was raised.")
except FileNotFoundError as err:
    print(f"The error ({err}) was raised.")


print("""\n3 - What if I want to directory inside my current work directory?""")
new_directory = os.path.join(os.getcwd(), 'new_directory', 'geek', 'university')
os.makedirs(new_directory, exist_ok=True)
# the os.mkdir() command will not make all directories I want in this tree


print("\n4 - Renaming a file/directory")
os.rename('new_directory', 'directory_new')
os.rename('directory_new', 'new_directory')
if not os.path.exists('new_directory/geek/university/file_here.py'):
    os.mknod('new_directory/geek/university/file_here.py')
os.rename('new_directory/geek/university/file_here.py', 'new_directory/geek/university/here_file.py')
os.rename('new_directory/geek/university/here_file.py', 'new_directory/geek/university/file_here.py')


print("\n5 - Deleting a file (be careful because the file doesn't go to trash):")
if not os.path.exists('new_directory/test.file'):
    os.mknod('new_directory/test.file')
os.remove('new_directory/test.file')
if not os.path.exists('test.file'):
    os.mknod('test.file')
os.remove('test.file')
if not os.path.exists('text.txt'):
    os.mknod('text.txt')
os.remove('text.txt')
if not os.path.exists('university.txt'):
    os.mknod('university.txt')
os.remove('university.txt')
# to remove empty directories use os.rmdir()
# to remove files from a directory use:
for the_file in list(os.scandir('new_directory')):
    if the_file.is_file():
        os.remove(the_file.path())
# we can delete an empty directory tree
# os.removedirs('new_directory/geek/university')


print("\n6 - Want to send the files to trash instead of deleting directly? ")
# instale o pacote send2trash: pip install send2trash
# instale se sua máquina travar: sudo apt-get install lsb-core
from send2trash import send2trash
try:
    send2trash('new_directory')
except OSError:
    print("Directory does not exist.")


print("\n7 - Working with temporary files and directories:")
import tempfile
with tempfile.TemporaryDirectory() as temp_directory:
    print(f"I've created the temporary directory in {temp_directory}")
    with open(os.path.join(temp_directory, 'temporary_file.txt'), 'w') as temp_file:
        temp_file.write('Geek University\n')
    input()
# only opening temp file, we must write only binary in the file.
with tempfile.TemporaryFile() as temp_file:
    # We need to use binary strings in temp-files at their root
    temp_file.write(b'Geek University')

# access: https://docs.python.org/3/library/os.html






