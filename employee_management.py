```python
"""
Module docstring for main.py
"""

from employee_management import EmployeeManagement

class Employee:
    """A class to represent an employee."""
    
    def __init__(self, emp_id, name, position, salary):
        self.id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

emp = Employee(4, "Chris Brown", "Intern", 5000)

manager = EmployeeManagement()
```