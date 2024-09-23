from datetime import datetime
from typing import Dict, List

from employee import Employee as EmployeeSchema
from orms.base_orm import BaseORM
from orms.models.employee import Employee as EmployeeModel
from sqlalchemy import Engine, create_engine, func
from sqlalchemy.orm import Session


class RelationalDatabase(BaseORM, extra="allow", arbitrary_types_allowed=True):
    host: str
    port: int
    user: str
    password: str
    database_name: str
    table_name: str
    database_type: str
    database_driver: str
    models: Dict = {"employee": EmployeeModel}

    engine: Engine = None

    def __init__(self, **data):
        super().__init__(**data)
        self.create_engine()

    def get_employees_whose_birthday_is(self, date: datetime) -> List[EmployeeSchema]:
        with Session(bind=self.engine) as session:
            result = (
                session.query(self.models["employee"])
                .filter(
                    (func.month(self.models["employee"].birthday) == date.month)
                    & (func.day(self.models["employee"].birthday) == date.day)
                )
                .all()
            )

        return [
            EmployeeSchema(
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email,
                date_of_birth=row.birthday,
            )
            for row in result
        ]

    def make_connection_string(self) -> str:
        driver = f"+{self.database_driver}" if self.database_driver else ""
        return (
            f"{self.database_type}{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}"
        )

    def create_engine(self):
        self.engine = create_engine(self.make_connection_string())
