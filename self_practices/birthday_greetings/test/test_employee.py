from employee import Employee


class TestEmployee:
    def test_employee_should_return_true_if_a_date_is_his_birthday(self):
        employee = Employee("John", "Doe", "john.doe@gmail.com", "1990-01-01")
        assert employee.is_birthday("2024-01-01") is True
