from datetime import datetime


class TestDatabaseRepository:
    def test_should_retrieve_employees_whose_birthday_is_today(self, mocker, db, today):
        mock_cursor = mocker.Mock()
        mock_cursor.fetchall.return_value = [
            (1, "Peter", "Smith", "peter.smith@gmail.com", datetime(1990, 9, 19)),
        ]
        mock_db_connection = mocker.Mock()
        mock_db_connection.cursor.return_value = mock_cursor
        mocker.patch.object(db, "db_cnx", mock_db_connection)

        employees = db.get_employees_whose_birthday_is(today)
        assert len(employees) == 1
        assert employees[0].first_name == "Peter"
