from typing import List

from pydantic import BaseModel

MAX_INTEGER = 65535


def logging_parsing_function(x, y):
    return True


def group_parsing_function(x, group):
    return group


def digits_parsing_function(x, digits: List[int]):
    return [int(digit) for digit in digits]


class Options(BaseModel):
    logging: bool = False
    port: int = 0
    directory: str = ""
    group: List = []
    digits: List[int] = []


class OptionConfiguration:
    parsing_function = None
    max_number_of_arguments: int = None
    min_number_of_arguments: int = None
    type_of_argument = None


class LoggingOptions(OptionConfiguration):
    parsing_function = logging_parsing_function
    max_number_of_arguments = 0
    min_number_of_arguments = 0
    type_of_argument = bool


class PortOptions(OptionConfiguration):
    parsing_function = int
    max_number_of_arguments = 1
    min_number_of_arguments = 1
    type_of_argument = int


class DirectoryOptions(OptionConfiguration):
    parsing_function = str
    max_number_of_arguments = 1
    min_number_of_arguments = 1
    type_of_argument = str


class GroupOptions(OptionConfiguration):
    parsing_function = group_parsing_function
    max_number_of_arguments = MAX_INTEGER
    min_number_of_arguments = 0
    type_of_argument = List


class DigitOptions(OptionConfiguration):
    parsing_function = digits_parsing_function
    max_number_of_arguments = MAX_INTEGER
    min_number_of_arguments = 0
    type_of_argument = List


flag_configuration_map = {
    "-l": ("logging", LoggingOptions()),
    "-p": ("port", PortOptions()),
    "-d": ("directory", DirectoryOptions()),
    "-g": ("group", GroupOptions()),
    "-D": ("digits", DigitOptions()),
}
