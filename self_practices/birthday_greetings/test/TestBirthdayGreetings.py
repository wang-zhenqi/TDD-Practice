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

- [ ] Write a program that reads the database and sends birthday greetings to all employees whose birthday is today.
    - [ ] Reading the database
        - [ ] The program should connect to the database
        - [ ] The program should retrieve the employees whose birthday is today
        - [ ] The program should return nothing when there are no employees whose birthday is today
    - [ ] Sending birthday greetings
        - [ ] The program should send a birthday greeting email to all employees whose birthday is today when such employees exist
            - [ ] The email should contain the message described above
            - [ ] The email should be sent to the employee's email address
        - [ ] The program should not send any email when there are no employees whose birthday is today
            - [ ] The program should print "No employees whose birthday is today"
"""
