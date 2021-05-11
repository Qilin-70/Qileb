class UnauthorisedAction(Exception):
    def __init__(self, message="Action not permitted."):
        self.message = message
        super().__init__(message)