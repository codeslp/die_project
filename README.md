# Dice Roller API

This repository contains a simple Flask application for rolling dice and recording the history of those rolls. The Dice Roller API is a web service with endpoints for both rolling dice and retrieving the history of dice rolls. 

## Components

The `Dice` class is a Python object that simulates a set of dice. It utilizes Python's special methods such as `__init__` for initializing dice with specific sides and numbers, and `__len__` for returning the number of dice in the set. The `Dice` class also provides methods to roll the dice and get the history of rolls.

The Flask application serves as the interface to interact with the `Dice` class via web endpoints. 

One of the core components of this application is the use of SQLAlchemy, a Python SQL toolkit and Object-Relational Mapping (ORM) library. SQLAlchemy provides the ability to "talk" to our SQLite database by converting Python classes to tables in our database and converting function calls to SQL statements. This allows us to persist the state of our application and save dice rolls across sessions.

The application uses a simple SQLite database to store the roll results. SQLite is a light, disk-based database, which requires zero configuration - perfect for development and testing. 

The `Roll` class defined in the code maps to a table in our database where each roll's results are stored. SQLAlchemy's ORM makes it easy for our application to insert new rolls, query roll history, and manage our database.

## How to Install and Run

1. Clone the repository:

```
git clone <repo_url>
```

2. Navigate into the cloned repository:

```
cd <repo_name>
```

3. Install a virtual environment:

```
python -m venv venv
```

4. Activate the virtual environment:

On Windows:

```
.\venv\Scripts\activate
```

On Unix or MacOS:

```
source venv/bin/activate
```

5. Install the required packages:

```
pip install -r requirements.txt
```

6. Run the Flask application:

```
flask run
```

The application will start running at `localhost:5000`.

## How to Use

To roll the dice, send a POST request to the `/roll` endpoint with a JSON object containing the number of sides and dice. For example:

```json
{
    "sides": 6,
    "number": 2
}
```

To retrieve the history of rolls, send a GET request to the `/history/<sides>/<number>` endpoint, replacing `<sides>` and `<number>` with the number of sides on the dice and the number of dice.

## How to Test

1. Run the test suite:

```
python -m unittest test_die.py
```

This will run a series of unit tests on the `Dice` class to ensure its functionality.
