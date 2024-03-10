from typing import List

from Exceptions.ArgumentQuantityException import insufficient_arguments, too_many_arguments
from Exceptions.InsufficientArgumentException import InsufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from Options.Options import OptionConfiguration, flag_configuration_map


class OptionParser:

    def __init__(self, option_configuration: OptionConfiguration):
        self.parsing_function = option_configuration.parsing_function
        self.max_number_of_arguments = option_configuration.max_number_of_arguments
        self.min_number_of_arguments = option_configuration.min_number_of_arguments
        self.expected_type = option_configuration.type_of_argument

    def parse(self, argument_list, index):
        validated_arguments_list = validate_the_quantity_of_arguments(argument_list,
                                                                      index,
                                                                      self.max_number_of_arguments,
                                                                      self.min_number_of_arguments,
                                                                      self.expected_type)

        applicable_arguments_list = get_applicable_arguments(validated_arguments_list,
                                                             self.expected_type)
        try:
            result = self.parsing_function(applicable_arguments_list[0])
        except ValueError as e:
            raise ValueError(f"The type of argument: {applicable_arguments_list[0]} is invalid.\nDetail: {str(e)}")
        else:
            return result


def get_parser_by_option_flag(option_flag) -> OptionParser:
    return OptionParser(flag_configuration_map[option_flag][1])


def validate_the_quantity_of_arguments(argument_list,
                                       index,
                                       max_number_of_arguments,
                                       min_number_of_arguments,
                                       expected_type):
    possible_arguments_list = get_possible_argument_list(argument_list, index)

    if too_many_arguments(possible_arguments_list, max_number_of_arguments):
        raise TooManyArgumentsException(argument_list[index])

    if insufficient_arguments(possible_arguments_list, min_number_of_arguments):
        raise InsufficientArgumentException(argument_list[index])

    return possible_arguments_list


def get_possible_argument_list(argument_list, index):
    result = []
    for i in range(index + 1, len(argument_list)):
        if argument_list[i].startswith("-"):
            break
        result.append(argument_list[i])
    return result


def get_applicable_arguments(possible_arguments_list,
                             expected_type):
    if expected_type == List:
        return [possible_arguments_list]

    if expected_type == bool:
        return [True]

    return possible_arguments_list
