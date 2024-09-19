import inspect
import sys
from typing import List, Any

from pydantic import Field, create_model

from Options.OptionsBase import OptionConfiguration, OptionDefinition

UPPER_BOUND_OF_LIST_SIZE = 65535


def boolean_parsing_function(*_):
    return True


def unary_parsing_function(arguments, process_func=None):
    return process_func(arguments[0]) if process_func is not None else arguments[0]


def list_parsing_function(arguments, process_func=None):
    return [process_func(argument) for argument in arguments] if process_func is not None else arguments


class LoggingConfig(OptionConfiguration):
    parsing_function: Any = boolean_parsing_function
    max_number_of_arguments: int = 0
    min_number_of_arguments: int = 0


class Logging(OptionDefinition, validate_assignment=True):
    name: str = "logging"
    flag: str = "-l"
    value: bool = False
    configs: OptionConfiguration = Field(default_factory=LoggingConfig)


class PortConfig(OptionConfiguration):
    parsing_function: Any = unary_parsing_function
    process_function: Any = int
    max_number_of_arguments: int = 1
    min_number_of_arguments: int = 1


class Port(OptionDefinition, validate_assignment=True):
    name: str = "port"
    flag: str = "-p"
    value: int = 0
    configs: OptionConfiguration = Field(default_factory=PortConfig)


class DirectoryConfig(OptionConfiguration):
    parsing_function: Any = unary_parsing_function
    max_number_of_arguments: int = 1
    min_number_of_arguments: int = 1


class Directory(OptionDefinition, validate_assignment=True):
    name: str = "directory"
    flag: str = "-d"
    value: str = ""
    configs: OptionConfiguration = Field(default_factory=DirectoryConfig)


class GroupConfig(OptionConfiguration):
    parsing_function: Any = list_parsing_function
    max_number_of_arguments: int = UPPER_BOUND_OF_LIST_SIZE
    min_number_of_arguments: int = 0


class Group(OptionDefinition, validate_assignment=True):
    name: str = "group"
    flag: str = "-g"
    value: List = []
    configs: OptionConfiguration = Field(default_factory=GroupConfig)


class DigitsConfig(OptionConfiguration):
    parsing_function: Any = list_parsing_function
    process_function: Any = int
    max_number_of_arguments: int = UPPER_BOUND_OF_LIST_SIZE
    min_number_of_arguments: int = 0


class Digits(OptionDefinition, validate_assignment=True):
    name: str = "digits"
    flag: str = "-D"
    value: List[int] = []
    configs: OptionConfiguration = Field(default_factory=DigitsConfig)


def generate_available_options():
    all_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    superclass = OptionDefinition

    filtered_classes = [cls for _, cls in all_classes if issubclass(cls, superclass) and cls != superclass]
    instance_list = [cls() for cls in filtered_classes]

    attributes = {instance.name: (instance.__class__, instance) for instance in instance_list}

    return create_model(
        "AvailableOptions",
        **attributes,
    )()


available_options = generate_available_options()
