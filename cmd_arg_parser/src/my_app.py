import sys
from typing import List
from pydantic import BaseModel


class Options(BaseModel):
    logging: bool = False
    port: int = 0
    directory: str = ""
    group: List = []
    digits: List[int] = []


def parse_arg(arguments: List[str]):
    options = Options()
    process_arg_list(arguments, options)
    return options


def process_arg_list(arguments, options):
    arg_mapping = {
        "-l": ("logging", lambda i: True),
        "-p": ("port", lambda i: int(arguments[i + 1])),
        "-d": ("directory", lambda i: arguments[i + 1]),
    }

    for index, arg in enumerate(iter(arguments)):
        if arg in arg_mapping:
            attr, method = arg_mapping[arg]
            setattr(options, attr, method(index))


if __name__ == "__main__":
    print(parse_arg(sys.argv[1:]))