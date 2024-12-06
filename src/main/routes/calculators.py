from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint('calc_route_bp', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculate():
    print(request.json)
    return jsonify("Success")
