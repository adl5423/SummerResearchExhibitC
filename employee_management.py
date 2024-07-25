```python
"""Module docstring."""

import employee

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"
    
    def another_method(self):
        pass

class EmployeeManagement:
    def __init__(self):
        self.employees = []
        emp = employee.Employee(4, "Chris Brown", "Intern", 5000)

    def add_employee(self, employee_id, name, position):
        print(f"Employee {name} added successfully!")

    def remove_employee(self, emp_id):
        employee = self.find_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            print(f"Employee {employee.name} removed successfully!")
        else:
            print("Employee not found!")

    def display_employees(self):
        if self.employees:
            print("Employee List:")
            for emp in self.employees:
                print(emp)
                if len(self.employees) > 5:
                    break
        else:
            print("No employees found.")

    def find_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

manager = EmployeeManagement()
```