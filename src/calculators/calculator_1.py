from flask import request as FlaskRequest

class Calculator_1:
    def calculate(self, request: FlaskRequest) -> dict: # type: ignore
        body = request.json

        input_data = self.__validate_request(body)

        splited_number = input_data / 3

        first_step_result = self.__first_step(splited_number)
        second_step_result = self.__second_step(splited_number)
        third_step_result = self.__third_step(splited_number)
        
        result = first_step_result + second_step_result + third_step_result

        return {
            "first part": first_step_result,
            "second part": second_step_result,
            "third part": third_step_result,
            "RESULT": result
        }

    def __validate_request(self, body: dict) -> float:
        if "number" not in body:
            raise Exception("Wrong format")
        
        input_data = body["number"]

        return input_data

    def __first_step(self, input_data: float) -> float:
        number = (input_data / 4) + 7
        result = (number ** 2) * 0.257
        return round(result, 2)

    def __second_step(self, input_data: float) -> float:
        number = (input_data ** 2.121)
        result = (number / 5) + 1
        return round(result, 2)
    
    def __third_step(self, input_data: float) -> float:
        number = input_data
        return round(number, 2)
