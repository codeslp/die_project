import unittest
from die import Dice

class TestDice(unittest.TestCase):
    """
    A class dedicated to testing the functionality of the Dice class. It checks if the dice rolling mechanism,
    history feature, and data validation are all working as expected.
    """

    def test_roll(self):
        """
        Tests the roll method of the Dice class to ensure each roll generates a value within the expected range.
        """
        dice = Dice(6, 1)
        roll = dice.roll()
        self.assertEqual(len(roll), 1)
        self.assertTrue(1 <= roll[0] <= 6)

    def test_invalid_sides(self):
        """
        Tests the Dice class constructor with an invalid number of sides to ensure it correctly raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Dice(101, 1)

    def test_invalid_number(self):
        """
        Tests the Dice class constructor with an invalid number of dice to ensure it correctly raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Dice(6, 6)

    def test_multiple_rolls(self):
        """
        Tests multiple rolls to ensure that the Dice class can handle and store multiple rolls correctly.
        """
        dice = Dice(6, 2)
        for _ in range(5):
            roll = dice.roll()
            self.assertEqual(len(roll), 2)
            for r in roll:
                self.assertTrue(1 <= r <= 6)

    def test_history(self):
        """
        Tests the get_history method of the Dice class to verify that roll results are stored correctly.
        """
        dice = Dice(6, 2)
        for _ in range(5):
            dice.roll()
        history = dice.get_history()
        self.assertEqual(len(history), 5)
        for roll in history:
            self.assertEqual(len(roll), 2)
            for r in roll:
                self.assertTrue(1 <= r <= 6)

if __name__ == "__main__":
    unittest.main()
