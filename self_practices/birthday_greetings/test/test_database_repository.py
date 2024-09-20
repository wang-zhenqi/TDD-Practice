from datetime import datetime

from models.employee import Employee


class TestDatabaseRepository:
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

        mocker.patch.object(db, "session", mock_session)
        db.session.query.return_value.filter.return_value.all.return_value = mock_result

        employees = db.get_employees_whose_birthday_is(today)
        assert len(employees) == 1
        assert employees[0].first_name == "Peter"
