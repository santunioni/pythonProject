"""
Writing a customized iterator
"""


# we will create something analogous to range()
class Counter:
    # The __init__ is a special function called constructor(),
    # which creates objects from the class
    # Always that creating function inside classes, self must be
    # the first argument, which represents the object itself.
    def __init__(self, minor, major):
        self.minor = minor
        self.major = major

    # the next special function will make the Counter class an iterable
    def __iter__(self):
        return self

    def __next__(self):
        if self.minor < self.major+1:
            self.minor += 1
            return self.minor - 1
        raise StopIteration


con = Counter(1, 10)
print(f"The minor and major are {con.minor} and {con.major}")
it = iter(con)
# In the next for I'm using the next() function on the iterator con
# two times per loop, one is used by the own for loop and other inside the print.
# therefore the printing will occur in steps of two numbers.
for i in con:
    print(next(it))

