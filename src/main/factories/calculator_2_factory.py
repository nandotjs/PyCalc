from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import NumpyHandler

def calculator_2_factory(numpy_handler: NumpyHandler) -> Calculator_2:
    return Calculator_2(numpy_handler)
