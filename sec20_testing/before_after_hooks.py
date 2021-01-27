"""
UnitTest - Hooks: before and after Hooks

Hooks: are the tests themselves.

In general we need to perform certain tasks before and after trying the tests. Examples: open and close DataBase \
connections, creating and entering some virtual environment.

The unittest model have two methods for handling before and after hooks:
 - setup() -> it's executed before each test method. It is useful to create objects instances and another data.
 - tearDown() -> it's executed after each test method. It's useful to delete data or close connections with DataBases.
"""

import unittest


class ModuleTest(unittest.TestCase):

    def setUp(self):
        # setTup configurations
        pass

    def test_first(self):
        # setUp will run before the test
        # tearDown() will run after the test
        pass

    def test_second(self):
        # setUp will run before the test
        # tearDown() will run after the test
        pass

    def tearDown(self):
        # setUp will run before the test
        # tearDown() will run after the test
        pass
