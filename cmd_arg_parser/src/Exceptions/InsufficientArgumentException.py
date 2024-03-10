from Exceptions.ArgumentQuantityException import ArgumentQuantityException


class InsufficientArgumentException(ArgumentQuantityException):
    def __init__(self, option_name):
        super().__init__(option_name)
        self.message = f"Insufficient arguments for option {self.option_name}"
