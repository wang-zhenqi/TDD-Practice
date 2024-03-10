import sys
from typing import List

from OptionParser import get_parser_by_option_flag
from Options.Options import Options, flag_configuration_map


def process_arguments(arguments_list: List[str]):
    options = Options()

    for index, arg in enumerate(iter(arguments_list)):
        if arg in flag_configuration_map:
            option_parser = get_parser_by_option_flag(arg)
            setattr(options, flag_configuration_map[arg][0], option_parser.parse(arguments_list, index))

    return options


if __name__ == "__main__":
    print(process_arguments(sys.argv[1:]))
