from typing import List
from flask import request as FlaskRequest

class Calculator2:
    def __init__(self) -> None:
        pass

    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        body = request.json
        input_data = self.__validate_request(body)

        return {
            "RESULT": result
        }

    def __validate_request(self, body: dict) -> List[float]:
        if not isinstance(body.get("number"), (int, float)):
            raise Exception("Wrong format")

        return float(body["number"])

    
