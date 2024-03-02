from Exceptions.OptionNumberException import OptionNumberException


class NotSufficientArgumentException(OptionNumberException):
    def __init__(self, option_name):
        super().__init__(option_name)
        self.message = f"Not sufficient arguments for option {self.option_name}"
