"""
# Object Relational Mapping

## Objectives

- Being able to connect to the database_name using SQLAlchemy
- Being able to read data from files using Pandas
- Retrieve the data of employees whose birthday is today to Employee objects

## Tasks

- [ ] Connect to the database_name using SQLAlchemy
    - [ ] The program should connect to the mysql database_name on localhost:3306
    - [ ] Retrieve the data of employees whose birthday is today
- [ ] Read data from a file using Pandas
    - [ ] The program should read data from a csv file
- [ ] Retrieve the data of employees whose birthday is today to Employee objects
    - [ ] The program should return the data of employees whose birthday is today to Employee objects
"""
from datetime import datetime
from unittest.mock import patch

from orms.models.employee import Employee


class TestRelationalDatabase:
    def test_should_retrieve_employees_whose_birthday_is_today(self, mocker, db, today):
        mock_session = mocker.Mock()
        mock_result = [
            Employee(
                id=1,
                first_name="Peter",
                last_name="Smith",
                email="peter.smith@gmail.com",
                birthday=datetime.today(),
            )
        ]
        mock_session.query.return_value.filter.return_value.all.return_value = mock_result

        with patch("orms.relational_database.Session.__enter__", return_value=mock_session):
            employees = db.get_employees_whose_birthday_is(today)
            assert len(employees) == 1
            assert employees[0].first_name == "Peter"
