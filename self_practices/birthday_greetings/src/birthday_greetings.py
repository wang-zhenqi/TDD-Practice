from EmailContent import EmailContent
from employee import Employee


def generate_message(employee: Employee) -> EmailContent:
    return EmailContent(
        sender="",
        recipient=employee.email,
        subject="Happy Birthday!",
        body="Happy Birthday, dear {}!".format(employee.first_name)
    )
