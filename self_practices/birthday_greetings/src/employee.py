from datetime import datetime


class Employee:
    def __init__(self, first_name: str, last_name: str, email: str, birth_date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = datetime.strptime(birth_date, "%Y-%m-%d")
