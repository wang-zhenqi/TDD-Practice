import re

from Options.OptionsBase import OptionDefinition


class OptionParser:

    def __init__(self, option: OptionDefinition):
        self.option = option

    def parse(self, argument_list, index):
        self.option.arguments = get_possible_argument_list(argument_list, index)
        try:
            result = self.option.configs.parsing_function(self.option.arguments, self.option.configs.process_function)
        except ValueError as e:
            raise ValueError(f"The type of argument: {self.option.arguments} is invalid.\nDetail: {str(e)}")
        else:
            return result


def get_possible_argument_list(argument_list, index):
    result = []
    for i in range(index + 1, len(argument_list)):
        if re.match(r"^-[a-zA-Z]", argument_list[i]):
            break
        result.append(argument_list[i])
    return result
