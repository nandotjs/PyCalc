from flask import Blueprint, jsonify, request
from src.drivers.numpy_handler import NumpyHandler
from src.main.factories.calculator_1_factory import calculator_1_factory
from src.main.factories.calculator_2_factory import calculator_2_factory

calc_route_bp = Blueprint('calc_route_bp', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculate():
    calculator = calculator_1_factory()
    result = calculator.calculate(request)

    return jsonify(result), 200

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculate_2():
    calculator = calculator_2_factory(NumpyHandler())
    result = calculator.calculate(request)

    return jsonify(result), 200

