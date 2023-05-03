from flask import Blueprint, jsonify, request

# Models
from models.exercisesModel import ExercisesModel

# Utils 
from utils.ListValidation import ListValidation


main = Blueprint('exercises_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_print_combinations():
    try:
        combinations = ExercisesModel.printCombinations()
        return combinations, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500


@main.route('/caesar-cipher/<message>/<n>', methods=['GET'])
def get_caesar_cipher():
    try:
        message = request.json['message']
        n = request.json['n']
        caesarCipher = ExercisesModel.caesar_cipher(message, n)
        return caesarCipher, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500


@main.route('/clear-duplicates/<numList>', methods=['GET'])
def get_clear_duplicates():
    try:
        numList = request.json['numList']
        if not ListValidation.is_list_valid(numList):
            return jsonify({'message' : "Invalid list"}), 401
        cleanList = ExercisesModel.clearDuplicates(numList)
        return cleanList, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500
    

@main.route('/eval-expression/<expression>', methods=['GET'])
def get_eval_expression():
    try:
        expression = request.json['expression']
        evaluated = ExercisesModel.evalExpression(expression)
        return evaluated, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500