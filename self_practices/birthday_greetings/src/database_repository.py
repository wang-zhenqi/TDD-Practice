from typing import List

from employee import Employee
from mysql.connector import MySQLConnection, connection
from pydantic import BaseModel


class RelationalDataBaseManager(BaseModel, arbitrary_types_allowed=True):
    host: str
    port: int
    user: str
    password: str
    database: str
    table_name: str
    db_cnx: MySQLConnection = None

    def get_employees_whose_birthday_is(self, date: str) -> List[Employee]:
        query = f"""
SELECT *
FROM {self.table_name}
WHERE MONTH(birthday) = MONTH('{date}') AND DAY(birthday) = DAY('{date}');
"""
        cursor = self.db_cnx.cursor()
        cursor.execute(query)

        return [
            Employee(
                first_name=employee[1],
                last_name=employee[2],
                email=employee[3],
                birth_date=employee[4].strftime("%Y-%m-%d"),
            )
            for employee in cursor.fetchall()
        ]

    def connect(self):
        self.db_cnx = connection.MySQLConnection(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )
