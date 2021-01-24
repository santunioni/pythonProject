"""
Making our own loop version
"""


def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


my_for('Geek University')
