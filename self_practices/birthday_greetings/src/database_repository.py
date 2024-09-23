from datetime import datetime
from typing import Dict, List

from employee import Employee as EmployeeSchema
from models.employee import Employee as EmployeeModel
from pydantic import BaseModel
from sqlalchemy import Engine, create_engine, func
from sqlalchemy.orm import Session


class RelationalDataBaseManager(BaseModel, arbitrary_types_allowed=True):
    host: str
    port: int
    user: str
    password: str
    database_name: str
    table_name: str
    database_type: str
    database_driver: str = None
    models: Dict = {"employee": EmployeeModel}
    engine: Engine = None

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


if __name__ == "__main__":
    db = RelationalDataBaseManager(
        host="localhost",
        port=3306,
        user="root",
        password="B9Lz_XFEKh",
        database_name="BirthdayGreetings",
        table_name="Employees",
        database_type="mysql",
        database_driver="mysqlconnector",
    )

    db.create_engine()
    employees = db.get_employees_whose_birthday_is(datetime(2021, 1, 1))
    print(employees)
