import sys
from typing import List

from Options.Options import available_options
from Parsers.OptionParser import OptionParser


def process_arguments(arguments_list: List[str]):
    options_flag_map = {option[1].flag: option[1] for option in available_options}

    for index, list_item in enumerate(iter(arguments_list)):
        if list_item in options_flag_map:
            options_flag_map[list_item].value = OptionParser(options_flag_map[list_item]).parse(arguments_list, index)

    return {option.name: option.value for option in options_flag_map.values()}


if __name__ == "__main__":
    print(process_arguments(sys.argv[1:]))
