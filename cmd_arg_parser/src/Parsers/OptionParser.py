from typing import List

from Exceptions.ArgumentQuantityException import insufficient_arguments, too_many_arguments
from Exceptions.InsufficientArgumentException import InsufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException

MAX_INTEGER = 65535


class OptionParser:

    def __init__(self,
                 parsing_function=None,
                 max_number_of_arguments=None,
                 min_number_of_arguments=None,
                 expected_type=None):
        self.parsing_function = parsing_function
        self.max_number_of_arguments = max_number_of_arguments
        self.min_number_of_arguments = min_number_of_arguments
        self.expected_type = expected_type

    def parse(self, argument_list, index):
        applicable_arguments_list = validate_the_quantity_of_applicable_arguments(argument_list,
                                                                                  index,
                                                                                  self.max_number_of_arguments,
                                                                                  self.min_number_of_arguments,
                                                                                  self.expected_type)

        try:
            result = self.parsing_function(applicable_arguments_list[0])
        except ValueError as e:
            raise ValueError(f"The type of argument: {applicable_arguments_list[0]} is invalid.\nDetail: {str(e)}")
        else:
            return result


option_type_parser_map = {
    bool: OptionParser(bool, 0, 0, bool),
    int: OptionParser(int, 1, 1, int),
    str: OptionParser(str, 1, 1, str),
    List: OptionParser(lambda x: x, MAX_INTEGER, 0, List),
}


def get_parser_by_option_type(option_type) -> OptionParser:
    return option_type_parser_map[option_type]


def validate_the_quantity_of_applicable_arguments(argument_list,
                                                  index,
                                                  max_number_of_arguments,
                                                  min_number_of_arguments,
                                                  expected_type):
    applicable_arguments_list = get_applicable_argument_list(argument_list, index)

    if too_many_arguments(applicable_arguments_list, max_number_of_arguments):
        raise TooManyArgumentsException(argument_list[index])

    if insufficient_arguments(applicable_arguments_list, min_number_of_arguments):
        raise InsufficientArgumentException(argument_list[index])

    if max_number_of_arguments == 0 and min_number_of_arguments == 0:
        applicable_arguments_list.append("valid")

    if expected_type == List:
        return [applicable_arguments_list]

    return applicable_arguments_list


def get_applicable_argument_list(argument_list, index):
    result = []
    for i in range(index + 1, len(argument_list)):
        if argument_list[i].startswith("-"):
            break
        result.append(argument_list[i])
    return result
