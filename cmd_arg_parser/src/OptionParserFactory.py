from OptionParser import OptionParser
from BooleanOptionParser import BooleanOptionParser
from SingleValuedOptionParser import SingleValuedOptionParser


class OptionParserFactory:
    option_type_parser_map = {
        bool: BooleanOptionParser(),
        int: SingleValuedOptionParser(int),
        str: SingleValuedOptionParser(str),
    }

    def get_parser_by_option_type(self, option_type) -> OptionParser:
        return self.option_type_parser_map[option_type]
