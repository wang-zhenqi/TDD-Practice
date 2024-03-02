class OptionParser:
    def __init__(self, option_type_class=None):
        self.option_type_class = option_type_class

    def parse(self, index, argument_list):
        raise NotImplementedError
