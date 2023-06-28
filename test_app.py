import unittest
from flask import json
from app import create_app, db, Roll

class TestApp(unittest.TestCase):
    """
    A class dedicated to testing the functionality of the Flask application. It ensures that all API endpoints are
    functioning as expected, the database interacts as expected, and the dice rolling and history retrieval are handled
    correctly.
    """

    def setUp(self):
        """
        Creates a Flask app and a test client to interact with the app.
        """
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test_dice.db'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Removes the database session and drops all tables.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_roll(self):
        """
        Tests the /roll endpoint.
        """
        response = self.client.post('/roll', json={'sides': 6, 'number': 2})
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertTrue(1 <= data[0] <= 6)
        self.assertTrue(1 <= data[1] <= 6)

    def test_history(self):
        """
        Tests the /history endpoint.
        """
        self.client.post('/roll', json={'sides': 6, 'number': 2})
        self.client.post('/roll', json={'sides': 6, 'number': 2})
        response = self.client.get('/history/6/2')
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        for d in data:
            self.assertEqual(len(d), 2)
            self.assertTrue(1 <= d[0] <= 6)
            self.assertTrue(1 <= d[1] <= 6)

if __name__ == "__main__":
    unittest.main()
