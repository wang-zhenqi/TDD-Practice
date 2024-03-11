from OptionsBase import OptionDefinition


class OptionParser:

    def __init__(self, option: OptionDefinition):
        self.option = option

    def parse(self, argument_list, index):
        self.option.arguments = get_possible_argument_list(argument_list, index)
        try:
            result = self.option.configs.parsing_function(self.option.arguments)
        except ValueError as e:
            raise ValueError(f"The type of argument: {self.option.arguments} is invalid.\nDetail: {str(e)}")
        else:
            return result


def get_parser_by_option(option: OptionDefinition):
    return OptionParser(option)


def get_possible_argument_list(argument_list, index):
    result = []
    for i in range(index + 1, len(argument_list)):
        if argument_list[i].startswith("-"):
            break
        result.append(argument_list[i])
    return result
