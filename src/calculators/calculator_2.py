from typing import List
from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator_2:
    def __init__(self, numpy_handler: DriverHandlerInterface) -> None:
        self.__numpy_handler = numpy_handler

    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        body = request.json
        input_data = self.__validate_request(body)
        result = self.__process_data(input_data)

        return {
            "RESULT": result
        }

    def __validate_request(self, body: dict) -> List[float]:
        numbers = body.get("numbers")
        if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
            raise Exception("Wrong format")

        return [float(x) for x in numbers]

    def __process_data(self, input_data: List[float]) -> float:
        processed_data = [(11 * x) ** 0.95 for x in input_data]
        std_dev = self.__numpy_handler.standard_derivation(processed_data)
        result = 1 / std_dev if std_dev != 0 else 0  # Avoid division by zero

        return result 
