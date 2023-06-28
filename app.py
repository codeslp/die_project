# Here we are going to create a web API
from flask import Flask, jsonify, request
from die import Dice
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Roll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sides = db.Column(db.Integer, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dice.db'
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    @app.route('/roll', methods=['POST'])
    def roll():
        """
        Rolls the dice and returns the result.
        """
        dice_data = request.json
        dice = Dice(dice_data['sides'], dice_data['number'])
        roll = dice.roll()
        new_roll = Roll(sides=dice_data['sides'], number=dice_data['number'], result=str(roll))
        db.session.add(new_roll)
        db.session.commit()
        return jsonify(roll)


    @app.route('/history/<int:sides>/<int:number>', methods=['GET'])
    def history(sides, number):
        """
        Returns the most recent rolls made with the dice.
        """
        history = Roll.query.filter_by(sides=sides, number=number).all()
        return jsonify([eval(roll.result) for roll in history])

    return app