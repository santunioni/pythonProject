"""
Manipulating Date and Time in Python

Python has aw builtin module called datetime
"""

import datetime

print("The datetime package dir: ", dir(datetime), end="\n")
print("The datetime.datetime module dir: ", dir(datetime.datetime), end="\n")

print(datetime.datetime.utcnow())
print(repr(datetime.datetime.utcnow()))

# replace() to adjust date/time
initial_time = datetime.datetime.utcnow()
# Alter the hour to 16hrs period. This won't change in object.
inicio = initial_time.replace(hour=16)
print(initial_time)
print(inicio)

# create date/time
event = datetime.datetime(2023, 1, 1, 0, 0, 1)
print(type(event))
print(event)

# Converting date from brazilian standard
birthday = input("Please inform your birthday (dd/mm/yyyy): ")
birthday = birthday.split('/')
birthday.reverse()
birthday = datetime.datetime(*(int(par) for par in birthday))
print(birthday)

print(f"You are {(datetime.datetime.now()-birthday).days/365} years old.")


current_date = datetime.datetime.now()
days_in_future = datetime.timedelta(days=10)
print(current_date+days_in_future)
