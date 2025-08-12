class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

    def get_full_name(self):
        first = getattr(self, 'name', '')
        last = getattr(self, 'surname', '')
        return f"{first} {last}".strip()

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_id, name, position, salary):
        employee = Employee(employee_id, name, position, salary)
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
        else:
            print("No employees found.")

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp.id == employee_id:
                return emp
        return None