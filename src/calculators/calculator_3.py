from typing import List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError


class Calculator_3:
    def __init__(self, numpy_handler: DriverHandlerInterface) -> None:
        self.__numpy_handler = numpy_handler

    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        body = request.json
        input_data = self.__validate_request(body)
        result = self.__process_data(input_data)

        if result:
            return {"RESULT": "Success"}
        else:
            return {"RESULT": "Fail"}

    def __validate_request(self, body: dict) -> List[float]:
        numbers = body.get("numbers")
        if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
            raise HttpBadRequestError("Wrong format")

        return [float(x) for x in numbers]

    def __process_data(self, input_data: List[float]) -> bool:
        variance = self.__numpy_handler.variance(input_data)
        multiplication = 1
        for number in input_data:
            multiplication *= number
        
        return variance < multiplication
