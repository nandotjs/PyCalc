from pytest import fail, raises
from src.calculators.calculator_3 import Calculator_3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List
from src.errors.http_bad_request import HttpBadRequestError


class MockRequest:
    def __init__(self, json: dict):
        self.json = json

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 1.0

    def variance(self, numbers: List[float]) -> float:
        return 1.0

def test_calculator_3():
    numpy_handler = NumpyHandler()
    calculator = Calculator_3(numpy_handler)
    request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    result = calculator.calculate(request)
    expected_keys = ["RESULT"]
    assert all(key in result for key in expected_keys), "Result does not contain all expected keys"
    # assert isinstance(result["RESULT"], bool), "Result is not a bool"
    assert result["RESULT"] == "Fail", "Result does not match expected value"

def test_calculator_3_with_no_handler():
    numpy_handler = MockDriverHandler()
    calculator = Calculator_3(numpy_handler)
    request = MockRequest({"numbers": [1, 2, 3]})
    result = calculator.calculate(request)
    expected_keys = ["RESULT"]
    assert all(key in result for key in expected_keys), "Result does not contain all expected keys"
    # assert isinstance(result["RESULT"], bool), "Result is not a bool"
    assert result["RESULT"] == "Success", "Result does not match expected value"

def test_calculator_3_with_wrong_format():
    numpy_handler = NumpyHandler()
    calculator = Calculator_3(numpy_handler)
    request = MockRequest({"numbers": "1, 2, 3"})
    with raises(HttpBadRequestError, match="Wrong format") as exinfo:
        calculator.calculate(request)
    assert str(exinfo.value) == "Wrong format"


