from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    last_name: str
    email: str
    date_of_birth: datetime
