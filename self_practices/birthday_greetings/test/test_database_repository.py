from datetime import datetime

from models.employee import Employee


class TestDatabaseRepository:
    def test_should_retrieve_employees_whose_birthday_is_today(self, mocker, db, today):
        mock_session = mocker.Mock()
        mock_query = mocker.Mock()
        mock_result = [
            Employee(
                id=1,
                first_name="Peter",
                last_name="Smith",
                email="peter.smith@gmail.com",
                birthday=datetime(1990, 9, 19),
            )
        ]
        mock_query.filter.return_value.all.return_value = mock_result
        mock_session.query.return_value = mock_query

        mocker.patch.object(db, "session", mock_session)

        employees = db.get_employees_whose_birthday_is(today)
        assert len(employees) == 1
        assert employees[0].first_name == "Peter"
