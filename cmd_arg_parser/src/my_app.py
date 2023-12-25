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


def parse_value(i, arguments, parse_func):
    if parse_func == bool:
        return True
    return parse_func(arguments[i + 1])


def process_arg_list(arguments, options):
    arg_mapping = {
        "-l": "logging",
        "-p": "port",
        "-d": "directory",
    }

    for index, arg in enumerate(iter(arguments)):
        if arg in arg_mapping:
            options.__setattr__(arg_mapping[arg], parse_value(index, arguments, Options.__annotations__[
                arg_mapping[arg]]))


if __name__ == "__main__":
    print(parse_arg(sys.argv[1:]))
