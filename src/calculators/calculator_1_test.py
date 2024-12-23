from src.calculators.calculator_1 import Calculator_1
from pytest import raises
from src.errors.http_bad_request import HttpBadRequestError

class MockRequest:
    def __init__(self, json: dict):
        self.json = json

def test_calculator_1():
    calculator = Calculator_1()
    request = MockRequest({"number": 60})
    result = calculator.calculate(request)
    expected_keys = ["RESULT"]
    assert all(key in result for key in expected_keys), "Result does not contain all expected keys"
    assert isinstance(result["RESULT"], float), "Result is not a float"
    assert round(result["RESULT"], 2) == 172.96, "Result does not match expected value"

def test_calculator_1_with_wrong_format():
    calculator = Calculator_1()
    request = MockRequest({"number": "60"})
    with raises(HttpBadRequestError, match="Wrong format") as exinfo:
        calculator.calculate(request)
    assert str(exinfo.value) == "Wrong format"

