from datetime import datetime


class Employee:
    def __init__(self, first_name: str, last_name: str, email: str, birth_date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def is_birthday(self, date: str):
        date = datetime.strptime(date, "%Y-%m-%d")
        return self.birth_date.month == date.month and self.birth_date.day == date.day
