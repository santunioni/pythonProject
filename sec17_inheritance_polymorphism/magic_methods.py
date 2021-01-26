"""
OOP - Magic Methods

Magic methods are all methods that use dunder.

dunder init -> __init__ our Class constructor
"""


class Book:

    print(f"All this magic methods come from class object: \n{dir(object)}", end="\n\n")

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        """This magic method will configure our object representation. Representation is how it looks when calling \
        print(object). This is a representation usually used only by the developers, in order to track the code \
        progress and search for references later in development stages."""
        return f'This is a Class called book. This book title is {self.title.title()} with {self.pages} pages written \
by author {self.author}.'

    def __str__(self):
        """This magic method will configure the final user representation of this class. This is not for development \
        only, but to present to users"""
        return f'This is a book called {self.title.title()} with {self.pages} pages written by author {self.author}.'

    def __len__(self):
        """I am defining the length of the book is measured as the number of pages."""
        return self.pages

    def __del__(self):
        """I am changing the behaviour of the function del. When deleting a book, a message will also be printed."""
        print(f"The Book entry 'title = {self.title}, author = {self.author}, pages = {self.pages}' was deleted from \
        volatile memory.")

    def __add__(self, *args):
        """I am defining how add two books behave.."""
        return f"{self}; " + '; '.join([f"{book}" for book in args])

    # def __add__(self, second):
    #     """I am defining how add two books behave.."""
    #     return f"{self}; " + f" {second}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += " " + str(self) + ";"
            return msg
        return "I can't multiply"


book1 = Book('Python Rocks!', 'Geek University', 400)
book2 = Book('Artificial intelligence with Python', 'Geek University', 350)

print(book1)
print(len(book1))
print('\n')

del book1, book2

python_rocks = Book('Python Rocks!', 'Geek University', 400)
artificial_intelligence = Book('Artificial intelligence with Python', 'Geek University', 350)
code_with_me = Book('Code with me!', 'Angela Yu', 80)

print('\n')

print(python_rocks + (artificial_intelligence, code_with_me))

print('\n')

print(python_rocks * 3)
