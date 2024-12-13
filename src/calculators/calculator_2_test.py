from src.calculators.calculator_2 import Calculator2
from pytest import raises

class MockRequest:
    def __init__(self, json: dict):
        self.json = json

def test_calculator_2():
    calculator = Calculator2()
    request = MockRequest({"numbers": [1, 2, 3]})
    result = calculator.calculate(request)

    
    assert result["RESULT"] == 6
