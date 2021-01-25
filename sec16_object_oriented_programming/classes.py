"""
OOP - Classes

Classes are models representing models from the real world to the computer.

Imagine you want to design a system to automatize the switching of lights in your house/company. \
You will probably create a class for the lamp, because computers don't known what lamps are.

Classes may contain:
 - Attributes -> representing the object characteristics. We can represent computationally the \
the object parameters. For example: the lamp voltage, the color, the status if it's turned or off \
luminosity, etc.

 - Methods (functions) -> represent the object behavior. The actions the object may realize in the \
system are represented here. In the lamp case, one required method is to turn on the lights.


In Python we use the reserved word Class to define a class.

OBS: We use the word 'pass' in Python when we have a code block not implemented yet.
OBS: When naming OUR CLASSES in Python we use CamelCase for convention. PEP8
OBS: In Java, the file-name is the same name as the class inside it. There is only one class per file.

 - When planning the software development, we cal ENTITY the objects from the real world that wew need \
to map as classes in the software.
"""


class Lamp:
    pass


class CheckingAccount:
    pass


class Product:
    pass


lamp = Lamp()
print(type(lamp))


print("""Despite only learning about classes now, we are using them since the course beginning. For example, when \
using the cast int('42'), whe are converting the string '42' to a integer by creating a new instance with \
the class int. The int class is a built-in, which by convention don't use CamelCase.""")
