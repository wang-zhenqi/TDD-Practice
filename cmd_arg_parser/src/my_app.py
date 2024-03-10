import sys
from typing import List, get_type_hints

from pydantic import BaseModel

from OptionParser import get_parser_by_option_type


class Options(BaseModel):
    logging: bool = False
    port: int = 0
    directory: str = ""
    group: List = []
    digits: List[int] = []


option_fields_map = {
    "-l": "logging",
    "-p": "port",
    "-d": "directory",
}


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
