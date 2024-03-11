from typing import List, Type, Any

from OptionsBase import OptionConfiguration, OptionDefinition

MAX_INTEGER = 65535


def logging_parsing_function(arguments):
    return True


def port_parsing_function(arguments):
    return int(arguments[0])


def directory_parsing_function(arguments):
    return str(arguments[0])


def group_parsing_function(arguments):
    return arguments


def digits_parsing_function(arguments: List[int]):
    return [int(digit) for digit in arguments]


class LoggingOptions(OptionConfiguration):
    parsing_function: Any = logging_parsing_function
    max_number_of_arguments: int = 0
    min_number_of_arguments: int = 0


class PortOptions(OptionConfiguration):
    parsing_function: Any = port_parsing_function
    max_number_of_arguments: int = 1
    min_number_of_arguments: int = 1


class DirectoryOptions(OptionConfiguration):
    parsing_function: Any = directory_parsing_function
    max_number_of_arguments: int = 1
    min_number_of_arguments: int = 1


class GroupOptions(OptionConfiguration):
    parsing_function: Any = group_parsing_function
    max_number_of_arguments: int = MAX_INTEGER
    min_number_of_arguments: int = 0


class DigitsOptions(OptionConfiguration):
    parsing_function: Any = digits_parsing_function
    max_number_of_arguments: int = MAX_INTEGER
    min_number_of_arguments: int = 0


class Logging(OptionDefinition, validate_assignment=True):
    name: str = "logging"
    flag: str = "-l"
    description: str = "Will add logging when this option is presented, no argument required"
    value: bool = False
    type: Type = bool
    arguments: List[str] = []
    configs: OptionConfiguration = LoggingOptions()


class Port(OptionDefinition, validate_assignment=True):
    name: str = "port"
    flag: str = "-p"
    description: str = ""
    value: int = 0
    type: Type = int
    configs: OptionConfiguration = PortOptions()


class Directory(OptionDefinition, validate_assignment=True):
    name: str = "directory"
    flag: str = "-d"
    description: str = ""
    value: str = ""
    type: Type = str
    configs: OptionConfiguration = DirectoryOptions()


class Group(OptionDefinition, validate_assignment=True):
    name: str = "group"
    flag: str = "-g"
    description: str = ""
    value: List = []
    type: Type = List
    configs: OptionConfiguration = GroupOptions()


class Digits(OptionDefinition, validate_assignment=True):
    name: str = "digits"
    flag: str = "-D"
    description: str = ""
    value: List[int] = []
    type: Type = List[int]
    configs: OptionConfiguration = DigitsOptions()


options_list = [
    Logging(),
    Port(),
    Directory(),
    Group(),
    Digits(),
]
