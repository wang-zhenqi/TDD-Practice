import sys
from typing import List

from pydantic import BaseModel


class Options(BaseModel):
    logging: bool = False
    port: int = 0
    directory: str = ""
    group: List = []
    digits: List[int] = []


def parse_value(i, arguments, parse_func):
    if parse_func == bool:
        return True
    return parse_func(arguments[i + 1])


def process_arg_list(arguments: List[str]):
    options = Options()

    arg_mapping = {
        "-l": "logging",
        "-p": "port",
        "-d": "directory",
    }

    for index, arg in enumerate(iter(arguments)):
        if arg in arg_mapping:
            options.__setattr__(
                arg_mapping[arg],
                parse_value(
                    index,
                    arguments,
                    Options.__annotations__[arg_mapping[arg]]
                )
            )
    return options


if __name__ == "__main__":
    print(process_arg_list(sys.argv[1:]))
