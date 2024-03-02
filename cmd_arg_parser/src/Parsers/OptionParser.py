class OptionParser:
    def __init__(self, parsing_function=None):
        self.parsing_function = parsing_function

    def parse(self, index, argument_list):
        raise NotImplementedError
