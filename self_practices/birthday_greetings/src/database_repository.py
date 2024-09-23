from datetime import datetime
from typing import List

from employee import Employee as EmployeeSchema
from orms.base_orm import BaseORM


class DatabaseRepository:
    def __init__(self, orm: BaseORM):
        self.orm = orm

    def get_employees_whose_birthday_is(self, date: datetime) -> List[EmployeeSchema]:
        pass
