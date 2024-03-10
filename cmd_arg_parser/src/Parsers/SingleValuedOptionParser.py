from Exceptions.NotSufficientArgumentException import NotSufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from OptionParser import OptionParser


def too_many_arguments(argument_list, index):
    return len(argument_list) - index > 2 and not argument_list[index + 2].startswith("-")


def not_sufficient_arguments(argument_list, index):
    return (len(argument_list) - index > 1 and argument_list[index + 1].startswith("-")) or \
        len(argument_list) - index == 1


class SingleValuedOptionParser(OptionParser):
    def parse(self, index, argument_list):
        if too_many_arguments(argument_list, index):
            raise TooManyArgumentsException(argument_list[index])
        if not_sufficient_arguments(argument_list, index):
            raise NotSufficientArgumentException(argument_list[index])
        try:
            result = self.parsing_function(argument_list[index + 1])
        except ValueError as e:
            raise ValueError("Invalid type of argument: " + argument_list[index + 1] + "\nDetail: " + str(e))
        else:
            return result
