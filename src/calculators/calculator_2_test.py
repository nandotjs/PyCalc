from src.calculators.calculator_2 import Calculator_2
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List

class MockRequest:
    def __init__(self, json: dict):
        self.json = json

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 1.0

def test_calculator_2():
    numpy_handler = NumpyHandler()
    calculator = Calculator_2(numpy_handler)
    request = MockRequest({"numbers": [1, 2, 3]})
    result = calculator.calculate(request)
    expected_keys = ["RESULT"]
    assert all(key in result for key in expected_keys), "Result does not contain all expected keys"
    assert isinstance(result["RESULT"], float), "Result is not a float"
    assert round(result["RESULT"], 4) == 0.1365, "Result does not match expected value"

def test_calculator_2_with_no_handler():
    numpy_handler = MockDriverHandler()
    calculator = Calculator_2(numpy_handler)
    request = MockRequest({"numbers": [1, 2, 3]})
    result = calculator.calculate(request)
    expected_keys = ["RESULT"]
    assert all(key in result for key in expected_keys), "Result does not contain all expected keys"
    assert isinstance(result["RESULT"], float), "Result is not a float"
    assert round(result["RESULT"], 4) == 1, "Result does not match expected value"

def test_calculator_2_with_wrong_format():
    numpy_handler = NumpyHandler()
    calculator = Calculator_2(numpy_handler)
    request = MockRequest({"numbers": "1, 2, 3"})
    with raises(Exception, match="Wrong format") as exinfo:
        calculator.calculate(request)
    assert str(exinfo.value) == "Wrong format"


