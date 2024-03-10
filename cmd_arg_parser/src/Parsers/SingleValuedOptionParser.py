from Exceptions.InsufficientArgumentException import InsufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from OptionParser import OptionParser


def too_many_arguments(argument_list, expected_number_of_arguments):
    return len(argument_list) > expected_number_of_arguments


def insufficient_arguments(argument_list, expected_number_of_arguments):
    return len(argument_list) < expected_number_of_arguments


def get_applicable_argument_list(argument_list, index):
    result = []
    for i in range(index + 1, len(argument_list)):
        if argument_list[i].startswith("-"):
            break
        result.append(argument_list[i])
    return result


def validate_the_quantity_of_applicable_arguments(argument_list,
                                                  index,
                                                  max_number_of_arguments,
                                                  min_number_of_arguments):
    applicable_arguments_list = get_applicable_argument_list(argument_list, index)
    if too_many_arguments(applicable_arguments_list, max_number_of_arguments):
        raise TooManyArgumentsException(argument_list[index])
    if insufficient_arguments(applicable_arguments_list, min_number_of_arguments):
        raise InsufficientArgumentException(argument_list[index])
    return applicable_arguments_list


class SingleValuedOptionParser(OptionParser):
    def parse(self, argument_list, index):
        applicable_arguments_list = validate_the_quantity_of_applicable_arguments(argument_list, index, 1, 1)
        try:
            result = self.parsing_function(applicable_arguments_list[0])
        except ValueError as e:
            raise ValueError(f"The type of argument: {applicable_arguments_list[0]} is invalid.\nDetail: {str(e)}")
        else:
            return result
