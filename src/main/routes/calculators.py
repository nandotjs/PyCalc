from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator_1
from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import NumpyHandler

calc_route_bp = Blueprint('calc_route_bp', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculate():
    calculator = Calculator_1()
    result = calculator.calculate(request)

    return jsonify(result), 200

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculate_2():
    numpy_handler = NumpyHandler()
    calculator = Calculator_2(numpy_handler)
    result = calculator.calculate(request)

    return jsonify(result), 200

