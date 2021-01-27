import unittest

from robot import Robot


class RobotTests(unittest.TestCase):

    def setUp(self):
        print("Running setUp ... ", end="")
        self.megaman = Robot("Mega Man", battery=40)
    
    def test_charge(self):
        self.megaman.charge()
        self.assertEqual(self.megaman.battery, 100)

    def test_say_name(self):
        self.assertEqual(self.megaman.say_name(), "BEEP BOOP BEEP BOOP. I AM MEGA MAN")
        self.assertEqual(self.megaman.battery, 39, "The battery should be 29.")

    def tearDown(self):
        print("Running tearDown!")
        del self.megaman


if __name__ == '__main__':
    unittest.main()
