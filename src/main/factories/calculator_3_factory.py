from src.calculators.calculator_3 import Calculator_3
from src.drivers.numpy_handler import NumpyHandler

def calculator_3_factory(numpy_handler: NumpyHandler) -> Calculator_3:
    return Calculator_3(numpy_handler)
