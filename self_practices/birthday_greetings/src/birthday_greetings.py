from datetime import datetime

from EmailContent import EmailContent
from database_repository import DatabaseRepository
from employee import Employee


def generate_message(employee: Employee) -> EmailContent:
    return EmailContent(
        sender="",
        recipient=employee.email,
        subject="Happy Birthday!",
        body="Happy Birthday, dear {}!".format(employee.first_name)
    )


if __name__ == "__main__":
    db_cnx = DatabaseRepository(
        "localhost",
        3306,
        "root",
        "B9Lz_XFEKh",
        "BirthdayGreetings",
        "Employees"
    )
    today = datetime.today().strftime("%Y-%m-%d")
    employees = db_cnx.get_employees_whose_birthday_is(today)
    for employee in employees:
        message = generate_message(employee)
        print(f"Sending email to {employee.email}")
        print(f"Subject: {message.subject}")
        print(f"\n{message.body}")
        print()
