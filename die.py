import collections
from random import choice

Die = collections.namedtuple('Die', ['sides', 'number'])


class Dice:
    """
    A class representing a set of dice.

    Attributes:
        sides (int): The number of sides on each die.
        number (int): The number of dice in the set.
        roll_history (collections.deque): A deque containing the most recent rolls made with the dice.
    """

    def __init__(self, sides, number):
        """
        Initializes a new instance of the Dice class.

        Args:
            sides (int): The number of sides on each die.
            number (int): The number of dice in the set.
        """
        if sides < 1 or sides > 100:
            raise ValueError("Number of sides must be greater than zero and less than 101.")
        elif number < 1 or number > 5:
            raise ValueError("Minimum of 1 die and maximum of 5 dice are allowed.")
        else:
            self._dice = [Die(sides, number) for _ in range(number)]
            self.roll_history = collections.deque(maxlen=100)

    def __len__(self):
        """
        Returns the number of dice in the set.
        """
        return len(self._dice)

    def roll(self):
        """
        Rolls all the dice in the set and returns the result.

        Returns:
            list: A list containing the result of each die roll.
        """
        roll = [choice(range(1, die.sides + 1)) for die in self._dice]
        self.roll_history.append(roll)
        return roll

    def get_history(self):
        """
        Returns the most recent rolls made with the dice.

        Returns:
            collections.deque: A deque containing the most recent rolls made with the dice.
        """
        return list(self.roll_history)