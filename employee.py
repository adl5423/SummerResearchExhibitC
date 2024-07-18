# employee.py

class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.slary = salary  # Easy error: Typo in attribute initialization (self.slary)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.nme}, Position: {self.position}, Salary: ${self.salary}"  # Easy error: Typo in attribute access (self.nme)