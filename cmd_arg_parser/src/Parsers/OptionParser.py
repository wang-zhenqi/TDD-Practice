class OptionParser:
    def __init__(self, parsing_function=None):
        self.parsing_function = parsing_function

    def parse(self, argument_list, index):
        raise NotImplementedError
