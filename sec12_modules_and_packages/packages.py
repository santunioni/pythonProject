"""
Packages

Module --> It's just a .py file that may have several functions available for use.
Package --> A directory enclosing several modules.

OBS: for a directory to be a python2.x package it must contain an empty __init__.py file.
OBS: for python 3.x the __init__.py file isn't necessary, but it's commonly used for retro-compatibility issues.
"""

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(6, 9))

print(funcao4())
