from database_repository import DatabaseRepository


class TestDatabaseRepository:
    def test_should_retrieve_employees_whose_birthday_is_today(self):
        db = DatabaseRepository(
            "localhost",
            "3306",
            "root",
            "B9Lz_XFEKh",
            "BirthdayGreetings",
            "Employees"
        )
        employees = db.get_employees_whose_birthday_is("2024-09-17")
        assert len(employees) == 1
        assert employees[0].first_name == "Peter"
