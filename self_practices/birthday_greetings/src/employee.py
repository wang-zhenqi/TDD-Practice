class Employee:
    def __init__(self, first_name, email=None):
        self.first_name = first_name

        self.email = email if email else ""
