import sys
import typing
from typing import List

from pydantic import BaseModel


class Options(BaseModel):
    logging: bool = False
    port: int = 0
    directory: str = ""
    group: List = []
    digits: List[int] = []


def process_arg_list(arguments: List[str]):
    options = Options()

    arg_mapping = {
        "-l": "logging",
        "-p": "port",
        "-d": "directory",
    }

    for index, arg in enumerate(iter(arguments)):
        def parse_value(arg_type):
            if arg_type == bool:
                return True
            return arg_type(arguments[index + 1])

        def get_field_type():
            return typing.get_type_hints(Options).get(arg_mapping[arg])

        if arg in arg_mapping:
            setattr(options, arg_mapping[arg], parse_value(get_field_type()))

    return options


if __name__ == "__main__":
    print(process_arg_list(sys.argv[1:]))
