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

    def test_invalid_sides(self):
        """
        Tests the Dice class constructor with an invalid number of sides.
        """
        with self.assertRaises(ValueError):
            Dice(101, 1)

    def test_invalid_number(self):
        """
        Tests the Dice class constructor with an invalid number of dice.
        """
        with self.assertRaises(ValueError):
            Dice(6, 6)

    def test_multiple_rolls(self):
        """
        Tests multiple rolls and checks history
        """
        dice = Dice(6, 2)
        for _ in range(5):
            roll = dice.roll()
            self.assertEqual(len(roll), 2)
            for r in roll:
                self.assertTrue(1 <= r <= 6)
        history = dice.get_history()
        self.assertEqual(len(history), 5)

if __name__ == "__main__":
    unittest.main()

