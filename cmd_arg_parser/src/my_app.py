import sys
from typing import List

from OptionParser import get_parser_by_option
from Options.Options import options_list


def process_arguments(arguments_list: List[str]):
    options = options_list

    for index, option_flag in enumerate(iter(arguments_list)):
        for i in range(len(options)):
            if options[i].flag == option_flag:
                parser = get_parser_by_option(options[i])
                options[i].value = parser.parse(arguments_list, index)

    return options


if __name__ == "__main__":
    print(process_arguments(sys.argv[1:]))
