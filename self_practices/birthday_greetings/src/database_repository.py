from typing import List, Dict

from pydantic import BaseModel
from sqlalchemy import create_engine, Connection
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, Session

from employee import Employee as employee_schema
from models.employee import Employee as employee_model


class RelationalDataBaseManager(BaseModel, arbitrary_types_allowed=True):
    host: str
    port: int
    user: str
    password: str
    database_name: str
    table_name: str
    database_type: str
    database_driver: str = None
    models: Dict = {"employee": employee_model}
    session: Session = None

    def get_employees_whose_birthday_is(self, date: str) -> List[employee_schema]:

        result = self.session.query(self.models["employee"]).filter(
            (func.month(self.models["employee"].birthday) == date[5:7]) &
            (func.day(self.models["employee"].birthday) == date[8:10])
        ).all()

        self.session.close()

        return [
            employee_schema(
                id=row.id,
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email,
                date_of_birth=row.birthday,
            )
            for row in result
        ]

    def make_connection_string(self) -> str:
        driver = f"+{self.database_driver}" if self.database_driver else ""
        return \
            f"{self.database_type}{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}"

    def make_session(self):
        self.session = sessionmaker(bind=(create_engine(self.make_connection_string())))()


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

    db.make_session()
    employees = db.get_employees_whose_birthday_is("2021-01-01")
    print(employees)
