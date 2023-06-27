# Dice Rolling Web API

This Python-based project simulates the rolling of dice. The project leverages the Flask framework to create a web API, which allows you to roll a dice and also to retrieve the history of dice rolls. The application supports a range of die configurations, enabling users to specify the number of sides on each die as well as the number of dice to be rolled.

## Features

- Create a die with a configurable number of sides and dice in the set.
- Roll the dice and get a result.
- Fetch the most recent dice rolls.

## Special Python Features

The application makes use of several special (dunder) methods in Python, also known as magic methods. 

- `__init__`: This is the class constructor method. It's called when a new object of the class is created and allows the class to set up its attributes.

- `__len__`: This method allows a class to define its "length". For our Dice class, the length is the number of dice in the set.

- `__getitem__`: This method allows a class to support indexing. In the Dice class, this allows us to retrieve a die at a specified position in the set.

## API Endpoints

- `POST /roll`: Roll the dice. This endpoint accepts a JSON object specifying the number of sides and number of dice. For example:

```json
{
    "sides": 6,
    "number": 2
}
```

- `GET /history`: Get the most recent dice rolls. The endpoint requires a JSON object specifying the sides and number of dice, as in the `/roll` endpoint.

## Testing

Unit tests have been written for the Dice class and can be run using the Python's built-in `unittest` module. 

To run the tests, navigate to the root directory of the project and run: 

```sh
python -m unittest test_die
