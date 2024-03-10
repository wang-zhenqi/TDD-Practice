from typing import List

from pydantic import BaseModel


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
    "-g": "group",
}
