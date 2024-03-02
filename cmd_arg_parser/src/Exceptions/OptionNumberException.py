class OptionNumberException(Exception):
    def __init__(self, option_name):
        self.option_name = option_name
