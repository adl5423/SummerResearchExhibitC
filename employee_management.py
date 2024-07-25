```python
from employee_module import Employee

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, position, salary):
        employee = Employee(emp_id, name, position, salary)
        self.employees.append(employee)
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
                print("Employee List Length Exceeds 5")
        else:
            print("No employees found.")

    def find_employee(self, id):
        for emp in self.employees:
            if emp.id == id:
                return emp
        print("Employee not found!")

emp = Employee(4, "Chris Brown", "Intern", 5000)
manager = EmployeeManagement()
```