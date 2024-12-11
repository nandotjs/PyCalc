from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator_1

calc_route_bp = Blueprint('calc_route_bp', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculate():
    calculator = Calculator_1()
    result = calculator.calculate(request)

    return jsonify(result), 200

