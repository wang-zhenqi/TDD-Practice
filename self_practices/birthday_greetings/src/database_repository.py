from typing import List, Dict

from mysql.connector import connection

from employee import Employee


class DatabaseRepository:
    def __init__(self, host: str, port: int, user: str, password: str, database: str, table_name: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table_name = table_name
        self.db_cnx = self.connect()

    def get_employees_whose_birthday_is(self, date: str) -> List[Employee]:
        query = f"""
SELECT *
FROM {self.table_name}
WHERE MONTH(birthday) = MONTH('{date}') AND DAY(birthday) = DAY('{date}');
"""
        cursor = self.db_cnx.cursor() if self.db_cnx else self.connect().cursor()
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
        return connection.MySQLConnection(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
