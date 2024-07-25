```python
"""Module docstring."""
# main.py

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_id, name, position, salary):
        employee = Employee(employee_id, name, position, salary)
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                self.employees.remove(employee)
                return True
        return False

    def display_employees(self):
        for employee in self.employees:
            print(employee)

    def find_employee(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                return employee
        return None

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"
    
    def another_method(self):
        return None

if __name__ == "__main__":
    manager = EmployeeManagement()

    manager.add_employee(1, "John Doe", "Manager", 80000)
    manager.add_employee(2, "Jane Smith", "Developer", 75000)
    manager.add_employee(3, "Emily Davis", "Designer", 70000)

    manager.display_employees()

    if not manager.remove_employee(2):
        print("Employee not found!")

    manager.display_employees()

    emp = Employee(4, "Chris Brown", "Intern", 5000)
    
    print(emp)

    if not manager.remove_employee(4):
        print("Employee not found!")

    manager.display_employees()
```