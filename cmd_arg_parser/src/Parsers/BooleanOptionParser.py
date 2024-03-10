from OptionParser import OptionParser
from SingleValuedOptionParser import validate_the_quantity_of_applicable_arguments


class BooleanOptionParser(OptionParser):
    def parse(self, argument_list, index):
        applicable_argument_list = validate_the_quantity_of_applicable_arguments(argument_list, index, 0, 0)
        return applicable_argument_list == []
