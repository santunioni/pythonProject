"""
PEP8 - Python enhancement proposal

They are proposals for python better code looking

The Zen of Python

The PEP8 idea is we write code in a pythonic way
"""




"""
1. Use camel-case for class names, examples: Computer, ScientificComputing, IDoNotKnowWhatNameToChooseForThisClass
"""
class ScientificComputing():
    pass




"""
2. Use lowercase names for functions and variables. For longer names, split words with underscore _
"""
def soma_2(x,y):
    return x+y




"""
3. Use 4 spaces for indentation! (Don't use tab)
"""
if 'a' in 'banana':
    print('tem')




"""
4. Blanklines: learn from PyCharm because it incorporates PEP8
  - Split functions and class definitions with two blank lines
  - Methods inside classes are split by only one blank line
"""




"""
5. Don't import several packages on the same line. Use one line for each.
  - No problems in importing multiple classes from a single package using:
"""
from types import StringType, ListType
"""
  - In case of several classes, it is better to use:
"""
from types import {
    StringType,
    ListType
}
"""
   Place imports after commentaries and docstrings and before global variables
"""




"""
6. Spaces in expressions and instructions:

  - Don't do:
"""

index = 1
function_with_long_name ( algo[ 1 ], { outro : 2 } ):
    return      None

my_dict ['key'] =   my_list [index]
variable      = 1
long_variable = 2


"""
  - Do:
"""
function_with_long_name(algo[1], {outro: 2}):
    return None

my_dict['key'] = my_list[index]
variable = 1
long_variable = 2




"""
7. Always finish an instruction with another line.
"""

import this

