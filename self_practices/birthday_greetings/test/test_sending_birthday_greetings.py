import pytest
from birthday_greetings import generate_message
from EmailContent import EmailContent
from employee import Employee


@pytest.fixture(scope="module")
def john_doe():
    return Employee(
        first_name="John",
        last_name="Doe",
        email="john.doe@gmail.com",
        birth_date="1990-01-01",
    )


class TestSendingBirthdayGreetings:
    def test_should_generate_message_with_the_employees_first_name_and_email_address(self, john_doe):
        expected = EmailContent(
            sender="",
            recipient="john.doe@gmail.com",
            subject="Happy Birthday!",
            body="Happy Birthday, dear John!",
        )
        actual = generate_message(john_doe)
        assert actual == expected
