"""
Manipulating Date and Time in Python

Python has aw builtin module called datetime

Let's see it's methods:
"""

import datetime

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# We will fix the software at mid-night

maintenance = datetime.datetime.combine(datetime.datetime.now()+datetime.timedelta(days=1), datetime.time())

# the method datetime.time() chooses only time, setting days=0.

print(maintenance)
print(type(maintenance))
print(repr(maintenance))

# Finding the weekday:
print(f"{maintenance.weekday()}: {weekdays[maintenance.weekday()]}")

# Formatting data/time with strftime() (String Format Time)
today = datetime.datetime.today()
print(today)
print(today.strftime("%d/%m/%y"))
print(today.strftime("%d/%B/%Y"))

# pip install textblob
from textblob import TextBlob


def format_date(date):
    return f"{date.day} de {TextBlob(date.strftime('%B')).translate(to='pt-br')} de {date.year}."


print(format_date(today))

# Transforming string to time
birthday = datetime.datetime.strptime('10/04/2912', '%d/%m/%Y')
print(birthday)

# Counting time to execute code
import timeit

print("\nGenerator time: ", end="")
time = timeit.timeit("'-'.join(str(n) for n in range(100))", number=100000)
print(time)
print("\nList comprehension time: ", end="")
time = timeit.timeit("'-'.join([str(n) for n in range(100)])", number=100000)
print(time)
print("\nMap time: ", end="")
time = timeit.timeit("'-'.join(map(str, range(100)))", number=100000)
print(time)


import functools


def test(n):
    sume = 0
    for num in range(n*200):
        sume += num**num+4
    return sume


print(timeit.timeit(functools.partial(test, 10), number=1000))
