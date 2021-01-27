"""
Introduction to Unittest module

Unittest -> Unitary Tests

What are unitary tests?
It is the way to test individual units of code.

Individual units can be: functions, methods, classes, modules, etc.

#OBS: Unit tests are not specific to python. It is a general philosophy of testing code while writing. It is used for \
all languages.

The UnitTest module is highly recommended for Python programmers, because it tests code in pythonic way.

To create unit tests, we create classes that inherit from unittest.TestCase, inheriting all 'assertions' present in \
UnitTest module.

To run the tests we use unittest.main()

TestCase -> Test cases you write to your unit.

# Knowing assertions: https://docs.python.org/3/library/unittest.html
_______________________________________________________________
    METHOD                     |         CHECK
---------------------------------------------------------------
    assertEqual(a, b)          |        a == b
    assertNotEqual(a, b        |        a != b
    assertTrue(x)              |        x is True
    assertFalse(x)             |        x  is False
    assertIs(a, b)             |        a is b
    assertIsNot(a, b)          |        a is not b
    assertIsNone(x)            |        x is None
    assertIsNotNone(x)         |        x is not None
    assertIn(a, b)             |        a is in b
    assertNotIn(a, b)          |        a is not in b
    assertIsInstance(a, b)     |        a is instance of b
    assertIsNotInstance(a, b)  |        a is not instance of b
----------------------------------------------------------------

# To execute tests with unittest: python test_module_name.py
# To execute tests with unittest verbose mode: python test_module_name.py -v

# Docstrings in tests:
    It's recommended to add short docstrings to your tests.

"""

# Practices: Using TDD approach
