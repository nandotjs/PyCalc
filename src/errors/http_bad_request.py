class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
        self.name = "HttpBadRequest"
        self.status_code = 400

