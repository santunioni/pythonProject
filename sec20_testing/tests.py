import unittest

from activities import eat, sleep, is_funny


class ActivitiesTests(unittest.TestCase):

    # By convention, all test names should be preceded by test_
    # Each module is a single test. We should assert only once per module.
    def test_eat_healthy(self):
        """Testing when eating healthy food."""
        self.assertEqual(
            eat('okra', True),
            'I am eating okra because I want to keep in shape.'
        )

    def test_eat_delicious(self):
        """Testing when eating not healthy food."""
        self.assertEqual(
            eat(food='pizza', is_healthy=False),
            'I am eating pizza because we only live once.'
        )

    def test_sleep_too_few(self):
        """Testing when we sleep few hours"""
        self.assertEqual(
            sleep(4),
            'I am still tired after spelling for 4 hours.'
        )

    def test_sleep_too_much(self):
        """Testing when we sleep too much"""
        self.assertEqual(
            sleep(10),
            'Ptz! I slept too much! I am late for work.'
        )
        
    def test_is_funny(self):
        """Testing the funny people."""
        # self.assertEqual(is_funny('Sérgio Malandro'), False)
        self.assertFalse(is_funny('Sérgio Malandro'))  # This is passing even when the function isn't implemented
        self.assertTrue(is_funny('Jim Carrey'), 'Jim Carrey should be funny.')


if __name__ == '__main__':
    unittest.main()
