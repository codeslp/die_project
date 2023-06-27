# Here we are going to create a web API
from flask import Flask, jsonify, request
from die import Dice

app = Flask(__name__)


@app.route('/roll', methods=['POST'])
def roll():
    """
    Rolls the dice and returns the result.
    """
    dice_data = request.json
    dice = Dice(dice_data['sides'], dice_data['number'])
    return jsonify(dice.roll())


@app.route('/history', methods=['GET'])
def history():
    """
    Returns the most recent rolls made with the dice.
    """
    dice = request.json
    dice = Dice(dice['sides'], dice['number'])
    return jsonify(dice.get_history())

if __name__ == '__main__':
    app.run(debug=True)