"""
# Birthday Greetings

## Problem Description

There's a database of employees and their birthdays. Write a program that sends a birthday greeting to all employees whose birthday is today.

A sample of the database is as below:

id | last_name | first_name | date_of_birth | email
---|-----------|------------|---------------|------
1  | Doe       | John       | 1982-10-08    | john.doe@gmail.com
2  | Ann       | Mary       | 1975-09-11    | mary.ann@gmail.com

The program should read the database and email all employees whose birthday is today. The email should contain the following message:

```
Subject: Happy Birthday!

Happy Birthday, dear <first_name>!
```

## Functionality Point

- **Given** "Today's Date", **When** there are employees whose birthday is today, **Then** send a birthday greeting email to all employees
    - **Given** a database, **When** the program reads the database, **Then** the program should retrieve the employees whose birthday is today
        - **Given** a database, **When** it returns no employees whose birthday is today, **Then** the program should not send any email, print "No employees whose birthday is today"
    - **Given** an employee's record, **When** the program sends a birthday greeting email, **Then** the email should contain the message described above.
        - **Given** an employee's first_name, **When** the program sends a birthday greeting email, **Then** the email should contain the employee's first_name
    - **Given** an employee's record, **When** the program sends a birthday greeting email, **Then** the email should be sent to the employee's email address

## Tasks

- [x] Write a program that reads the database and sends birthday greetings to all employees whose birthday is today.
    - [x] Connecting to the mysql database
        - [x] The program should connect to the mysql database on localhost:3306
        - [x] The program should retrieve the employees whose birthday is today
        - [x] The program should return nothing when there are no employees whose birthday is today
    - [x] Generating birthday greetings
        - [x] The program should generate emails to all employees whose birthday is today when such employees exist
            - [x] The email body should contain the message described above
            - [x] The recipient of the email should be the employee's email address
"""
from datetime import datetime

import pytest

from birthday_greetings import generate_message
from database_repository import DatabaseRepository


@pytest.fixture(scope="module")
def db_cnx():
    return DatabaseRepository(
        "localhost",
        3306,
        "root",
        "B9Lz_XFEKh",
        "BirthdayGreetings",
        "Employees"
    )


@pytest.fixture(scope="module")
def today():
    return datetime.today().strftime("%Y-%m-%d")


class TestBirthdayGreetings:
    def test_should_send_email_when_there_are_employees_whose_birthday_is_today(self, db_cnx, today):
        employees = db_cnx.get_employees_whose_birthday_is(today)
        email_contents = [generate_message(employee) for employee in employees]
        assert len(email_contents) == 1
        assert len(employees) == 1
        assert employees[0].first_name == "Peter"
        assert email_contents[0].recipient == "peter.smith@gmail.com"
        assert email_contents[0].body == "Happy Birthday, dear Peter!"

    def test_should_not_send_email_when_there_are_no_employees_whose_birthday_is_today(self, db_cnx):
        employees = db_cnx.get_employees_whose_birthday_is("2024-09-11")
        assert len(employees) == 0