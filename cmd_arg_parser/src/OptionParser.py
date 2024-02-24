class OptionParser:
    def __init__(self, option_type_class=None):
        self.option_type_class = option_type_class

    def parse(self, index, argument_list):
        raise NotImplementedError

class BooleanOptionParser(OptionParser):
    def parse(self, index, argument_list):
        return True

class SingleValuedOptionParser(OptionParser):
    def parse(self, index, argument_list):
        return self.option_type_class(argument_list[index + 1])

class ParserFactory:
    option_type_parser_map = {
        bool: BooleanOptionParser(),
        int: SingleValuedOptionParser(int),
        str: SingleValuedOptionParser(str),
    }

    def get_parser_by_option_type(self, option_type) -> OptionParser:
        return self.option_type_parser_map[option_type]
