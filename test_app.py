import unittest
from die import Dice

class TestDice(unittest.TestCase):
    """
    A test suite for the Dice class.
    """

    def test_roll(self):
        """
        Tests the roll method of the Dice class.
        """
        dice = Dice(6, 1)
        roll = dice.roll()
        self.assertEqual(len(roll), 1)
        self.assertTrue(1 <= roll[0] <= 6)


    def test_history(self):
        """
        Tests the get_history method of the Dice class.
        """
        dice = Dice(6, 1)
        roll = dice.roll()
        history = dice.get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0], roll)

if __name__ == "__main__":
    unittest.main()
