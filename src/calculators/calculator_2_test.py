from src.calculators.calculator_2 import Calculator_2
from pytest import raises

class MockRequest:
    def __init__(self, json: dict):
        self.json = json

def test_calculator_2():
    calculator = Calculator_2()
    request = MockRequest({"numbers": [1, 2, 3]})
    result = calculator.calculate(request)
    expected_keys = ["RESULT"]
    assert all(key in result for key in expected_keys), "Result does not contain all expected keys"
    assert isinstance(result["RESULT"], float), "Result is not a float"
    assert round(result["RESULT"], 4) == 0.1365, "Result does not match expected value"

def test_calculator_2_with_wrong_format():
    calculator = Calculator_2()
    request = MockRequest({"numbers": "1, 2, 3"})
    with raises(Exception, match="Wrong format") as exinfo:
        calculator.calculate(request)
    assert str(exinfo.value) == "Wrong format"


