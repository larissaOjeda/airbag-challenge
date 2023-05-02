from flask import Blueprint, jsonify, request
import uuid

# Entities 
#from models.entities.ChargingDetails import ChargingDetails 

# Models
from models.exercises import Exercises
from models.StatisticsModel import StatisticsModel

# Utils 
from utils.ListValidation import ListValidation


main = Blueprint('charging_detail_blueprint', __name__)




@main.route('/clear-duplicates/<id>', methods=['GET'])
def get_clear_duplicates():
    try:
        numList = request.json['numList']
        if not ListValidation.is_list_valid(numList):
            return jsonify({'message' : "Invalid list"}), 401
        cleanList = Exercises.clearDuplicates(numList)
        return cleanList, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500