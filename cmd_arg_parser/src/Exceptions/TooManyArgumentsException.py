from Exceptions.ArgumentQuantityException import ArgumentQuantityException


class TooManyArgumentsException(ArgumentQuantityException):
    def __init__(self, option_name):
        super().__init__(option_name)
        self.message = f"Too many arguments for option {self.option_name}"
