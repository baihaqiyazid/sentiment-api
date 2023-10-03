class ResponseFormat():
    def __init__(self, data, code=200, status="success", message="success",):
        self.code = code
        self.status = status
        self.message = message
        self.data = data

    def to_dict(self):
        if self.data == None:
            return {
                "code": self.code,
                "status": self.status,
                "message": self.message,
            }
        else:
            return {
                "code": self.code,
                "status": self.status,
                "message": self.message,
                "result": self.data
            }

class BadRequestException(Exception):
    pass