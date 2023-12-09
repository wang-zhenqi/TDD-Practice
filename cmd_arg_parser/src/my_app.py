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
    for index, arg in enumerate(iter(arguments)):
        if "-l" == arg:
            options.logging = True
        if "-p" == arg:
            options.port = int(arguments[index + 1])
        if "-d" == arg:
            options.directory = arguments[index + 1]
    return options

if __name__ == "__main__":
    print(parse_arg(sys.argv[1:]))