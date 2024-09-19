from datetime import datetime

from database_repository import RelationalDataBaseManager
from EmailContent import EmailContent
from employee import Employee
from utils import read_yaml_file


def generate_message(employee: Employee) -> EmailContent:
    return EmailContent(
        sender="",
        recipient=employee.email,
        subject="Happy Birthday!",
        body="Happy Birthday, dear {}!".format(employee.first_name),
    )


if __name__ == "__main__":
    db_configs = read_yaml_file("../database_connection.yaml")
    db_cnx = RelationalDataBaseManager(**db_configs)
    db_cnx.connect()

    today = datetime.today().strftime("%Y-%m-%d")

    employees = db_cnx.get_employees_whose_birthday_is(today)
    for employee in employees:
        message = generate_message(employee)
        print(f"Sending email to {employee.email}")
        print(f"Subject: {message.subject}")
        print(f"\n{message.body}")
        print()
