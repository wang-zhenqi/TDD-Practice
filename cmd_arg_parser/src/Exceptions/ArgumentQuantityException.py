class ArgumentQuantityException(Exception):
    def __init__(self, option_name):
        self.option_name = option_name


def insufficient_arguments(argument_list, expected_number_of_arguments):
    return len(argument_list) < expected_number_of_arguments


def too_many_arguments(argument_list, expected_number_of_arguments):
    return len(argument_list) > expected_number_of_arguments
