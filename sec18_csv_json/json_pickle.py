"""
JSON and Pickle

JSON -> JavaScript Object Notation: they are common in API's
It is a dictionary!

API -> Are communication means between companies services and third parties (us, developers)

"""

import json
import jsonpickle

ret = json.dumps(["product", {"""Playstation 4""": ('2TB', 'Novo', '220V', 2340)}])

print("Class ret: ", type(ret))
print("ret: ", ret, end="\n\n")


class Cat:

    def __init__(self, name, race):
        self.__name = name
        self.__race = race

    @property
    def name(self):
        return self.__name

    @property
    def race(self):
        return self.__race


felix = Cat('Felix', """Vira-lata""")
print("Cat dict: ", felix.__dict__)
ret1 = json.dumps(felix.__dict__)
print("ret1: ", ret1, end="\n\n")

"""
Integrating JSON and Pickle
pip install jsonpickle
"""

ret2 = jsonpickle.encode(felix)
print("ret2: ", ret2, end="\n\n")

with open('felix.json', 'w') as file:
    ret3 = jsonpickle.encode(felix)
    file.write(ret3)

with open('felix.json', 'r') as file:
    content = file.read()
    ret3 = jsonpickle.decode(content)

print("ret3: ", ret3)
print("Type ret3: ", type(ret3))
print("Name ret3: ", ret3.name)
print("Race ret3: ", ret3.race)
