"""Employee module for the Summer Research Exhibit project, containing the Employee class and related utilities."""

class Employee:
    """Represents an employee."""

    def __init__(self, employee_id, name, position, salary):
        self.id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return (
            f"ID: {self.id}, Name: {self.name}, Position: {self.position}, "
            f"Salary: ${self.salary}"
        )

    def get_full_name(self):
        first = getattr(self, 'name', '')
        last = getattr(self, 'surname', '')
        return f"{first} {last}".strip()