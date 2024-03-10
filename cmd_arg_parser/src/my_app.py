import sys
from typing import List, get_type_hints

from OptionParser import get_parser_by_option_type
from Options.Options import Options, option_fields_map


def process_arguments(arguments_list: List[str]):
    options = Options()

    for index, arg in enumerate(iter(arguments_list)):
        if arg in option_fields_map:
            option_parser = get_parser_by_option_type(
                option_type=get_type_hints(Options).get(option_fields_map[arg])
            )

            setattr(options, option_fields_map[arg], option_parser.parse(arguments_list, index))

    return options


if __name__ == "__main__":
    print(process_arguments(sys.argv[1:]))
